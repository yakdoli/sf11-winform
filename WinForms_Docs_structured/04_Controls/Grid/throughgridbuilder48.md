---
title: throughgridbuilder48.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder48.md
created_at: 2025-08-05
---






##### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

1.   Create a model in the application.

2.   Create a strongly typed view[[.]]{.MsoHyperlink}

3.   Call the **AllowVirtualScrolling** method to enable/disable virtual scrolling in the grid.

4.   Call the **VirtualScroll** method to set the virtual scrolling mode to the normal or Facebook modes.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\] ]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [ [\<%][=]Html.Syncfusion().Grid\<[EditableOrder]\>([\"Grid\"])]                                              |
|                                                                                                                                                                                                                                                    |
| [                      .Datasource(Model)]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [                  .Column(column =\>]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [                  {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [                      column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [                      column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [                      column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [                      column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                |
|                                                                                                                                                                                                                                                    |
| [                      column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:MM/dd/yyyy}\"]);]                                       |
|                                                                                                                                                                                                                                                    |
| [                      column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [                  })]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [                  \-\-\--]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [.Scrolling(scroll=\>{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [                      **scroll.AllowVirtualScrolling([true])**]                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| **[                            .VirtualScrollMode([VirtualScrollMode].Facebook);]**[ [// Configuring virtual scroll modes.]] |
|                                                                                                                                                                                                                                                    |
| [                  })                                                        ]                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [\-\-\--]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [                    ]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [         [%\>]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**[]                                                                                                                    |
|                                                                                                                                                                                                              |
| []                                                                                                                                                   |
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
| [                      column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:MM/dd/yyyy}\"]);] |
|                                                                                                                                                                                                              |
| [                      column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                                                   |
|                                                                                                                                                                                                              |
| [                  })]                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [                  \-\-\--]                                                                                                                                              |
|                                                                                                                                                                                                              |
| [                .Scrolling(scroll=\>{]                                                                                                                                  |
|                                                                                                                                                                                                              |
| [                      scroll.AllowVirtualScrolling([true])]                                                                                        |
|                                                                                                                                                                                                              |
| [                            .VirtualScrollMode([VirtualScrollMode].Facebook); [// Configuring virtual scroll modes.]]     |
|                                                                                                                                                                                                              |
| [                  })                                                        ]                                                                                           |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
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

 

5.   Set the data source and render the view.

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

 

6.   In order to work with filter actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the following code.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller     []]**                                                                                                                       |
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

 

7.   Run the application. You can see the grid with the initial records loaded and on scrolling the required data is loaded.

 

{border="0"}

Figure 227: Initial Items Loaded in the Facebook Mode

[]{#related-topics}

