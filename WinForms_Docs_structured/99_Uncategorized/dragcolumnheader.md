---
title: dragcolumnheader.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\dragcolumnheader.md
created_at: 2025-07-03
---






#### Drag Column Header {#drag-column-header style="tab-stops: 0pt"}

[] 

In Grid control, a column header can be dragged to a new position by clicking on it, similar to how the fields in Microsoft Outlook are dragged without selecting the columns. This feature can be enabled in Grid control by adding the **DragColumnHeader** option under the **ControllerOptions** property. The event **QueryAllowDragColumnHeader** can be handled, while performing the drag operation.

 

The following code examples illustrate this feature.

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [this][.gridControl1.ControllerOptions \|= [GridControllerOptions].DragColumnHeader;]                                          |
|                                                                                                                                                                                                                                             |
| [void][ gridControl1_QueryAllowDragColumnHeader([object] sender, [GridQueryDragColumnHeaderEventArgs] e)] |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [if][ (e.Reason != [GridQueryDragColumnHeaderReason].HitTest)]                                                                 |
|                                                                                                                                                                                                                                             |
| [System.Diagnostics.[Debug].WriteLine([\"gridControl1_QueryAllowDragColumnHeader: \"] + e.ToString());]                                                 |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Me][.gridControl1.ControllerOptions = [Me].gridControl1.ControllerOptions [Or] GridControllerOptions.DragColumnHeader]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] gridControl1_QueryAllowDragColumnHeader([ByVal] sender [As] [Object], [ByVal] e [As]                                                    GridQueryDragColumnHeaderEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [If] e.Reason \<\> GridQueryDragColumnHeaderReason.HitTest [Then]]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        System.Diagnostics.Debug.WriteLine([\"gridControl1_QueryAllowDragColumnHeader: \"] & e.ToString())]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [End] [If]]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 The following screen shot illustrates how to drag the column header.

[] 

{border="0"}

[] 

*[Figure ][185][: Drag Column Header]*

 

[]{#p341} 

 

[]{#related-topics}

