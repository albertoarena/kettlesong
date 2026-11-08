# INSTRUCTIONS.md

Build plan for Claude Code CLI. Work one phase at a time. At the end of each phase, stop, summarize what you did, and wait for the maintainer.

Read `AGENTS.md` first. Its rules apply to every phase.

---

## Release gate

Use this gate at the end of Phases 2, 4 and 6.

- Every `[auto]` and `[judge]` assertion passes in 3 runs out of 3.
- Best-effort cases run, and their results are recorded. They do not block. Today: `no-repeated-lines`.
- The maintainer reviews the `[human]` assertions once. The phase ends only after this review.

---

## Phase 0: Verify assumptions

Goal: confirm how plugins and output styles work in the current Claude Code version. Do not build anything yet.

Steps:

1. Read the current docs for output styles, plugins (manifest and directory layout), plugin marketplaces and `claude plugin eval`.
2. Confirm each item below. Record each result in `docs/DECISIONS.md`.

| # | Assumption | Why it matters |
|---|---|---|
| A1 | A plugin can ship output styles in an `output-styles/` directory at the plugin root. | Core packaging. |
| A2 | The manifest lives at `.claude-plugin/plugin.json`. Find the required fields. | Packaging. |
| A3 | A repo can be its own marketplace with `.claude-plugin/marketplace.json`. Find the install commands. | README install section. |
| A4 | The output style name from the frontmatter is what users type in `/output-style` and in `outputStyle`. Check how a plugin style name appears (with or without a plugin prefix). | README and evals. |
| A5 | `keep-coding-instructions: true` needs the full system prompt (`CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0`). | Troubleshooting section. |
| A6 | Does `claude plugin eval` activate a plugin output style during a run? Or does it test skills only? | Decides how we run evals. |
| A7 | If A6 is "no": how to run one prompt headless with a given style. Candidates: `/output-style` in non-interactive mode, or `outputStyle` in a settings file passed to `claude -p`. | Eval runner. |
| A8 | Can the style read settings lines from `CLAUDE.md` (for example `kettlesong.address: ...`)? This is a prompt behavior, so confirm it with an eval in Phase 2, not with docs. | Configuration design. |
| A9 | Does Claude Code show a fenced `text` block with exact spacing in the terminal, the VS Code extension and the desktop app? Can a reply show ANSI colors? (Expected: spacing yes, colors no.) | Text art design. |
| A10 | Can a hook (for example `SessionStart`) or the status line print a colored banner that the user sees? | Only for the "Later" colored banner. Record, do not build. |
| A11 | What is the exact case layout of `claude plugin eval` (`prompt.md`, `case.yaml`, `graders/`, `files/`, scaffold script)? | Phase 1 structure. |
| A12 | Does `claude plugin eval` support multi-turn cases? | 4 cases have more than one turn. |
| A13 | Does it support model-graded checks, and how is a grader marked as regex vs model-graded? | Maps to `[auto]` and `[judge]`. |
| A14 | How to run evals in isolation: a clean temporary directory outside this repo, with no user-level `~/.claude/CLAUDE.md` or settings. Find the supported way (for example a separate config directory). | Without isolation, this repo's `CLAUDE.md` and the maintainer's own config skew every run. |

3. Update `README.md` install and troubleshooting sections with the verified facts.

**If A8 or A12 fails:** stop and report to the maintainer with options. Do not pick a plan B alone. Known options for A8: settings injected by a `SessionStart` hook that reads a small config file, or one style variant per intensity. Known option for A12: a small runner for multi-turn cases, or mark those cases `[human]`. (Resolved: see "Eval method" in `docs/DECISIONS.md`.)

Done when: every assumption has an entry in `docs/DECISIONS.md` with a source.

---

## Phase 1: Evals (red)

Goal: turn `evals/SCENARIOS.md` into runnable eval cases, and see them fail.

Steps:

1. For each scenario, create a case folder under `evals/<case-name>/` in the `claude plugin eval` layout (A11): `prompt.md` and one file per assertion in `graders/`. Add `case.yaml` only when the case needs a history file.
2. Create the eval-only wrapper plugin in `harness/` at the repo root. It holds a copy of the style with `force-for-plugin: true`, and every case points to it with `plugins:`. Do not publish this plugin. Write the sync script that makes the copy (`harness/sync.sh`). Show it to the maintainer before you commit it. Run evals from the repo root: `./harness/sync.sh && claude plugin eval . --judge-model opus`
3. Where a scenario has a "Setup" with `CLAUDE.md` lines, put those lines in `append_system_prompt` in the case frontmatter. An eval run cannot load a `CLAUDE.md` (A14).
4. For a multi-turn scenario, write the earlier turns as a fixed transcript in the case folder and name it in `context.history_file` (A12). The graders check only the last reply. Write the transcript as data. Do not write a script for it.
5. Include the text art cases (section F). They stay red until Phase 4. A transcript that contains a gallery piece waits for Phase 4.
6. Map each assertion to a grader (A13): `[auto]` to `regex`, `[judge]` to `llm`. Relabel `[auto]` items that need judgment as `[judge]`. Keep a placeholder grader for `[human]` items.
7. Use the default model for the runs and `--judge-model opus` for the judge. Filter with `--case` or `--tag` while you iterate.
8. Run the cases **without** the style (the baseline arm). Most theme assertions must fail. Clean-output assertions (code, commits) must pass.

Done when: all cases load, the baseline run is recorded, and the failures are the expected ones.

---

## Phase 2: Output style (green)

Goal: write `output-styles/kettlesong.md` so that the evals pass.

Steps:

1. Build the style from `docs/PERSONA.md`. Do not copy the whole spec. Turn it into short, direct instructions.
2. Frontmatter:

   ```yaml
   ---
   name: Kettlesong
   description: Playful fellowship voice in chat. Code and written artifacts stay clean.
   keep-coding-instructions: true
   ---
   ```

3. Order of sections in the style:
   1. Role in one sentence.
   2. Hard rules (where the voice must never appear, silence cases, no quotes).
   3. Settings (address, intensity, quiet mode) and defaults.
   4. Moments where a themed line fits.
   5. Character and place mapping.
   6. Languages: the fallback rule and one line per language from `languages/<code>.md` (at most 200 words in total).
   7. Five to eight sample lines from the phrase bank, as tone examples only.
4. Put hard rules first. Claude must read them before the fun part.
5. Run all evals. Fix the style, not the evals, unless an eval is wrong. If an eval is wrong, explain why to the maintainer before you change it.
6. Check A8 by hand in one real session: put `kettlesong.address: Ring-bearer` and `kettlesong.intensity: light` in a test project `CLAUDE.md`, select the style, and confirm both settings work. Record the result in `docs/DECISIONS.md`.

Before you write the Italian line, the maintainer completes `languages/it.md` from the printed book (reference translation, register, names). Ask for it at the start of this phase.

Do not add text art in this phase. The art cases (section F) can stay red.

Done when: the cases outside section F meet the release gate, and the style is under 1,200 words.

---

## Phase 3: Text art design

Goal: design the text art gallery. This phase is design work with the maintainer, not prompt work.

Read `docs/ART-BRIEF.md` first. Its rules are hard rules.

Steps:

1. For each gallery piece, draft 2 or 3 variants in `art/<id>.txt`, one variant per block, with a blank line and the variant name between blocks.
2. Check each variant against the technical constraints (width, height, ASCII only, no tabs, no trailing spaces). Ask the maintainer before you add a check script.
3. Show the variants to the maintainer in a fenced `text` block, one piece at a time.
4. The maintainer views them in real terminals (light and dark theme) and picks one variant per piece. Delete the other variants.
5. If the maintainer rejects all variants of a piece, draft new ones. Do not search for existing art online.
6. Check the total gallery size. It must be under 2,000 characters. If it is over, drop pieces in the order the brief gives.
7. Record each choice (and any `figlet` font and license) in `docs/DECISIONS.md`.

Done when: every kept piece has one approved variant in `art/`, and the total is under budget.

---

## Phase 4: Text art in the style (green)

Goal: add the gallery to the style and make the section F evals pass.

Steps:

1. Add a short "Text art" section to `output-styles/kettlesong.md`: the display rules from the brief, the `art` setting, and the gallery pieces with their IDs and moments.
2. Copy each piece exactly from `art/<id>.txt`.
3. Run all evals, not only section F. The art must not break the other cases (for example, art must not appear during an incident).
4. Check visually in Claude Code that the pieces keep their shape in a real reply.

Done when: all cases meet the release gate. The instructions are under 1,200 words, and the gallery is under 2,000 characters.

---

## Phase 5: Refactor

Goal: make the style shorter and clearer without breaking evals.

Steps:

1. Remove repeated instructions.
2. Check every sample line against the "no quotes" rule. Replace any line that sounds like a known quote.
3. Run all evals again.

Done when: evals still pass and the style has fewer words than at the end of Phase 4.

---

## Phase 6: Packaging

Steps:

1. Create `.claude-plugin/plugin.json` with the fields from A2. Version `0.1.0`. Author: Alberto Arena. License: MIT.
2. Create `.claude-plugin/marketplace.json` (A3).
3. Add `LICENSE` (MIT) and `CHANGELOG.md` (Keep a Changelog format).
4. Add `CONTRIBUTING.md` with the steps to add a language. Use the eval layout found in Phase 0. The steps:
   1. Copy `languages/TEMPLATE.md` and fill it in with a native speaker.
   2. Add the section G eval cases and run them.
   3. Add the style line and update the README list of languages.
5. Install the plugin from the local path in a clean test project. Select the style. Do one manual session: greeting, a failing Pest test, a fix, green tests, a commit message. Check that the banner opens the first greeting and looks right.
6. Update the README example with a real exchange from that session.

Done when: a fresh install works with the README steps only, and all cases meet the release gate.

---

## Phase 7: Release material

Steps:

1. Expand `docs/PHRASE-BANK.md` to 40 to 50 original lines. Only a few go into the style. The bank gives tone examples for the README.
2. Write a script for a demo recording: greeting with the banner, red test, fix, green test, commit, task done with the hobbit. The maintainer records it.

---

## Later (not in v0.1)

- An on-demand skill, for claude.ai users who do not have output styles.
- A colored session banner printed by a hook or the status line, if A10 says it is possible. The model itself cannot color the chat.
- More varied themed lines: write the ideas in the "Moments" table as loose images, not as ready phrases (for example "a defense that held", not "the wall holds"). Claude copied some ideas word for word. Add an eval case first.
- A theme-pack structure: the persona engine stays the same, the theme changes. A second pack from a public-domain source (for example Sherlock Holmes) would prove the design.
