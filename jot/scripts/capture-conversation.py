#!/usr/bin/env python3
"""SubagentStart hook: extract last 5 message pairs from parent transcript."""
import json
import sys

hook_input = json.load(sys.stdin)
transcript_path = hook_input.get("transcript_path", "")

pairs = []
if transcript_path:
    try:
        with open(transcript_path) as f:
            for line in f:
                entry = json.loads(line)
                entry_type = entry.get("type", "")
                if entry_type not in ("user", "assistant"):
                    continue
                msg = entry.get("message", {})
                role = msg.get("role", entry_type)
                content = msg.get("content", "")
                if isinstance(content, list):
                    content = " ".join(
                        c.get("text", "")
                        for c in content
                        if c.get("type") == "text"
                    )
                content = content.strip()
                if not content:
                    continue
                pairs.append(f"{role}: {content}")
    except (IOError, json.JSONDecodeError):
        pass

recent = pairs[-10:]
conversation = "\n---\n".join(recent) if recent else "No conversation history available."

output = {
    "hookSpecificOutput": {
        "hookEventName": "SubagentStart",
        "additionalContext": f"## Recent Conversation\n\n{conversation}",
    }
}
json.dump(output, sys.stdout)
