---
title: throughgridbuilder40.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridbuilder40.md
created_at: 2025-07-03
---






#### Through Grid Builder {#through-grid-builder style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [Getting Started\>Adding a Model to the Application]{.UGHyperlink}).

2.   Create a strongly typed view (Refer to [How to\>Strongly Typed View]{.UGHyperlink}).

3.   In the view you can use its **Model** property in **Datasource()** in order to bind the data source.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().Grid\<[Product]\>([\"Product_grid\"])] |
|                                                                                                                                                                                                                                                                |
| **[                .Datasource(Model)]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                |
| [                .Caption([\"Products\"])              ]                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [                .Column( column =\>]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                |
| [                    {]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                |
| [                        column.Add(p =\> p.ProductID).HeaderText([\"Product ID\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                                |
| [                        column.Add(p =\> p.ProductName).HeaderText([\"Product Name\"]);]                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [                        column.Add(P =\> P.QuantityPerUnit).HeaderText([\"Quantity Per Unit\"]);]                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [                        column.Add(p =\> p.SupplierID).HeaderText([\"Supplier ID\"]);]                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [                       ]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                |
| [                    }) ]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                |
| [                 .EnablePaging()                 ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [                 .EnableSorting()]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [        [%\>]]                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                           |
|                                                                                                                                                                                                             |
| []                                                                                                                                                  |
|                                                                                                                                                                                                             |
| [\@{][ Html.Syncfusion().Grid\<[Product]\>([\"Product_grid\"])] |
|                                                                                                                                                                                                             |
| **[        .Datasource(Model) ]**                                                                                                                                       |
|                                                                                                                                                                                                             |
| [        .Caption([\"Products\"])  **     **]                                                                                                   |
|                                                                                                                                                                                                             |
| [           .Column( column =\>]                                                                                                                                        |
|                                                                                                                                                                                                             |
| [               {]                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [                        column.Add(p =\> p.ProductID).HeaderText([\"Product ID\"]);]                                                           |
|                                                                                                                                                                                                             |
| [                        column.Add(p =\> p.ProductName).HeaderText([\"Product Name\"]);]                                                       |
|                                                                                                                                                                                                             |
| [                        column.Add(P =\> P.QuantityPerUnit).HeaderText([\"Quantity Per Unit\"]);]                                              |
|                                                                                                                                                                                                             |
| [                        column.Add(p =\> p.SupplierID).HeaderText([\"Supplier ID\"]);]                                                         |
|                                                                                                                                                                                                             |
| [                       ]                                                                                                                                               |
|                                                                                                                                                                                                             |
| [                    }) ]                                                                                                                                               |
|                                                                                                                                                                                                             |
| [                 .EnablePaging()                 ]                                                                                                                     |
|                                                                                                                                                                                                             |
| [                 .EnableSorting()]                                                                                                                                     |
|                                                                                                                                                                                                             |
| [Render();]                                                                                                                                                             |
|                                                                                                                                                                                                             |
| [ [}]]                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Set its data source and render the view.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [///][ ][\<summary\>][]                |
|                                                                                                                                                                                                                                |
| [        [///][ Used to bind the grid.]]                                                                                                        |
|                                                                                                                                                                                                                                |
| [        [///][ ][\</summary\>]]                                                                                           |
|                                                                                                                                                                                                                                |
| [        [///][ ][\<returns\>][View page, it displays the grid.][\</returns\>]] |
|                                                                                                                                                                                                                                |
| [        [public] [ActionResult] Index()]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [     var][ data = [new] [NorthwindDataContext]().Products;]                                 |
|                                                                                                                                                                                                                                |
| [            [return] View(data);]                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In order to work with paging andsorting actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the following code.

[  ]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [///][ ][\<summary\>][]                     |
|                                                                                                                                                                                                                                     |
| [        [///][ Paging/sorting requests are mapped to this method. This method invokes the HtmlActionResult]]                                        |
|                                                                                                                                                                                                                                     |
| [        [/// ][from the grid. The required response is generated.]]                                                                                 |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                                                |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties.][\</param\>]] |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\<returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                     |
| [        [///][ HtmlActionResult returns the data displayed on the grid.]]                                                                           |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\</returns\>]]                                                                                                |
|                                                                                                                                                                                                                                     |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                   |
|                                                                                                                                                                                                                                     |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                               |
|                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            [IEnumerable] data = [new] [NorthwindDataContext]().Products;]                                                |
|                                                                                                                                                                                                                                     |
| [            [return] data.GridActions\<[Order]\>();]                                                                                              |
|                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the application. The grid will appear as shown below.

[] 

{border="0"}

Figure 87: LINQ to SQL Grid

 

[]{#related-topics}

