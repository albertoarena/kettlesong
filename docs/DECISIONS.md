# Decisions

One entry per decision. Newest at the bottom.

## 2026-11-05: Quote check is model-graded
Context: The `no-verbatim-quotes` case needs to detect known quotes. A regex needs a quote list, and hard rule 1 bans quotes in the repo.
Decision: Grade it with a model (`[judge]`), with no quote list in the repo. Add the `[judge]` level to the legend in `evals/SCENARIOS.md`.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Scaffold script is pre-approved
Context: Phase 1 needs a script to copy a case `files/` folder. `AGENTS.md` rule 7 asks for approval before any script.
Decision: Phase 1 approves the standard scaffold script only. Any other script still needs approval. `AGENTS.md` rule 7 has this exception.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Banner always opens the first greeting
Context: At `rare`, art is about one piece every 10 to 15 replies, so the banner could be missing in a demo or a short session.
Decision: The banner always opens the first greeting, at `rare` and `often`. It is skipped when art is `off` or a silence rule applies. It does not count toward the frequency. It does count for "never in two replies in a row". New case: `art-banner-at-default-setting`.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Address appears only inside a themed line
Context: Graders must know if a bare address is themed.
Decision: The address appears only inside a themed line. "Sure, master." in a plain answer counts as a themed line.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Art does not count toward the line limit
Context: The banner and the greeting line can appear in the same reply.
Decision: Text art does not count toward the themed-line limit.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: More eval tool assumptions in Phase 0
Context: Phase 1 depends on the case layout, multi-turn support and model-graded checks.
Decision: Add A11 (layout), A12 (multi-turn, 4 cases), A13 (model-graded checks) to Phase 0.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Evals run in isolation
Context: This repo's `CLAUDE.md` and the maintainer's user config can skew eval runs.
Decision: Run evals in a clean directory outside the repo, without user-level config. Added as A14 and Phase 1 step 3.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Stop if A8 or A12 fails
Context: The settings design depends on A8. Multi-turn cases depend on A12.
Decision: If either fails, stop and report options to the maintainer. Options for A8: a `SessionStart` hook that injects settings from a config file, or one style variant per intensity. Options for A12: a small runner, or mark the cases `[human]`.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Frequency at `often`
Context: `often` had no definition.
Decision: About one piece every 3 to 5 replies, never in two replies in a row.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Voice can come back after quiet mode
Context: Quiet mode had no way back.
Decision: The voice comes back when the user clearly asks ("voice on", "talk like a hobbit again"). New case: `quiet-then-resume`.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Address in other languages
Context: The user can write in another language.
Decision: Translate the default "master" to the form the hobbit servant uses in that language. Italian: "padrone" (the Italian translation uses "Padron Frodo"). Superseded: see "Italian reference translation and address". Use a single word only, never a phrase from a translation. A custom address is used exactly as written. New case: `lang-it-custom-address` (section G).
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Frustration and repetition cases
Context: Two persona rules had no eval.
Decision: New case `frustration-silent`. New multi-turn case `no-repeated-lines`, best-effort, does not block a release.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Scope of theme-term checks
Context: Words like "master" or "Sam" appear in technical text.
Decision: Silence checks ignore inline code and code blocks. Clean-artifact checks are model-graded, so technical uses are not themed. A custom address joins the theme terms for its case, and `custom-address-from-claude-md` also checks a commit message.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Borderline lines
Context: "This key is precious" leaned on a famous line.
Decision: The line is replaced. The phrase bank now has "This key belongs in the vault, master, never in the repository."
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Phrase bank expansion and Gimli mapping
Context: Phrase bank work is not refactoring. Gimli did not match `dwarf-axe`.
Decision: Move the phrase bank expansion to Phase 7. Gimli covers "brute-force fixes, and celebrating a hard-won victory".
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Relabel model-judged assertions in Phase 1
Context: The legend defines `[auto]` as script or regex. About 30 of 48 `[auto]` items need judgment (for example "contains exactly one themed line", "suggests a rollback").
Decision: In Phase 1, relabel these as `[judge]` while building the graders. Keep `[auto]` only for checks a regex can do.
Source: maintainer decision, 2026-11-05.

## 2026-11-05: Release gate
Context: "All automatic assertions pass 3 out of 3" did not say how `[judge]`, best-effort and `[human]` checks count.
Decision: At the end of Phases 2, 4 and 6, every `[auto]` and `[judge]` assertion passes 3 out of 3. Best-effort cases run and are recorded, but do not block (today: `no-repeated-lines`). The maintainer reviews `[human]` assertions once, and the phase ends after this review. See "Release gate" in `INSTRUCTIONS.md`.
Source: maintainer decision, 2026-11-05.

## 2026-11-06: Language structure
Context: The plugin is open source. Contributors must be able to add languages. The style is sent with every request, so it must stay small.
Decision: One file per language in `languages/<code>.md`, from `languages/TEMPLATE.md`. `PERSONA.md` uses neutral IDs for names. The style holds one line per language (at most 40 words) and a languages block of about 200 words. A `SessionStart` hook that loads one language is a later option. A language without a file keeps English names and translates the default address. `CONTRIBUTING.md` comes in Phase 6.
Source: maintainer decision, 2026-11-06.

## 2026-11-06: Languages in v0.1
Context: The scope of the first release.
Decision: English and Italian only, plus the template and `CONTRIBUTING.md`. No setting to force a language.
Source: maintainer decision, 2026-11-06.

## 2026-11-06: No quotes from translations
Context: Translations of the books are protected text.
Decision: Hard rule 1 also covers translations. Single words and names are allowed. Sentences are not.
Source: maintainer decision, 2026-11-06.

## 2026-11-06: Italian names and register
Context: Italian has more than one translation. The names and the register can differ.
Decision: Register: the formal "voi". Names: Contea, Gran Burrone, Cavalieri Neri, Anello, seconda colazione (the Italian film dubbing uses the same names). "Padron Frodo" is confirmed in the book (superseded: see "Italian reference translation and address"). Open: the maintainer confirms "voi" and chooses the reference edition (translator, publisher, year) before Phase 2.
Source: maintainer decision, 2026-11-06.

## 2026-11-06: No grammatical gender rule in v0.1
Context: The default address and some greetings are gendered in Italian and in other languages.
Decision: No gender rule in v0.1. Sample lines avoid gendered words. Users who want another form set a custom address.
Source: maintainer decision, 2026-11-06.

## 2026-11-06: Workflow that removes attribution from pull requests
Context: Cloud sessions can add an attribution line to a pull request body. `AGENTS.md` bans AI attribution.
Decision: Add `.github/workflows/strip-attribution.yml`. It removes these lines when a pull request is opened or edited. It does not check out code.
Source: maintainer decision, 2026-11-06.

## 2026-11-06: A1 Output styles in a plugin
Context: Core packaging.
Decision: Confirmed. A plugin ships styles in `output-styles/` at the plugin root. No manifest field is needed. The optional `outputStyles` field replaces the default folder.
Source: https://code.claude.com/docs/en/output-styles.md ("Plugins can also ship output styles in an `output-styles/` directory"), https://code.claude.com/docs/en/plugins/manifest-reference.md

## 2026-11-06: A2 Manifest fields
Context: Packaging.
Decision: Confirmed. The manifest is `.claude-plugin/plugin.json`. `name` is the only required field (kebab-case). `version`, `description` and `author` are recommended. `license`, `homepage`, `repository` and `keywords` are optional.
Source: https://code.claude.com/docs/en/plugins/manifest-reference.md ("`name` is the only required key")

## 2026-11-06: A3 Repo as its own marketplace
Context: README install section.
Decision: Confirmed. `.claude-plugin/marketplace.json` needs `name`, `owner.name` and `plugins`. A plugin at the repo root uses `"source": "./"`. Install: `/plugin marketplace add albertoarena/kettlesong`, then `/plugin install kettlesong@<marketplace name>`. CLI: `claude plugin marketplace add` and `claude plugin install`.
Source: https://code.claude.com/docs/en/plugins/marketplace-reference.md

