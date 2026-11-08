#!/usr/bin/env bash
# Copy the output style into the eval harness plugin and add force-for-plugin.
# The eval runs cannot select a style, so the harness forces it.
# Run this before each eval run. The copy is gitignored.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
src="$root/output-styles/kettlesong.md"
dst_dir="$root/harness/output-styles"
dst="$dst_dir/kettlesong.md"

mkdir -p "$dst_dir"

if [ ! -f "$src" ]; then
  rm -f "$dst"
  echo "No style at output-styles/kettlesong.md. The harness runs without a style."
  exit 0
fi

if [ "$(head -n 1 "$src")" != "---" ]; then
  echo "Error: the style must start with a frontmatter line '---'." >&2
  exit 1
fi

if grep -q '^force-for-plugin:' "$src"; then
  echo "Error: the style sets force-for-plugin. AGENTS.md hard rule 4 bans it." >&2
  exit 1
fi

awk 'NR == 1 { print; print "force-for-plugin: true"; next } { print }' "$src" > "$dst"
echo "Copied the style to harness/output-styles/ with force-for-plugin: true."
