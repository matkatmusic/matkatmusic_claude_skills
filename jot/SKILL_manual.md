---
name: jot
description: Capture a TODO or user idea instantly without breaking current conversation flow.
allowed-tools: Agent Read Write(Todos/*) Edit(Todos/*) Glob Bash(mkdir *)
argument-hint: <idea> or "add to {NNN} — <idea>"
---

# /jot — Fast Idea Capture

Capture an idea instantly without breaking flow. No questions, no confirmation, no waiting.

## Jot Text

$ARGUMENTS

## Pre-gathered State

- Branch: !`${CLAUDE_SKILL_DIR}/scripts/git-branch.sh `
- Commits: !`${CLAUDE_SKILL_DIR}/scripts/git-commits.sh `
- Uncommitted: !`${CLAUDE_SKILL_DIR}/scripts/git-uncommitted.sh `
- Open TODOs: !`${CLAUDE_SKILL_DIR}/scripts/scan-open-todos.sh `

## Main Agent Steps

1. Collect the last 5 user/assistant message pairs from the current conversation. Copy them verbatim — no summarization.
2. Spawn a background agent with all of the following. Tell the background agent to read `${CLAUDE_SKILL_DIR}/background.md`, `${CLAUDE_SKILL_DIR}/template.md`, and `${CLAUDE_SKILL_DIR}/rules.md` for its instructions.
   - **Jot Text** from above
   - **Pre-gathered State** from above
   - **Message pairs** collected in step 1
   - **Working directory**: the current working directory
3. Continue the conversation immediately. Do not wait.
4. When the background agent completes, display: `jotted <filename>`
