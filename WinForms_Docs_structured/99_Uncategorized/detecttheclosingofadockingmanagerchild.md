---
title: detecttheclosingofadockingmanagerchild.md
original_path: WinForms_Docs/99_Uncategorized/detecttheclosingofadockingmanagerchild.md
created_at: 2025-08-05
---






#### Detect the closing of a DockingManagerchild {#detect-the-closing-of-a-dockingmanagerchild style="tab-stops: 0pt"}

 

**DockStateChanged** and **CloseButtonClick** are the two events, which can be used to detect whether the child is closed. **DockStateChanged** event is raised whenever a child changes its State. **CloseButtonClick** event is raised only when close button of the Document child is clicked. The following code describes how to handle the closing of a child using **DockStateChanged** event.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:]**[DockingManager]**[ DockStateChanged][=\"**DockingManager**\_DockStateChanged\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][Grid][/\>]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][syncfusion][:]**[DockingManager]**[\>][]                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| [private][ [void] **DockingManager**\_DockStateChanged([FrameworkElement] sender,[DockStateEventArgs] e)] |
|                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [     [if] (e.NewState == [DockState].Hidden)]                                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
| [     {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [        [//TODO:your code here to handle the closed state.]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [     }]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [}        ][]                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

