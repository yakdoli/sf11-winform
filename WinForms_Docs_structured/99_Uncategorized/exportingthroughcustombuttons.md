---
title: exportingthroughcustombuttons.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\exportingthroughcustombuttons.md
created_at: 2025-07-03
---






#### Exporting through Custom Buttons {#exporting-through-custom-buttons style="tab-stops: 0pt"}

 

The steps to export through custom buttons are as follows:

1.   Create a model in the application. Refer to [[GettingStarted\>Adding a model to the Application]]{.underline}.

2.   Create a strongly typed view. Refer to [[How to\>Strongly Typed View]]{.underline}.

3.   In the view, use the **Model** property in the **DataSource** to bind the data source.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\][]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
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
| **[View \[cshtml\][]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [            .Datasource(Model)]                                                                                                                                                                                       |
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
| [                column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.ShipPostalCode).HeaderText([\"Ship postal Code\"]);]                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                column.Add(c =\> c.Freight).HeaderText([\"Frieght\"]).Format([\"{Freight:#,#}\"]);]                                                                   |
|                                                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [                .EnablePaging()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [                .EnableSorting()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                .AutoFormat([Skins].Sandune)]                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [                .Render();]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [         [}]]                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

4.   Create a button element in the view page and write the code displayed below for the button click event.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][sscript][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [               \$(document).ready([function] () {]                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [                   \$([\"#export\"]).bind([\'click\'], [function] () {                   ]                              |
|                                                                                                                                                                                                                                 |
| [                       [// Find the gridobject;]]                                                                                                                |
|                                                                                                                                                                                                                                 |
| [                       [var] gridObj = \$find([\"OrdersGrid\"]);]                                                                              |
|                                                                                                                                                                                                                                 |
| [                       [// Set the ExcelExport action mapper using Set_ExcelExportMapper().]]                                                                    |
|                                                                                                                                                                                                                                 |
| [                       gridObj.set_ExcelExportMapper([\"ExportToExcel\"]);]                                                                                         |
|                                                                                                                                                                                                                                 |
| [                       ]                                                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [                       [// Call the SendExcelExportRequest().]]                                                                                                  |
|                                                                                                                                                                                                                                 |
| [                       gridObj.sendExcelExportRequest();]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [                   });]                                                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [               });]                                                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [               ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                 |
| [         [\</][script][\>]]                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   Specify the file name and Excel version details in the **ExportToExcel()** method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [///][ ][\<summary\>][]                                                      |
|                                                                                                                                                                                                                                                                      |
| [        [///][ Used to export the grid as an Excel worksheet.]]                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [        [///][ ][\</summary\>]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [        [///][ ][\<param name=\"grid\"\>][Grid object.][\</param\>]]                                                 |
|                                                                                                                                                                                                                                                                      |
| [        [///][ ][\<returns\>][Excel file.][\</returns\>]]                                                            |
|                                                                                                                                                                                                                                                                      |
| [        [public] [ActionResult] ExportToExcel()]                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [            [var] data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();]                                                                           |
|                                                                                                                                                                                                                                                                      |
| [  **return**]**[ data.GridExportToExcel\<[Order]\>([\"GridExcel.xlsx\"], [ExcelVersion].Excel2007);]** |
|                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Run the application and click the **Export** button. The grid will appear as displayed below.

 

{border="0"}

Figure 199: Exported Grid Content

 

[]{#related-topics}

