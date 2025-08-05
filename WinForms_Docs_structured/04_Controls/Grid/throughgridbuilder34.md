---
title: throughgridbuilder34.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder34.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view create the Grid control and configure its properties.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);  ]                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                .EnablePaging()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                .EnableSorting()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                [%\>]]                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml[\]]]**                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                column.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);  ]                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                .EnablePaging()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                .EnableSorting()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                .Render();         ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| [      [}]]                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Specify the skin name using the **AutoFormat()** method.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [  .........]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [  .........]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| **[            .AutoFormat([Skins].Almond)]**                                                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| [         [%\>]]                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml[\]]]**                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [  .........]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [  .........]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| **[            .AutoFormat([Skins].Almond)]**                                                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| **[            ]**[.Render();]                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [         [}]]                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

5.   Run the application. The grid will appear as shown below.

{border="0"}

Figure 259: Grid with Almond Skin

**[]** 

[]{#related-topics}

