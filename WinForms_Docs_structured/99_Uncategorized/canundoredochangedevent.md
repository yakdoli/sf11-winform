---
title: canundoredochangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\canundoredochangedevent.md
created_at: 2025-07-03
---








  









### CanUndoRedoChanged Event {#canundoredochanged-event style="tab-stops: 0pt"}

 

This event occurs when the **CanUndoRedo** state is changed. The CanUndo and CanRedo properties indicate whether it is possible to undo and redo the actions in Edit Control respectively.

 

The event handler receives an argument of type **EventArgs**.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [private][ [void] editControl1_CanUndoRedoChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [Console][.WriteLine([\" CanUndoRedoChanged event is raised \"]);]                                                         |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] editControl1_CanUndoRedoChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                              |
| [Console.WriteLine([\" CanUndoRedoChanged event is raised \"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p111} 

[]{#related-topics}

