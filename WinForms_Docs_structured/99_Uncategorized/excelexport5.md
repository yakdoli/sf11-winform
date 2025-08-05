---
title: excelexport5.md
original_path: WinForms_Docs/99_Uncategorized/excelexport5.md
created_at: 2025-08-05
---








  





### Excel Export {#excel-export style="tab-stops: 0pt"}

The OlapGrid can be exported to an Excel file using the following code:

 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                           |
| [// Export OLAP Grid data to Excel.][] |
|                                                                                                                                           |
| [this][.OlapGrid1.ExportToExcel();]                  |
+-------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                         |
|                                                                                                                                          |
| **[]**                                                                                               |
|                                                                                                                                          |
| [\'Export OLAP Grid data to Excel][.] |
|                                                                                                                                          |
| [Me][.OlapGrid1.ExportToExcel()]                    |
+------------------------------------------------------------------------------------------------------------------------------------------+

 

The OlapGrid supports the Excel file customization using the **QueryExcelExportCellInfo** event while exporting.

 

Refer to the code snippet below to add an event handler to customize the Excel file.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                    |
| [this][.OlapGridControl1.QueryExcelExportCellInfo += [new] [EventHandler]\<[ExcelExportCellInfoEventArgs]\>(OlapGridControl1_QueryExcelExportCellInfo);] |
|                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                    |
| [void][ OlapGridControl1_QueryExcelExportCellInfo([object] sender, [ExcelExportCellInfoEventArgs] e)]                                                                            |
|                                                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                    |
| [    e.Cell.HorizontalAlignment = Syncfusion.XlsIO.[ExcelHAlign].HAlignJustify;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                           |
| [this][.OlapGridControl1.QueryExcelExportCellInfo += [new] [EventHandler]\<[ExcelExportCellInfoEventArgs]\>(OlapGridControl1_QueryExcelExportCellInfo);]                                        |
|                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] OlapGridControl1_QueryExcelExportCellInfo([ByVal] sender [As] [Object], [ByVal] e [As] ExcelExportCellInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                           |
| [      e.Cell.HorizontalAlignment = Syncfusion.XlsIO.ExcelHAlign.HAlignJustify]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]][]                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 30: OLAP Grid Data Exported to Excel

[]{#related-topics}

