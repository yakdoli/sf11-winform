---
title: currentcelldeactivated1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\currentcelldeactivated1.md
created_at: 2025-07-03
---






#### CurrentCellDeactivated {#currentcelldeactivated style="tab-stops: 0pt"}

[]{#p239}It occurs after the grid activates the specified cell as current cell. It receives an argument of type GridCurrentCellDeactivatedEventArgs that gives the cell co-ordinates.

 

Example

 

This event can be triggered using the following code:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                     |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [grid.CurrentCellDeactivated += [new] [GridCurrentCellDeactivatedEventHandler](grid_CurrentCellDeactivated);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event Handler

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                              |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                         |
| [void][ grid_CurrentCellDeactivated([object] sender, GridCurrentCellDeactivatedEventArgs args)]               |
|                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [    MessageBox.Show([\"Cell deactivated:\"] + args.CellRowColumnIndex.RowIndex + [\", \"] + args.CellRowColumnIndex.ColumnIndex);] |
|                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

