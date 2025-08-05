---
title: excelconverteroptions.md
original_path: WinForms_Docs/99_Uncategorized/excelconverteroptions.md
created_at: 2025-08-05
---






#### Excel Converter Options {#excel-converter-options style="tab-stops: 0pt"}

[] 

The **GridExcelConverter** class enables you to export specific grid elements like column headers, row headers, and so on. By default, the **GridExcelConverterControl** exports all the elements in the grid.

[] 

The following code example illustrates how to include both row and column headers during the export.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [gecc.GridToExcel([this].grid.Model, [@\"C:\\MyGGC.xls\"], Syncfusion.GridExcelConverter.[ConverterOptions].RowHeaders \| Syncfusion.GridExcelConverter.[ConverterOptions].ColumnHeaders);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [gecc.GridToExcel([Me].grid.Model, [\"C:\\MyGGC.xls\"], Syncfusion.GridExcelConverter.ConverterOptions.RowHeaders\|Syncfusion.GridExcelConverter.ConverterOptions.ColumnHeaders)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p32} 

 

[]{#related-topics}

