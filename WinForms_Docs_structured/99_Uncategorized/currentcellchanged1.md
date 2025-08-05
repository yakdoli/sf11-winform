---
title: currentcellchanged1.md
original_path: WinForms_Docs/99_Uncategorized/currentcellchanged1.md
created_at: 2025-08-05
---






#### CurrentCellChanged {#currentcellchanged style="tab-stops: 0pt"}

[]{#p245}It occurs when the user changes the contents of active current cell.

 

Example

 

This event can be triggered using the following code:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                             |
|                                                                                                                                                                        |
| **[]**                                                                                                               |
|                                                                                                                                                                        |
| [grid.CurrentCellChanged += [new] [GridRoutedEventHandler](grid_CurrentCellChanged);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event Handler

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                  |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                             |
| [void][ grid_CurrentCellChanged([object] sender, SyncfusionRoutedEventArgs args)] |
|                                                                                                                                                                                             |
| [{]                                                                                                                                                     |
|                                                                                                                                                                                             |
| [    Console.WriteLine(grid.CurrentCell.ToString());]                                                                                                   |
|                                                                                                                                                                                             |
| [}]                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[]{#related-topics}

