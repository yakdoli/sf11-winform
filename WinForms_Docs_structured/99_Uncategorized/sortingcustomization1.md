---
title: sortingcustomization1.md
original_path: WinForms_Docs/99_Uncategorized/sortingcustomization1.md
created_at: 2025-08-05
---






##### Sorting Customization[] {#sorting-customization style="tab-stops: 0pt"}

 

[·      ]If you want to enable or disable the multi-sort feature, use the **AllowMultiSorting** property.[  ]

[  ]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [GridPropertiesModel][\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [                DataSource = [new] [NorthwindDataContext]().Orders,]                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [                Caption = [\"Orders\"],]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| [                AllowPaging = [true],]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| [                AllowSorting=[true],]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| **[                AllowMultiSorting=[true],]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [                AutoFormat=[Skins].Sandune                ]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]If you want to render the grid with initial sorting use the **SortDescriptors** property.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [///][ ][\<summary\>][]                                              |
|                                                                                                                                                                                                                                                              |
| [        [///][ Used for rendering the grid initially.]]                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\</summary\>]]                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\<returns\>][Veiw page, it displays the grid.][\</returns\>]]                               |
|                                                                                                                                                                                                                                                              |
| [        [public] [ActionResult] Index()]                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [                DataSource = [new] [NorthwindDataContext]().Orders,]                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [                Caption = [\"Orders\"],]                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [                AllowPaging = [true],]                                                                                                                                                             |
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
| **[            [SortDescriptor] sort = [new] [SortDescriptor]();]**                                                                                 |
|                                                                                                                                                                                                                                                              |
| **[            sort.ColumnName = [\"CustomerID\"];]**                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| **[            ]**[// Add the SortDescriptor to the grid using SortDescriptors property.][]                                        |
|                                                                                                                                                                                                                                                              |
| **[            gridModel.SortDescriptors.Add(sort);]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [            ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]If you want to render the grid with initial sorting with direction use the **SortDescriptors** property.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [///][ ][\<summary\>][]                                              |
|                                                                                                                                                                                                                                                              |
| [        [///][ Used for rendering the grid initially.]]                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\</summary\>]]                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\<returns\>][Veiw page, it displays the grid.][\</returns\>]]                               |
|                                                                                                                                                                                                                                                              |
| [        [public] [ActionResult] Index()]                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [                DataSource = [new] [NorthwindDataContext]().Orders,]                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [                Caption = [\"Orders\"],]                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [                AllowPaging = [true],]                                                                                                                                                             |
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
| [            [// Create SortDescriptor object and specify the column name for initial sorting.]]                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [            [SortDescriptor] sort = [new] [SortDescriptor]();]                                                                                     |
|                                                                                                                                                                                                                                                              |
| [            sort.ColumnName = [\"CustomerID\"];]                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| [            [// Specify the sort direction using the SortDirection property.]]                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| **[            sort.SortDirection = System.ComponentModel.[ListSortDirection].Descending;]**                                                                                                     |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [            [// Add the SortDescriptor to the grid using the SortDescriptors property.]]                                                                                                          |
|                                                                                                                                                                                                                                                              |
| **[            gridModel.SortDescriptors.Add(sort);]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [            ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

