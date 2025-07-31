---
title: sortingcustomization3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\sortingcustomization3.md
created_at: 2025-07-03
---






##### Sorting Customization {#sorting-customization style="tab-stops: 0pt"}

 

[·      ]To enable or disable the multi-sorting feature, use the **AllowMultiSorting** property.[  ]

[  ]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[ ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [GridPropertiesModel][\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [                Caption = [\"Orders\"],]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| **[                AllowSorting=[true],]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| **[                AllowMultiSorting=[true]]**[,]                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| **[                ActionMode = ActionMode.JSON]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [           ]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [            };][]                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]To render the grid with initial sorting, use the **SortDescriptors** property.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [        [public] [ActionResult] Index()]                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [                Caption = [\"Orders\"],]                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [                AllowSorting=[true],]                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [                AllowMultiSorting=[true],]                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [                AutoFormat=[Skins].Sandune                ]                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| **[            ]**[// Create SortDescriptor object and specify the column name for initial sorting.][]                             |
|                                                                                                                                                                                                                                                              |
| **[            [SortDescriptor] sort = [new] [SortDescriptor]();]**[]                                           |
|                                                                                                                                                                                                                                                              |
| **[            sort.ColumnName = [\"CustomerID\"];]**[]                                                                                                      |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| **[         ]**[   [// Add the SortDescriptor to the grid using SortDescriptors property.]][]                              |
|                                                                                                                                                                                                                                                              |
| **[            gridModel.SortDescriptors.Add(sort);]**[]                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        }][]                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]To render the grid with initial sorting in a specific direction, use the **SortDescriptors** property.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [        [public] [ActionResult] Index()]                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [                Caption = [\"Orders\"],]                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [                AllowSorting=[true],]                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [                AllowMultiSorting=[true],]                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [                AutoFormat=[Skins].Sandune                ]                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            [// Create SortDescriptor object and specify the column name for initial sorting.]]                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [            [SortDescriptor] sort = [new] [SortDescriptor]();]                                                                                     |
|                                                                                                                                                                                                                                                              |
| [            sort.ColumnName = [\"CustomerID\"];]                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| [            [// Specify the sort direction using the SortDirection property.]]                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| **[            sort.SortDirection = System.ComponentModel.[ListSortDirection].Descending;]**[]                                                               |
|                                                                                                                                                                                                                                                              |
| [            [// Add the SortDescriptor to the grid using SortDescriptors property.]]                                                                                                              |
|                                                                                                                                                                                                                                                              |
| **[            gridModel.SortDescriptors.Add(sort);]**[]                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [            ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        }][]                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

