---
title: cellbuttonclick1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\cellbuttonclick1.md
created_at: 2025-07-03
---






#### CellButtonClick {#cellbuttonclick style="tab-stops: 0pt"}

[]{#p233}This event is triggered when a cell button is clicked. It receives an argument of type GridCellButtonClickEventArgs, which helps display the row and column indices of the cell whose button is clicked. For example: If the cell button clicked is placed in the second row and second column, the display message will be- "Button clicked at cell \[2,2\]".

**[]** 

Example

 

This event can be triggered using the following code:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                |
|                                                                                                                                                                           |
| **[]**                                                                                                                  |
|                                                                                                                                                                           |
| [grid.CellButtonClick += [new] [GridCellButtonClickEventHandler](grid_CellButtonClick);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

**[]** 

The following event handler sets up new data for clipboard paste.

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                           |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [void][ grid_CellButtonClick([object] sender, GridCellButtonClickEventArgs e)]                             |
|                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [    MessageBox.Show([\"Button clicked at cell\[\"] + e.RowIndex + [\",\"] + e.ColumnIndex + [\"\]\"]);] |
|                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Output

**[]** 

The following output is generated using the code above.

[] 

{border="0"}

Figure 99: CellButtonClick

 

 

[]{#related-topics}

