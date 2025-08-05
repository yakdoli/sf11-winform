---
title: throughgridbuilder50.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder50.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

 

To enable the row drag-and-drop feature you need to perform the following.

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view you can use its **Model** property in **Datasource()** to bind the data source.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"GridSrc\"])] |
|                                                                                                                                                                                                                                                         |
| [                         .Datasource(([IEnumerable]\<[Order]\>)ViewData\[[\"data\"]\])]                                                    |
|                                                                                                                                                                                                                                                         |
| [                         .Caption([\"First Grid Order\"])                         ]                                                                                                        |
|                                                                                                                                                                                                                                                         |
| [                         .Column(column =\>]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                         |
| [                         {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                         |
| [                             column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                      |
|                                                                                                                                                                                                                                                         |
| [                             column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                |
|                                                                                                                                                                                                                                                         |
| [                             column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                |
|                                                                                                                                                                                                                                                         |
| [                             ]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [                         })]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                         |
| [                        .AllowRowsDragging([true])]                                                                                                                                           |
|                                                                                                                                                                                                                                                         |
| [                        .AllowDragAndDrop([false])                                ]                                                                                                           |
|                                                                                                                                                                                                                                                         |
| [                        .TargetHtmlElementId([\"#GridDest\"])        ]                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [                        .RowsDraggingMode([DragandDropMode].GhostRows)]                                                                                                                    |
|                                                                                                                                                                                                                                                         |
| [                        .AutoFormat([Skins].Midnight)]                                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [                        .RowsDroppingMapper([\"Dragged\"])                        ]                                                                                                        |
|                                                                                                                                                                                                                                                         |
| [                        .ClientSideEvents(events =\> {]                                                                                                                                                            |
|                                                                                                                                                                                                                                                         |
| [                            events.OnRowDropping([\"OnDropping\"]);]                                                                                                                       |
|                                                                                                                                                                                                                                                         |
| [                            events.OnRowDropped([\"DroppedTarget\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [                        })]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                         |
| [                          [%\>]][]                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                         |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"GridSrc\"])] |
|                                                                                                                                                                                                                                                         |
| [                         .Datasource(([IEnumerable]\<[Order]\>)ViewData\[[\"data\"]\])]                                                    |
|                                                                                                                                                                                                                                                         |
| [                         .Caption([\"First Grid Order\"])                         ]                                                                                                        |
|                                                                                                                                                                                                                                                         |
| [                         .Column(column =\>]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                         |
| [                         {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                         |
| [                             column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                      |
|                                                                                                                                                                                                                                                         |
| [                             column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                |
|                                                                                                                                                                                                                                                         |
| [                             column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                |
|                                                                                                                                                                                                                                                         |
| [                             ]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [                         })]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                         |
| [                        .AllowRowsDragging([true])]                                                                                                                                           |
|                                                                                                                                                                                                                                                         |
| [                        .AllowDragAndDrop([false])                                ]                                                                                                           |
|                                                                                                                                                                                                                                                         |
| [                        .TargetHtmlElementId([\"#GridDest\"])        ]                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [                        .RowsDraggingMode([DragandDropMode].GhostRows)]                                                                                                                    |
|                                                                                                                                                                                                                                                         |
| [                        .AutoFormat([Skins].Midnight)]                                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [                        .RowsDroppingMapper([\"Dragged\"])                        ]                                                                                                        |
|                                                                                                                                                                                                                                                         |
| [                        .ClientSideEvents(events =\> {]                                                                                                                                                            |
|                                                                                                                                                                                                                                                         |
| [                            events.OnRowDropping([\"OnDropping\"]);]                                                                                                                       |
|                                                                                                                                                                                                                                                         |
| [                            events.OnRowDropped([\"DroppedTarget\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| [                        }).Render();]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                         |
| [                          [}]][]                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Set the data source in the **Index** action and render the view.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                         |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [   [///][ ][\<summary\>]]                                                                                                 |
|                                                                                                                                                                                                                                |
| [        [///][ Used for rendering the grid initially.]]                                                                                        |
|                                                                                                                                                                                                                                |
| [        [///][ ][\</summary\>]]                                                                                           |
|                                                                                                                                                                                                                                |
| [        [///][ ][\<returns\>][Veiw page; it displays the grid.][\</returns\>]] |
|                                                                                                                                                                                                                                |
| [        [public] [ActionResult] Index()]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [            ViewData\[[\"data\"]\] = [GridOrders].SrcOrders;]                                                                             |
|                                                                                                                                                                                                                                |
| [            ViewData\[[\"dataDest\"]\] = [GridOrders].DestOrders;]                                                                        |
|                                                                                                                                                                                                                                |
| [            [if] (ControllerContext.HttpContext.Request.IsAjaxRequest())]                                                                                            |
|                                                                                                                                                                                                                                |
| [            {]                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [                [return] PartialView([\"DragResetPartialView\"], [this].ViewData);]                                     |
|                                                                                                                                                                                                                                |
| [            }]                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [return] View();]                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [        ]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [        }][]                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Now you can select any rows in your grid and drop them into any other target element. In the sample, you set the target element as another grid. Please refer to example above. The following screenshot shows rows being dropped in another element.

 

 

{border="0"}

Figure 238: Drag and Drop of Grid Records

[]{#related-topics}

