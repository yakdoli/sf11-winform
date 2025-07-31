---
title: serversideevents18.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\serversideevents18.md
created_at: 2025-07-03
---






##### Server-Side Events {#server-side-events style="tab-stops: 0pt"}

[] 

The server side events can be triggered to perform some action, for which the following properties has to be set accordingly for the required event to be triggered when that action is performed on the snap elements.

[] 


  --------------- -------------------------------------------------------------------
  Property        Description
  Dock            Specifies the function to execute, when the control is docked.
  Collapse        Specifies the function to execute, when the control is collapsed.
  Expand          Specifies the function to execute, when the control is expanded.
  Minimize        Specifies the function to execute, when the control is minimized.
  UnMinimize      Specifies the function to execute, when the control is maximized.
  --------------- -------------------------------------------------------------------


[] 

Make sure the following **AutoPostBack** properties are enabled for the respective server side events to be executed.

[] 


  ----------------------------- -----------------------------------------------------
           Property             Description
  AutoPostBackOnDock            Triggers a postback, when the control is docked.
  AutoPostBackOnCollapse        Triggers a postback, when the control is collapsed.
  AutoPostBackOnExpand          Triggers a postback, when the control is expanded.
  AutoPostBackOnMinimize        Triggers a postback, when the control is minimized.
  AutoPostBackOnUnMinimize      Triggers a postback, when the control is maximized.
  ----------------------------- -----------------------------------------------------


[] 

The server side events when triggered, executes the function defined inside the various events. Make sure to set the server side events to the respective event name and turn on the corresponding AutoPostBack property.

 

The **Snap1_Dock** server event will be triggered, when the snap is docked inside a container which will display the fired event name. The **Snap_Expand** event will be triggered on expanding the content template of the snap which will display the name of the fired event.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [protected][ [void] Snap1_Dock([object] sender, Syncfusion.Web.UI.WebControls.Tools.Snap.[SnapDockEventArgs] e)] |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [     lblPostBackAction.Text = [\"\<b\>Snap1\</b\> Docked.\"];]                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [protected][ [void] Snap1_Expand([object] sender, Syncfusion.Web.UI.WebControls.Tools.Snap.[SnapEventArgs] e)]   |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [    lblPostBackAction.Text = [\"\<b\>Snap1\</b\> Expanded.\"];]                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    ]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Protected][ [Sub] Snap1_Dock([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Web.UI.WebControls.Tools.Snap.SnapDockEventArgs)]   |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    lblPostBackAction.Text = [\"\<b\>Snap1\</b\> Docked.\"]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Protected][ [Sub] Snap1_Expand([ByVal] sender [As] [Object], [ByVal] e [As ]Syncfusion.Web.UI.WebControls.Tools.Snap.SnapDockEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    lblPostBackAction.Text = [\"\<b\>Snap1\</b\> Expanded.\"]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Similarly the events for snap Collapse, Minimize and UnMinimize actions can be fired.

[]{#related-topics}

