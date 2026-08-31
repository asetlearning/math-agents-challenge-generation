"""Tests for the filesystem vault layer (no network, no MCP runtime needed)."""

from __future__ import annotations

from pathlib import Path

import pytest

from obsidian_research_mcp.vault import Note, Vault, VaultError


@pytest.fixture
def vault(tmp_path: Path) -> Vault:
    (tmp_path / "_meta").mkdir()
    (tmp_path / "Research" / "Group theory").mkdir(parents=True)
    (tmp_path / "Research" / "Group theory" / "havas-1980.md").write_text(
        "---\ntitle: Test Paper\ndomain: group-theory\nstatus: draft\n"
        "tags:\n  - paper\n  - topic/burnside-groups\n---\n\n"
        "# Test Paper\n\nBody mentions Burnside and Knuth-Bendix.\n",
        encoding="utf-8",
    )
    return Vault(tmp_path)


def test_read_parses_frontmatter_and_body(vault: Vault):
    note = vault.read("Research/Group theory/havas-1980.md")
    assert note.frontmatter["title"] == "Test Paper"
    assert note.frontmatter["domain"] == "group-theory"
    assert "Burnside" in note.body


def test_path_traversal_rejected(vault: Vault):
    with pytest.raises(VaultError):
        vault.read("../../etc/passwd")


def test_write_and_roundtrip(vault: Vault):
    note = Note(
        rel_path="Research/Group theory/new-note.md",
        frontmatter={"title": "New", "status": "draft"},
        body="# New\n\nHello.",
    )
    written = vault.write_note(note)
    assert written.endswith("new-note.md")
    back = vault.read(written)
    assert back.frontmatter["title"] == "New"
    assert "Hello" in back.body


def test_overwrite_false_guards(vault: Vault):
    with pytest.raises(VaultError):
        vault.write(
            "Research/Group theory/havas-1980.md", "x", overwrite=False
        )


def test_append(vault: Vault):
    vault.append("Research/Group theory/havas-1980.md", "\nAppended line.")
    assert "Appended line." in vault.read("Research/Group theory/havas-1980.md").body


def test_search_ranks_matches(vault: Vault):
    results = vault.search("burnside")
    assert results
    assert results[0]["path"].endswith("havas-1980.md")
    assert results[0]["matches"] >= 1


def test_manage_frontmatter_merges(vault: Vault):
    fm = vault.manage_frontmatter(
        "Research/Group theory/havas-1980.md", {"status": "review", "year": 1980}
    )
    assert fm["status"] == "review"
    assert fm["year"] == 1980
    # unchanged keys preserved
    assert fm["title"] == "Test Paper"


def test_manage_tags_add_remove(vault: Vault):
    tags = vault.manage_tags(
        "Research/Group theory/havas-1980.md",
        add=["#topic/word-problem", "status/draft"],
        remove=["paper"],
    )
    assert "topic/word-problem" in tags
    assert "paper" not in tags


def test_list_tags_counts(vault: Vault):
    counts = vault.list_tags()
    assert counts.get("topic/burnside-groups", 0) >= 1


def test_list_notes(vault: Vault):
    notes = vault.list_notes("Research")
    assert any(n.endswith("havas-1980.md") for n in notes)
