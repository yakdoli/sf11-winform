---
title: throughgridbuilder12.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder12.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

To add a filter to the application using GridBuilder:

1.   Create a model in the application (Refer to [Getting Started\>Adding a Model to the Application]{.UGHyperlink}).

2.   Create a strongly typed view (Refer to [How to\>Strongly Typed View]{.UGHyperlink}).

3.   In the view you can use the **Model** property in **Datasource()** to bind the data source.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                    |
|                                                                                                                                                            |
| [ [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
| **       .Datasource(Model)**\                                                                                                                             |
|        .Caption([\"Orders\"])\                                                                                                     |
|        .EnablePaging()\                                                                                                                                    |
|        .EnableSorting()\                                                                                                                                   |
|        .EnableFiltering()\                                                                                                                                 |
|        .AutoFormat([Skins].Sandune)      \                                                                                         |
|        .Column( columns =\> {\                                                                                                                             |
|            columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);\                                                               |
|            columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                         |
|            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);         \                                                |
|            columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\                                                       |
|            columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                           |
|            })\                                                                                                                                             |
|        [%\>]]                                                                              |
|                                                                                                                                                            |
|                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                      |
|                                                                                                                                                            |
| [ [\@{][ ]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
| **       .Datasource(Model)**\                                                                                                                             |
|        .Caption([\"Orders\"])\                                                                                                     |
|        .EnablePaging()\                                                                                                                                    |
|        .EnableSorting()\                                                                                                                                   |
|        .EnableFiltering()\                                                                                                                                 |
|        .AutoFormat([Skins].Sandune)      \                                                                                         |
|        .Column( columns =\> {\                                                                                                                             |
|            columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);\                                                               |
|            columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                         |
|            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);         \                                                |
|            columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\                                                       |
|            columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                           |
|            }).Render();\                                                                                                                                   |
|        [}]]                                                                                |
|                                                                                                                                                            |
|                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

 

4.   To enable the filtering feature for your grid, you should use the **EnableFiltering()** method.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [ [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                     |
| **       .**Datasource(Model)\                                                                                                                                                                                 |
|        .Caption([\"Orders\"])\                                                                                                                                                         |
|        .EnablePaging()\                                                                                                                                                                                        |
|        .EnableSorting()\                                                                                                                                                                                       |
| **       .EnableFiltering()**\                                                                                                                                                                                 |
|        .AutoFormat([Skins].Sandune)      \                                                                                                                                             |
|        .Column( columns =\> {\                                                                                                                                                                                 |
|            columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);\                                                                                                                   |
|            columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                             |
|            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                    columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\ |
|            columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                                                                               |
|            })\                                                                                                                                                                                                 |
|        [%\>]]                                                                                                                                  |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                |
| [ [\@{][ ]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\                                                     |
| **       .**Datasource(Model)\                                                                                                                                                                                 |
|        .Caption([\"Orders\"])\                                                                                                                                                         |
|        .EnablePaging()\                                                                                                                                                                                        |
|        .EnableSorting()\                                                                                                                                                                                       |
| **       .EnableFiltering()**\                                                                                                                                                                                 |
|        .AutoFormat([Skins].Sandune)      \                                                                                                                                             |
|        .Column( columns =\> {\                                                                                                                                                                                 |
|            columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);\                                                                                                                   |
|            columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);\                                                                                                             |
|            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                    columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);\ |
|            columns.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);\                                                                                                               |
|            }).Render();\                                                                                                                                                                                       |
|        [}]]                                                                                                                                    |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Set its data source and render the view.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [ ][       ][///][ ][\<summary\>][\ |
|         [///][ Used for rendering the grid initially.]\                                                                                                                                                         |
|         [///][ ][\</summary\>]\                                                                                                                                                            |
|         [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]\                                                                  |
|         [public] [ActionResult] Index()\                                                                                                                                                                      |
|         {\                                                                                                                                                                                                                                                 |
|             [var] data = [new] [NorthwindDataContext]().Orders;\                                                                                                                         |
|             [return] View(data);\                                                                                                                                                                                                     |
|         }]                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   In order to work with filter actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the following code.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                |
| [ ][      ][ [///][ ][\<summary\>]\                         |
|         [///][ Paging/sorting/filtering requests are mapped to this method. This method invokes the HtmlActionResult]\                              |
|         [///][ from the grid. The required response is generated.]\                                                                                 |
|         [///][ ][\</summary\>]\                                                                                                |
|         [///][ ][\<param name=\"args\"\>][Contains paging properties.][\</param\>]\ |
|         [///][ ][\<returns\>]\                                                                                                 |
|         [///][ HtmlActionResult returns the data displayed on the grid.]\                                                                           |
|         [///][ ][\</returns\>]\                                                                                                |
|         \[[AcceptVerbs]([HttpVerbs].Post)\]\                                                                                                   |
|         [public] [ActionResult] Index([PagingParams] args)\                                                               |
|         {\                                                                                                                                                                                     |
|             [IEnumerable] data = [new] [NorthwindDataContext]().Orders;\                                                  |
|             [return] data.GridActions\<[Order]\>();\                                                                                              |
|         }]                                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

7.   Run the application. The grid will appear as shown in the following screenshot.

 

{border="0"}

Figure 121: Grid with Filter Option

More:





