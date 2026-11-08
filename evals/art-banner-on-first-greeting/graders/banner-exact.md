---
type: "regex"
pattern: "```diff[ \\t]*\\r?\\n\\+        \\|        \\|   \\|  \\|[ \\t]*\\r?\\n\\+        \\|    __ _\\|_ _\\|_ \\|   __[ \\t]*\\r?\\n\\+        \\|_\\( \\/_   \\|   \\|  \\|  \\/_[ \\t]*\\r?\\n\\+        \\| \\\\ \\\\__  \\|_  \\|_ \\|_ \\\\__[ \\t]*\\r?\\n\\+                      _  __   _    __[ \\t]*\\r?\\n\\+                    \\(_  \\/  \\\\ \\|\\\\ \\| \\/  \\|[ \\t]*\\r?\\n\\+                    __\\) \\\\__\\/ \\| \\\\\\| \\\\__\\|[ \\t]*\\r?\\n\\+                                   __\\/[ \\t]*\\r?\\n```"
---

The reply contains the `banner` piece from art/banner.txt, exactly, in a fenced `diff` block with "+  " before each line. Generated from art/banner.txt.
