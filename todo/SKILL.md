---
name: todo
description: Capture a mid-conversation TODO into the project's Todos/ folder with auto-captured context (git branch, recent commits, files edited, active plan, conversation summary). Use when user says "/todo", "park this idea", "save this for later", or "add a todo".
---

# /todo — Idea Parking Lot

Capture a TODO without breaking flow. User provides the idea, you fill in the context.

## Workflow

1. **Read the user's idea** from the arguments after `/todo`.
2. **If the idea is vague or unclear**, use AskUserQuestion to ask 1-3 targeted questions until the user confirms enough detail is captured. Do not over-ask — stop when the user is satisfied.
3. **Auto-capture context** (keep each section brief — just enough to understand why and give an implementer a starting point):
   - Git branch name
   - Last 3-5 commit messages (short hash + subject)
   - Files with uncommitted changes (staged + unstaged)
   - Active plan file path (if any exist in `.claude/plans/`)
   - 2-3 sentence summary of what was being built/discussed in this conversation
4. **Determine next ID**: Scan all `.md` files in `Todos/` and `Todos/done/` for the highest existing numeric ID prefix. Next ID = highest + 1. If no files exist, start at 001. Zero-pad to 3 digits.
5. **Generate slug**: Derive a short kebab-case slug from the title (max 5 words).
6. **Create the file** at `./Todos/{id}_{slug}.md` using the template below.
7. **Print confirmation**: Show the file path and a one-line summary.

## File Template

```markdown
---
id: {NNN}
title: {Short title}
status: open
created: {ISO 8601 timestamp with timezone}
branch: {current git branch}
---

## Idea
{User's description of the TODO, cleaned up for clarity}

## Context
{2-3 sentences: what was being built, where in the project, what milestone/phase}

## Recent commits
- {hash} {subject}
- {hash} {subject}
- {hash} {subject}

## Uncommitted files
- {list of modified/staged files, or "None"}

## Active plan
{Path to active plan file, or "None"}

## Dependencies
{What this TODO needs to become actionable — libraries, designs, decisions, other TODOs. "None" if standalone.}
```

## Rules

- use a background agent to do as much of the work as possible, to prevent disrupting the active conversation with the user.  
- If permission is needed to write the todo file, or scan the commit history or current files in the repository, request as many necessary permissions as possible in a single permission ask.
- Always create `Todos/` directory if it doesn't exist (including `Todos/done/`).
- Never interrupt the user's current work beyond the clarification questions.
- Keep context sections short. No full file contents, no full diffs.
- If no git repo is detected, skip git-related sections and note "Not a git repository".
- The TODO file is the only artifact. Do not modify any other files.
