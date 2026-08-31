"""Direct-filesystem Obsidian vault access.

This replaces the cyanheads Obsidian-Local-REST-API dependency with plain
filesystem operations, so the only thing a user has to install is this server
(via `uv`). No Node.js, no Obsidian plugin, no API key.

All paths are vault-relative. Absolute paths and `..` traversal are rejected so
the server can never touch anything outside the configured vault root.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)


class VaultError(Exception):
    """Raised for any vault-access problem worth surfacing to the model."""


@dataclass
class Note:
    """A parsed Obsidian note: frontmatter dict + markdown body."""

    rel_path: str
    frontmatter: dict = field(default_factory=dict)
    body: str = ""

    def render(self) -> str:
        """Serialize back to `---\\nyaml\\n---\\nbody` form."""
        if not self.frontmatter:
            return self.body
        fm = yaml.safe_dump(
            self.frontmatter, sort_keys=False, allow_unicode=True
        ).strip()
        return f"---\n{fm}\n---\n\n{self.body.lstrip()}\n"


class Vault:
    """Filesystem-backed Obsidian vault, scoped to a single root directory."""

    def __init__(self, root: Path):
        self.root = root.expanduser().resolve()
        if not self.root.is_dir():
            raise VaultError(f"Vault root does not exist or is not a dir: {self.root}")

    # ---- path safety -------------------------------------------------------

    def _resolve(self, rel_path: str) -> Path:
        """Resolve a vault-relative path, rejecting escapes outside the root."""
        rel_path = rel_path.strip().lstrip("/")
        if not rel_path:
            raise VaultError("Empty path.")
        if not rel_path.endswith(".md"):
            rel_path += ".md"
        candidate = (self.root / rel_path).resolve()
        try:
            candidate.relative_to(self.root)
        except ValueError:
            raise VaultError(
                f"Path escapes the vault root (rejected): {rel_path}"
            )
        return candidate

    def rel(self, p: Path) -> str:
        return str(p.relative_to(self.root))

    # ---- read --------------------------------------------------------------

    def read(self, rel_path: str) -> Note:
        p = self._resolve(rel_path)
        if not p.is_file():
            raise VaultError(f"Note not found: {self.rel(p)}")
        return self._parse(self.rel(p), p.read_text(encoding="utf-8"))

    def exists(self, rel_path: str) -> bool:
        try:
            return self._resolve(rel_path).is_file()
        except VaultError:
            return False

    @staticmethod
    def _parse(rel_path: str, raw: str) -> Note:
        m = _FRONTMATTER_RE.match(raw)
        if not m:
            return Note(rel_path=rel_path, frontmatter={}, body=raw)
        fm_text, body = m.group(1), m.group(2)
        try:
            fm = yaml.safe_load(fm_text) or {}
            if not isinstance(fm, dict):
                fm = {}
        except yaml.YAMLError:
            fm = {}
        return Note(rel_path=rel_path, frontmatter=fm, body=body)

    # ---- write -------------------------------------------------------------

    def write(self, rel_path: str, content: str, *, overwrite: bool = True) -> str:
        p = self._resolve(rel_path)
        if p.exists() and not overwrite:
            raise VaultError(f"Note already exists (overwrite=false): {self.rel(p)}")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        return self.rel(p)

    def write_note(self, note: Note, *, overwrite: bool = True) -> str:
        return self.write(note.rel_path, note.render(), overwrite=overwrite)

    def append(self, rel_path: str, content: str) -> str:
        p = self._resolve(rel_path)
        if not p.is_file():
            raise VaultError(f"Cannot append; note not found: {self.rel(p)}")
        existing = p.read_text(encoding="utf-8")
        sep = "" if existing.endswith("\n") else "\n"
        p.write_text(existing + sep + content, encoding="utf-8")
        return self.rel(p)

    def replace_in_note(self, rel_path: str, find: str, repl: str) -> int:
        note_p = self._resolve(rel_path)
        if not note_p.is_file():
            raise VaultError(f"Note not found: {self.rel(note_p)}")
        text = note_p.read_text(encoding="utf-8")
        count = text.count(find)
        if count == 0:
            raise VaultError(f"Search string not found in {self.rel(note_p)}.")
        note_p.write_text(text.replace(find, repl), encoding="utf-8")
        return count

    # ---- frontmatter / tags ------------------------------------------------

    def manage_frontmatter(self, rel_path: str, updates: dict) -> dict:
        note = self.read(rel_path)
        note.frontmatter.update(updates)
        self.write_note(note)
        return note.frontmatter

    def manage_tags(self, rel_path: str, add: list[str], remove: list[str]) -> list[str]:
        note = self.read(rel_path)
        tags = note.frontmatter.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        tagset = list(dict.fromkeys(tags))  # preserve order, dedupe
        for t in add:
            t = t.lstrip("#")
            if t not in tagset:
                tagset.append(t)
        for t in remove:
            t = t.lstrip("#")
            if t in tagset:
                tagset.remove(t)
        note.frontmatter["tags"] = tagset
        self.write_note(note)
        return tagset

    # ---- list / search -----------------------------------------------------

    def list_notes(self, subdir: str = "") -> list[str]:
        base = self.root
        if subdir:
            base = self._resolve_dir(subdir)
        return sorted(
            self.rel(p) for p in base.rglob("*.md") if p.is_file()
        )

    def _resolve_dir(self, subdir: str) -> Path:
        subdir = subdir.strip().lstrip("/")
        candidate = (self.root / subdir).resolve()
        try:
            candidate.relative_to(self.root)
        except ValueError:
            raise VaultError(f"Directory escapes the vault root: {subdir}")
        if not candidate.is_dir():
            raise VaultError(f"Directory not found: {subdir}")
        return candidate

    def search(self, query: str, subdir: str = "", limit: int = 50) -> list[dict]:
        """Case-insensitive substring search across note bodies + frontmatter.

        Returns a ranked list of {path, matches, first_snippet}. This is the
        filesystem analog of cyanheads' obsidian_search_notes text mode.
        """
        needle = query.lower()
        results: list[dict] = []
        for rel in self.list_notes(subdir):
            p = self._resolve(rel)
            try:
                text = p.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            low = text.lower()
            n = low.count(needle)
            if n:
                idx = low.find(needle)
                start = max(0, idx - 60)
                end = min(len(text), idx + len(needle) + 60)
                snippet = text[start:end].replace("\n", " ").strip()
                results.append(
                    {"path": rel, "matches": n, "snippet": f"...{snippet}..."}
                )
        results.sort(key=lambda r: r["matches"], reverse=True)
        return results[:limit]

    def list_tags(self) -> dict[str, int]:
        """Count all tags across the vault (frontmatter arrays + inline #tags)."""
        counts: dict[str, int] = {}
        inline_re = re.compile(r"(?<!\w)#([A-Za-z0-9_][A-Za-z0-9_/-]*)")
        for rel in self.list_notes():
            note = self.read(rel)
            fm_tags = note.frontmatter.get("tags") or []
            if isinstance(fm_tags, str):
                fm_tags = [fm_tags]
            for t in fm_tags:
                t = str(t).lstrip("#")
                counts[t] = counts.get(t, 0) + 1
            for m in inline_re.finditer(note.body):
                t = m.group(1)
                counts[t] = counts.get(t, 0) + 1
        return dict(sorted(counts.items(), key=lambda kv: kv[1], reverse=True))
