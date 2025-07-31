---
title: throughgridpropertiesmodel42.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridpropertiesmodel42.md
created_at: 2025-07-03
---






##### Through GridProperties model {#through-gridproperties-model style="tab-stops: 0pt"}

[[1.   ]]{.MsoHyperlink}Create a model in the application.[**[]**]{.MsoHyperlink}

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

 

3.   Create a **GridPropertiesModel** in the **Index** actions.

4.   To enable the **FilterBar** filtering mode, set the **FilterMode** to **FilterBar** as shown in the code snippets below:

 

The following  controller code will help you customize the Grid.

 

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
| [                AllowPaging = [true],]                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [                AllowSorting = [true],]                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [                AllowFiltering = [true],]                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [                AutoFormat = [Skins].Sandune]                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| **[            gridModel.Filters.FilterMode = [FilterMode].FilterBar;]**                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| **[            gridModel.Filters.FilterBarMode = [FilterBarMode].Immediate;]**                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| **[            gridModel.Filters.ShowFilterStatusMessage = [true];]**                                                                                                                               |
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
| [        [///][ Paging, editing, and filtering requests are mapped to this method. This method invokes the HtmlActionResult]]                                                 |
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

 

5.   Run the application and use the filtering tokens in the filter bar to filter the data table. The valid tokens are listed in the filter token table.

The following figure is an output sample of a filter bar implemented in a grid.

 

{border="0"}[]

Figure 128: Implementation of Filter Bar through GridPropertiesModel

 

[]{#related-topics}

