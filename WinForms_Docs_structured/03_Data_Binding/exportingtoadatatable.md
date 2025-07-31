---
title: exportingtoadatatable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\exportingtoadatatable.md
created_at: 2025-07-03
---






##### Exporting to a Data Table {#exporting-to-a-data-table style="tab-stops: 0pt"}

Similarly, you can to export the Spreadsheet data to a data table by using the ExportDataTable method of Worksheet. The following code demonstrates this:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| [IWorksheet][ sheet  = [this].spreadsheetControl.ExcelProperties.WorkBook.Worksheets\[0\];]                                                        |
|                                                                                                                                                                                                                                                                                           |
| [IRange][ range = sheet.Range\[[\"A1:K50\"]\];]                                                                                                 |
|                                                                                                                                                                                                                                                                                           |
| [DataTable][ Dt = sheet.ExportDataTable(range, [ExcelExportDataTableOptions].ColumnNames);]                                                     |
|                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| **\[VB\]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| [Dim][ sheet [As] [IWorksheet] = [Me].spreadsheetControl.ExcelProperties.WorkBook.Worksheets(0)]         |
|                                                                                                                                                                                                                                                                                           |
| [Dim][ range [As] [IRange] = sheet.Range([\"A1:K50\"])]                                               |
|                                                                                                                                                                                                                                                                                           |
| [Dim][ Dt [As] [DataTable] = sheet.ExportDataTable(range, [ExcelExportDataTableOptions].ColumnNames)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

