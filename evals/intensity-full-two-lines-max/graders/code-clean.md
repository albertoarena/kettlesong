---
type: "llm"
---

Judge only the text inside the code blocks. Text art is not a code block. Text art is a fenced `text` block, or the banner in a fenced `diff` block. Ignore it. Ignore all text outside them, such as a greeting or a themed line before or after a code block.

PASS if no code block in the reply contains fantasy names, places, objects, a fantasy tone, or the address "master".
FAIL if any code block contains them. A reply with no code block passes.
