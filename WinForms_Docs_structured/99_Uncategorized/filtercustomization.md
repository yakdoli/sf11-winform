---
title: filtercustomization.md
original_path: WinForms_Docs/99_Uncategorized/filtercustomization.md
created_at: 2025-08-05
---






##### Filter Customization {#filter-customization style="tab-stops: 0pt"}

[] 

[·      ]If you want to enable or disable the filter based on some condition, use the **AllowFiltering(bool)** method:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [ [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                                                                   |
| **       .**Datasource(Model)\                                                                                                                                                                                                                               |
|        .Caption([\"Orders\"])\                                                                                                                                                                                                       |
|        .EnablePaging()\                                                                                                                                                                                                                                      |
|        .EnableSorting()\                                                                                                                                                                                                                                     |
| **       **.Filtering(filter =\>\                                                                                                                                                                                                                            |
|            {\                                                                                                                                                                                                                                                |
|                **filter.AllowFiltering([true]);\**                                                                                                                                                                                      |
|            })]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [       [%\>]]                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| **[ ]**[\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
| **       .**Datasource(Model)\                                                                                                                                                                                                                               |
|        .Caption([\"Orders\"])\                                                                                                                                                                                                       |
|        .EnablePaging()\                                                                                                                                                                                                                                      |
|        .EnableSorting()\                                                                                                                                                                                                                                     |
| **       **.Filtering(filter =\>\                                                                                                                                                                                                                            |
|            {\                                                                                                                                                                                                                                                |
|                **filter.AllowFiltering([true]);\**                                                                                                                                                                                      |
|            }).Render();]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [       [}]]                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]If you want to enable or disable the filter options for individual columns, use the **AllowFilter(bool)** method in column mapping.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [ [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                 |
| **       .**Datasource(Model)\                                                                                                                                                                             |
|        .Caption([\"Orders\"])\                                                                                                                                                     |
|        .EnablePaging()\                                                                                                                                                                                    |
|        .EnableSorting()\                                                                                                                                                                                   |
|        .EnableFiltering()\                                                                                                                                                                                 |
|        .AutoFormat([Skins].Sandune)      \                                                                                                                                         |
|        .Column( columns =\> {\                                                                                                                                                                             |
|        columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).**AllowFilter**([false]);\                                                                     |
|        columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                             |
|        columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                    columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\ |
|        columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                                                                               |
|            })\                                                                                                                                                                                             |
|        [%\>]]                                                                                                                              |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                  |
|                                                                                                                                                                                                            |
| [ [\@{][ ]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                 |
| **       .**Datasource(Model)\                                                                                                                                                                             |
|        .Caption([\"Orders\"])\                                                                                                                                                     |
|        .EnablePaging()\                                                                                                                                                                                    |
|        .EnableSorting()\                                                                                                                                                                                   |
|        .EnableFiltering()\                                                                                                                                                                                 |
|        .AutoFormat([Skins].Sandune)      \                                                                                                                                         |
|        .Column( columns =\> {\                                                                                                                                                                             |
|        columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).**AllowFilter**([false]);\                                                                     |
|        columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                             |
|        columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                    columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\ |
|        columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                                                                               |
|            }).Render();\                                                                                                                                                                                   |
|        [}]]                                                                                                                                |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]If you want to render the filter menu in a simple drop-down list, use the **FilterDropDownType()** method.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
| **       .**Datasource(Model)\                                                                                                                                                                                    |
|        .Caption([\"Orders\"])\                                                                                                                                                            |
|        .EnablePaging()\                                                                                                                                                                                           |
|        .EnableSorting()\                                                                                                                                                                                          |
|        .Filtering(filter =\>\                                                                                                                                                                                     |
|            {\                                                                                                                                                                                                     |
|                **filter.FilterDropDownType([FilterDropDownType].SimpleList);**\                                                                                                           |
|            })]                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| [       [%\>]]                                                                                                                                    |
|                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
| **       .**Datasource(Model)\                                                                                                                                                                                    |
|        .Caption([\"Orders\"])\                                                                                                                                                            |
|        .EnablePaging()\                                                                                                                                                                                           |
|        .EnableSorting()\                                                                                                                                                                                          |
|        .Filtering(filter =\>\                                                                                                                                                                                     |
|            {\                                                                                                                                                                                                     |
|                **filter.FilterDropDownType([FilterDropDownType].SimpleList);**\                                                                                                           |
|            }).Render();]                                                                                                                                                      |
|                                                                                                                                                                                                                   |
| [       [}]]                                                                                                                                      |
|                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

There are two ways to specify the initial filters information namely:

[·      ]Use the **Filtering()** method to add the initial filters.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                    |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                 |
|                                                                                                                                                                                                            |
| [ [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                 |
| **       .**Datasource(Model)\                                                                                                                                                                             |
|        .Caption([\"Orders\"])\                                                                                                                                                     |
|        .EnablePaging()\                                                                                                                                                                                    |
|        .EnableSorting()\                                                                                                                                                                                   |
| **       .Filtering(filter =\>\                                                                                                                                                                            |
|            {\                                                                                                                                                                                              |
|       filter.FilterDescriptors(descriptor =\>\                                                                                                                                                             |
|         {\                                                                                                                                                                                                 |
|         descriptor.Add(c =\> c.EmployeeID).FilterBy([FilterType].Equals).FilterValue(5);\                                                                                          |
|         });\                                                                                                                                                                                               |
|            })**]                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [       .AutoFormat([Skins].Sandune)      \                                                                                                                                        |
|        .Column( columns =\> {\                                                                                                                                                                             |
|        columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).AllowFilter([false]);\                                                                         |
|        columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                             |
|        columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                    columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\ |
|        columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                                                                               |
|            })\                                                                                                                                                                                             |
|        [%\>]]                                                                                                                              |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                  |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                 |
|                                                                                                                                                                                                            |
| [ [\@{][ ]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                 |
| **       .**Datasource(Model)\                                                                                                                                                                             |
|        .Caption([\"Orders\"])\                                                                                                                                                     |
|        .EnablePaging()\                                                                                                                                                                                    |
|        .EnableSorting()\                                                                                                                                                                                   |
| **       .Filtering(filter =\>\                                                                                                                                                                            |
|            {\                                                                                                                                                                                              |
|       filter.FilterDescriptors(descriptor =\>\                                                                                                                                                             |
|         {\                                                                                                                                                                                                 |
|         descriptor.Add(c =\> c.EmployeeID).FilterBy([FilterType].Equals).FilterValue(5);\                                                                                          |
|         });\                                                                                                                                                                                               |
|            })**]                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [       .AutoFormat([Skins].Sandune)      \                                                                                                                                        |
|        .Column( columns =\> {\                                                                                                                                                                             |
|        columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).AllowFilter([false]);\                                                                         |
|        columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                             |
|        columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                    columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\ |
|        columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                                                                               |
|            }).Render();\                                                                                                                                                                                   |
|        [}]]                                                                                                                                |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[·      ]Through **GridPropertiesModel**

a.  Create **GridPropertiesModel** in **Controller Index** action and add the initial filters using the **FilterDescriptors** property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [ [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>();\                                                    |
|  \                                                                                                                                                                                                                                                                |
|             [// Apply intial filters to the grid. ]\                                                                                                                                                                                        |
|   gridModel.Filters.FilterDescriptors.Add([new] [FilterDescriptor]() { ColumnName = [\"EmployeeID\"], Operator = Syncfusion.Linq.[FilterType].Equals, Value = 5 });\ |
|              ]                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

b.  Pass the **GridPropertiesModel** to the view using the **ViewData()** method. Use the grid's ID as the key in **ViewData**.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [ [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>();\                                                    |
|  \                                                                                                                                                                                                                                                                |
|             [// Apply intial filters to the grid. ]\                                                                                                                                                                                        |
|   gridModel.Filters.FilterDescriptors.Add([new] [FilterDescriptor]() { ColumnName = [\"EmployeeID\"], Operator = Syncfusion.Linq.[FilterType].Equals, Value = 5 });\ |
|  \                                                                                                                                                                                                                                                                |
|             [//Pass the GridPropertiesModel to grid using GridID. Here FilterGrid is the grid\'s ID.]\                                                                                                                                      |
| **            ViewData\[[\"FilterGrid\"]\] = gridModel;**]                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

