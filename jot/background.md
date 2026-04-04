# Background Agent Workflow

## 1. Gather git state

Run in parallel:
- `git branch --show-current`
- `git log --oneline -5`
- `git status --short`
- Check for active plan files in `.claude/plans/`

## 2. Check for explicit ID reference

If jot text matches `add to {NNN}` (e.g., "add to 005 — also handle timeout"), extract the ID and skip to step 4 (append mode). Text after the `—` or `-` delimiter is the new jot content.

## 3. Scan for existing related TODOs

1. Read all `status: open` TODO files in `./Todos/`.
2. Compare jot text and message pairs against each TODO's title, Idea, and Context sections.
3. Decide:
   - **Strong match**: Proceed to step 4 (append mode).
   - **Uncertain**: Create new file with `## See Also` listing possibly-related TODO IDs and titles.
   - **No match**: Create new file.
4. Err toward creating new files. False merges are worse than duplicates.

## 4. Append to existing TODO (append mode)

1. Read the existing TODO file.
2. Update `## Context`: prefer adjusting the original text to incorporate the new idea. If that would distort the original meaning, append a new paragraph. Max 3 sentences added. Think like a filing assistant — user hands you a post-it, you update the manila folder.
3. Add relevant new message pairs below the existing `## Conversation` section, separated by `--- <ISO timestamp> ---`. Include only relevant pairs — not necessarily all 5.
4. Do NOT change frontmatter (id, title, status, created, branch).

## 5. Create new TODO file

1. **Next ID**: Scan `.md` files in `Todos/` and `Todos/done/` for highest numeric ID prefix. Increment by 1. Zero-pad to 3 digits.
2. **Filename**: Kebab-case the jot text, truncate to first 5-6 words. Format: `{id}_{slug}.md`.
3. **Write** using the template in `template.md`.
