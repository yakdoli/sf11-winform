---
title: throughgridbuilder47.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder47.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

1.   Create a model in to application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view you can use its **Model** property in **Datasource()** to bind the data source.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [       .PageSettings(page =\> page.PageSize(20))]                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [       .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       .AutoFormat([Skins].Sandune)      ]                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [       .Column( columns =\> {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);           ]                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);]                                                            |
|                                                                                                                                                                                                                                                       |
| [           })]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [       [%\>]]                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [       .PageSettings(page =\> page.PageSize(20))]                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [       .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       .AutoFormat([Skins].Sandune)      ]                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [       .Column( columns =\> {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                               |
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

[] 

4.   Specify the column width using the **Width()** method in **IGridColumnBuilder\<T\>**.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\][]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [       .PageSettings(page =\> page.PageSize(20))]                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [       .EnableSorting()       ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [       .AutoFormat([Skins].Sandune)      ]                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [       .Column( columns =\> {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"])**.Width(150)**;]                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"])**.Width(200)**;]                                                                                                |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);           ]                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dd-MM-yyyy}\"]);]                                                            |
|                                                                                                                                                                                                                                                       |
| [           })]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [       [%\>]]                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\][]]**                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [       .PageSettings(page =\> page.PageSize(20))]                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [       .EnableSorting()       ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [       .AutoFormat([Skins].Sandune)      ]                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [       .Column( columns =\> {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"])**.Width(150)**;]                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"])**.Width(200)**;]                                                                                                |
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

[] 

[] 

5.   Enable the scrolling feature by the **AllowScrolling()** method. Specify the grid width and height by using **Width()** and **Height()**.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\][]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [       .PageSettings(page =\> page.PageSize(20))]                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [       .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       **.Scrolling( scroll =\> {**]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                       |
| **[           scroll.AllowScrolling([true]);]**                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| **[           scroll.Height(400);]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| **[           scroll.Width(900);]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| **[       })]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [       .AutoFormat([Skins].Sandune)      ]                                                                                                                                               |
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
| [           })]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [       [%\>]]                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\][]]**                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [       .Caption([\"Orders\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [       .PageSettings(page =\> page.PageSize(20))]                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [       .EnableSorting()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       **.Scrolling( scroll =\> {**]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                       |
| **[           scroll.AllowScrolling([true]);]**                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| **[           scroll.Height(400);]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| **[           scroll.Width(900);]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| **[       })]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [       .AutoFormat([Skins].Sandune)      ]                                                                                                                                               |
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
| [           }).Render();]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [       [}]]                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 219: Grid with Scroll Bar

 

[]{#related-topics}

