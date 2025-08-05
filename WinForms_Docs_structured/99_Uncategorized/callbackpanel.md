---
title: callbackpanel.md
original_path: WinForms_Docs/99_Uncategorized/callbackpanel.md
created_at: 2025-08-05
---








  









### CallbackPanel {#callbackpanel style="tab-stops: 0pt"}

 

The CallbackPanel control is a panel derived class that lets you invoke AJAX style callbacks from the client and refresh the contents of the panel in the server.

The common usage for this control is very simple.

 

1.   Drag the CallbackPanel control from the toolbox onto your page.

9.   Fill more controls within this panel.

10.  Decide when to invoke a callback on this panel. For example, on a button click or listbox selection change.

11.  Write java script code to invoke the callback on the panel, from the button element\'s click, for example, as given below.

 

  ---------------------------------------------------------------------------------------------------
  [\_sfCallbackPanel1.callback(\'some args\');]
  ---------------------------------------------------------------------------------------------------

 

This will load the page on the server and will call the CallbackPanel\'s CallbackRefresh event. In this event handler, the new values selected / changed by the user in the page are available, based on which you can update the CallbackPanel\'s content.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [protected][ [void] CallbackPanel1_CallbackRefresh([object] sender, Syncfusion.Web.UI.WebControls.[CancellableCallbackEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                          |
| [// Update CallbackPanel1 contents here.]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following diagram illustrates the sequence of events that result in a CallbackPanel\'s refresh.

 

[]{#p244}{border="0"}

[[[]]]{.underline} 

More:









