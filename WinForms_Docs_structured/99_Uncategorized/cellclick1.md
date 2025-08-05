---
title: cellclick1.md
original_path: WinForms_Docs/99_Uncategorized/cellclick1.md
created_at: 2025-08-05
---






#### CellClick {#cellclick style="tab-stops: 0pt"}

[]{#p234}This event is triggered when a cell is clicked. It receives an argument of type GridCellClickEventArgs  which helps display the row and column indices of the cell that is clicked with its click count. For example: If the cell clicked is placed in the third row and second column and clicked once, the display message will be- "Cell \[3,2\] is clicked 1 times".

 

Example

 

This event can be triggered using the following code:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                              |
|                                                                                                                                                         |
| **[]**                                                                                                |
|                                                                                                                                                         |
| [grid.CellClick += [new] [GridCellClickEventHandler](grid_CellClick);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event Handler

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [void][ grid_CellClick([object] sender, GridCellClickEventArgs e)]                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                        |
| [    MessageBox.Show([\"Cell\[\"] + e.RowIndex + [\", \"] + e.ColumnIndex + [\"\] is clicked \"] + e.ClickCount + [\" times.\"]);] |
|                                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The following output is generated using the code above.

 

{border="0"}

Figure 100: CellClick

 

 

[]{#related-topics}

