---
title: fillsplitterpanechangedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\fillsplitterpanechangedevent.md
created_at: 2025-07-03
---






##### FillSplitterPaneChanged Event {#fillsplitterpanechanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The FillSplitterPane property of a TreeViewAdv control is the one that toggles support for using the control inside a dynamic splitter window and sharing scrollbars with the parent window. The FillSplitterPaneChanged event will be raised when this property is changed.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [private][ [void] treeViewAdv1\_[FillSplitterPaneChanged]([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [//The below line will be printed in the output window at run time.]                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [Console][.Write([\"][FillSplitterPaneChanged][ Event is raised \"]);]                                   |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Private Sub ][treeViewAdv1\_[FillSplitterPaneChanged(][ByVal][ sender][ As Object][, ][ByVal][ e ][As][ EventArgs)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\'The below line will be printed in the output window at run time.]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Console][.Write([\"][FillSplitterPaneChanged][ Event is raised \"])]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End Sub][]                                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

