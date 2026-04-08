---
name: jot
description: Capture a TODO or user idea instantly without breaking current conversation flow. 
allowed-tools: Agent Read Write(Todos/*) Edit(Todos/*) Glob Bash(mkdir *)
argument-hint: <idea> or "add to {NNN} — <idea>"
---

# /jot — Fast Idea Capture

Capture an idea instantly without breaking flow. No questions, no confirmation, no waiting.
Run as a background agent with auto-captured git state and conversation context. Deduplicate against existing TODOs

## Pre-gathered State

- Branch: !`${CLAUDE_SKILL_DIR}/scripts/git-branch.sh "$(pwd)"`
- Commits: !`${CLAUDE_SKILL_DIR}/scripts/git-commits.sh "$(pwd)"`
- Uncommitted: !`${CLAUDE_SKILL_DIR}/scripts/git-uncommitted.sh "$(pwd)"`
- Open TODOs: !`${CLAUDE_SKILL_DIR}/scripts/scan-open-todos.sh "$(pwd)"`

## Main Agent Steps

1. Collect the last 5 user/assistant message pairs from the current conversation. Copy them verbatim — no summarization.
2. Spawn a background agent with `$ARGUMENTS`, the 5 message pairs, the current working directory, and the **Pre-gathered State** above. Tell the background agent to read these files for its instructions (use the "Base directory for this skill" path from your system context to build absolute paths):
   - `./background.md` — full background workflow
   - `./template.md` — file template for new TODOs
   - `./rules.md` — constraints
3. Continue the conversation immediately. Do not wait.
4. When the background agent completes, display: `jotted <filename>`
