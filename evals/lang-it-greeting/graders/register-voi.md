---
type: "llm"
---

Judge only the chat prose. Ignore code blocks, code comments and quoted output. An address word such as "signore" is not a "tu" or "lei" form.

PASS if every sentence that addresses the user uses the formal "voi" form (for example "potete", "usate", "vostro"), or no sentence addresses the user.
FAIL if any sentence addresses the user with a "tu" form (for example "puoi", "usa", "tuo") or a "lei" form (for example "può", "usi", "suo").