## 2026-11-06: A4 Name of a plugin style
Context: README and evals need the exact style name.
Decision: A plugin style has the plugin prefix: `<plugin>:<style name>`. In a test, `outputStyle: "probe:Probe"` activated the style. `outputStyle: "Probe"` did not. The value is case-sensitive, and a wrong value falls back to the Default style with no error. For this plugin: `kettlesong:Kettlesong`. Check the `/output-style` argument in Phase 6. `/output-style` and `/config` both work.
Source: local test with Claude Code 2.1.287 (`claude -p --plugin-dir <probe> --settings '{"outputStyle":"probe:Probe"}'`). https://code.claude.com/docs/en/output-styles.md ("A value that doesn't match a style name exactly ... gives you the Default style"). The docs do not mention the prefix.

## 2026-11-06: A5 keep-coding-instructions and the system prompt
Context: Troubleshooting section.
Decision: Confirmed. The field works only on the full system prompt. `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0` selects the full prompt on any model.
Source: https://code.claude.com/docs/en/output-styles.md

## 2026-11-06: A6 Output styles in claude plugin eval
Context: Decides how we run evals.
Decision: An eval run does not select a plugin style, and a case has no field for it. A style with `force-for-plugin: true` is active in an eval run (local test: pass with the plugin, fail without). Hard rule 4 bans this field in the shipped style, so the evals need another method. See "Eval method" (open).
Source: local test with Claude Code 2.1.287. https://code.claude.com/docs/en/plugin-evals.md (prompt.md and case.yaml field tables)

## 2026-11-06: A7 One headless prompt with a style
Context: Fallback eval runner.
Decision: Confirmed. `claude -p --plugin-dir <path> --settings '{"outputStyle":"<plugin>:<style>"}' "<prompt>"`. There is no `--output-style` flag.
Source: local test. https://code.claude.com/docs/en/headless.md

## 2026-11-06: A9 Text art and colors in replies
Context: Text art design.
Decision: Not documented. The docs say nothing about how fenced blocks keep spacing in the terminal, VS Code or the desktop app, or about ANSI colors in replies. Check by hand in Phase 3.
Source: https://code.claude.com/docs/en/terminal-config.md (no section on this)

## 2026-11-06: A10 Colored banner from a hook or the status line
Context: "Later" colored banner. Record only.
Decision: The status line supports ANSI colors. `SessionStart` plain stdout goes to Claude's context, not to the user. A hook `systemMessage` is shown to the user as a warning. A colored status line is the realistic option.
Source: https://code.claude.com/docs/en/statusline.md, https://code.claude.com/docs/en/hooks.md ("Claude Code adds plain-text stdout as context")

## 2026-11-06: A11 Eval case layout
Context: Phase 1 structure.
Decision: A case is `evals/<case>/prompt.md` (frontmatter and prompt) with `graders/<name>.md`. `case.yaml` is optional and adds `context.scaffold_script`, `context.history_file` and `context.add_dirs`. There is no `files/` folder: a scaffold script creates files, and it runs only with `--scaffold`. Runs per case default to 3.
Source: https://code.claude.com/docs/en/plugin-evals.md. Local `claude plugin eval init --bare`.

## 2026-11-06: A12 Multi-turn cases
Context: 4 cases have more than one turn.
Decision: Partly supported. A case can resume a saved `.jsonl` transcript with `context.history_file`. The prompt becomes the next turn. The earlier replies are fixed in the file, so Claude does not write them during the run. There is no other multi-turn syntax. Open: see "Eval method".
Source: https://code.claude.com/docs/en/plugin-evals.md ("the case's prompt becomes the next user turn")

## 2026-11-06: A13 Grader types
Context: Maps to `[auto]` and `[judge]`.
Decision: Confirmed. `[auto]` maps to `regex`, `tool_used`, `tool_order` or `file_exists`. `[judge]` maps to `llm`, with a plain-language rubric in the grader body (judge model: haiku by default, majority of 3 votes). `[human]` has no grader type.
Source: https://code.claude.com/docs/en/plugin-evals.md. Local test (`judge votes: FAIL FAIL FAIL`).

## 2026-11-06: A14 Eval isolation
Context: This repo's config and the maintainer's config must not skew runs.
Decision: Confirmed, built in. Each run has a temporary home, config and workspace. No user or project `CLAUDE.md`, settings, hooks or other plugins load. This also means a `CLAUDE.md` with `kettlesong.*` lines cannot reach a run, even if a scaffold script writes it. Open: see "Eval method".
Source: https://code.claude.com/docs/en/plugin-evals.md ("no `.claude/` directory, `CLAUDE.md`, or `.mcp.json` loads ... even one a `scaffold_script` wrote")

## 2026-11-06: A8 Settings from CLAUDE.md
Context: Configuration design. The plan checks A8 with an eval in Phase 2.
Decision: Deferred to Phase 2. A14 shows that an eval run cannot load a `CLAUDE.md`, so the Phase 2 check needs another method. See "Eval method" (open).
Source: https://code.claude.com/docs/en/plugin-evals.md

## 2026-11-06: Eval method
Context: A6, A12 and A14 change the Phase 1 plan. An eval run does not select the style, cannot load `CLAUDE.md`, and has no native multi-turn cases.
Decision:
- Style: an eval-only wrapper plugin in `harness/` holds a copy of the style with `force-for-plugin: true`. It is never published, so hard rule 4 still holds for the shipped style. A sync script makes the copy. This replaces the scaffold script exception in `AGENTS.md` rule 7.
- Settings: the `CLAUDE.md` lines of a case go into `append_system_prompt`. This is close but not exact, so Phase 2 adds one manual check of A8 in a real session.
- Multi-turn: each case has a fixed transcript in `context.history_file`. The graders check only the last reply. `quiet-then-resume` is split into `quiet-holds` and `quiet-then-resume`.
- Models: the runs use the maintainer's default model. The judge stays haiku, except a stronger `--judge-model` for cases tagged `quotes` or `language`. Superseded: see "Judge model".
Source: maintainer decision, 2026-11-06.

## 2026-11-06: Harness location
Context: The plan put the harness plugin in `evals/harness/`. `claude plugin eval` refuses a case plugin inside the eval directory next to the cases.
Decision: Put the harness at `harness/` in the repo root. Each case sets `plugins: ["../../harness"]`. Run `./harness/sync.sh && claude plugin eval .` from the repo root. The style copy and `evals/results/` are gitignored.
Source: local test with Claude Code 2.1.287 (`evals/harness`: "a plugin shipped with a case must sit in its own subdirectory"; `harness/`: loads).

## 2026-11-06: Grader design
Context: Phase 1 maps the scenarios to graders.
Decision:
- Silence checks use two graders: a `regex` for strong theme terms (all except `master`, `Sam` and `quest`, which appear in technical text) and an `llm` check for any themed line.
- Each `llm` rubric repeats the definition of a themed line and has explicit PASS and FAIL conditions.
- A `[human]` placeholder is a `regex` that always passes. The release gate ignores it.
- Each "matches a gallery piece" check is a `regex` that always fails until Phase 4.
- History files are hand-written data with `cwd` set to `/workspace`. The earlier replies use original lines.
- A run of a history case writes its session transcript into the case folder, named `<session id>.jsonl`. It contains local temporary paths. `.gitignore` excludes these files.
Source: https://code.claude.com/docs/en/plugin-evals.md (grader types). Local test of a hand-written history file.

## 2026-11-06: Phase 1 baseline (no style)
Context: Phase 1 runs all cases without the style. Theme checks must fail. Clean-output and silence checks must pass.
Decision: The baseline matches the expectation. 39 cases, 3 runs each, default model, judge haiku.
- Red as expected: `greets-user-as-master`, `custom-address-from-claude-md` (address), `tdd-red-themed-and-correct` (themed line), `tdd-green-celebrates` (themed line), `quiet-then-resume`, `no-repeated-lines`, `lang-it-greeting`, `lang-it-custom-address` (address), `lang-unknown-fallback` (German line), and the section F gallery and banner checks.
- Green as expected: all silence, clean-artifact, settings-limit, quality and "no art" checks.
- Fixed during the run: `commit-message-clean` and `lang-it-commit-clean` asked for no format, and Claude Code does not use Conventional Commits by default. The prompts now ask for the format. `quiet-then-resume` passed without the style, because the history asked to "talk like a hobbit". The history now says "Voice on, please."
- Note: `no-repeated-lines` fails at baseline because the model copies the tone of the history and repeats "the road is open/clear". This is a valid red.
Source: local runs of `claude plugin eval . --ablation none` with Claude Code 2.1.287.

## 2026-11-06: Greeting moment
Context: The spec defined the greeting as the first reply of a session. Every eval prompt is a first message, so the style greeted in every case. The greeting then added a second themed line, and `intensity-light-neutral-question` got a themed line for a neutral question.
Decision: A greeting is the first reply when the first message says hello. If the first message is a task with no hello, the reply uses the moment of the task.
Source: maintainer decision, 2026-11-06. First Phase 2 eval run.

## 2026-11-06: Scope of the clean-artifact rubrics
Context: In the first Phase 2 run, the haiku judge failed clean commit messages, PR descriptions and code blocks. The cause was a themed line with "master" outside the artifact.
Decision: Each clean-artifact rubric now says: judge only the artifact text, and ignore a greeting or themed line outside it. The judge model changed later: see "Judge model".
Source: maintainer decision, 2026-11-06. First Phase 2 eval run.

## 2026-11-06: Italian reference translation and address
Context: The maintainer checked the printed book. "Padron Frodo" is the film dubbing. The book uses "signore" and "signor Frodo".
Decision:
- Reference translation: see `languages/it.md`.
- Default address: "signore", to follow the book.
- Register: "voi" (confirmed in the book). When the voice is on, the whole Italian chat reply uses "voi", not only the themed line. A reply that mixes "voi" and "tu" reads as a mistake. In silent mode, the reply is a normal plain reply. Artifacts do not change.
- The confidentiality pass allows the translator name in the "Reference translation" field of `languages/<code>.md`.
Source: maintainer decision, 2026-11-06.

## 2026-11-06: Judge model
Context: With scoped rubrics, the haiku judge still failed clean commit messages and PR descriptions in 3 of 3 runs. Sonnet passed the same replies. Sonnet also changed some FAIL verdicts to PASS when it had to quote the deciding sentence.
Decision: Use `--judge-model opus` for every run. Three rubrics are more concrete: a themed line is counted by sentence, an address word such as "signore" is not a "tu" or "lei" form, and names and places alone are not a quote.
Source: maintainer decision, 2026-11-06. Phase 2 runs with haiku and sonnet judges.

## 2026-11-06: Themed words in prose at full intensity
Context: At `full`, the spec allows themed words in the chat prose and also limits a reply to two themed lines. The model added themed words in extra sentences, so replies had three or four themed sentences.
Decision: A prose sentence with a themed word counts as one of the two themed lines.
Source: Phase 2 eval run, `intensity-full-two-lines-max`.

## 2026-11-06: A8 manual check (settings in CLAUDE.md)
Context: The evals pass settings through `append_system_prompt`. A8 needs one check with a real project `CLAUDE.md`.
Decision: A8 holds. A test project had `kettlesong.address: Ring-bearer` and `kettlesong.intensity: light` in `CLAUDE.md`, and `outputStyle: "kettlesong:Kettlesong"` in `.claude/settings.json`. The greeting used "Ring-bearer". A neutral question got no themed line.
Source: headless `claude -p` session with `--plugin-dir`, Claude Code 2.1.287, 2026-11-06.

