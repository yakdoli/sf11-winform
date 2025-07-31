---
title: serversideevents19.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\serversideevents19.md
created_at: 2025-07-03
---






##### Server-side Events {#server-side-events style="tab-stops: 0pt"}

[] 

The server-side event can be triggered to perform an action by setting the following properties accordingly for the required event to be triggered, when the action is performed on the drag elements.

[] 


  ------------------- -----------------------------------------------------------------------------
  Server-side Event   Description
  Drop                Specifies the function to be executed after the dragged element is dropped.
  ------------------- -----------------------------------------------------------------------------


[] 


[{border="0"}]Note: Ensure the following AutoPostBack properties are enabled for the respective server-side events to be executed.


[] 


  -------------------- --------------------------------------------------
  Property             Description
  AutoPostBackOnDrop   Triggers a postback when the element is dropped.
  -------------------- --------------------------------------------------


[] 


[{border="0"}]Note: The server-side event when triggered, executes the function defined inside various events. Ensure that the server-side events are set to the respective event name and turn on the corresponding AutoPostBack property.


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [protected][ [void] DragDropManager1_Drop([object] sender, Syncfusion.Web.UI.WebControls.Shared.[DropEventArgs] e)] |
|                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [    Label1.Text = [\"\<b\>Element Dropped\</b\>\"];]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Protected][ [Sub] DragDropManager1_Drop([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Web.UI.WebControls.Shared.DropEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Label1.Text = [\"\<b\>Element Dropped\</b\>\"]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

