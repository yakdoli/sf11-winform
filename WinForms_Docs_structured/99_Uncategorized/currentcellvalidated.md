---
title: currentcellvalidated.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\currentcellvalidated.md
created_at: 2025-07-03
---






#### CurrentCellValidated {#currentcellvalidated style="tab-stops: 0pt"}

[] 

It occurs when the grid has successfully validated the contents of active current cell.

[] 

Example

**[]** 

This event can be triggered using the following code:

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| **[]**                                                                                                                   |
|                                                                                                                                                                            |
| [grid.CurrentCellValidated += [new] [GridRoutedEventHandler](grid_CurrentCellValidated);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| **[]**                                                                                                                                      |
|                                                                                                                                                                                               |
| [void][ grid_CurrentCellValidated([object] sender, SyncfusionRoutedEventArgs args)] |
|                                                                                                                                                                                               |
| [{]                                                                                                                                                       |
|                                                                                                                                                                                               |
| [    Console.WriteLine(grid.CurrentCell.ToString());]                                                                                                     |
|                                                                                                                                                                                               |
| [}]                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p218} 

 

[]{#related-topics}

