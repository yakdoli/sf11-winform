---
title: forpdf.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\forpdf.md
created_at: 2025-07-03
---






##### For PDF {#for-pdf style="tab-stops: 0pt"}

Certain events are used to format cells and rows in a grid that was exported to PDF. These are specified in the following sections.

You can format cells in MVC Grid in two ways:

Through GridBuilder

The steps to enable the PDF exporting feature through **GridBuilder** are as follows:

1.   Create a model in the application[.]

2.   Create a strongly typed view[.]

3.  In the view, use the **Model** property in the **Datasource()** to bind the data source.

4.  Configure the grid toolbar and add a mapper to enable grid record exporting.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [                .Datasource(Model)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [                .Caption([\"Orders\"])]                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [               \-\-\-\-\-\-\-\-\-\-\-\--]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [               \-\-\-\-\-\-\-\-\-\-\-\--]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [                .ToolBar( toolbar =\>]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                    {]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                        toolbar.Add([GridToolBarItems].PDFExport,[\"PDF Export\"]);]                                                                                  |
|                                                                                                                                                                                                                                                            |
| [                    })]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [                    ]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [                .Mappers(map =\>]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                    {]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                        map.ExportPdfAction([\"ExportToPDF\"]);]                                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                    })]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [    [%\>]][]                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| [                ][]                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [@ {][ ][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\"])] |
|                                                                                                                                                                                                                                                            |
| [                .Datasource(Model)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [                .Caption([\"Orders\"])]                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [               \-\-\-\-\-\-\-\-\-\-\-\--]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [               \-\-\-\-\-\-\-\-\-\-\-\--]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [                .ToolBar( toolbar =\>]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                    {]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                        toolbar.Add([GridToolBarItems].PDFExport,[\"PDF Export\"]);]                                                                                  |
|                                                                                                                                                                                                                                                            |
| [                    })]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [                    ]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [                .Mappers(map =\>]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [                    {]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [                        map.ExportPdfAction([\"ExportToPDF\"]);]                                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [                    })]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [   [}]][]                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [                ][]                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.  Add the events for formatting rows and cells.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| [QueryExportPdfRowInfo][]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                   |
| [public][ [ActionResult] ExportToPDF([PagingParams] args)]                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [IEnumerable][ data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();]                                                             |
|                                                                                                                                                                                                                                                                                   |
| [var][ engine = data.GridExportToPDF\<[Order]\>() [as] [GridPDFExportActionResult]\<[Order]\>;] |
|                                                                                                                                                                                                                                                                                   |
| [engine.GridModel.QueryExportPdfRowInfo = OnQueryRowInfo;]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| [return][ engine;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [public][ [void] OnQueryRowInfo([PdfGridRow] Row)]                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [Row.Style.BackgroundBrush = [new] [PdfSolidBrush]([Color].Bisque);]                                                                                                     |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [QueryExportPdfCellInfo][]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [public][ [ActionResult] ExportToPDF([PagingParams] args)]                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [IEnumerable][ data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();]                                                             |
|                                                                                                                                                                                                                                                                                   |
| [var][ engine = data.GridExportToPDF\<[Order]\>() [as] [GridPDFExportActionResult]\<[Order]\>;] |
|                                                                                                                                                                                                                                                                                   |
| [engine.GridModel.QueryExportPdfCellInfo = OnQueryCellInfo;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                   |
| [return][ engine;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [public][ [void] OnQueryCellInfo([PdfGridCell] cell, [GridTableCellType] cellType)]                                     |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [if][ (cellType == [GridTableCellType].ColumnHeaderCell)]                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [cell.Style.BackgroundBrush = [new] [PdfSolidBrush]([Color].BlueViolet);]                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Through GridPropertiesModel

 

1.   Create a model in the application[.]

2.  Add the following code to the view.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\",\"GridModel\",] column =\>] |
|                                                                                                                                                                                                                                                                                     |
| [                {]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [                    column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                     |
| [                    column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dddd, MMMM d, yyyy}\"]);]                                                                          |
|                                                                                                                                                                                                                                                                                     |
| [                    column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [                    column.Add(c =\> c.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [                    column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                     |
| [                    column.Add(c =\> c.ShipPostalCode).HeaderText([\"Ship postal Code\"]);]                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [                    column.Add(c =\> c.Freight).HeaderText([\"Frieght\"]).Format([\"{Freight:#,#}\"]);]                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [                });]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                     |
| [%\>]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [@ {][ Html.Syncfusion().Grid\<[Order]\>([\"OrdersGrid\",\"GridModel\",] column =\>] |
|                                                                                                                                                                                                                                  |
| [                {]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [                    column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                        |
|                                                                                                                                                                                                                                  |
| [                    column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{0:dddd, MMMM d, yyyy}\"]);]                       |
|                                                                                                                                                                                                                                  |
| [                    column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                  |
|                                                                                                                                                                                                                                  |
| [                    column.Add(c =\> c.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                |
|                                                                                                                                                                                                                                  |
| [                    column.Add(c =\> c.ShipCity).HeaderText([\"Ship City\"]);]                                                                                      |
|                                                                                                                                                                                                                                  |
| [                    column.Add(c =\> c.ShipPostalCode).HeaderText([\"Ship postal Code\"]);]                                                                         |
|                                                                                                                                                                                                                                  |
| [                    column.Add(c =\> c.Freight).HeaderText([\"Frieght\"]).Format([\"{Freight:#,#}\"]);]                                     |
|                                                                                                                                                                                                                                  |
| [                });]                                                                                                                                                                        |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                      |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.  Create a **GridPropertiesModel** and assign the grid properties in the model.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [    [GridPropertiesModel] \<[Order]\> model = [new] [GridPropertiesModel] \<[Order]\>()] |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        DataSource = [new] [NorthwindDataContext]().Orders.Take(200),]                                                                                           |
|                                                                                                                                                                                                                                                    |
| [        Caption = [\"Orders\"],]                                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [        AllowPaging = [true],]                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [        AllowSorting = [true]]                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [    };]                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.  Configure the **GridPropertiesModel** as displayed below to accept the WordExport, ActionMapper, and to render the toolbar.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                             |
|                                                                                                                                                                                                                                      |
| [ToolbarSettings][ toolbar = [new] [ToolbarSettings] ();][] |
|                                                                                                                                                                                                                                      |
| [toolbar.Enable = [true]; [// Used to enable the toolbar.]]                                                                                           |
|                                                                                                                                                                                                                                      |
| [// Add the PDF toolbar item in toolbar with caption and mapper name.][]                                                                       |
|                                                                                                                                                                                                                                      |
| [toolbar.Items.Add([GridToolBarItems].PDFExport, [\" ExportToPDF \"]);]                                                                          |
|                                                                                                                                                                                                                                      |
| [model.ToolBar = toolbar;]                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.  Add the events for formatting rows and cells.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                   |
| [QueryExportPdfRowInfo][]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                   |
| [public][ [ActionResult] ExportToPDF([PagingParams] args)]                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [IEnumerable][ data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();]                                                             |
|                                                                                                                                                                                                                                                                                   |
| [var][ engine = data.GridExportToPDF\<[Order]\>() [as] [GridPDFExportActionResult]\<[Order]\>;] |
|                                                                                                                                                                                                                                                                                   |
| [engine.GridModel.QueryExportPdfRowInfo = OnQueryRowInfo;]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| [return][ engine;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [public][ [void] OnQueryRowInfo([PdfGridRow] Row)]                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [Row.Style.BackgroundBrush = [new] [PdfSolidBrush]([Color].Bisque);]                                                                                                     |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [QueryExportPdfCellInfo][]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [public][ [ActionResult] ExportToPDF([PagingParams] args)]                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [IEnumerable][ data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();]                                                             |
|                                                                                                                                                                                                                                                                                   |
| [var][ engine = data.GridExportToPDF\<[Order]\>() [as] [GridPDFExportActionResult]\<[Order]\>;] |
|                                                                                                                                                                                                                                                                                   |
| [engine.GridModel.QueryExportPdfCellInfo = OnQueryCellInfo;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                   |
| [return][ engine;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [public][ [void] OnQueryCellInfo([PdfGridCell] cell, [GridTableCellType] cellType)]                                     |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [if][ (cellType == [GridTableCellType].ColumnHeaderCell)]                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [cell.Style.BackgroundBrush = [new] [PdfSolidBrush]([Color].BlueViolet);]                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

[]{#related-topics}

