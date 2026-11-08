# Text art brief

Design brief for the small text images (ASCII art) that Kettlesong shows from time to time in chat.

## 1. Goal

Add a visual surprise to a session: a small figure (an elf, a dwarf, a wizard, a hobbit) or a short banner, at a few key moments. The art must look good in any terminal, cost few tokens, and never get in the way of the work.

## 2. Why a fixed gallery

Language models are weak at drawing text art on the fly. Lines shift, shapes break, and every reply looks different. For this reason:

- We **design a fixed gallery** of pieces by hand, test them in real terminals, and put them in the style.
- Claude **picks** a piece from the gallery. Claude does **not** draw new art.

## 3. Legal rules

- **Generic archetypes only:** an elf archer, a dwarf with an axe, a wizard with a pointed hat and a staff, a hobbit-like figure with a teacup, a volcano, a tower, a dragon or a fire demon.
- **No likeness** of a specific film character, actor, costume, logo, map, inscription or prop design.
- **Original work.** Do not copy art from websites, art archives or other tools. Do not trace a figure from a film still.
- **Reference images** in issues or chats (for example banners from other CLI tools) are mood references only. Do not copy their shapes or mascots.
- **Banner fonts.** If a banner is made with `figlet` or `toilet`, record the font name and its license in `docs/DECISIONS.md`. Use only fonts with a free license that allows redistribution. Hand-made letters are also fine.

## 4. Technical constraints

| Constraint | Value | Reason |
|---|---|---|
| Max width | 40 columns | Fits narrow terminals and split panes |
| Max height | 8 lines (figures and banner) | Small surprise, not a wall |
| Characters | printable ASCII only (code 32 to 126) | Alignment is the same in every font |
| No tabs | spaces only | Tabs break alignment |
| No trailing spaces | trimmed lines | Clean diffs |
| Color | banner only | Claude cannot emit colors. A `diff` block with `+  ` before each line shows the banner in green. Figures have no color |
| Total gallery size | under 2,000 characters | The style is sent with every request |
| No words inside figures | wordless | Keeps the evals simple, works in every language |

## 5. Gallery (pieces to design)

| ID | Piece | Moment | Notes |
|---|---|---|---|
| `banner` | "kettlesong" letters, on two lines ("kettle", "song") | first greeting of a session | The only piece with letters |
| `hobbit-tea` | small figure with a teacup or plate | task done | The signature piece |
| `dwarf-axe` | short wide figure, big beard, raised axe | tests pass after a fix | Celebration of a hard-won victory (matches the Gimli mapping) |
| `elf-bow` | tall thin figure with a drawn bow | bug found | Sharp eyes |
| `wizard` | pointed hat, staff, long beard | refactor or design proposal | Wisdom |
| `fire-demon` | horns, flames, or a small dragon | severe bug or a risk of data loss | Danger, keep it friendly |
| `volcano` | mountain with smoke | production deploy or release | Serious moment |

Seven pieces is the maximum for v0.1. If the gallery is over budget, drop `volcano` first, then `fire-demon`.

## 6. Display rules (for the style)

- At `often` (the default), show a piece at every moment that matches it. At `rare`, about one piece every 10 to 15 replies. Never in two replies in a row.
- **Banner exception:** the `banner` always opens the first greeting of a session, at `rare` and `often`. It does not count toward the frequency, but it does count for "never in two replies in a row". It is skipped when art is `off` or a silence rule applies.
- Art does not count toward the themed-line limit.
- Show art only at the moment that matches the piece (table above).
- Put the art alone in a fenced block with the `text` language tag, at the start or at the end of the reply. Never inside a technical explanation.
- The banner goes in a fenced `diff` block instead, with `+  ` (a plus and two spaces) before each line. Claude Code shows these lines in green. The source in `art/banner.txt` has no prefix.
- Copy the piece exactly. Do not change, mirror or redraw it.
- Art follows the same silence rules as the themed lines (incidents, security, frustration, "quiet, please").
- Setting in `CLAUDE.md`: `kettlesong.art: off | rare | often`. Default: `often`. At intensity `light`, the default is `off`.

Note: a model cannot keep an exact count over a long session. "About one in 10 to 15 replies" is a target, not a guarantee. The evals check the hard limits (banner on the first greeting, no art in two replies in a row, no art when silent, no art when `off`) and three moments at the default setting (`elf-bow`, `dwarf-axe`, `wizard`).

## 7. Design process

1. Draft 2 or 3 variants of each piece in `art/<id>.txt`.
2. Check each variant against section 4 with a simple command (`awk` line length, `grep -P '[^\x20-\x7E]'` for non-ASCII). Ask the maintainer before adding a script for this.
3. View each variant in at least: macOS Terminal, iTerm2, the VS Code terminal, and Claude Code itself, with a light theme and a dark theme.
4. The maintainer picks one variant per piece. Delete the others.
5. Record the choice in `docs/DECISIONS.md`.
