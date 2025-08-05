---
title: currentcelleditingcomplete1.md
original_path: WinForms_Docs/99_Uncategorized/currentcelleditingcomplete1.md
created_at: 2025-08-05
---






#### CurrentCellEditingComplete {#currentcelleditingcomplete style="tab-stops: 0pt"}

[]{#p241}It occurs when the grid completes the editing mode for active current cell. \[After editing the cell, when you click to next cell or when you click any other form control or when you press escape, the cell editing mode gets stopped. This event is fired at that time.\]

 

Example

 

This event can be triggered using the following code:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                             |
|                                                                                                                                                                                        |
| **[]**                                                                                                                               |
|                                                                                                                                                                                        |
| [grid.CurrentCellEditingComplete += [new] [GridRoutedEventHandler](grid_CurrentCellEditingComplete);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event Handler

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                          |
|                                                                                                                                                                                                     |
| **[]**                                                                                                                                            |
|                                                                                                                                                                                                     |
| [void][ grid_CurrentCellEditingComplete([object] sender, SyncfusionRoutedEventArgs args)] |
|                                                                                                                                                                                                     |
| [{]                                                                                                                                                             |
|                                                                                                                                                                                                     |
| [    Console.WriteLine(grid.CurrentCell.ToString());]                                                                                                           |
|                                                                                                                                                                                                     |
| [}]                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

CurrentCellValidating

[]{#p242} 

It occurs when the grid validates the contents of active current cell. It receives an argument of type SyncfusionCancelRoutedEventArgs that provides an option to cancel this event.\[After editing completes, the text you entered will be checked for validity before getting applied to the cell. You can place your validation code here and if the text is invalid, you can cancel the operation by setting args.Cancel to true, which in turn will ignore the new text and will keep the old text. This event is fired during the validation operation.\]

 

Example

 

This event can be triggered using the following code:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                         |
|                                                                                                                                                                                    |
| **[]**                                                                                                                           |
|                                                                                                                                                                                    |
| [grid.CurrentCellValidating += [new] [GridCancelRoutedEventHandler](grid_CurrentCellValidating);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event Handler

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                           |
|                                                                                                                                                                                                      |
| **[]**                                                                                                                                             |
|                                                                                                                                                                                                      |
| [void][ grid_CurrentCellValidating([object] sender, SyncfusionCancelRoutedEventArgs args)] |
|                                                                                                                                                                                                      |
| [{]                                                                                                                                                              |
|                                                                                                                                                                                                      |
| [    args.Cancel = [true];]                                                                                                                 |
|                                                                                                                                                                                                      |
| [}]                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

