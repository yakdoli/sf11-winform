---
title: currentcelldeactivated.md
original_path: WinForms_Docs/99_Uncategorized/currentcelldeactivated.md
created_at: 2025-08-05
---






#### CurrentCellDeactivated {#currentcelldeactivated style="tab-stops: 0pt"}

[] 

It occurs after the grid activates the specified cell as current cell. It receives an argument of type GridCurrentCellDeactivatedEventArgs that gives the cell co-ordinates.

[] 

Example

**[]** 

This event can be triggered using the following code:

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [grid.CurrentCellDeactivated += [new] [GridCurrentCellDeactivatedEventHandler](grid_CurrentCellDeactivated);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
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

[]{#p214} 

 

[]{#related-topics}

