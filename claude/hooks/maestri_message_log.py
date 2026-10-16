#!/usr/bin/env python3
"""Claude Code hook: log inter-agent `maestri ask` traffic to the vault.

Created by: Alex Myasnikov
Date: October 13, 2026

Appends one line per event to
    <vault>/Agents/<handle>/_shared/message-log-YYYY-MM.md
following _meta/agents/_common.md § Message log.

Modes (first argument), each reading the hook JSON on stdin:
  sent   PreToolUse  (Bash)  -> one SENT line per `maestri ask` target
  reply  PostToolUse (Bash)  -> one REPLY line per target (the synchronous answer)
  recv   UserPromptSubmit    -> one RECV line for prompts carrying a TYPE: header

Options:
  --vault <path>    vault root (default: ../../obsidian relative to this file)
  --handle <name>   owning user handle (default: $MATH_VAULT_HANDLE, then the
                    "My vault handle:" line in ~/.claude/CLAUDE.md)

No-op outside Maestri terminals. Prints nothing to stdout (UserPromptSubmit
would inject it into the agent's context). Never blocks the agent: always exits 0;
failures are logged as ERROR lines in the same file when possible.
"""
import json
import os
import re
import shlex
import subprocess
import sys
import time

TYPES = ("REQUEST", "REPORT", "QUESTION", "BLOCKER", "VERDICT", "ACK")
TYPE_RE = re.compile(r"^\s*TYPE:\s*(%s)\b" % "|".join(TYPES), re.M)
ASK_RE = re.compile(r"""(?:^|[\s;&|(`"'])(?:\S*/)?["']?(?:maestri|\$\{?MAESTRI_CLI\}?)["']?\s+ask\b""")
ASK_LEN = 200
REPLY_LEN = 1000


def field(text, name):
    """Value of a `NAME: value` header line in a message, or '-'."""
    m = re.search(r"(?:^|\s/\s)\s*%s:\s*(.+)$" % name, text, re.M)
    if not m:
        return "-"
    return clean(re.split(r"\s+/\s+(?=[A-Z]+:)", m.group(1))[0])  # one-line "A: x / B: y" form


def clean(s, limit=None):
    s = " ".join(str(s).split()).replace("|", "/")
    if limit and len(s) > limit:
        s = s[: limit - 1] + "…"
    return s or "-"


def entry(kind, sender, receiver, msg):
    """One log line from a message body (header fields + ASK)."""
    if TYPE_RE.search(msg):
        typ, topic = field(msg, "TYPE"), field(msg, "TOPIC")
        ask = field(msg, "ASK")
    else:  # off-protocol message: keep its first words
        typ, topic, ask = "-", "-", clean(msg)
    return " | ".join([
        "- " + time.strftime("%Y-%m-%d %H:%M:%S"), kind,
        "%s → %s" % (clean(sender), clean(receiver)), typ, topic,
        field(msg, "PROJECT"), field(msg, "CONTEXT"),
        "ASK: " + clean(ask, ASK_LEN),
    ])


def parse_asks(command):
    """[(target, message)] for every `maestri ask` in a shell command.

    Falls back to ('?', raw command) when the command can't be tokenized
    (heredocs, command substitution), so no send goes unlogged. A command that
    tokenizes without a `maestri ask` call only mentions it (in text): [].
    """
    try:
        tokens = shlex.split(command, comments=False, posix=True)
    except ValueError:
        return [("?", command)]
    out = []
    for i, tok in enumerate(tokens[:-1]):
        base = os.path.basename(tok)
        if base not in ("maestri", "$MAESTRI_CLI", "${MAESTRI_CLI}") or tokens[i + 1] != "ask":
            continue
        args = tokens[i + 2:]
        if "--raw" in args[:3]:
            continue  # raw keystrokes, not a message
        if args and args[0] == "--batch":
            try:
                batch = json.loads(args[1])
                out += [(name, str(msg)) for name, msg in batch.items()]
            except (IndexError, ValueError, AttributeError):
                out.append(("?", command))
            continue
        target = args[0] if args else "?"
        message = args[1] if len(args) > 1 else ""
        if not message or message.startswith("$("):
            message = command  # body was substituted; header lines are still in the raw text
        out.append((target, message))
    return out


def answer(screen):
    """The agent's answer from a `maestri ask` reply, which is a terminal screen dump.

    Claude Code marks each response block with `●`; the last block runs until the
    status line (`✻`), input box rule (`───`) or prompt (`❯`). Screens without a marker pass through.
    """
    lines = str(screen).splitlines()
    starts = [i for i, l in enumerate(lines) if l.lstrip().startswith("●")]
    if not starts:
        return screen
    out = [lines[starts[-1]].lstrip()[1:]]
    for l in lines[starts[-1] + 1:]:
        if l.lstrip().startswith(("─", "❯", "✻")):
            break
        out.append(l)
    return "\n".join(out).strip() or screen


