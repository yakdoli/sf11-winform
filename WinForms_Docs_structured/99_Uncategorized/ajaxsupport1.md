---
title: ajaxsupport1.md
original_path: WinForms_Docs/99_Uncategorized/ajaxsupport1.md
created_at: 2025-08-05
---






##### AJAX Support {#ajax-support style="tab-stops: 0pt"}

[] 

The RichTextEditor control, by default, fires it\'s server-side events using AJAX style callbacks. So, when the user clicks the **Update** or **Cancel** button, a callback will be triggered, which will result in the appropriate server-side event. This behavior can be changed to use postbacks instead using the **EnableCallbacks** property.

[] 


  ----------------- --------------------------------------------------------------------------------
  AJAX Property     Description
  EnableCallbacks   Specifies whether to use callbacks or postbacks to trigger server-side events.
  ----------------- --------------------------------------------------------------------------------


[] 

When callbacks are turned on, the various client-side events that will be triggered and the properties through which you can setup listeners for those events are given below.

[] 


  --------------------------------------- -----------------------------------------------------------------------------------------------------------
  Client-Side Event                       Description
  BeforeCallbackScript                    Specifies the client side script to execute before the callback  request is sent to the server.
  AfterCallbackScript                     Specifies the client side script that will be executed after the  callback request is sent to the server.
  BeforeCallbackResponseProcessedScript   Specifies the client side script to be executed before the callback request gets processed.
  AfterCallbackResponseProcessedScript    Specifies the client side script to be executed after the callback request gets processed.
  --------------------------------------- -----------------------------------------------------------------------------------------------------------


[] 

Note that the RichTextEditor\'s client side object exposes a **Refresh** method. When calling this method via JavaScript, the following server-side event will be triggered.

[] 


  ------------------- ---------------------------------------------------------------
  Server-Side Event   Description
  CallbackRefresh     Triggered when the client object\'s Refresh method is called.
  ------------------- ---------------------------------------------------------------


 

[]{#p140} 

[]{#related-topics}

