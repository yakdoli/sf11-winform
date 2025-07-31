---
title: ajaxsupport2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\ajaxsupport2.md
created_at: 2025-07-03
---






##### AJAX support {#ajax-support style="tab-stops: 0pt"}

[] 

The various callback events that can be fired to perform the various user-defined functions and refresh the control without triggering a postback are as follows.

[] 


+----------------------------------------+---------------------------------------------------------------------------------------------------------+
|                                        |                                                                                                         |
|                                        |                                                                                                         |
| Client-Side Event                      | Description                                                                                             |
+----------------------------------------+---------------------------------------------------------------------------------------------------------+
| AfterCallbackResponseProcessedScript   | Specifies the script that will be executed after the callback result gets processed.                    |
+----------------------------------------+---------------------------------------------------------------------------------------------------------+
| AfterCallbackScript                    | Specifies the client side function to call after the callback occurs.                                   |
+----------------------------------------+---------------------------------------------------------------------------------------------------------+
| BeforeCallbackResponseProcessingScript | Specifies the script that will be executed before the callback result gets processed.                   |
+----------------------------------------+---------------------------------------------------------------------------------------------------------+
| BeforeCallbackScript                   | Specifies the client side function to call before the callback occurs.                                  |
+----------------------------------------+---------------------------------------------------------------------------------------------------------+
| EnableCallbacks                        | Specifies whether control refresh operations should be performed via callbacks. Default value is False. |
+----------------------------------------+---------------------------------------------------------------------------------------------------------+


[] 


+-----------------------------------+-----------------------------------------+
|                                   |                                         |
|                                   |                                         |
| Server-Side Event                 | Description                             |
+-----------------------------------+-----------------------------------------+
| CallbackRefresh                   | Refreshes the control without postback. |
+-----------------------------------+-----------------------------------------+


[] 

To perform callback the **EnableCallbacks** property must be set to **True**.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                         |
|                                   |                                                                                                         |
| Property                          | Description                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------+
| EnableCallbacks                   | Specifies whether control refresh operations should be performed via callbacks. Default value is False. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------+


[] 

Invoking Callback

[] 

A callback can be invoked using the **Refresh** method. This invokes the various above listed client side events during this process

[] 


  --------- ----------- ------------------------------------------------------------------------------------------------------------------------------------------------------
  Method    Parameter   Description
  Refresh   string      Sends CallBack to server without page refreshing. Handle this event to change the contents of the panel according to the event args the client sent.
  --------- ----------- ------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

1.   Set the various client event properties to the function name that should be executed.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][cc1][:][TreeView][ [ID][=\"TreeView1\"] [runat][=\"server\"] [ClientObjectId][=\"tree\"] [BorderColor][=\"Gray\"] [BorderStyle][=\"Solid\"]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    [BorderWidth][=\"1px\"] [Height][=\"80px\"] [Width][=\"160px\"] [EnableCallbacks][=\"True\"] [OnCallbackRefresh][=\"TreeView1_CallbackRefresh\"] [AfterCallbackResponseProcessedScript][=\"AfterScriptProcess()\"] [AfterCallbackScript][=\"AfterScriptCall()\"] [BeforeCallbackResponseProcessingScript][=\"BeforeScriptProcess()\"] [BeforeCallbackScript][=\"BeforeScriptCall()\"] [\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    [\<%][\--Add the required items\--][%\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][cc1][:][TreeView][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][br][ [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][input][ [type][=\"button\"] [id][=\"click\"] [onclick][=\"OnRefresh()\"] [value][=\"Click\"] [/\>]]                                                                                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

58.  Define the functions that should be performed when the respective client events are invoked.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[script\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                                |
| [    [function] OnRefresh(OData)]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        tree.Refresh();           ]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [    [function] AfterScriptProcess()]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        alert([\"AfterCallbackResponseProcessedScript client event is fired\"]);]                                                                                                                  |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [    [function] AfterScriptCall()]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        alert([\"AfterCallbackScript client event is fired\"]);]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [    [function] BeforeScriptProcess()]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [    {   ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [        alert([\"BeforeCallbackResponseProcessingScript client event is fired\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [    [function] BeforeScriptCall()]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [        alert([\"BeforeCallbackScript client event is fired\"]);]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Server side Event

[] 

Here, on button click, the Refresh method is called which triggers the **CallbackRefresh** event and adds a child node to Node1 parent item and refreshes the control using callback.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [protected][ [void] TreeView1_CallbackRefresh([object] sender, Syncfusion.Web.UI.WebControls.Tools.[CallbackEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [    [TreeViewNode] AddedNode = [new] [TreeViewNode]();]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                |
| [    AddedNode.Text = [\"Inbox\"];]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| [    [TreeViewNode] node1 = [this].TreeView1.FindNode([\"Node1\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                |
| [    node1.Items.Add(AddedNode);]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                            |
| [Protected [Sub] TreeView1_CallbackRefresh([ByVal] sender [As] Object, [ByVal] e [As] Syncfusion.Web.UI.WebControls.Tools.CallbackEventArgs)] |
|                                                                                                                                                                                                                                                                                                            |
| [       [Dim] AddedNode [As] TreeViewNode = [New] TreeViewNode()]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [       AddedNode.Text = [\"Inbox\"]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| [       [Dim] node1 [As] TreeViewNode = [Me].TreeView1.FindNode([\"Node1\"])]                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| [       node1.Items.Add(AddedNode)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