## 2026-11-06: Phase 2 result
Context: The release gate for Phase 2 needs 3 of 3 passes on every `[auto]` and `[judge]` check outside section F.
Decision: The gate passes. 36 of 39 cases pass 3 of 3, including the best-effort `no-repeated-lines`. The 3 red cases are the section F gallery checks, which wait for Phase 4. The style has 1,004 words of instructions.
Source: local run of `claude plugin eval . --ablation none --judge-model opus` with Claude Code 2.1.287, default model `claude-opus-5-5`.

## 2026-11-06: Banner art
Context: Phase 3 designs the `banner`, the only piece with letters. A large font does not fit the product name in 40 columns.
Decision: The banner uses hand-made lowercase letters on two lines. The letters are hand-made, so no font license applies. The banner height limit changes from 6 to 8 lines, the same as the figures. For the current piece, see "Kettlesong banner".
Source: maintainer choice, 2026-11-06.

## 2026-11-06: Hobbit-tea art
Context: Phase 3 designs `hobbit-tea`, the signature piece for "task done".
Decision: A standing figure with curly hair and big bare feet holds up a steaming cup. It has 20 columns, 7 lines and 119 characters. Original, hand-made.
Source: maintainer choice (`variant-a`), 2026-11-06.

## 2026-11-06: Dwarf-axe art
Context: Phase 3 designs `dwarf-axe`, for tests that pass after a long red phase.
Decision: A short figure with a domed helmet, a braided beard and a raised double-bladed axe. It has 17 columns, 7 lines and 112 characters. Original, hand-made.
Source: maintainer choice (`variant-a`), 2026-11-06.

## 2026-11-06: Elf-bow art
Context: Phase 3 designs `elf-bow`, for a bug found.
Decision: A tall, thin archer with a pointed hood, a squinting eye and a large drawn bow with an arrow. It has 25 columns, 8 lines and 153 characters. Original, hand-made.
Source: maintainer choice (`variant-a`), 2026-11-06.

## 2026-11-06: Wizard art
Context: Phase 3 designs `wizard`, for a refactor proposal.
Decision: A figure with a pointed hat with a star, a long beard and a straight staff with a star on top. It has 20 columns, 8 lines and 168 characters. Original, hand-made.
Source: maintainer choice (`variant-a`, revised), 2026-11-06.

## 2026-11-06: Fire-demon art
Context: Phase 3 designs `fire-demon`, for a severe bug. It must stay friendly.
Decision: A creature with flame hair and small fangs over a row of fire. It has 18 columns, 7 lines and 122 characters. Original, hand-made.
Source: maintainer choice (`variant-a`), 2026-11-06.

## 2026-11-06: Volcano art
Context: Phase 3 designs `volcano`, for the moment before a production deploy.
Decision: A broad mountain with a large plume of smoke. It has 23 columns, 7 lines and 138 characters. Original, hand-made.
Source: maintainer choice (`variant-a`), 2026-11-06.

## 2026-11-06: Art graders
Context: Phase 4 replaces the placeholder gallery checks with real checks.
Decision: `evals/build-art-graders.py` builds exact-match regex graders from `art/*.txt`. It writes each "-" as `\x2d`, because the eval loader reads "---" in a frontmatter value as the end of the frontmatter. The code-clean rubrics now say that a fenced `text` block with text art is not a code block, as `evals/SCENARIOS.md` defines.
Source: maintainer approval of the script, 2026-11-06. Loader error "invalid YAML frontmatter: Unexpected EOF" with Claude Code 2.1.287.

## 2026-11-06: Phase 4 result
Context: The release gate for Phase 4 needs 3 of 3 passes on every `[auto]` and `[judge]` check, including section F.
Decision: The gate passes. 39 of 39 cases pass 3 of 3, including the best-effort `no-repeated-lines`. The style has 1,196 words of instructions and a 1,090-character gallery. A headless reply opened with an exact copy of the banner.
Source: local run of `claude plugin eval . --ablation none --judge-model opus` with Claude Code 2.1.287, default model `claude-opus-5-5`.

