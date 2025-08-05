---
title: callbackscripteventsinvokesequence.md
original_path: WinForms_Docs/99_Uncategorized/callbackscripteventsinvokesequence.md
created_at: 2025-08-05
---






#### Callback script events invoke sequence[] {#callback-script-events-invoke-sequence style="tab-stops: 0pt"}

[] 

The sequence in which the client-side events will be triggered when Callback is called is as follows.

[] 

1.   **BeforeCallbackScript**: gets executed before a callback is generated on the client

28.  **AfterCallbackScript**: gets executed after a callback has been invoked

29.  **BeforeCallbackResponseProcessingScript**: gets executed in the callback return event handler on client, before the returned value is processed

30.  **AfterCallbackResponseProcessedScript**: gets executed in the callback return event handler on the client

 

[]{#related-topics}

