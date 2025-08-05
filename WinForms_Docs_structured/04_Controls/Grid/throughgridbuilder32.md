---
title: throughgridbuilder32.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder32.md
created_at: 2025-08-05
---






#### Through Grid Builder {#through-grid-builder style="tab-stops: 0pt"}

1.   Create a model in the application.

2.   Create a strongly typed view.

3.   Call the **EnableContextMenu** method to enable the context menu in the grid.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\] ]**                                                                                                                                                          |
|                                                                                                                                                                                                              |
| [ [\<%][=]Html.Syncfusion().Grid\<[EditableOrder]\>([\"Grid\"])]        |
|                                                                                                                                                                                                              |
| [                      .Datasource(Model)]                                                                                                                               |
|                                                                                                                                                                                                              |
| [                  .Column(column =\>]                                                                                                                                   |
|                                                                                                                                                                                                              |
| [                  {]                                                                                                                                                    |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                  |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                            |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                            |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                          |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:MM/dd/yyyy}\"]);] |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                                                   |
|                                                                                                                                                                                                              |
| [                  })]                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [                  \-\-\--]                                                                                                                                              |
|                                                                                                                                                                                                              |
| [                  .EnableContextMenu()  [// Enabling the context menu.]]                                                                          |
|                                                                                                                                                                                                              |
| [                                                        ]                                                                                                               |
|                                                                                                                                                                                                              |
| [\-\-\--]                                                                                                                                                                |
|                                                                                                                                                                                                              |
| [                    ]                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [         [%\>]]                                                                                                                             |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\] ]**                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [\@{]                                                                                                                                                |
|                                                                                                                                                                                                              |
| [Html.Syncfusion().Grid\<[EditableOrder]\>([\"Grid\"])]                                                                  |
|                                                                                                                                                                                                              |
| [                      .Datasource(Model)]                                                                                                                               |
|                                                                                                                                                                                                              |
| [                  .Column(column =\>]                                                                                                                                   |
|                                                                                                                                                                                                              |
| [                  {]                                                                                                                                                    |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                  |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                            |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                            |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                          |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:MM/dd/yyyy}\"]);] |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                                                   |
|                                                                                                                                                                                                              |
| [                  })]                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [                  \-\-\--]                                                                                                                                              |
|                                                                                                                                                                                                              |
| [                  .EnableContextMenu()  [// Enabling the context menu.]]                                                                          |
|                                                                                                                                                                                                              |
| [                                             ]                                                                                                                          |
|                                                                                                                                                                                                              |
| [\-\-\--]                                                                                                                                                                |
|                                                                                                                                                                                                              |
| [.Render()]                                                                                                                                                              |
|                                                                                                                                                                                                              |
| [                    ]                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [         [}]]                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Set the data source and render the view

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [///][ ][\<summary\>][]                |
|                                                                                                                                                                                                                                |
| [        [///][ Used for rendering the grid initially.]]                                                                                        |
|                                                                                                                                                                                                                                |
| [        [///][ ][\</summary\>]]                                                                                           |
|                                                                                                                                                                                                                                |
| [        [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]] |
|                                                                                                                                                                                                                                |
| [        [public] [ActionResult] Index()]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [            [IEnumerable] data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();]                          |
|                                                                                                                                                                                                                                |
| [            [return] View(data);]                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [       ]                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   In order to work with filter actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the following code.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller[]]**                                                                                                                            |
|                                                                                                                                                                                                        |
| []                                                                                                                                                    |
|                                                                                                                                                                                                        |
| [\<summary\>][]                                                                                                   |
|                                                                                                                                                                                                        |
| [        [///][ Paging/editing/filtering requests are mapped to this method. This method invokes the HtmlActionResult]] |
|                                                                                                                                                                                                        |
| [        [///][ from the grid and the required response is generated.]]                                                 |
|                                                                                                                                                                                                        |
| [        [///][ ][\</summary\>]]                                                                   |
|                                                                                                                                                                                                        |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                      |
|                                                                                                                                                                                                        |
| [        [public] [ActionResult] Index([PagingParams] args)]                                  |
|                                                                                                                                                                                                        |
| [        {]                                                                                                                                                        |
|                                                                                                                                                                                                        |
| [            [IEnumerable] data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();]  |
|                                                                                                                                                                                                        |
| [            [return] data.GridActions\<[Order]\>();]                                                                 |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [        }]                                                                                                                                                        |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Run the application. You can see the context menu as shown below in specified grid elements.

 

 

{border="0"}

Figure 249: Grid with Context Menu Items in the Header**[]**

 

 

 

{border="0"}

Figure 250: Grid with Context Menu Items in Pager**[]**

 

{border="0"}

Figure 251: Grid with Context Menu Items for Records**[]**

{border="0"}

Figure 252: Grid with Context Menu in Expanded Group**[]**

 

[]{#related-topics}

