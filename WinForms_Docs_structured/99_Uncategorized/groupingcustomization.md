---
title: groupingcustomization.md
original_path: WinForms_Docs/99_Uncategorized/groupingcustomization.md
created_at: 2025-08-05
---






##### Grouping Customization {#grouping-customization style="tab-stops: 0pt"}

[·      ]If you want to enable or disable the grouping based on some condition, use the **AllowGrouping(bool)** method.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])       ]                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [       .EnablePaging()]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [            .EnableSorting()]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [              .Grouping( group =\> **group.AllowGrouping([true])**)    ]                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [       [%\>]]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| [1. If you want to render the grid with the initial grouping, use **GroupDescriptors()** method.]                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [       .EnablePaging()]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [       .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       **.Grouping(group =\>**]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| **[       {]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| **[           group.GroupDescriptors(cols =\> cols.Add(c =\> c.CustomerID));]**                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| **[       })]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [       ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [%\>]                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])       ]                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [       .EnablePaging()]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [            .EnableSorting()]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [              .Grouping( group =\> **group.AllowGrouping([true])**)    ]                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [       [}]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [2. If you want to render the grid with the initial grouping, use **GroupDescriptors()** method.]                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [\@{][ Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])]                                                    |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [       .EnablePaging()]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [       .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       **.Grouping(group =\>**]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| **[       {]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| **[           group.GroupDescriptors(cols =\> cols.Add(c =\> c.CustomerID));]**                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| **[       }).]**[Render();]                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [       ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

