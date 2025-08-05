---
title: throughgridpropertiesmodel51.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridpropertiesmodel51.md
created_at: 2025-08-05
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

1.   Create a model in the application.

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"], [\"GridModel\"], column =\>] |
|                                                                                                                                                                                                                                                                                                           |
| [    {]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                           |
| [        column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [        column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [        column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                           |
| [        column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/MM/yyyy}\"]);]                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| [        column.Add(p =\> p.Freight).HeaderText([\"Price\"]).Format([\"{0:c}\"]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| [     })[%\>]]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [\@{][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"], [\"GridModel\"], column =\>] |
|                                                                                                                                                                                                                                                       |
| [    {]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [        column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [        column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [        column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [        column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/MM/yyyy}\"]);]                                                        |
|                                                                                                                                                                                                                                                       |
| [        column.Add(p =\> p.Freight).HeaderText([\"Price\"]).Format([\"{0:c}\"]);]                                                                                |
|                                                                                                                                                                                                                                                       |
| [     }).Render();]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [    )[}]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Create a **GridPropertiesModel** in the **Index** action method.

4.   To enable the context menu, set the **EnableContextMenu** to **True** as shown in the code snippets below:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [///][ ][\<summary\>][]                                              |
|                                                                                                                                                                                                                                                              |
| [        [///][ Used for rendering the grid initially.]]                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\</summary\>]]                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]]                               |
|                                                                                                                                                                                                                                                              |
| [public][ [ActionResult] Index()]                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [                DataSource = [new] [NorthwindDataContext]().Orders.Take(200).ToList(),]                                                                                    |
|                                                                                                                                                                                                                                                              |
| [                Caption = [\"Orders\"],]                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [                **EnableContextMenu** = [true],]                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [                \-\-\-\--]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| **[            ]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [            ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [///][ ][\<summary\>][]                                              |
|                                                                                                                                                                                                                                                              |
| [        [///][ Paging/editing/filtering requests are mapped to this method. This method invokes the HtmlActionResult]]                                                       |
|                                                                                                                                                                                                                                                              |
| [        [///][ from the grid and the required response is generated.]]                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [        [///][ ][\</summary\>]]                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                                                        |
|                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            [IEnumerable] data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();]                                                        |
|                                                                                                                                                                                                                                                              |
| [            [return] data.GridActions\<[Order]\>();]                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Run the application. You will be able to see the context menu as shown below:

{border="0"}

Figure 253: Grid with Context Menu Items in the Header**[]**

 

{border="0"}

Figure 254: Grid with Context Menu Items in the Pager**[]**

{border="0"}

Figure 255: Grid with Context Menu Items for Records**[]**

 

{border="0"}

Figure 256: Grid with Context Menu in Expanded Group**[]**

 

[]{#related-topics}

