---
title: howtoholdtherowselectionafterthecellisdeactivated.md
original_path: WinForms_Docs/99_Uncategorized/howtoholdtherowselectionafterthecellisdeactivated.md
created_at: 2025-08-05
---








  









### How to Hold the Row Selection After the Cell is Deactivated {#how-to-hold-the-row-selection-after-the-cell-is-deactivated style="tab-stops: 0pt"}

Essential Grid enables you to hold the selection after the cell is deactivated. To hold the selection, cancel the *SelectionChanging* event, when the *[e.Reason]*[ is ]*MouseDown* or *Clear*.

 

The following code holds the selection even after the cell is deactivated:

[] 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [void][ Model_SelectionChanging([object] sender, [GridSelectionChangingEventArgs] e)] |
|                                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [            [if] (e.Reason == [GridSelectionReason].MouseDown \|\| e.Reason == [GridSelectionReason].Clear)]               |
|                                                                                                                                                                                                                                                   |
| [                e.Cancel = [true];]                                                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] Model_SelectionChanging([ByVal] sender [As] [Object], [ByVal] e [As] [GridSelectionChangingEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [            [If] e.Reason = [GridSelectionReason].MouseDown [OrElse] e.Reason = [GridSelectionReason].Clear [Then]]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [                e.Cancel = [True]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [            [End] [If]]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [        [End] [Sub]]                                                                                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[]{#related-topics}

