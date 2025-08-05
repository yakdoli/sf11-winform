---
title: groupingcustomization1.md
original_path: WinForms_Docs/99_Uncategorized/groupingcustomization1.md
created_at: 2025-08-05
---






##### Grouping Customization {#grouping-customization style="tab-stops: 0pt"}

 

[·      ]If you want to render the grid with initial grouping, use the **GroupDescriptors** property.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [///][ ][\<summary\>][]                                              |
|                                                                                                                                                                                                                                                              |
| [        [///][ Used for rendering the grid initially.]]                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\</summary\>]]                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\<returns\>][Veiw page; it displays the grid.][\</returns\>]]                               |
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
| [                AllowSorting = [true],]                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [                AllowMultiSorting = [true],]                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [                AllowGrouping = [true],]                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [                AutoFormat = [Skins].Sandune            ]                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [            ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            [// Add the grouped columns to the grid using GroupDescriptors.]]                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [            **gridModel.GroupDescriptors.Add([\"CustomerID\"]);**]                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#_Filtering} 

[]{#related-topics}

