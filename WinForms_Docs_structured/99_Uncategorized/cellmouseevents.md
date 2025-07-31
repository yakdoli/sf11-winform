---
title: cellmouseevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\cellmouseevents.md
created_at: 2025-07-03
---






#### Cell Mouse Events {#cell-mouse-events style="tab-stops: 0pt"}

[] 

The following are the cell mouse events:

**[]** 

[·      ]**CellMouseDown**-Occurs when a mouse button is pressed in a grid cell with the click count.

[·      ]**CellMouseUP**--Occurs when a mouse button is released in a grid cell with the click count.

[·      ]**CellMouseHover** -- Occurs when the mouse is hovered over a grid cell.

[·      ]**CellMouseMove** -- Occurs when the mouse is moved around the grid cell.

[] 

These events receive an argument of type GridCellMouseControllerEventArgs that provides information related to mouse events including the click position.

**[]** 

Example

**[]** 

These events can be triggered using the following code:

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [grid.CellMouseDown += [new] [GridCellMouseControllerEventHandler](grid_CellMouseDown);]   |
|                                                                                                                                                                             |
| [grid.CellMouseHover += [new] [GridCellMouseControllerEventHandler](grid_CellMouseHover);] |
|                                                                                                                                                                             |
| [grid.CellMouseMove += [new] [GridCellMouseControllerEventHandler](grid_CellMouseMove);]   |
|                                                                                                                                                                             |
| [grid.CellMouseUp += [new] [GridCellMouseControllerEventHandler](grid_CellMouseUp);]       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handlers

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [void][ grid_CellMouseUp([object] sender, GridCellMouseControllerEventArgs args)]                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [    MessageBox.Show([\"Mouse \"] + args.MouseControllerEventArgs.Button + [\" Button is clicked \"] + args.MouseControllerEventArgs.ClickCount + [\" times\"]);] |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [void][ grid_CellMouseMove([object] sender, GridCellMouseControllerEventArgs args)]                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [    RowColumnIndex cell = grid.PointToCellRowColumnIndex(args.MouseControllerEventArgs.Location);]                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [    MessageBox.Show([\"Mouse is at cell\[\"] + cell.RowIndex + [\", \"] + cell.ColumnIndex + [\"\]\"]);]                                                         |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [void][ grid_CellMouseHover([object] sender, GridCellMouseControllerEventArgs args)]                                                                                |
|                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [    RowColumnIndex cell = grid.PointToCellRowColumnIndex(args.MouseControllerEventArgs.Location);]                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [    MessageBox.Show([\"Mouse is hovering the cell\[\"]+cell.RowIndex+[\", \"]+cell.ColumnIndex+[\"\]\"]);]                                                       |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [void][ grid_CellMouseDown([object] sender, GridCellMouseControllerEventArgs args)]                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [    MessageBox.Show([\"Mouse \"] + args.MouseControllerEventArgs.Button + [\" Button is clicked \"] + args.MouseControllerEventArgs.ClickCount + [\" times\"]);] |
|                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Output

**[]** 

The following outputs are generated using the code above.

[] 

{border="0"}

[] 

Figure 86: MouseUp

***[]*** 

***[{border="0"}]**[]***

***[]*** 

Figure 87: MouseMove

***[]*** 

{border="0"}

 

Figure 88: MouseHover

***[]*** 

{border="0"}

***[]*** 

Figure 89: MouseDown

[]{#p210} 

 

[]{#related-topics}

