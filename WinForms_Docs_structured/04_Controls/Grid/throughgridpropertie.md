---
title: throughgridpropertie.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridpropertie.md
created_at: 2025-07-03
---






#### Through GridPropertiesModel: {#through-gridpropertiesmodel style="tab-stops: 0pt"}

1.   Create a model in to application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **HomeController.cs** file to create the Grid control in the view.[ ]

[       ]

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                         |
| [///][ ][\<summary\>][]                     |
|                                                                                                                                                                                                                                                                                         |
| [        [///][ Used for rendering the grid initially.]]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [        [///][ ][\</summary\>]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                         |
| [        [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]]                                             |
|                                                                                                                                                                                                                                                                                         |
| [        [public] [ActionResult] OrderGrid()]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [            [GridPropertiesModel]\<[ShoppingCart]\> gridModel = [new] [GridPropertiesModel]\<[ShoppingCart]\>()] |
|                                                                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                         |
| [                DataSource = [ShoppingCartOrders].CartOrders.Where(p =\> p.Count \> 0).ToList(),]                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| [                AutoFormat = [Skins].Marble,]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [                AllowDragAndDrop = [false],]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                         |
| [                Caption = [\"Shopping Cart\"],]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [                Droppable = [true],]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| [                EnableHighlighting = [false],]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [                EnableSelectionOnDragging = [false],]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                         |
| [                OnGridRowsDropEvent = [\"DroppedTarget\"],]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [                ElementtoDrag = [\".ItemsDraggable\"]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                         |
| [            };]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                         |
| [            ]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                         |
| [            ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                         |
| [            [return] View();]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| [        ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().Grid\<[ShoppingCart]\>(] |
|                                                                                                                                                                                                                                                                 |
| [             [\"Grid1\"], [\"GridModel\"],column =\>]                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [                         {]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                 |
| [                             column.Add(p =\> p.ProductID).HeaderText([\"Product ID\"]);]                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [                             column.Add(p =\> p.Count).HeaderText([\"Count\"]);]                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [                             column.Add(p =\> p.Price).HeaderText([\"Price\"]).Format([\"\${Price:0.00}\"]);]                                                 |
|                                                                                                                                                                                                                                                                 |
| [                             ]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                 |
| [                         })]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [                          [%]]                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| [ ][@(][new][ [HtmlString](Html.Syncfusion().Grid\<[ShoppingCart]\>(] |
|                                                                                                                                                                                                                                                                                                                                               |
| [             [\"Grid1\"], [\"GridModel\"],column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [                         {]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [                             column.Add(p =\> p.ProductID).HeaderText([\"Product ID\"]);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [                             column.Add(p =\> p.Count).HeaderText([\"Count\"]);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                               |
| [                             column.Add(p =\> p.Price).HeaderText([\"Price\"]).Format([\"\${Price:0.00}\"]);]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| [                             ]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                               |
| [                         })]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| [.][ToString())[)] ][]                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

[] 

The following screenshot shows that any element within the **ElementtoDrag Selector** can be dragged. Here the items are set as draggable elements.

 

{border="0"}

Figure 240: Element Dragged to Drag Selector

 

The following screenshot shows the dropped grid that is updated using the event.

 

{border="0"}

Figure 241: Grid Updated Using the Event

 

 

[]{#related-topics}

