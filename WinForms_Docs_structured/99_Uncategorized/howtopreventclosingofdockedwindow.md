---
title: howtopreventclosingofdockedwindow.md
original_path: WinForms_Docs/99_Uncategorized/howtopreventclosingofdockedwindow.md
created_at: 2025-08-05
---






##### How to prevent closing of docked window? {#how-to-prevent-closing-of-docked-window style="tab-stops: 0pt"}

[]{#p131}This can be done in the DockVisibilityChanging event. When the end users tries to change the docking control visibility, this event will be handled. The members of this event is as follows.

[] 


  --------- --------------------------------------------------------------------------------------
  Members   Description
  Cancel    This property gets / sets the value indicating whether the event should be canceled.
  Control   Gets the control which is undergoing the transfer.
  --------- --------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [private][ [void] dockingManager1_DockVisibilityChanging([object] sender, Syncfusion.Windows.Forms.Tools.[DockVisibilityChangingEventArgs] arg)] |
|                                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [    arg.Cancel = [true];]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] dockingManager1_DockVisibilityChanging([ByVal] sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.DockVisibilityChangingEventArgs) [Handles] dockingManager1.DockVisibilityChanging] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    arg.Cancel = [True]]                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Additionally, the dock visibility of a control can be retrieved using **GetDockVisibility** method by passing the control as the parameter. Also DockVisibility can be set for the controls using **SetDockVisibility** method.

[]{#related-topics}

