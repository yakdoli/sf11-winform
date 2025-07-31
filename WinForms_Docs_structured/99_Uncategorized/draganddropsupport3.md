---
title: draganddropsupport3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\draganddropsupport3.md
created_at: 2025-07-03
---






#### Drag-and-Drop Support {#drag-and-drop-support style="tab-stops: 0pt"}

Essential Grid for WPF provides support for drag-and-drop functionality. This feature enables the user to just click a column header and drag it to a new position. It is not required to select the column header for dragging. This is an easy way of rearranging the columns dynamically. You can enable or disable this feature using AllowDragColumns property of the Grid as follows:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                         |
|                                                                                                                                                    |
| **[]**                                                                                           |
|                                                                                                                                                    |
| [//Allow column dragging]                                                                        |
|                                                                                                                                                    |
| [this][.grid.AllowDragColumns = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following image illustrates this feature:

 

{border="0"}

Figure 68: Drag and Drop support

**[]** 

In the above image, you can see the column header 1 being dragged to be placed before column 3.

[]{#related-topics}

