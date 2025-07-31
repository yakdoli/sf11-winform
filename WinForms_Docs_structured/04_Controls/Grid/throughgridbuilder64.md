---
title: throughgridbuilder64.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridbuilder64.md
created_at: 2025-07-03
---






#### Through Grid Builder {#through-grid-builder style="tab-stops: 0pt"}

 

To enable the drag any other element and drop it into grid rows feature you need to perform the following:

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view you can use its **Model** property in **DataSource** to bind the data source.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().Grid\<[ShoppingCart]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                                                                     |
| [                    .Datasource(([IEnumerable]\<[ShoppingCart]\>)ViewData\[[\"CartGrid\"]\])]                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [                    .Caption([\"Shopping Cart\"])]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                     |
| [                    .Column(column =\>]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| [                         {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                     |
| [                             column.Add(p =\> p.ProductID).HeaderText([\"Product ID\"]);]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [                             column.Add(p =\> p.Count).HeaderText([\"Count\"]);]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [                             column.Add(p =\> p.Price).HeaderText([\"Price\"]).Format([\"\${Price:0.00}\"]);]                                                                                     |
|                                                                                                                                                                                                                                                                                                     |
| [                             ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                     |
| [                     })]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [                    .Droppable([true])]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| [                    .ElementtoDrag([\".ItemsDraggable\"])  ]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [                    .AutoFormat([Skins].Marble)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [                    .EnableHighlighting([true])]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [                    .EnableSelectionOnDragging([true])]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| [                    .ClientSideEvents(events=\>{]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [                                events.OnGridRowsDropEvent([\"DroppedTarget\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                     |
| [                    })]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| [                    ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [                          [%\>]]                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[        ]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [\@{][ ][Html.Syncfusion().Grid\<[ShoppingCart]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                                                                     |
| [                    .Datasource(([IEnumerable]\<[ShoppingCart]\>)ViewData\[[\"CartGrid\"]\])]                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [                    .Caption([\"Shopping Cart\"])]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                     |
| [                    .Column(column =\>]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                     |
| [                         {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                     |
| [                             column.Add(p =\> p.ProductID).HeaderText([\"Product ID\"]);]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [                             column.Add(p =\> p.Count).HeaderText([\"Count\"]);]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [                             column.Add(p =\> p.Price).HeaderText([\"Price\"]).Format([\"\${Price:0.00}\"]);]                                                                                     |
|                                                                                                                                                                                                                                                                                                     |
| [                             ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                     |
| [                     })]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [                    .Droppable([true])]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| [                    .ElementtoDrag([\".ItemsDraggable\"])  ]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [                    .AutoFormat([Skins].Marble)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [                    .EnableHighlighting([true])]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [                    .EnableSelectionOnDragging([true])]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| [                    .ClientSideEvents(events=\>{]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [                                events.OnGridRowsDropEvent([\"DroppedTarget\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                     |
| [                    }).Render();]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                     |
| [                    ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [                          [}]]                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[        ]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                             |
| [///][ ][\<summary\>][]         |
|                                                                                                                                                                                                                                                                             |
| [        [///][ Used for rendering the grid initially.]]                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [        [///][ ][\</summary\>]]                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [        [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>][        ]] |
|                                                                                                                                                                                                                                                                             |
| [        [public] [ActionResult] Index()]                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                             |
| [            ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| [            ViewData\[[\"CartGrid\"]\] = [ShoppingCartOrders].CartOrders.Where(p =\> p.Count \> 0).ToList();]                                                             |
|                                                                                                                                                                                                                                                                             |
| [            [return] View();]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

