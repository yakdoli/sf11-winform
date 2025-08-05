---
title: currentcelldeactivating.md
original_path: WinForms_Docs/99_Uncategorized/currentcelldeactivating.md
created_at: 2025-08-05
---






#### CurrentCellDeactivating {#currentcelldeactivating style="tab-stops: 0pt"}

[] 

It occurs before the grid deactivates the specified cell as current cell. It receives an argument of type SyncfusionCancelRoutedEventArgs that let you cancel this event. When you click a second cell, it first deactivates the first(current) cell and then designates the second cell as current cell.

[] 

Example

**[]** 

This event can be triggered using the following code:

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| **[]**                                                                                                                               |
|                                                                                                                                                                                        |
| [grid.CurrentCellDeactivating += [new] [GridCancelRoutedEventHandler](grid_CurrentCellDeactivating);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [void][ grid_CurrentCellDeactivating([object] sender, SyncfusionCancelRoutedEventArgs args)] |
|                                                                                                                                                                                                        |
| [{]                                                                                                                                                                |
|                                                                                                                                                                                                        |
| [    args.Cancel = [true];]                                                                                                                   |
|                                                                                                                                                                                                        |
| [}]                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p213} 

 

[]{#related-topics}

