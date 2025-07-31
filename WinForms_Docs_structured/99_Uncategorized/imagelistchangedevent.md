---
title: imagelistchangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\imagelistchangedevent.md
created_at: 2025-07-03
---






##### ImageListChanged Event {#imagelistchanged-event style="tab-stops: 0pt"}

[] 

When the imagelist property is changed, ImageListChanged event will be raised. Every docked control will have SetDockIcon property to set the icons for the control. When this property is changed, the above event will be triggered.

[] 


  --------- ----------------------------------------------------------------------
  Member    Description
  Control   Gets the docked control for which the imagelist property is changed.
  --------- ----------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                |
| [//Occurs when the ImageList property changes]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                |
| [private void ][dockingManager1_ImageListChanged(][object ][sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine(\"ImageList Changed Event Is Triggered\");]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                |
| [//Here the code which set the Docking Icon dynamically.]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| [dockingManager1.SetDockIcon(][this][.panel1,0);]                                                                                         |
|                                                                                                                                                                                                                                                                                                |
| [dockingManager1.SetDockIcon(][this][.panel2,1);]                                                                                         |
|                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                      |
| [\'Occurs when the ImageList property changes]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] dockingManager1_ImageListChanged([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                      |
| [Console.WriteLine([\"ImageList Changed Event Is Triggered\"])]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                      |
| [\'Here the code which set the Docking Icon dynamically.]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                      |
| [dockingManager1.SetDockIcon([Me].panel1, 0)]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [dockingManager1.SetDockIcon([Me].panel2, 1)]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p117}[]{#_InitializeControlOnLoad_Event} 

[]{#related-topics}

