---
title: oledraganddrop.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\oledraganddrop.md
created_at: 2025-07-03
---






#### OLE Drag-and-Drop {#ole-drag-and-drop style="tab-stops: 0pt"}

[] 

Essential Grid offers support functionality like Object Linking and Embedding (OLE) Drag-and-Drop. A range in one grid can be selected and dragged to another grid or into a **Rich Edit Box**. The following screen shot shows a selected region of grid, that has been dragged and dropped into another grid:

[] 

{border="0"}

[] 

*[Figure 1: OLE Drag-and-Drop]****[]***

[] 

The following code example illustrates this feature.

[] 

1.   Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [gridControl1.AllowDrop = [true];]                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [gridControl2.AllowDrop = [true];]                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [private][ [void] gridControl1_DragOver([object] sender, [DragEventArgs] e)] |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [    e.Effect = [DragDropEffects].Copy;]                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [private][ [void] gridControl2_DragOver([object] sender, [DragEventArgs] e)] |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [    e.Effect = [DragDropEffects].Copy;]                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                 |
|                                                                                                                                                                                    |
| []                                                                                                                               |
|                                                                                                                                                                                    |
| [gridControl1.AllowDrop = [True]]                                                                                         |
|                                                                                                                                                                                    |
| [gridControl2.AllowDrop = [True]]                                                                                         |
|                                                                                                                                                                                    |
| []                                                                                                                                |
|                                                                                                                                                                                    |
| [private][ void gridControl1_DragOver([Object] sender, DragEventArgs e)] |
|                                                                                                                                                                                    |
| [e.Effect = DragDropEffects.Copy]                                                                                                              |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [private][ void gridControl2_DragOver([Object] sender, DragEventArgs e)] |
|                                                                                                                                                                                    |
| [e.Effect = DragDropEffects.Copy]                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p342} 

 

[]{#related-topics}

