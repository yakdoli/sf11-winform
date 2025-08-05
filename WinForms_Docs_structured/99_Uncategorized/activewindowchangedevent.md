---
title: activewindowchangedevent.md
original_path: WinForms_Docs/99_Uncategorized/activewindowchangedevent.md
created_at: 2025-08-05
---






#### ActiveWindow Changed Event {#activewindow-changed-event style="tab-stops: 0pt"}

The **ActiveWindowChanged** event is raised whenever the **ActiveWindow** property of **DockingManager** is changed. This event is used whenever you need to track the change in **ActiveChild** and do some content changes to the child. The following example demonstrates the changing of the **Child** header, based on the **ActiveWindow**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion][:]**[DockingManager]**[ Name][=\"**DockingManager**\"][ ActiveWindowChanged][=\"**DockingManager**\_ActiveWindowChanged\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\<][Grid][/\>]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\<][Grid][/\>]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][syncfusion][:]**[DockingManager]**[\>]                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [//Changing the ActiveWindow Header based on activewindow change]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                    |
| [private][ [void] **DockingManager**\_ActiveWindowChanged([DependencyObject] d, [DependencyPropertyChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| [     [if] (e.NewValue != [null])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [     {]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [       [FrameworkElement] element = e.NewValue [as] [FrameworkElement];]                                                                                                 |
|                                                                                                                                                                                                                                                                                    |
| [       **[DockingManager]**.SetHeader(element, [\"Active\"]);]                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [     }]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [     [if] (e.OldValue != [null])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [     {]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [       [FrameworkElement] element = e.OldValue [as] [FrameworkElement];]                                                                                                 |
|                                                                                                                                                                                                                                                                                    |
| [       **[DockingManager]**.SetHeader(element, [\"\"]);]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [     }]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [}    ]                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

