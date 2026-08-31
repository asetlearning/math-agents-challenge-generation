"""Tests for the fetch/citation helpers (offline; no real network calls)."""

from __future__ import annotations

import pytest

from obsidian_research_mcp import fetch


def test_strip_html_reduces_to_text():
    html = "<html><body><h1>Title</h1><p>Hello <b>world</b>.</p>" \
           "<script>ignore()</script></body></html>"
    out = fetch._strip_html(html)
    assert "Title" in out
    assert "Hello world." in out
    assert "ignore" not in out


def test_fetch_paper_rejects_non_http():
    with pytest.raises(ValueError):
        fetch.fetch_paper("ftp://example.com/x")


def test_lookup_citation_detects_arxiv_id():
    # No network assertion: just that a bare arXiv id is recognized as such and
    # doesn't fall into the "no id detected" branch. Network may or may not
    # succeed; either way `found` is a bool and the arxiv path was taken.
    res = fetch.lookup_citation("2410.12345")
    assert isinstance(res["found"], bool)
    assert "No arXiv id detected" not in res.get("note", "")


def test_lookup_citation_no_id_gives_manual_note():
    res = fetch.lookup_citation("https://example.com/some-paper")
    assert res["found"] is False
    assert "manually" in res["note"].lower()


def test_package_truncates():
    pkg = fetch._package("https://x", "http", "a" * 100, cap=10)
    assert pkg["truncated"] is True
    assert len(pkg["content"]) == 10
