---
title: throughgridbuilder37.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridbuilder37.md
created_at: 2025-07-03
---








  









### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

 

Specify the route values using **QueryParam()** method as shown below:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\][]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])       ]                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [       .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       .EnablePaging()      ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [       .AutoFormat([Skins].Sandune)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                       |
| **[       .QueryParam([\"Category= 5\"])      ]**                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       .Column( columns =\> {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).Width(150);]                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]).Width(200);]                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);           ]                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);]                                                            |
|                                                                                                                                                                                                                                                       |
| [           })]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [       [%\>]]                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**[]                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])       ]                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [       .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       .EnablePaging()      ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [       .AutoFormat([Skins].Sandune)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                       |
| **[       .QueryParam([\"Category= 5\"])      ]**                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       .Column( columns =\> {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]).Width(150);]                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]).Width(200);]                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);           ]                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);]                                                            |
|                                                                                                                                                                                                                                                       |
| [           }).Render();]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       [}]]                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The value passed in a category is shared among all other grid actions like paging requests, sorting requests, grouping requests, group expand requests, and filtering requests.

[]{#related-topics}

