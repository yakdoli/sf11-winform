---
title: excelexport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\excelexport.md
created_at: 2025-07-03
---








  









### Excel Export {#excel-export style="tab-stops: 0pt"}

Export to Excel is one of the most common functionalities that is required in .NET. The Essential Grid Control has in-built support for Excel Export. You can download data from the Grid control to an Excel spreadsheet for offline verification and/or computation. This can be achieved by using the GridExcelExportActionResult\<T\> extension. This extension applies the Grid control\'s styles and formats to Excel. The GridExcelExportActionResult\<T\> is derived from GridActionResultBase\<T\>. The XlsIO libraries are used to support the conversion of the Grid contents to Excel.

All the content from a Grid can be converted to an Excel Spreadsheet. It also provides the option to specify the version of the Excel file by using the ExcelVersion enum. The versions that can be specified are as follows:

[·      ]ExcelVersion.Excel97to2003

[·      ]ExcelVersion.Excel2007

[·      ]ExcelVersion.Excel2010

 

Properties

 


+--------------+----------------------------------------------------+------------------+---------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Property     | Description                                        | Type of property | Value it accepts                                  | Property syntax                                                                                 | Any other dependencies/sub-properties associated |
+--------------+----------------------------------------------------+------------------+---------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------------------+
| FileName     | Gets or sets the Excel file name.                  | String           | Any string value.                                 |             var data = new NorthwindDataContext().Orders.Take(200).ToList();                    |                                                  |
|              |                                                    |                  |                                                   |                                                                                                 |                                                  |
|              |                                                    |                  |                                                   |             return data.GridExportToExcel\<Order\>(\"GridExcel.xlsx\", ExcelVersion.Excel2007); |                                                  |
|              |                                                    |                  |                                                   |                                                                                                 |                                                  |
|              |                                                    |                  |                                                   |                                                                                                 |                                                  |
+--------------+----------------------------------------------------+------------------+---------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------------------+
| ExcelVersion | Gets or sets the Excel version for the Excel file. | Enum             | ExcelVersion.Excel97to2003 ExcelVersion.Excel2007 |             var data = new NorthwindDataContext().Orders.Take(200).ToList();                    | NA                                               |
|              |                                                    |                  |                                                   |                                                                                                 |                                                  |
|              |                                                    |                  | ExcelVersion.Excel2010                            |             return data.GridExportToExcel\<Order\>(\"GridExcel.xlsx\", ExcelVersion.Excel2007); |                                                  |
|              |                                                    |                  |                                                   |                                                                                                 |                                                  |
|              |                                                    |                  |                                                   |                                                                                                 |                                                  |
+--------------+----------------------------------------------------+------------------+---------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------------------+


[] 

Methods

 


+------------------------------------------+----------------------------------+-----------------+-----------------------------------------------------------------------------------+
| Name                                     | Parameters                       | Return type     | Description                                                                       |
+------------------------------------------+----------------------------------+-----------------+-----------------------------------------------------------------------------------+
| GridExportToExcel                        | ExcelFileName, ExcelVersion      | ActionResult    | Used to export the grid content to the Excel format.                              |
|                                          |                                  |                 |                                                                                   |
|  (IEnumerable\<T\>)                      |                                  |                 |                                                                                   |
+------------------------------------------+----------------------------------+-----------------+-----------------------------------------------------------------------------------+
| Export(GridToolbarItem,mapper)           | GridToolbarItem, Mapper          | IToolBarBuilder | Used to add the GridExcel toolbar button and the Excel export action mapper.      |
|                                          |                                  |                 |                                                                                   |
|                                          |                                  |                 |                                                                                   |
+------------------------------------------+----------------------------------+-----------------+-----------------------------------------------------------------------------------+
| Export(GridToolbarItem, Caption, mapper) | GridToolBarItem, Caption, Mapper | IToolBarBuilder | Used to add the GridExcel toolbar button with the caption and  the action mapper. |
+------------------------------------------+----------------------------------+-----------------+-----------------------------------------------------------------------------------+


 

The Excel exporting feature can be enabled through two ways:

[·      ]GridBuilder

[·      ]GridPropertiesModel

More:









