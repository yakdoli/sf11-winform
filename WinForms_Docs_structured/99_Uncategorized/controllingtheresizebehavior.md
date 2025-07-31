---
title: controllingtheresizebehavior.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\controllingtheresizebehavior.md
created_at: 2025-07-03
---






##### Controlling the Resize Behavior {#controlling-the-resize-behavior style="tab-stops: 0pt"}

[] 

Essential Grid supports the resizing behavior of columns and rows in the Grid control. This is achieved by using the **ResizeColsBehavior** and **ResizeRowsBehavior** properties.

 

The **GridResizeCellsBehavior** enumeration provides the following options to control the resizing behavior.

[] 

[·      ]**AllowDragOutside**-Allows the user to drag the cell boundary outside the grid client area and resize the specific row or column.

[] 


{border="0"}Note: Grid client area is the area where the cells along with row and column headers are visible to the client. Dragging outside the client area means dragging beyond the boundary of the grid.


[] 

[·      ]**InsideGrid**-Allows the user to resize rows or columns from anywhere inside the grid by dragging the divider between any two row or column headers.

[·      ]**None**-Turns off the mouse control over the resizing rows and columns.

[·      ]**OutlineBounds**-Highlights the original cell boundaries of resizing row or column.

[·      ]**OutlineHeaders**-Highlights the header boundaries when the user resizes the associated row or column.

[·      ]**ResizeAll**-Resizes all rows or columns automatically when the user resizes one row or column with the mouse. All rows and columns are resized to the same size as the current row/column being resized.

[·      ]**ResizeSingle**-Resizes the row or column being resized by the user using the mouse.

[] 


{border="0"}Note: Also you can control the mouse controller\'s behavior at run time while the user is performing the action by subscribing to the ResizingColumns and ResizingRows events.


[] 

The following code illustrates how to use this method in Grid control:

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [this][.gridControl1.ResizeColsBehavior = [GridResizeCellsBehavior].InsideGrid;] |
|                                                                                                                                                                                               |
| [this][.gridControl1.ResizeRowsBehavior = [GridResizeCellsBehavior].InsideGrid;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [Me][.gridControl1.ResizeColsBehavior = GridResizeCellsBehavior.InsideGrid] |
|                                                                                                                                                                  |
| [Me][.gridControl1.ResizeRowsBehavior = GridResizeCellsBehavior.InsideGrid] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p332} 

 

[]{#related-topics}

