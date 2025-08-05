---
title: filtercustomization3.md
original_path: WinForms_Docs/99_Uncategorized/filtercustomization3.md
created_at: 2025-08-05
---






##### Filter Customization {#filter-customization style="tab-stops: 0pt"}

 

[·      ]To enable or disable the filtering options for individual columns, use the **AllowFilter(bool)** method in column mapping.[]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"FilteringGrid\"],[\"GridModel\"], columns =\> {\ |
|             columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).AllowFilter([false]);\                                                                                                                                         |
|             columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                                                                                             |
|             columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);\                                                                                                                                                                             |
|             columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\                                                                                                                                                                           |
|             columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);\                                                                                                                          |
|      })[%\>]][]                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

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

[·      ]To render the filter menu in a simple drop-down list, use the **FilterDropDownType** property.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                 |
|                                                                                                                                                                                                                    |
| [      // Create the GridPropertiesModel.][\                                                                                                                          |
|       [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>();\ |
|           \                                                                                                                                                                                                        |
|       [// Specify the drop-down type.]]                                                                                                                       |
|                                                                                                                                                                                                                    |
| [       gridModel.Filters.FilterDropDownType = [FilterDropDownType].SimpleList;]                                                                            |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]To render the grid with the initial filtering, add filter conditions using the **FilterDescriptors** property.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                 |
|                                                                                                                                                                                                                    |
| [      ][// Create the GridPropertiesModel.][\                                                          |
|       [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>();\ |
|           \                                                                                                                                                                                                        |
|       [// Specify the drop-down type.]\                                                                                                                                                      |
|       gridModel.Filters.FilterDropDownType = [FilterDropDownType].SimpleList;][]                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]To render the grid with initial filtering, add the filter conditions using the **FilterDescriptors** property.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| [ public][ [ActionResult] Filtering1()\                                                                                                                                                                    |
|  {\                                                                                                                                                                                                                                                                                 |
|      [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()\                                                                    |
|      {]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                     |
| **[        ]**[ActionMode = ActionMode.JSON,][\                                                                                                                                                             |
|         Caption = [\"Orders\"],\                                                                                                                                                                                                                            |
|         AllowFiltering = [true],\                                                                                                                                                                                                                              |
|         AutoFormat = [Skins].Sandune\                                                                                                                                                                                                                       |
|       };][]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [      [// Apply intial filters to the grid. ]\                                                                                                                                                                                                               |
|      **gridModel.Filters.FilterDescriptors.Add([new] [FilterDescriptor]() { ColumnName = [\"EmployeeID\"], Operator = Syncfusion.Linq.[FilterType].Equals, Value = 5 });**           \ |
|  \                                                                                                                                                                                                                                                                                  |
|         ViewData\[[\"GridModel\"]\] = gridModel;\                                                                                                                                                                                                           |
|         [return] View();\                                                                                                                                                                                                                                      |
|   }][]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Tables for properties, methods, and events

Properties

*[]* 


+--------------------------------------+-----------------------------------------------+-----------------+--------------------------------------+
| Property                             | Description                                   | Type            | Data type                            |
+--------------------------------------+-----------------------------------------------+-----------------+--------------------------------------+
| ActionMode[] | Gets or sets the **ActionMode** for the grid. | Server-side     | ActionMode[] |
|                                      |                                               |                 |                                      |
|                                      | \                                             |                 |                                      |
|                                      | **Possible Values:**                          |                 |                                      |
|                                      |                                               |                 |                                      |
|                                      | ActionMode.JSON                               |                 |                                      |
|                                      |                                               |                 |                                      |
|                                      | ActionMode.Server                             |                 |                                      |
|                                      |                                               |                 |                                      |
|                                      |                                               |                 |                                      |
|                                      |                                               |                 |                                      |
|                                      | **Default value:**                            |                 |                                      |
|                                      |                                               |                 |                                      |
|                                      | ActionMode.Server                             |                 |                                      |
+--------------------------------------+-----------------------------------------------+-----------------+--------------------------------------+


*[]* 

Methods

*[]* 


+-------------+-----------------------------------+----------------------+-------------+-------------+
| Method      | Description                       | Parameters           | Type        | Return type |
+-------------+-----------------------------------+----------------------+-------------+-------------+
| ActionMode  | Gets the ActionMode for the Grid. | (ActionMode mode)    | Server-side | Void        |
|             |                                   |                      |             |             |
|             |                                   | **Possible Values:** |             |             |
|             |                                   |                      |             |             |
|             |                                   | ActionMode.JSON      |             |             |
|             |                                   |                      |             |             |
|             |                                   | ActionMode.Server    |             |             |
|             |                                   |                      |             |             |
|             |                                   |                      |             |             |
|             |                                   |                      |             |             |
|             |                                   | **Default value:**   |             |             |
|             |                                   |                      |             |             |
|             |                                   | ActionMode.Server    |             |             |
+=============+===================================+======================+=============+=============+


[]{#related-topics}