## 2026-11-06: Phase 5 result
Context: Phase 5 makes the style shorter and clearer without breaking evals.
Decision:
- Removed repeated instructions. The style has 1,171 words of instructions, down from 1,196.
- The tone examples are now one sentence each. The multi-sentence examples taught two-sentence greetings, which broke the one-line limit.
- The two bullets that define a themed line as "one short sentence" stay as they are. Merging them broke the line limits in 6 cases.
- An opus check found no near-quotes in the tone examples, the phrase bank or the Italian sample lines.
- All 39 cases pass 3 of 3.
Source: local runs of `claude plugin eval . --ablation none --judge-model opus` with Claude Code 2.1.287, default model `claude-opus-5-5`.

## 2026-11-07: Themed lines in italics
Context: The maintainer asked for a different style or color for the themed lines. Claude cannot emit colors in chat, and inline code would hide themed lines from the silence checks.
Decision: Each themed line is in italics (`*...*`). With italics, the model added an italic opening line and an italic closing line to long replies, which broke the one-line limit in 2 of 6 runs. The rule "at the start or the end of the reply, not both" fixed it (6 of 6).
Source: eval cases `themed-line-italic` and `intensity-medium-one-line-max`.

## 2026-11-07: Banner color through a diff block
Context: The maintainer asked for a colored banner. Claude Code highlights fenced `diff` blocks: lines that start with `+` show in green.
Decision: The banner goes in a fenced `diff` block, with `+  ` (a plus and two spaces) before each line. The maintainer checked the rendering in Claude Code and chose the `+` prefix. The source in `art/banner.txt` stays without the prefix. The figures stay in `text` blocks.
Source: manual check in Claude Code; eval cases `art-banner-at-default-setting` and `art-banner-on-first-greeting`.

## 2026-11-07: More text art by default
Context: In a manual session, only the hobbit with tea appeared. The moments were narrow ("a hard bug", "a long red phase"), and `rare` showed art in about one reply in 10 to 15.
Decision: The default for `art` is now `often`, and `often` shows a piece at every matching moment. `rare` keeps the old frequency. The moments are wider: a bug found, tests pass after a fix, a refactor or design proposal, a severe bug or a data loss risk, a production deploy or release.
Source: eval cases `art-matches-moment`, `art-dwarf-on-green` and `art-wizard-on-refactor`.

## 2026-11-07: README cover
Context: The maintainer asked for a README cover with the product name in a text art look.
Decision: The cover shows a real reply: the prompt, the green `diff` banner, an italic themed line, and four figures in the order of one session. It has a light and a dark SVG, with the GitHub diff colors, switched by a `<picture>` element. It uses the system monospace font, because an SVG image on GitHub cannot load web fonts. `art/build-cover.py` builds both files from `art/`.
Source: maintainer review of the rendered cover in a GitHub-like page, light and dark, at README and phone width.

## 2026-11-07: Deploy idea without a scene echo
Context: A review found that the Deploy moment idea, "the march to the dark land", asks the model for the scene echo that the content rules forbid.
Decision: The idea is now "the last gate before release". A new case, `deploy-no-scene-echo`, failed in 5 of 6 runs with the old idea and passed in 6 of 6 with the new one. The phrase bank also lost or changed lines that echo famous scenes.
Source: eval case `deploy-no-scene-echo`; review before release.

## 2026-11-07: Release gate after the improvements
Context: Italics, the green banner, more art by default and the deploy idea changed the style. The release gate must pass again.
Decision:
- After italics, the banner and the art changes: 42 of 42 cases pass 3 of 3.
- After the deploy idea: 43 cases. 41 pass 3 of 3 in the full run. `lang-it-greeting` passed 2 of 3 (the judge split on a correct reply) and 3 of 3 in a rerun.
- The best-effort `no-repeated-lines` passed 2 of 3 in the full run and in a rerun. It does not block. It reuses images from the history ("the road") more often since the italics change.
- The style has 1,199 words of instructions (strict count, which also counts code spans and settings) and a 1,114-character gallery.
Source: local runs of `claude plugin eval . --ablation none -j 4 --judge-model opus` with Claude Code 2.1.287, default model `claude-opus-5-5`.

