---
title: throughgridbuilder41.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridbuilder41.md
created_at: 2025-07-03
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

1.   Create a model in the application (Refer to [Getting Started\>Adding a Model to the Application]{.UGHyperlink}).

2.   Create a strongly typed view (Refer to [How to\>Strongly Typed View]{.UGHyperlink}).

3.   In the view you can use its **Model** property in **Datasource()** in order to bind the data source alone. Don't specify any visible column collections to grid. The grid automatically populates the columns from its model.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [\<%][=][Html.Syncfusion().Grid\<[Product]\>([\"ProductGrid\"])] |
|                                                                                                                                                                                                                                                               |
| **[       .Datasource(Model)          ]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [       .Caption([\"Product Details\"])]                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [       [%\>]]                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                                                      |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| [\@{][ Html.Syncfusion().Grid\<[Product]\>([\"ProductGrid\"])] |
|                                                                                                                                                                                                            |
| **[       .Datasource(Model)          ]**                                                                                                                              |
|                                                                                                                                                                                                            |
| [       .Caption([\"Product Details\"])]                                                                                                       |
|                                                                                                                                                                                                            |
| [       [}]]                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

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
| [        [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]] |
|                                                                                                                                                                                                                                |
| [        [public] [ActionResult] Index()]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [    var][ data = [new] [NorthwindDataContext]().Products.Take(15);]                         |
|                                                                                                                                                                                                                                |
| [            [return] View(data);]                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 95: Grid with Auto-Generated Columns

[]{#related-topics}

