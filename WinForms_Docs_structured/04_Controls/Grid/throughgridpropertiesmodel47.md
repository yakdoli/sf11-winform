---
title: throughgridpropertiesmodel47.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridpropertiesmodel47.md
created_at: 2025-07-03
---






#### Through GridPropertiesModel: {#through-gridpropertiesmodel style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **HomeController.cs** file to create the Grid control in the view.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [      ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [ [///][ ][\<summary\>]]                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [        [///][ Used for rendering the grid initially.]]                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\</summary\>]]                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\<returns\>][View page; it displays the Grid.][\</returns\>]]                               |
|                                                                                                                                                                                                                                                              |
| [        [public] [ActionResult] OrderGrid()]                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [                DataSource = [new] [NorthwindDataContext]().Orders.ToList(),]                                                                                              |
|                                                                                                                                                                                                                                                              |
| [                AutoFormat = [Skins].Sandune,]                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [                Caption = [\"First Grid Order\"],]                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [                AllowPaging = [true],]                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [                RowsSelectionMode = [RowsSelectionMode].Toggle]                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [            ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [        }][]                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Create the Grid control in the view.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [   [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"], [\"GridModel\"], column =\>] |
|                                                                                                                                                                                                                                                      |
| [                         {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| [                             column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                   |
|                                                                                                                                                                                                                                                      |
| [                             column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                             |
|                                                                                                                                                                                                                                                      |
| [                             column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                             |
|                                                                                                                                                                                                                                                      |
| [                             column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:MM/dd/yyyy}\"]);]                                  |
|                                                                                                                                                                                                                                                      |
| [                             column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                                                                                    |
|                                                                                                                                                                                                                                                      |
| [                             ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                      |
| [                         })                                                ]                                                                                                                                    |
|                                                                                                                                                                                                                                                      |
| [        [%\>]][]                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [ ][@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"], [\"GridModel\"], column =\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                         {]                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                             column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                             column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                             column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                             column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:MM/dd/yyyy}\"]);]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                             column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                             ]                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                         })][.][ToString())[)] ][]                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

Run the application and select any row in the grid. The grid will appear as shown below.

{border="0"}

Figure 236: Grid with Row Selected

***[]*** 

If you click on the selected row, the selected row will be unselected as shown in the following screenshot.

 

{border="0"}

Figure 237: Grid with Row Unselected

[]{#_Drag_and_Drop} 

[]{#related-topics}

