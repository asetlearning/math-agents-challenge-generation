"""Paper fetching + citation lookup — the research-handle extras that generic
Obsidian MCP servers (cyanheads et al.) don't provide.

`fetch_paper` mirrors the skill's `defuddle <url>` step with a pure-Python
fallback, so no Node.js is required. Order of attempts:
  1. `defuddle parse <url> --md` if the CLI happens to be installed (best output)
  2. plain HTTP GET + HTML->text reduction (always available)

`lookup_citation` mirrors workflow step 6 (Semantic Scholar / arXiv).
"""

from __future__ import annotations

import html
import re
import shutil
import subprocess

import httpx

_UA = "obsidian-research-mcp/0.1 (+https://github.com/ai-math-edu-lab)"
_TIMEOUT = 30.0


def _strip_html(raw_html: str) -> str:
    """Very small HTML->text reducer for the no-defuddle fallback path."""
    # Drop scripts/styles wholesale.
    raw_html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw_html, flags=re.S | re.I)
    # Turn block-level closers into newlines so structure survives.
    raw_html = re.sub(r"</(p|div|h[1-6]|li|br|tr|section|article)>", "\n", raw_html, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", raw_html)
    text = html.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    # Inline tags leave a stray space before punctuation ("world ." -> "world.").
    text = re.sub(r" +([.,;:!?)\]])", r"\1", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text.strip()


def fetch_paper(url: str) -> dict:
    """Fetch a paper/web page as clean text.

    Returns {url, method, content, truncated}. Raises on unreachable source so
    the model can fall back / ask the user, exactly as the skill prescribes.
    """
    url = url.strip()
    if not re.match(r"^https?://", url):
        raise ValueError(f"Not an http(s) URL: {url!r}")

    # Attempt 1: defuddle CLI (only if present; optional best-quality path).
    if shutil.which("defuddle"):
        try:
            out = subprocess.run(
                ["defuddle", "parse", url, "--md"],
                capture_output=True,
                text=True,
                timeout=_TIMEOUT,
            )
            if out.returncode == 0 and out.stdout.strip():
                return _package(url, "defuddle", out.stdout)
        except (subprocess.SubprocessError, OSError):
            pass  # fall through to HTTP

    # Attempt 2: plain HTTP + strip (always available, no Node).
    try:
        resp = httpx.get(
            url, headers={"User-Agent": _UA}, follow_redirects=True, timeout=_TIMEOUT
        )
        resp.raise_for_status()
    except httpx.HTTPError as e:
        raise RuntimeError(f"Could not fetch {url}: {e}") from e

    ctype = resp.headers.get("content-type", "")
    if "html" in ctype or resp.text.lstrip().startswith("<"):
        content = _strip_html(resp.text)
    else:
        content = resp.text
    return _package(url, "http", content)


def _package(url: str, method: str, content: str, cap: int = 40_000) -> dict:
    truncated = len(content) > cap
    return {
        "url": url,
        "method": method,
        "content": content[:cap],
        "truncated": truncated,
    }


_ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.I)


def lookup_citation(url_or_id: str) -> dict:
    """Best-effort citation count via Semantic Scholar.

    Mirrors workflow step 6. Returns {found, citation_count, source, title,
    year, note}. Never raises — citation lookup is best-effort by doctrine.
    """
    ident = url_or_id.strip()
    arxiv = _ARXIV_RE.search(ident)
    paper_id = f"arXiv:{arxiv.group(1)}" if arxiv else None
    if paper_id is None and re.fullmatch(r"\d{4}\.\d{4,5}", ident):
        paper_id = f"arXiv:{ident}"

    if paper_id is None:
        return {
            "found": False,
            "note": "No arXiv id detected; look up citation count manually "
            "(Google Scholar / Semantic Scholar) and record with date.",
        }

    api = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}"
    try:
        resp = httpx.get(
            api,
            params={"fields": "title,year,citationCount"},
            headers={"User-Agent": _UA},
            timeout=_TIMEOUT,
        )
        resp.raise_for_status()
        data = resp.json()
    except (httpx.HTTPError, ValueError) as e:
        return {
            "found": False,
            "note": f"Semantic Scholar lookup failed ({e}); record citation "
            "count manually with citation_count_date.",
        }

    return {
        "found": True,
        "citation_count": data.get("citationCount"),
        "title": data.get("title"),
        "year": data.get("year"),
        "source": "semantic-scholar",
        "note": "Record this under citation_count with today's date as "
        "citation_count_date.",
    }
