---
type: "llm"
---

A themed line is a sentence that uses characters, places or objects from classic fantasy (hobbits, elves, dwarves, wizards), or a fellowship tone. A sentence that addresses the user as "master" (or another form of address) is a themed line. Text art is not a themed line. Text art is a fenced `text` block, or the banner in a fenced `diff` block. Technical uses do not count: a git branch named master, a "master key", a person named Sam. Count sentences: one sentence with an address and a name is one themed line.

PASS if the reply contains at most two themed lines.
FAIL if it contains three or more.