def reply_texts(response, targets):
    """[(target, reply text)] from a Bash tool_response."""
    if isinstance(response, dict):
        stdout = response.get("stdout") or ""
        failed = response.get("interrupted") or (not stdout and response.get("stderr"))
        if failed:
            note = "(no reply: %s)" % ("interrupted/timeout" if response.get("interrupted") else clean(response.get("stderr"), 120))
            return [(t, note) for t in targets]
    else:
        stdout = str(response or "")
    if len(targets) > 1:  # --batch returns [{name, output|error}]
        try:
            items = json.loads(stdout)
            return [(i.get("name", "?"), answer(i["output"]) if i.get("output") else "(error: %s)" % i.get("error"))
                    for i in items]
        except (ValueError, AttributeError):
            pass
    return [(t, answer(stdout) if stdout else "(empty reply)") for t in targets]


def canvas_name(entry):
    """`Lead` from a `maestri list` entry such as `name: "Lead", maestro: true`."""
    m = re.search(r'name:\s*"([^"]*)"', entry)
    return m.group(1) if m else entry


def my_name():
    """This terminal's canvas name, from the `You:` entry of `maestri list`."""
    if os.environ.get("MAESTRI_AGENT"):
        return os.environ["MAESTRI_AGENT"]
    cli = os.environ.get("MAESTRI_CLI") or "maestri"
    try:
        out = subprocess.run([cli, "list"], capture_output=True, text=True, timeout=3).stdout
    except (OSError, subprocess.SubprocessError):
        return "?"
    lines = out.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^\s*You:\s*(.*)$", line)
        if m:
            name = m.group(1).strip() or (lines[i + 1].strip() if i + 1 < len(lines) else "")
            return canvas_name(name.strip("-*• ")) or "?"
    return "?"


def handle_from_claude_md():
    try:
        with open(os.path.expanduser("~/.claude/CLAUDE.md")) as f:
            m = re.search(r"My vault handle:\s*([a-z0-9-]+)", f.read())
            return m.group(1) if m else None
    except OSError:
        return None


def opt(args, name):
    return args[args.index(name) + 1] if name in args and args.index(name) + 1 < len(args) else None


def append(shared, lines):
    os.makedirs(shared, exist_ok=True)
    path = os.path.join(shared, "message-log-%s.md" % time.strftime("%Y-%m"))
    fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
    try:
        os.write(fd, ("\n".join(lines) + "\n").encode())  # one write per event
    finally:
        os.close(fd)


def main(argv):
    if not (os.environ.get("MAESTRI_TERMINAL_ID") or os.environ.get("MAESTRI_SOCKET")):
        return
    mode = argv[0] if argv else ""
    raw = sys.stdin.read()
    if mode in ("sent", "reply") and not (("maestri" in raw or "MAESTRI_CLI" in raw) and " ask" in raw):
        return  # fast path: not a maestri ask
    data = json.loads(raw)

    here = os.path.dirname(os.path.abspath(__file__))
    vault = opt(argv, "--vault") or os.path.normpath(os.path.join(here, "..", "..", "obsidian"))
    handle = opt(argv, "--handle") or os.environ.get("MATH_VAULT_HANDLE") or handle_from_claude_md()
    if not handle:
        raise RuntimeError("no vault handle (pass --handle or set MATH_VAULT_HANDLE)")
    shared = os.path.join(vault, "Agents", handle, "_shared")

    try:
        if mode in ("sent", "reply"):
            command = (data.get("tool_input") or {}).get("command", "")
            if not ASK_RE.search(command):
                return
            asks = parse_asks(command)
            if not asks:
                return
            me = my_name()
            if mode == "sent":
                lines = [entry("SENT", me, t, msg) for t, msg in asks]
            else:
                replies = reply_texts(data.get("tool_response"), [t for t, _ in asks])
                lines = [" | ".join(["- " + time.strftime("%Y-%m-%d %H:%M:%S"), "REPLY",
                                     "%s → %s" % (clean(t), clean(me)), "REPLY: " + clean(r, REPLY_LEN)])
                         for t, r in replies]
        elif mode == "recv":
            prompt = data.get("prompt", "")
            if not TYPE_RE.search(prompt):
                return  # human prompt, not an agent message
            sender = field(prompt, "FROM")
            if sender == "-":
                sender = "?" + clean(prompt, 60)  # shows what Maestri injects before the header
            lines = [entry("RECV", sender, my_name(), prompt)]
        else:
            return
        if lines:
            append(shared, lines)
    except Exception as e:  # never break the agent; leave a trace instead
        try:
            append(shared, ["- %s | ERROR | %s: %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), mode, clean(e, 300))])
        except Exception:
            pass


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        print("maestri_message_log: %s" % e, file=sys.stderr)
    sys.exit(0)
