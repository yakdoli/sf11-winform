---
title: filtercustomization1.md
original_path: WinForms_Docs/99_Uncategorized/filtercustomization1.md
created_at: 2025-08-05
---






##### Filter Customization {#filter-customization style="tab-stops: 0pt"}

[·      ]If you want to enable or disable the filtering options for individual columns, then use the **AllowFilter(bool)** method in column mapping.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"FilteringGrid\"],[\"GridModel\"], columns =\> {\ |
|             columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).AllowFilter([false]);\                                                                                                                                         |
|             columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                                                                                             |
|             columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);\                                                                                                                                                                             |
|             columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\                                                                                                                                                                           |
|             columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);\                                                                                                                          |
|      })[%\>]][]                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [   ]                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Order]\>([\"FilteringGrid\"],[\"GridModel\"],] |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [ columns =\> {\                                                                                                                                                                                                                                                                                                                                                                                                          |
|             columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).AllowFilter([false]);\                                                                                                                                                                                                                                                                                   |
|             columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                                                                                                                                                                                                                                       |
|             columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);\                                                                                                                                                                                                                                                                                                                       |
|             columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\                                                                                                                                                                                                                                                                                                                     |
|             columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);\                                                                                                                                                                                                                                                                    |
|      })][.ToString())[)]    ][    ][]                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[·      ]If you want to render the filter menu in a simple drop-down list, then use the **FilterDropDownType** property.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                    |
| [      // Create GridPropertiesModel.][\                                                                                                                         |
|       [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>();\ |
|           \                                                                                                                                                                                                        |
|       [// Specify the drop-down type.]\                                                                                                                                                      |
|       gridModel.Filters.FilterDropDownType = [FilterDropDownType].SimpleList;]                                                                         |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]If you want to render the grid with initial filtering, add the filter conditions using the **FilterDescriptors** property.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                    |
| [      // Create GridPropertiesModel.][\                                                                                                                         |
|       [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>();\ |
|           \                                                                                                                                                                                                        |
|       [// Specify the drop-down type.]\                                                                                                                                                      |
|       gridModel.Filters.FilterDropDownType = [FilterDropDownType].SimpleList;]                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]If you want to render the grid with initial filtering, add the filter conditions using the **FilterDescriptors** property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                     |
| [ public][ [ActionResult] Filtering1()\                                                                                                                                                                    |
|  {\                                                                                                                                                                                                                                                                                 |
|      [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()\                                                                    |
|      {\                                                                                                                                                                                                                                                                             |
|         DataSource = [new] [NorthwindDataContext]().Orders,\                                                                                                                                                                           |
|         Caption = [\"Orders\"],\                                                                                                                                                                                                                            |
|         AllowPaging = [true],\                                                                                                                                                                                                                                 |
|         AllowSorting = [true],\                                                                                                                                                                                                                                |
|         AllowFiltering = [true],\                                                                                                                                                                                                                              |
|         AutoFormat = [Skins].Sandune\                                                                                                                                                                                                                       |
|       };]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                     |
| [      [// Apply intial filters to the grid. ]\                                                                                                                                                                                                               |
|      **gridModel.Filters.FilterDescriptors.Add([new] [FilterDescriptor]() { ColumnName = [\"EmployeeID\"], Operator = Syncfusion.Linq.[FilterType].Equals, Value = 5 });**           \ |
|  \                                                                                                                                                                                                                                                                                  |
|         ViewData\[[\"GridModel\"]\] = gridModel;\                                                                                                                                                                                                           |
|         [return] View();\                                                                                                                                                                                                                                      |
|   }]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

