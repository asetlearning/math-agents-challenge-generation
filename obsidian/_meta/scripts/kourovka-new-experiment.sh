#!/usr/bin/env bash
# kourovka-new-experiment.sh — scaffold the write-up directory for one Kourovka problem.
#
#   bash _meta/scripts/kourovka-new-experiment.sh <problem-id> <slug>
#   e.g. bash _meta/scripts/kourovka-new-experiment.sh 18.31 dpi-groups
#
# Creates Experiments/Kourovka/<id>-<slug>/{_experiment.md,methodology,results,data}
# from _TEMPLATE/, with <ID>, <slug> and the date substituted.
#
# Lead runs this at spawn time. The directory must exist BEFORE the problem agent
# starts — see _common-kourovka.md §12. Safe to re-run: it will not overwrite an
# existing directory.
#
# (Maria, 2026-08-20 — added after the August campaign left Experiments/Kourovka
#  completely empty for all sixteen problems it opened.)

set -euo pipefail

if [ $# -ne 2 ]; then
  echo "usage: $0 <problem-id> <slug>" >&2
  echo "   e.g. $0 18.31 dpi-groups" >&2
  exit 2
fi

ID="$1"
SLUG="$2"

# Resolve the vault root from this script's location (_meta/scripts/ -> vault root),
# so the script works regardless of the caller's cwd.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT="$(cd "$SCRIPT_DIR/../.." && pwd)"

TEMPLATE="$VAULT/Experiments/Kourovka/_TEMPLATE"
DEST="$VAULT/Experiments/Kourovka/${ID}-${SLUG}"

if [ ! -d "$TEMPLATE" ]; then
  echo "error: template not found at $TEMPLATE" >&2
  exit 1
fi

if [ -e "$DEST" ]; then
  echo "note: $DEST already exists — leaving it alone."
  exit 0
fi

# Validate the problem id looks like NN.MM, so a typo doesn't create a stray dir.
if ! printf '%s' "$ID" | grep -Eq '^[0-9]{1,2}\.[0-9]{1,3}[a-z]?$'; then
  echo "error: '$ID' does not look like a Kourovka problem id (expected e.g. 18.31)" >&2
  exit 1
fi

cp -R "$TEMPLATE" "$DEST"

# The per-cycle and per-artifact templates are scaffolding for the agent to copy;
# rename them so the directory doesn't read as if work has been done.
mv "$DEST/methodology/cycle-N-template.md" "$DEST/methodology/_template-cycle.md" 2>/dev/null || true
mv "$DEST/results/results-template.md"     "$DEST/results/_template-results.md"   2>/dev/null || true
mv "$DEST/data/data-template.md"           "$DEST/data/_template-data.md"         2>/dev/null || true

TODAY="$(date -u +%Y-%m-%d)"

# Substitute the placeholders. Portable in-place sed (GNU and BSD differ on -i).
find "$DEST" -name '*.md' -type f -print0 | while IFS= read -r -d '' f; do
  sed -e "s|<ID>|${ID}|g" \
      -e "s|<slug>|${SLUG}|g" \
      -e "s|opened: <YYYY-MM-DD>|opened: ${TODAY}|" \
      "$f" > "$f.tmp" && mv "$f.tmp" "$f"
done

# Drop the template-only rubric section from the real experiment note; it lives in
# _TEMPLATE/_experiment.md for reference and would be noise in every problem dir.
awk '/^## §12 — what "human-readable" means here/{exit} {print}' \
    "$DEST/_experiment.md" \
  | awk 'BEGIN{n=0} {lines[n++]=$0} END{
        while (n>0 && (lines[n-1]=="" || lines[n-1]=="---")) n--;
        for(i=0;i<n;i++) print lines[i]
    }' > "$DEST/_experiment.md.tmp" \
  && mv "$DEST/_experiment.md.tmp" "$DEST/_experiment.md"

cat >> "$DEST/_experiment.md" <<EOF

---

*Scaffolded ${TODAY}. Rubric for what "human-readable" means here:
[[Experiments/Kourovka/_TEMPLATE/_experiment|the template]], §12.*
EOF

echo "created $DEST"
echo
echo "Lead's next steps:"
echo "  1. Fill _experiment.md frontmatter (issue, page, proposers, tractability, shape)"
echo "  2. Transcribe the problem statement FROM THE SOURCE PDF (not the corpus text)"
echo "  3. Fill the 'Why this problem was selected' table, incl. first_computation"
echo "  4. Record the staleness check"
echo "  5. Add the row to Experiments/Kourovka/_kourovka.md"
