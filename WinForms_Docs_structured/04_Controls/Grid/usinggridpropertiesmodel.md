---
title: usinggridpropertiesmodel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\usinggridpropertiesmodel.md
created_at: 2025-07-03
---






#### Using GridPropertiesModel {#using-gridpropertiesmodel style="tab-stops: 0pt"}

 

Create a model in the application. Refer to [[Getting Started\>Adding a model to the Application]]{.underline}.

1.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]][]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Orders_Grid\"],[\"GridModel\"], column=\> {] |
|                                                                                                                                                                                                                                                                                                                 |
| [            column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                 |
| [            column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dddd, MMMM d, yyyy}\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                 |
| [            column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [            column.Add(c =\> c.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                 |
| [            column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [            column.Add(c =\> c.ShipPostalCode).HeaderText([\"Ship postal Code\"]);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| [            column.Add(c =\> c.Freight).HeaderText([\"Frieght\"]).Format([\"{Freight:#,#}\"]);]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                 |
| [    })[%\>]]                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [ ][@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Order]\>([\"Orders_Grid\"],[\"GridModel\"], column=\> {] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dddd, MMMM d, yyyy}\"]);]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            column.Add(c =\> c.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            column.Add(c =\> c.ShipPostalCode).HeaderText([\"Ship postal Code\"]);]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            column.Add(c =\> c.Freight).HeaderText([\"Frieght\"]).Format([\"{Freight:#,#}\"]);]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    }).][ToString())[)]    ][    ][]                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[                                                                     ][  ]**[]**

[] 

[] 

2.   Create a **GridPropertiesModel** in the **Index** method and the assign grid properties in the model.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [            GridPropertiesModel][\<[Order]\> model = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                                                      |
| [            {]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| [                DataSource = [new] [NorthwindDataContext]().Orders.Take(200),]                                                                                                                     |
|                                                                                                                                                                                                                                                                                      |
| [                Caption = [\"Product\"],]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [                AllowPaging = [true],]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                      |
| [                AllowSorting = [true]                             ]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                      |
| [            };]                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Configure the GridPropertiesModel as displayed below, to accept the ExcelExport ActionMapper and to render the toolbar.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                               |
|                                                                                                                                                                                                  |
| [   ToolbarSettings][ toolbar = [new] [ToolbarSettings]();] |
|                                                                                                                                                                                                  |
| [            toolbar.Enable = [true];[// Used to enable the toolbar. ]]                                           |
|                                                                                                                                                                                                  |
| [           // Add the Excel tool item in the toolbar with caption and mapper name.][]                     |
|                                                                                                                                                                                                  |
| [            toolbar.Items.Add([GridToolBarItems].ExcelExport, [\"Export\~ExportToExcel\"]);  ]              |
|                                                                                                                                                                                                  |
| [            model.ToolBar = toolbar;]                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: The syntax for the ExcelExport item is toolbarcaption + \~ +mapperName. In this example, Export is the caption and ExcelToExcel is the name of the mapper.


[] 

4.   Pass the **GridPropertiesModel** to the view by using **ViewData**.

 

+------------------------------------------------------------------------------------------------------+
| **[Controller]**                                   |
|                                                                                                      |
| [     ]                                                          |
|                                                                                                      |
| [  ViewData\[[\"GridModel\"]\] = model;] |
+------------------------------------------------------------------------------------------------------+

 

 

5.   Specify the file name and the Excel version details in the **ExportToExcel()** method.

[    ]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [///][ ][\<summary\>][]                                                         |
|                                                                                                                                                                                                                                                                         |
| [        [///][ Used to export the grid as an Excel worksheet.]]                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [        [///][ ][\</summary\>]]                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [        [///][ ][\<param name=\"grid\"\>][Grid object.][\</param\>]]                                                    |
|                                                                                                                                                                                                                                                                         |
| [        [///][ ][\<returns\>][Excel file.][\</returns\>]]                                                               |
|                                                                                                                                                                                                                                                                         |
| [        [public] [ActionResult] ExportToExcel()]                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [            [var] data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();]                                                                              |
|                                                                                                                                                                                                                                                                         |
| [     **return**]**[ data.GridExportToExcel\<[Order]\>([\"GridExcel.xlsx\"], [ExcelVersion].Excel2007);]** |
|                                                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Run the application and click the **Export** button. The grid will appear as displayed below.

 

 

{border="0"}

Figure 198: Exported Grid Content

**** 

[]{#related-topics}

