---
title: usinggridbuilder.md
original_path: WinForms_Docs/04_Controls/Grid/usinggridbuilder.md
created_at: 2025-08-05
---






#### Using GridBuilder {#using-gridbuilder style="tab-stops: 0pt"}

 

The steps to enable the Excel exporting feature through GridBuilder are as follows:

[1.   ]Create a model in the application. Refer to **[[Getting Started]]{.underline}**[[\>**Adding a Model to the Application**]]{.underline}[.]

2.   Create a strongly typed view. Refer to [[How to\>Strongly Typed View]]{.underline}.

3.   In the view, use the **Model** property in the **Datasource()**, to bind the data source.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| **[            .Datasource(Model)]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dddd, MMMM d, yyyy}\"]);                ]                                     |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipPostalCode).HeaderText([\"Ship postal Code\"]);]                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.Freight).HeaderText([\"Frieght\"]).Format([\"{Freight:#,#}\"]);]                                                                   |
|                                                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                .EnablePaging()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                .EnableSorting()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                .AutoFormat([Skins].Sandune)]                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [         [%\>]]                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| **[            .Datasource(Model)]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            .Column(column =\>]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dddd, MMMM d, yyyy}\"]);                ]                                     |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipPostalCode).HeaderText([\"Ship postal Code\"]);]                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.Freight).HeaderText([\"Frieght\"]).Format([\"{Freight:#,#}\"]);]                                                                   |
|                                                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                .EnablePaging()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                .EnableSorting()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                .AutoFormat([Skins].Sandune)]                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [                .Render();]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [         [}]]                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

4.   Configure the grid toolbar to enable exporting grid records.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [   **.ToolBar(tools =\> tools.Export([GridToolBarItems].ExcelExport, [\"Export\"], [\"ExportToExcel\"]))**]                                   |
|                                                                                                                                                                                                                                                            |
| [         [%\>]]                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [            .Caption([\"Orders\"])            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [   **.ToolBar(tools =\> tools.Export([GridToolBarItems].ExcelExport, [\"Export\"], [\"ExportToExcel\"])).**Render();]                         |
|                                                                                                                                                                                                                                                            |
| [         [}]]                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Specify the file name and Excel version details in the **ExportToExcel()** method.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [        [///][ ][\<summary\>]]                                                                                                            |
|                                                                                                                                                                                                                                                |
| [        [///][ Used to export the grid as an Excel file.]]                                                                                                     |
|                                                                                                                                                                                                                                                |
| [        [///][ ][\</summary\>]]                                                                                                           |
|                                                                                                                                                                                                                                                |
| [        [///][ ][\<param name=\"grid\"\>][Grid object.][\</param\>]]                           |
|                                                                                                                                                                                                                                                |
| [        [///][ ][\<returns\>][Excel file.][\</returns\>]]                                      |
|                                                                                                                                                                                                                                                |
| [        [public] [ActionResult] ExportToExcel()]                                                                                                             |
|                                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                |
| [            [var] data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();]                                                     |
|                                                                                                                                                                                                                                                |
| [            [return] data.GridExportToExcel\<[Order]**\>([\"GridExcel.xlsx\"], [ExcelVersion].Excel2007)**;] |
|                                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

 

6.   Run the application and click the **Export** button. The grid will appear as displayed below.

 

{border="0"}

Figure 197: Exported Grid Content

 

[]{#related-topics}

