# Background Agent Workflow

## 1. Use pre-gathered state

The SKILL.md preprocesses shell scripts via `!` backtick syntax before you receive the prompt. By the time you see the "Pre-gathered State" section, the commands have already run and been replaced with their output:
- **Branch** → current git branch
- **Commits** → space-separated short hashes
- **Uncommitted** → filenames with uncommitted changes, or "None"
- **Plan** → extract from your conversation context (the system reminder names the active plan file path, if any). Use "None" if no plan is active.
- **Open TODOs** → file paths of open TODOs (one per line, may be empty)

These values are already resolved. Use them directly when filling the template.

## 2. Check for explicit ID reference

If jot text matches `add to {NNN}` (e.g., "add to 005 — also handle timeout"), extract the ID and skip to step 4 (append mode). Text after the `—` or `-` delimiter is the new jot content.

## 3. Scan for existing related TODOs

1. The main agent included a list of open TODO file paths in your prompt (one per line, may be empty). Read only those files.
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
2. **Filename**: `{id}_{slug}.md` where `{slug}` is the jot text kebab-cased and truncated to 5-6 words.
3. **Write** using the template in `./template.md`.
