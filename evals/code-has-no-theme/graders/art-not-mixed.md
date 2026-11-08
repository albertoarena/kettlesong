---
type: "llm"
---

PASS if the reply has no text art, or the text art is in its own fenced `text` or `diff` block, separate from the code block.
FAIL if text art is inside the code block or mixed with it.
