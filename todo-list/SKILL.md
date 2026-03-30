---
name: todo-list
description: Show all open TODOs from the project's Todos/ folder with ID, title, date, and branch. Use when user says "/todo-list", "show my todos", "what todos are open", or "list todos".
---

# /todo-list — View Open TODOs

Show a summary of all incomplete TODO items in the project.

## Workflow

1. **Check for Todos/ directory**. If it doesn't exist, say "No Todos/ folder found in this project." and stop.
2. **Read all `.md` files in `Todos/`** (not `Todos/done/`).
3. **Parse YAML frontmatter** from each file to extract: id, title, status, created, branch.
4. **Filter** to `status: open` only.
5. **Sort by ID** (ascending).
6. **Display as an itemized list**, one TODO per block:

```
ID: 001
Created: 2026-03-20
Title: Polish GUI visual design
Branch: feature/mvp-gui

ID: 003
Created: 2026-03-21
Title: Add export to CSV
Branch: feature/mvp-data
```

7. **Show count**: "2 open TODOs" (or "No open TODOs").

## Rules

- Read-only. Never modify any files.
- If a file has malformed frontmatter, skip it and note the filename as unreadable.
- Keep output concise — table only, no file contents.
