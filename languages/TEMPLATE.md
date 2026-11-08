# <Language name> (`<code>`)

Copy this file to `languages/<code>.md`. Use the ISO 639-1 code (for example `de`, `is`). Fill in every field. See `CONTRIBUTING.md` for the full steps.

## Status

| Field | Value |
|---|---|
| Status | draft / verified |
| Reviewed by | a native speaker (name or GitHub handle) |

## Reference translation

The published translation of the books that this file follows. Give the translator, the publisher and the edition year. If the language has more than one translation, choose one and use only its names.

## Address and register

| Field | Value | Notes |
|---|---|---|
| Default address | | The word the hobbit servant uses for his master in the reference translation. One word only. |
| Formal or informal "you" | | For example: German `Sie` or `du`. Write `n/a` if the language has no difference. |
| Grammatical gender | | Does the address or the greeting change with gender? How do the sample lines avoid it? |

## Names

Use the names from the reference translation. Leave a cell empty if the name does not change. Keep the IDs as they are: they match `docs/PERSONA.md`.

| ID | English | This language |
|---|---|---|
| `gandalf` | Gandalf | |
| `legolas` | Legolas | |
| `gimli` | Gimli | |
| `sam` | Sam | |
| `frodo` | Frodo | |
| `gollum` | Gollum | |
| `balrog` | Balrog | |
| `ents` | Ents | |
| `black-riders` | Black riders | |
| `shire` | the Shire | |
| `rivendell` | Rivendell | |
| `mordor` | Mordor | |
| `moria` | Moria | |
| `isengard` | Isengard | |
| `palantir` | palantír | |
| `mithril` | mithril | |
| `ring` | the Ring | |
| `hobbit` | hobbit | |
| `second-breakfast` | second breakfast | A natural phrase, not a quote. |

## Theme terms (for evals)

The words that the silence checks look for in this language. Include the default address, the translated names and the words for "quest" and "fellowship".

## Sample lines

5 to 10 original lines, written in this language. Do not translate the English phrase bank word by word. Do not copy any sentence from the reference translation: a sentence from a translation is a quote. Single words and names are fine.

## Style line

One line for the output style, at most 40 words. Format:

```text
<code>: address "<word>", <register>, <id>=<name>, <id>=<name>, ...
```

List only the names that change.

## Eval cases

Add these cases to `evals/SCENARIOS.md`, section G, with the prompts in this language:

- `lang-<code>-greeting`: the greeting uses the default address.
- `lang-<code>-custom-address`: a custom address stays exactly as written.
- `lang-<code>-incident-silent`: no themed line during a production incident.
- `lang-<code>-commit-clean`: a commit message contains no theme term.
