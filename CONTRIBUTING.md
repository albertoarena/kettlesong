# Contributing

## Add a language

A new language needs a native speaker. The names must come from the published translation of the books in that language.

1. Copy `languages/TEMPLATE.md` to `languages/<code>.md`. Use the ISO 639-1 code (for example `de`).
2. Fill in every field with a native speaker. Write original sample lines. Do not copy any sentence from the translation.
3. Add the four cases from the template to `evals/SCENARIOS.md`, section G. Write the prompts in the new language.
4. Create one folder for each case in `evals/`. Copy the `lang-it-*` folders and change the prompts and the graders.
5. Run the cases and confirm that they fail (see "Run the evals").
6. Add the style line from your language file to the "Languages" section of `plugin/output-styles/kettlesong.md`.
7. Run all the cases again. Every `[auto]` and `[judge]` grader must pass in 3 runs out of 3.
8. Add the language to the list in `README.md`, section "Configure".

## Change the text art

Follow the steps in `art/README.md`. A change to a piece also changes the style, the eval graders and the README cover.

## Run the evals

The evals use `claude plugin eval`. Run them from the repository root:

```bash
./harness/sync.sh && claude plugin eval . --judge-model opus
```

The sync script copies the style into the eval harness plugin in `harness/`. The harness turns the style on for each run. Do not publish the harness plugin.

A full run uses many requests. To run one case, add `--case <case-name>`.

## Rules

Read `AGENTS.md` before you change a file. The most important rules:

- Write the eval case first. Change the style only after the case fails.
- Never add text from the books, their translations or the films.
- Keep the style instructions under 1,200 words.
