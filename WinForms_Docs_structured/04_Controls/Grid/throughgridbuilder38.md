---
title: throughgridbuilder38.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder38.md
created_at: 2025-08-05
---






#### Through Grid Builder {#through-grid-builder style="tab-stops: 0pt"}

1.   Create a model in the application (Refer to [Getting Started\>Adding a Model to the Application]{.UGHyperlink}).

2.   Create a strongly typed view (Refer to [How to\>Strongly Typed View]{.UGHyperlink}).

3.   In the view you can use its **Model** property in **Datasource()** in order to bind the data source.

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                      |
| [\<%][=][Html.Syncfusion().Grid\<MvcSampleApplication.Models.[Order]\>([\"FlatGrid\"])] |
|                                                                                                                                                                                                                                                                                      |
| **[        .Datasource(Model)        ]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                      |
| [        .EnablePaging()]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                      |
| [        .EnableSorting()]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                      |
| [        .ActionMode([\"Server\"])]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [        .Column( column =\> {]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| [            column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                      |
| [            column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [            column.Add(c =\> c.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [            column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/mm/yyyy}\"]);]                                                                                   |
|                                                                                                                                                                                                                                                                                      |
| [            column.Add(c =\> c.Freight).HeaderText([\"Freight\"]);            ]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                      |
| [            })]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                      |
| [        [%\>]]                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                                                  |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [\@{][ Html.Syncfusion().Grid\<MvcSampleApplication.Models.[Order]\>([\"Flat Grid\"])] |
|                                                                                                                                                                                                                                    |
| **[        .Datasource(Model)        ]**                                                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [        .EnablePaging()]                                                                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [        .EnableSorting()]                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [        .ActionMode([\"Server\"])]                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        .Column( column =\> {]                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                  |
|                                                                                                                                                                                                                                    |
| [            column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                            |
|                                                                                                                                                                                                                                    |
| [            column.Add(c =\> c.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                            |
|                                                                                                                                                                                                                                    |
| [            column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/mm/yyyy}\"]);]                                 |
|                                                                                                                                                                                                                                    |
| [            column.Add(c =\> c.Freight).HeaderText([\"Freight\"]);            ]                                                                                       |
|                                                                                                                                                                                                                                    |
| [            }).Render();]                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [ [}]]                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Set its data source and render the view

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                               |
| [///][ ][\<summary\>][]               |
|                                                                                                                                                                                                                               |
| [        [///][ Used to bind the Grid.]]                                                                                                       |
|                                                                                                                                                                                                                               |
| [        [///][ ][\</summary\>]]                                                                                          |
|                                                                                                                                                                                                                               |
| [        [///][ ][\<returns\>][View page, it displays the Grid][\</returns\>]] |
|                                                                                                                                                                                                                               |
| [        [public] [ActionResult] Index()]                                                                                                    |
|                                                                                                                                                                                                                               |
| [        {  ]                                                                                                                                                                             |
|                                                                                                                                                                                                                               |
| [            [var] data = [new] [NorthwindDataContext]().Orders.Take(200);]                                             |
|                                                                                                                                                                                                                               |
| [            [return] View(data);]                                                                                                                                   |
|                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In order to work with paging and sorting actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the following code.

***[]*** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                               |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [  ///][ ][\<summary\>][]                    |
|                                                                                                                                                                                                                                      |
| [        [///][ Paging/sorting Requests are mapped to this method. This method invokes the HtmlActionResult]]                                         |
|                                                                                                                                                                                                                                      |
| [        [///][ from the grid. Required response is generated.]]                                                                                      |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</summary\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties. ][\</param\>]] |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<returns\>]]                                                                                                  |
|                                                                                                                                                                                                                                      |
| [        [///][ HtmlActionResult returns the data displayed on the grid.]]                                                                            |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                    |
|                                                                                                                                                                                                                                      |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                                |
|                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [            [IEnumerable] data = [new] [NorthwindDataContext]().Orders.Take(200);]                                         |
|                                                                                                                                                                                                                                      |
| [            [return] data.GridActions\<[Order]\>();]                                                                                               |
|                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 83: Grid with Data

[]{#related-topics}

