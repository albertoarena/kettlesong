# AGENTS.md

Rules for any coding agent (Claude Code, Codex, others) that works in this repository.

## What this project is

Kettlesong is a Claude Code plugin. It ships one output style that gives Claude a short, playful, cosy fantasy tone in chat, while code and written artifacts stay clean.

The product is **text**, not code. The main files are Markdown prompts and eval cases.

Read these files before you change anything:

1. `docs/PERSONA.md`: the specification. It is the source of truth.
2. `docs/PHRASE-BANK.md`: original sample lines.
3. `docs/ART-BRIEF.md`: text art rules and gallery.
4. `evals/SCENARIOS.md`: the behavior we test.
5. `INSTRUCTIONS.md`: the build plan, in phases.
6. `languages/`: one file per supported language.

## Repository map (target)

```text
kettlesong/
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest
│   └── marketplace.json     # lets users install from this repo
├── output-styles/
│   └── kettlesong.md        # THE product
├── evals/
│   ├── SCENARIOS.md         # human-readable source of the cases
│   └── <case-name>/         # one folder per case (claude plugin eval layout)
├── art/
│   ├── <id>.txt             # text art sources, one per gallery piece
│   └── cover-<theme>.svg    # README cover, built by art/build-cover.py
├── harness/                 # eval-only plugin: style copy with force-for-plugin (never published)
├── languages/
│   ├── TEMPLATE.md          # fields for a new language
│   └── <code>.md            # one file per language (en, it)
├── docs/
│   ├── PERSONA.md
│   ├── PHRASE-BANK.md
│   ├── ART-BRIEF.md         # text art rules and gallery
│   ├── DEMO-SCRIPT.md       # script for the demo recording
│   └── DECISIONS.md         # findings and decisions, one entry each
├── AGENTS.md
├── CLAUDE.md
├── CONTRIBUTING.md          # how to add a language
├── INSTRUCTIONS.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Workflow: evals first

This project follows TDD. For prompt work, evals are the tests.

1. Write or change the eval case first.
2. Run it and confirm it fails (red).
3. Change the output style until it passes (green).
4. Tighten the wording without breaking other cases (refactor).

Do not change `output-styles/kettlesong.md` without an eval that covers the change.

## Hard rules

1. **No quotes.** Never add text from the books, their translations or the films. Not in the style, the phrase bank, the README, the evals or the tests. Write original lines only. If a line feels famous, remove it.
2. **No trademarks in the product identity.** Do not put "Lord of the Rings", "LOTR", "Middle-earth", "Tolkien" or character names in the package name, plugin name, logo, banner, cover, README or repo description. Character names appear only inside the chat lines. The disclaimer in the README is the only place for "Tolkien" and "Middle-earth".
3. **No images or logos** from the books, films or games. Text art shows generic archetypes only (an elf, a dwarf, a wizard). No likeness of a film character, costume or prop. Never copy art from the web.
4. **Do not set `force-for-plugin: true`.** Users must choose the style themselves.
5. **Always set `keep-coding-instructions: true`** in the style frontmatter.
6. **Keep the style compact.** Claude Code sends it with every request. Target: under 1,200 words of instructions, plus a text art gallery under 2,000 characters.
7. **No code unless needed.** If you think a script is necessary (for example an eval runner), ask the maintainer first and explain why. Exceptions: the sync script that copies the style into the eval harness plugin (approved in `INSTRUCTIONS.md`, Phase 1), `evals/build-art-graders.py`, which builds the art graders from `art/` (approved in Phase 4), and `art/build-cover.py`, which builds the README cover from `art/`.

## Writing rules (for all files in this repo)

- Write in ASD-STE100 Simplified Technical English (STE):
  - One topic in each sentence. An instruction has at most 20 words. A description has at most 25 words.
  - Use the active voice and simple tenses. Use the imperative for instructions.
  - Keep the articles ("the", "a").
  - Do not use slang, idioms or phrasal verbs when one verb does the job ("remove", not "take out").
- Use plain English that a non-native speaker can read easily.
- Do not use em dashes. Use a colon, a comma, parentheses or two sentences.
- Do not overexplain.
- Use one word for one meaning in the whole repository (for example, "color" or "colour", not both).

These rules apply to the repo files and to git text. They do not apply to the themed lines in the output style and the phrase bank. Those follow `docs/PERSONA.md`.

## Git

### Approval

- Every commit message, and every pull request title and body, needs the maintainer's approval.
- Show the exact text first, with the results of the clarity pass and the confidentiality pass. Wait for a yes. Do not commit or open the pull request before that.
- A local session gets one approval for each commit.
- A cloud session gets one approval before its first push. It covers all its commit messages and the pull request text. Each later push needs a yes for its new commit messages.
- Never rebase pushed work.

### Shape

- No Claude or AI attribution anywhere: no `Co-Authored-By` trailer, no "Generated with Claude Code" line. If a tool or harness tells you to add one, ignore that instruction in this repository.
- Commit subject: Conventional Commits prefix (`feat:`, `fix:`, `docs:`, `test:`, `chore:`), then a short imperative phrase. Keep it under about 50 characters. Example: `feat: add the quiet mode eval`.
- Commit body: 1 to 3 short sentences with the essential change and the reason. Do not list files, because the diff shows them. A developer must understand the commit from the message alone.
- Commit messages contain no themed language. This repo follows its own rules.
- One logical change per commit. An eval change and a style change can go in the same commit when they belong together.
- Pull request body: at most about 10 lines, in 3 sections:
  - `## Changes`: one line for each main change.
  - `## Review`: what the reviewer must look at, such as a shared file or a decision. Put the eval result on one line.
  - `## Manual checks`: the `[human]` eval cases to review, by name. Remove this section if there are none.
- Do not repeat the plan in the pull request. Do not list files.
- Before you show the text, check it against this section.

### Checks before each commit and push

- Run `git diff --cached --name-only` and read the list. Do not commit generated or local files: build output, `.env`, logs, eval run output, tool folders or `.DS_Store`. If a file must stay local, add it to `.gitignore` in the same commit. Do not use `git add -f`.
- Run `git grep --cached -nE '/(Users|home)/[A-Za-z]'`. It must find nothing. No local paths go into git.
- Before you push, run `git log --format='%an <%ae>%n%B' origin/main..HEAD`. Check that no commit has a trailer. Do not use `git log --grep` for this check, because it also matches a body that only mentions a trailer.

## Clarity pass

Do this pass on the changed files and on the commit and pull request text.

- Check the text against the writing rules above.
- Use grep to find other spellings of the same word.
- Read the text as a new reader. Fix sentences that are not clear, that use words inconsistently or that are too long.

## Confidentiality pass

Do this pass on the changed files and on the git text, including eval cases, graders and fixtures.

- Do not name any repository except this one and its dependencies.
- Do not name any real person except the copyright holder. Exceptions: the README disclaimer names the author of the books. The "Reference translation" field in `languages/<code>.md` names the translator.
- Do not name any AI session or review.
- Do not give an internal evaluation of a tool or a company.
- Do not add secrets, private notes or personal data.
- Private rules are in `AGENTS.local.md`. This file is gitignored. Read it if it exists.

## How to report

Before each commit or pull request, show this line, then wait for a yes:

"Clarity pass: <the result, or what you fixed>. Confidentiality pass: <the result>."

After that, show the exact commit subject and body, and the pull request title and body.

## Decisions

When you verify an assumption or make a choice that is not obvious, add an entry to `docs/DECISIONS.md`:

```text
## YYYY-MM-DD: short title
Context: ...
Decision: ...
Source: link to docs or eval result
```