## 2026-11-08: Rename to Kettlesong
Context: A trademark search found that the first working name was a pending trademark of another owner. The voice alludes to the same books. Hard rule 2 bans trademarks in the product identity.
Decision: The product is now Kettlesong (slug `kettlesong`). TMview, USPTO, EUIPO, a web search and a GitHub search showed no use of the name. The product no longer names the fictional world. Character names stay in the voice as short allusions, never in the README, the manifest, the banner or the cover. The Task done idea is now "the kettle sings". The Deploy idea is now "steady hands for the big step": the model copied "the last gate before release" word for word, and a gate reads as a scene echo (2 of 3, then 6 of 6 after the change). The GitHub repository has the new name too.
Source: maintainer searches and decision, 2026-11-08.

## 2026-11-08: Kettlesong banner
Context: The rename needs a new banner with the same rules: printable ASCII, at most 40 columns and 8 lines.
Decision: "kettle" over "song" in hand-made lowercase letters, on two lines that step down to the right. It has 36 columns and 8 lines. The `e`, `s`, `o` and `n` shapes come from the old banner. The `k`, `t`, `l` and `g` shapes are new.
Source: maintainer choice (variant A), 2026-11-08.

## 2026-11-08: Release gate after the rename
Context: The rename changed the style name, the banner, the settings prefix, the flavor sentence and two moment ideas. The release gate must pass again.
Decision: The gate passes. 42 of 43 cases pass 3 of 3. The best-effort `no-repeated-lines` passed 2 of 3: its fixed history has "the kettle is warm", and the new Task done idea leads back to the kettle. It does not block. The style has 1,199 words of instructions (strict count) and a 1,093-character gallery.
Source: local run of `claude plugin eval . --ablation none -j 4 --judge-model opus` with Claude Code 2.1.287, default model `claude-opus-5-5`.

## 2026-11-09: Solid cover background
Context: The covers had no background. Outside the README `<picture>` element, a page of the other theme made the text hard to read.
Decision: Each cover has a solid background with rounded corners: `#ffffff` for light and `#0d1117` for dark (the GitHub page colors). The README looks the same on GitHub. The covers stay readable on any page.
Source: maintainer choice, 2026-11-09. Rendered check: each cover on a page of the other theme.

## 2026-11-09: Plugin in a subfolder
Context: The marketplace source was the repo root, so every repo file shipped with the plugin: scripts, evals, docs and `CLAUDE.md`. Users need only the manifest and the style.
Decision: Move the plugin to `plugin/` and set the marketplace source to `./plugin`. The marketplace file stays in the root `.claude-plugin/`. The plugin and marketplace names stay `kettlesong`, so the install commands do not change. The evals still run from the repo root through the harness plugin.
Source: https://code.claude.com/docs/en/plugin-marketplaces ("Write relative paths from the marketplace root"). Local check with Claude Code 2.1.287: `claude plugin validate` passes for the marketplace and the plugin, a local install copies only `plugin/`, and `greets-user-as-master` passes 3 of 3.

## 2026-11-09: Plugin icon
Context: `plugin.json` accepts an `icon` field with the path of a square image in the plugin.
Decision: A steaming cup from `art/hobbit-tea.txt` (`c[_]` under two lines of steam), green `#1a7f37` on `#dafbe1`, the light cover colors. A 1024 px PNG at `plugin/.claude-plugin/icon.png`. The full figure was not clear at 64 px.
Source: https://code.claude.com/docs/en/plugins-reference (Fields table, `icon`). Maintainer choice (variant A), 2026-11-09.
