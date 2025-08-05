---
title: callbackmultiplexer.md
original_path: WinForms_Docs/99_Uncategorized/callbackmultiplexer.md
created_at: 2025-08-05
---








  









### CallbackMultiplexer {#callbackmultiplexer style="tab-stops: 0pt"}

 

 

A CallbackMultiplexer gives you the most flexibility when executing callbacks. In a general sense, you can trigger a callback from any event in the page on the multiplexer and return any data from multiplexer\'s Callback event handler, all this without automatically affecting any UI in the page. On the other hand you can also choose to update the contents of more than one callback control or panel in the Callback event handler and hence the name multiplexer.

The CallbackMultiplexer control is a CallbackWebControl-derived class that lets you invoke AJAX style callbacks from the client and refresh the contents of Multiple CallbackPanels in the server.

The common usage for this control is very simple.

 

1.   Drag the CallbackMultiplexer control from the Toolbox onto your page.

20.  Fill more CallbackPanels and add more controls inside these panels.

21.  Decide which and when to invoke a callback on these CallbackPanels. For example, on a button click or listbox selection change.

22.  Write java script code to invoke the callback on panel from button element\'s click, for example, as given below.

 

  ----------------------------------------------------------------------------------------------------------------------------------
  [\_sfCallbackMultiplexer1.callback([\"some args\"]);]
  ----------------------------------------------------------------------------------------------------------------------------------

 

This will load the page on server and calls the CallbackMultiplexer\'s Callback event handler. In this event handler, the new values that the user might have selected / changed in the page are available based on which you can update CallbackPanel\'s content.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                       |
| [protected][ [void] CallbackMultiplexer1_Callback([object] sender, Syncfusion.Web.UI.WebControls.CallbackEventArgs e)] |
|                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                       |
| [   [// Refresh elements within the particular Callback panels based up on the Arguments ]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Protected][ [Sub] CallbackMultiplexer1_Callback([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Web.UI.WebControls.CallbackEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [    [\' Refresh elements within the particular Callback panels based up on the Arguments ]]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p253} 

More:







