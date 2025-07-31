---
title: throughgridpropertiesmodel48.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridpropertiesmodel48.md
created_at: 2025-07-03
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **HomeController.cs** file to create the Grid control in the view.[   ]

[     ]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [///][ ][\<summary\>][]                                            |
|                                                                                                                                                                                                                                                            |
| [        [///][ Used for rendering the grid initially.]]                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [        [///][ ][\</summary\>]]                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [        [///][ ][\<returns\>][Veiw page; it displays the grid.][\</returns\>]]                             |
|                                                                                                                                                                                                                                                            |
| [        [public] [ActionResult] OrderGrid()]                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                            |
| [            [GridPropertiesModel]\<[Order]\> Srcmodel= [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                DataSource = [GridOrders].SrcOrders,]                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [                Caption = [\"First Grid Order\"],]                                                                                                                                            |
|                                                                                                                                                                                                                                                            |
| [                AllowRowsDragging = [true],]                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                AllowDragAndDrop = [false],]                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                TargetHtmlElementId = [\"#GridDest\"],]                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                RowsDraggingMode = [DragandDropMode].GhostRows,]                                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                AutoFormat = [Skins].Midnight,]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [                RowsDroppingMapper = [\"Dragged\"],]                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [                OnRowDropping = [\"OnDropping\"],]                                                                                                                                            |
|                                                                                                                                                                                                                                                            |
| [                OnRowDropped=[\"DroppedTarget\"]]                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [            };]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [    ViewData\[[\"SrcGrid\"]\] = Srcmodel;]                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [    Return View();]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                         |
| [        [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"GridSrc\"],[\"SrcGrid\"],column =\>] |
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
| [                         })                         ]                                                                                                                                                              |
|                                                                                                                                                                                                                                                         |
| [                          [%\>]][]                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ ][@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Order]\>([\"GridSrc\"],[\"SrcGrid\"],column =\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                         {]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                             column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                             column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                             column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                             ]                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                         }).][ToString())[)] ][]                                                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

Now you can select any rows in your grid and drop them into any other target element. In the sample, you set the target element as another grid. Please refer to example above. The following screenshot shows rows being dropped in another element.

{border="0"}

Figure 239: Drag and Drop of Grid Records

 

[]{#related-topics}

