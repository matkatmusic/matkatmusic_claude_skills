---
name: jot
description: Ultra-fast TODO capture with zero interaction. Runs entirely in a background agent. Auto-captures git state and recent conversation context. Deduplicates against existing TODOs. Use when user says "/jot <idea>".
---

# /jot — Fast Idea Capture

Capture an idea instantly without breaking flow. No questions, no confirmation, no waiting.

## Trigger

`/jot <raw text>` — the raw text after `/jot` is the idea.
`/jot add to {NNN} — <text>` — appends to an existing TODO by ID.

## Main Agent Steps

1. Extract the raw jot text from the arguments.
2. Collect the last 5 user/assistant message pairs from the current conversation. Copy them verbatim — no summarization.
3. Spawn a background agent with the jot text, the 5 message pairs, and the current working directory. Tell the background agent to read these files for its instructions (use the "Base directory for this skill" path from your system context to build absolute paths):
   - `./background.md` — full background workflow
   - `./template.md` — file template for new TODOs
   - `./rules.md` — constraints
4. Continue the conversation immediately. Do not wait.
5. When the background agent completes, display: `jotted <filename>`
