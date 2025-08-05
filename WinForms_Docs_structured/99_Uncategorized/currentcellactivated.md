---
title: currentcellactivated.md
original_path: WinForms_Docs/99_Uncategorized/currentcellactivated.md
created_at: 2025-08-05
---






#### CurrentCellActivated {#currentcellactivated style="tab-stops: 0pt"}

[] 

It occurs after the grid activates the specified cell as current cell. It receives an argument of type SyncfusionRoutedEventArgs that provides the cell co-ordinates, hence the location of the cell.

**[]** 

Example

**[]** 

This event can be triggered using the following code:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                  |
| []                                                                                                           |
|                                                                                                                                                  |
| [grid.CurrentCellActivated += [new] GridRoutedEventHandler(grid_CurrentCellActivated);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [void][ grid_CurrentCellActivated([object] sender, SyncfusionRoutedEventArgs args)]           |
|                                                                                                                                                                                                         |
| [{]                                                                                                                                                                 |
|                                                                                                                                                                                                         |
| [    MessageBox.Show([\"CurrentCell is \"] + grid.CurrentCell.RowIndex + [\", \"] + grid.CurrentCell.ColumnIndex);] |
|                                                                                                                                                                                                         |
| [}]                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p212} 

 

[]{#related-topics}

