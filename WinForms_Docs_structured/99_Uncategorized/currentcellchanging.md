---
title: currentcellchanging.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\currentcellchanging.md
created_at: 2025-07-03
---






#### CurrentCellChanging {#currentcellchanging style="tab-stops: 0pt"}

[] 

It occurs when the user wants to modify the contents of current cell. It receives an argument of type SyncfusionCancelRoutedEventArgs that provides an option to cancel this event.

[] 

Example

**[]** 

This event can be triggered using the following code:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| **[]**                                                                                                                       |
|                                                                                                                                                                                |
| [grid.CurrentCellChanging += [new] [GridCancelRoutedEventHandler](grid_CurrentCellChanging);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| **[]**                                                                                                                                           |
|                                                                                                                                                                                                    |
| [void][ grid_CurrentCellChanging([object] sender, SyncfusionCancelRoutedEventArgs args)] |
|                                                                                                                                                                                                    |
| [{]                                                                                                                                                            |
|                                                                                                                                                                                                    |
| [    args.Cancel = [true];]                                                                                                               |
|                                                                                                                                                                                                    |
| [}]                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p219} 

 

[]{#related-topics}

