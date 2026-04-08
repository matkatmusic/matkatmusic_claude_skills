---
name: jot
description: Capture a TODO or user idea instantly without breaking current conversation flow.
context: fork
allowed-tools: Read Write(Todos/*) Edit(Todos/*) Glob Bash(mkdir *) Bash(*matkatmusic_claude_skills_jot/scripts/*)
argument-hint: <idea> or "add to {NNN} — <idea>"
hooks:
  SubagentStart:
    - hooks:
        - type: command
          command: "python3 /Users/matkatmusicllc/Programming/dotfiles/claude/skills/matkatmusic_claude_skills/jot/scripts/capture-conversation.py"
---

# /jot — Fast Idea Capture

Capture this idea as a TODO. Zero interaction — no questions, no confirmation.

## Jot Text

$ARGUMENTS

## Pre-gathered State

- Branch: !`${CLAUDE_SKILL_DIR}/scripts/git-branch.sh `
- Commits: !`${CLAUDE_SKILL_DIR}/scripts/git-commits.sh `
- Uncommitted: !`${CLAUDE_SKILL_DIR}/scripts/git-uncommitted.sh `
- Open TODOs: !`${CLAUDE_SKILL_DIR}/scripts/scan-open-todos.sh `

## Conversation Context

Injected via SubagentStart hook as additionalContext. Contains up to 5 recent user/assistant message pairs verbatim. If empty, no conversation was available.

## Workflow

1. If jot text matches `add to {NNN}`, extract ID and skip to step 4.
2. If Open TODOs listed above, read those files. Compare jot text against each TODO's title, Idea, and Context. Err toward creating new — false merges are worse than duplicates.
   - **Strong match**: skip to step 4 (append mode).
   - **Uncertain**: create new file with `## See Also` listing related TODO IDs.
   - **No match**: create new file.
3. **Create new TODO**: Scan `Todos/` and `Todos/done/` for highest numeric ID. Increment, zero-pad to 3 digits. Filename: `{id}_{slug}.md` where `{slug}` is jot text kebab-cased, truncated to 5-6 words. Write using template in `${CLAUDE_SKILL_DIR}/template.md`.
4. **Append mode**: Read existing TODO. Update `## Context` (max 3 sentences added). Add relevant message pairs below `## Conversation`, separated by `--- <ISO timestamp> ---`. Do NOT change frontmatter.

## Rules

- NEVER ask questions. Zero interaction.
- NEVER summarize message pairs. Store verbatim.
- Create `Todos/` and `Todos/done/` if they don't exist.
- The TODO file is the only artifact. Do not modify any other files.
- If no git repo detected, skip git fields, note "Not a git repository".
- Keep Context concise. No full file contents or diffs.
- Use same frontmatter format as `/todo` so `/todo-list` and `/todo-clean` work. `/todo-clean` checks from the original `created` date.
