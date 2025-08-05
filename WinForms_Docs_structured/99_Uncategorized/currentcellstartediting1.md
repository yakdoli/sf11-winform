---
title: currentcellstartediting1.md
original_path: WinForms_Docs/99_Uncategorized/currentcellstartediting1.md
created_at: 2025-08-05
---






#### CurrentCellStartEditing {#currentcellstartediting style="tab-stops: 0pt"}

[]{#p240}It occurs before the current cell switches into editing mode (when the cell is double-clicked). It receives an argument of type SyncfusionCancelRoutedEventArgs that provides an option to cancel this event.

 

 Example

This event can be triggered using the following code:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                             |
|                                                                                                                                                                                        |
| **[]**                                                                                                                               |
|                                                                                                                                                                                        |
| [grid.CurrentCellStartEditing += [new] [GridCancelRoutedEventHandler](grid_CurrentCellStartEditing);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event Handler

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                             |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [void][ grid_CurrentCellStartEditing([object] sender, SyncfusionCancelRoutedEventArgs args)] |
|                                                                                                                                                                                                        |
| [{]                                                                                                                                                                |
|                                                                                                                                                                                                        |
| [    args.Cancel = [true];]                                                                                                                   |
|                                                                                                                                                                                                        |
| [}]                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

