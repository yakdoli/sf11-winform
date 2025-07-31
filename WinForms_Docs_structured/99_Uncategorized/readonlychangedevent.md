---
title: readonlychangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\readonlychangedevent.md
created_at: 2025-07-03
---








  









### ReadOnlyChanged Event {#readonlychanged-event style="tab-stops: 0pt"}

 

This event occurs when the **ReadOnly** property is changed. The ReadOnly property specifies whether the Edit Control is in the read-only mode.

 

The event handler receives an argument of type **EventArgs**.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [// Handle the ReadOnlyChanged event.]                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [this][.editControl1.ReadOnlyChanged+=[new] EventHandler(editControl1_ReadOnlyChanged);]                                  |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [// Set the ReadOnly property to True.]                                                                                                                                           |
|                                                                                                                                                                                                                                     |
| [this][.editControl1.ReadOnly = [true];]                                                                                  |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [private][ [void] editControl1_ReadOnlyChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [Console][.WriteLine([\" ReadOnlyChanged event is raised \"]);]                                                         |
|                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [\' Handle the ReadOnlyChanged event.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                           |
| [Me][.editControl1.ReadOnlyChanged+=[New] EventHandler(editControl1_ReadOnlyChanged)]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                           |
| [\' Set the ReadOnly property to True.]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                           |
| [Me][.editControl1.ReadOnly = [True]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] editControl1_ReadOnlyChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine([\" ReadOnlyChanged event is raised \"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p161} 

[]{#related-topics}

