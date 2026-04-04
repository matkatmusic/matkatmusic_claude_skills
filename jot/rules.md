# Rules

- NEVER ask the user any questions. Zero interaction.
- NEVER summarize message pairs. Pass and store them verbatim.
- Create `Todos/` and `Todos/done/` directories if they don't exist.
- The TODO file is the only artifact. Do not modify any other files.
- If no git repo is detected, skip git-related fields and note "Not a git repository".
- Keep Context concise. No full file contents, no full diffs. Code snippets only when directly relevant.
- Use the same frontmatter format as `/todo` so `/todo-list` and `/todo-clean` work unchanged. `/todo-clean` checks from the original `created` date.
