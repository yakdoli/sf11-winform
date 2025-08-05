---
title: howcanthenudgeoperationbestopped.md
original_path: WinForms_Docs/99_Uncategorized/howcanthenudgeoperationbestopped.md
created_at: 2025-08-05
---








  









### How can the nudge operation be stopped? {#how-can-the-nudge-operation-be-stopped style="tab-stops: 0pt"}

The nudge operation can be stopped by handling the DiagramControl's PreviewKeyDown event, as shown in the code snippet displayed below.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| [        [//Register the PreviewKeyDown event.]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [        diagramControl.PreviewKeyDown += [new] [KeyEventHandler](MainWindow_PreviewKeyDown);]                                                                                             |
|                                                                                                                                                                                                                                                                             |
| [        [//Handle the PreviewKeyDown event for the arrow keys.]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| [        [void] MainWindow_PreviewKeyDown([object] sender, [KeyEventArgs] e)]                                                                                         |
|                                                                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| [            [if] (e.Key == [Key].Up \|\| e.Key == [Key].Down \|\| e.Key == [Key].Right \|\| e.Key == [Key].Left)] |
|                                                                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| [                e.Handled = [true];]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [\'Register the PreviewKeyDown event.][]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ diagramControl.PreviewKeyDown += New KeyEventHandler(AddressOf MainWindow_PreviewKeyDown)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [        [\'Handle the PreviewKeyDown event for the arrow keys.]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [        [Private] [Sub] MainWindow_PreviewKeyDown([ByVal] sender [As] [Object], [ByVal] e [As] [KeyEventArgs])]                                              |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [            [If] e.Key = [Key].Up [OrElse] e.Key = [Key].Down [OrElse] e.Key = [Key].Right [OrElse] e.Key = [Key].Left [Then]] |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [                e.Handled = [True]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [            [End] [If]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [        [End] [Sub]][]                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

