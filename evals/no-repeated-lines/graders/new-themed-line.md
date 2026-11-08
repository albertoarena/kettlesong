---
type: "llm"
---

A themed line is a sentence that uses characters, places or objects from classic fantasy (hobbits, elves, dwarves, wizards), or a fellowship tone. A sentence that addresses the user as "master" (or another form of address) is a themed line. Text art is not a themed line. Text art is a fenced `text` block, or the banner in a fenced `diff` block. Technical uses do not count: a git branch named master, a "master key", a person named Sam. Count sentences: one sentence with an address and a name is one themed line.

Earlier themed lines in this conversation:
- Welcome back, master. The kettle is warm and the road is open. What is our task today?
- The test has fallen, master. It saw a danger that we missed.
- The wall holds, master. Every test stands.

PASS if the reply has no themed line, or its themed line is clearly different from all earlier themed lines.
FAIL if the reply repeats an earlier themed line, or a close variant of one.
