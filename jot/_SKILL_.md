---
name: jot
description: Capture a TODO or user idea instantly without breaking current conversation flow.
hooks: 
  UserPromptSubmit: 
    - hooks:      
      - type: "command"
        command: "./scripts/jot.sh"
        async: true     
---

<!-- 
got the following working: 
installed a hook to ~/.claude/hooks/jot.sh that prints out the prompt that was passed in to ~/.jot-log.txt and blocks the prompt from reaching Claude. 

the hook is registered in this repo's settings.json, which is symlinked into the ~/.claude/settings.json file. 

 -->