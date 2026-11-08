#!/usr/bin/env python3
"""Build the exact-match text art graders from art/*.txt.

Run from the repo root after you change a piece in art/:
    python3 evals/build-art-graders.py
Then update the banner in evals/art-never-two-replies-in-a-row/history.jsonl.

The banner is shown in a fenced `diff` block. Each line starts with "+  ",
so Claude Code shows it in color.
"""
import glob
import json
import os
import re

BANNER_CASES = ["art-banner-at-default-setting", "art-banner-on-first-greeting"]
GALLERY_CASE = "art-is-exact-copy"
MOMENT_CASES = {
    "art-matches-moment": "elf-bow",
    "art-dwarf-on-green": "dwarf-axe",
    "art-wizard-on-refactor": "wizard",
}
BANNER_PREFIX = "+  "


def escape(line):
    # Write "-" as \x2d: the eval loader reads "---" as the end of the frontmatter.
    return re.sub(r"([\\^$.*+?()\[\]{}|/])", r"\\\1", line).replace("-", r"\x2d")


def piece_pattern(path, prefix=""):
    lines = open(path).read().rstrip("\n").split("\n")
    return r"[ \t]*\r?\n".join(escape(prefix + line.rstrip()) for line in lines) + r"[ \t]*"


def write_grader(path, front, body):
    with open(path, "w") as f:
        f.write("---\n")
        for key, value in front.items():
            f.write(f"{key}: {json.dumps(value)}\n")
        f.write("---\n\n" + body + "\n")


pieces = {os.path.basename(p)[:-4]: piece_pattern(p) for p in sorted(glob.glob("art/*.txt"))}

banner = r"```diff[ \t]*\r?\n" + piece_pattern("art/banner.txt", BANNER_PREFIX) + r"\r?\n```"
for case in BANNER_CASES:
    write_grader(
        f"evals/{case}/graders/banner-exact.md",
        {"type": "regex", "pattern": banner},
        "The reply contains the `banner` piece from art/banner.txt, exactly, in a fenced `diff` block with \"+  \" before each line. Generated from art/banner.txt.",
    )

for case, piece in MOMENT_CASES.items():
    write_grader(
        f"evals/{case}/graders/{piece}-exact.md",
        {"type": "regex", "pattern": r"```text[ \t]*\r?\n" + pieces[piece] + r"\r?\n```"},
        f"The reply contains the `{piece}` piece from art/{piece}.txt, exactly, in a fenced `text` block. Generated from art/{piece}.txt.",
    )

any_piece = r"```text[ \t]*\r?\n(?!(?:" + "|".join(pieces.values()) + r")\r?\n```)"
write_grader(
    f"evals/{GALLERY_CASE}/graders/gallery-exact.md",
    {"type": "regex", "pattern": any_piece, "match": "not_contains"},
    "FAIL if a fenced `text` block is not an exact copy of a piece in art/. A reply with no text block passes. Generated from art/*.txt.",
)
print(f"Built graders for {len(pieces)} pieces.")
