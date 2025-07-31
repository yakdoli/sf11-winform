---
title: controlremovedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\controlremovedevent.md
created_at: 2025-07-03
---






#### ControlRemoved Event {#controlremoved-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event occurs when a new control is removed from this TabControlAdv.

 

**Event Data**

 

This Event Handler receives an argument of type **ControlEventArgs** containing data related to this event. The following ControlEventArgs property provides information specific to this event.

[] 


  --------- ---------------------------------------------
  Member    Description
  Control   Gets the control object used by this event.
  --------- ---------------------------------------------


[] 


{border="0"} Note:[ ]The TabControlAdv.RemoveAll() method removes all the TabPages and additional controls from the TabControlAdv.


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                  |
| [private][ [void] tabControlAdv1_ControlRemoved([object] sender, System.Windows.Forms.[ControlEventArgs] e)] |
|                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                  |
| [//Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                                   |
|                                                                                                                                                                                                                                                                  |
| [Console][.Write([\"Control Removed event is raised\"]);]                                                                                             |
|                                                                                                                                                                                                                                                                  |
| [//Gets the control object used by this event.]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                  |
| [Console][.Write([\"Control Name :\"] + e.Control.ToString());]                                                                                      |
|                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] tabControlAdv1_ControlRemoved([ByVal] sender [As] [Object], [ByVal] e [As] System.Windows.Forms.ControlEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                        |
| [\'Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Console][.Write([\"Control Removed event is raised\"])]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                        |
| [\'Gets the control object used by this event.]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Console][.Write([\"Control Name :\"] + e.Control.ToString())]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

