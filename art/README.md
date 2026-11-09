# Art sources

One file per gallery piece: `<id>.txt`. See `docs/ART-BRIEF.md` for rules and IDs.

These files are the source of truth. The output style contains copies. The README cover (`cover-light.svg`, `cover-dark.svg`) is built from the `banner` and four figures.

## Change a piece

Run all commands from the repo root.

1. Edit `art/<id>.txt`. Follow the size and character rules in `docs/ART-BRIEF.md`.
2. Copy the piece into `plugin/output-styles/kettlesong.md`, section "Text art":
   - A figure goes in a fenced `text` block, exactly as in the source.
   - The banner goes in a fenced `diff` block. Put `+  ` (a plus and two spaces) before each line.
3. Rebuild the graders: `python3 evals/build-art-graders.py`.
4. If you changed the banner, update it in `evals/art-never-two-replies-in-a-row/history.jsonl`. Use the `diff` form from step 2.
5. If you changed the banner, `elf-bow`, `dwarf-axe`, `wizard` or `hobbit-tea`, rebuild the README cover: `python3 art/build-cover.py`.
6. Run the evals and check that all cases pass. See `CONTRIBUTING.md`, section "Run the evals".
