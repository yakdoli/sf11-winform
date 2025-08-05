---
title: selectedhierarchynavigatoritemchanged.md
original_path: WinForms_Docs/99_Uncategorized/selectedhierarchynavigatoritemchanged.md
created_at: 2025-08-05
---






#### Selected Hierarchy Navigator Item Changed {#selected-hierarchy-navigator-item-changed style="tab-stops: 0pt"}

 

Users can handle selected item changed by using the methods Command (ICommand) property or HierarchyNavigatorSelectedItemChanged event in Hierarchy Navigator control.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[XAML]**[]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][HierarchyNavigator][ HierarchyNavigatorSelectedItemChanged][=\"HierarchyNavigatorSelectedItemChanged\" /\>][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#]**[]                                                                                                                                 |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [HierarchyNavigator][ hierarchyNavigator = [new] [HierarchyNavigator]();\                                                                      |
| hierarchyNavigator.HierarchyNavigatorSelectedItemChanged += [new] [HierarchyNavigatorSelectedItemChangedEventHandler](HierarchyNavigatorSelectedItemChanged);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#]**[]                                                                                         |
|                                                                                                                                                                                                 |
| []                                                                                                                                                  |
|                                                                                                                                                                                                 |
| [private][ [void] HierarchyNavigatorSelectedItemChanged([object] sender, ] |
|                                                                                                                                                                                                 |
| [HierarchyNavigatorSelectedItemChangedEventArgs][ e)]                                                             |
|                                                                                                                                                                                                 |
| [{\                                                                                                                                                                                             |
| [     //Occurs when Selected Item Changed]]                                                                                                |
|                                                                                                                                                                                                 |
| [}]                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Passing the argument "HierarchyNavigator item" in a method called SelectNavigationItem can change the selected item.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#]**[]                                                                                           |
|                                                                                                                                                                                                      |
| []                                                                                                                                                    |
|                                                                                                                                                                                                      |
| [HierarchyNavigator][ hierarchyNavigator = [new] [HierarchyNavigator]();] |
|                                                                                                                                                                                                      |
| [hierarchyNavigator.SelectNavigationItem(hierarchyitem);]                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

