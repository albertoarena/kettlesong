---
type: "llm"
---

PASS if the reply has no text art, or the text art is alone in a fenced block at the start or the end of the reply (a `text` block, or a `diff` block for the banner).
FAIL if text art is in the middle of the reply, mixed with other text, or not in a fenced `text` or `diff` block.
