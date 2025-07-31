---
title: currentcellactivating.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\currentcellactivating.md
created_at: 2025-07-03
---






#### CurrentCellActivating {#currentcellactivating style="tab-stops: 0pt"}

[] 

When you click a grid cell at run time, it becomes the CurrentCell (activated/designated as CurrentCell). This event is fired while activating this cell. It occurs before the grid activates the specified cell as current cell. It receives an argument of type GridCurrentCellActivatingEventArgs that let you specify -- **ActivateCurrentCellOptions** for the given cell.

[] 

Example

**[]** 

This event can be triggered using the following code:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [grid.CurrentCellActivating += [new] [GridCurrentCellActivatingEventHandler](grid_CurrentCellActivating);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [void][ grid_CurrentCellActivating([object] sender, GridCurrentCellActivatingEventArgs args)] |
|                                                                                                                                                                                                         |
| [{]                                                                                                                                                                 |
|                                                                                                                                                                                                         |
| [    args.ActivateOptions.SetCurrentCellOptions = GridSetCurrentCellOptions.ScrollInView;]                                                                          |
|                                                                                                                                                                                                         |
| [}]                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p211} 

 

[]{#related-topics}

