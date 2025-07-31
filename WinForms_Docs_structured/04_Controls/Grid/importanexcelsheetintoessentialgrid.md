---
title: importanexcelsheetintoessentialgrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\importanexcelsheetintoessentialgrid.md
created_at: 2025-07-03
---






#### Import an Excel Sheet into Essential Grid {#import-an-excel-sheet-into-essential-grid style="tab-stops: 0pt"}

[] 

An Excel sheet can also be imported to the Grid control or Grid Data Bound Grid. This can be done by using the **ExcelToGrid** method in the **GridExcelConverterControl** class.

[] 

The following code example illustrates how to transfer Excel content to the Grid control.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [Syncfusion.GridExcelConverter.[GridExcelConverterControl] gecc = [new] Syncfusion.GridExcelConverter.[GridExcelConverterControl]();] |
|                                                                                                                                                                                                                                                |
| [gecc.ExcelToGrid([@\"C:\\MyGC.xls\"], [this].gridControl1.Model);]                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [Dim][ gecc [As] Syncfusion.GridExcelConverter.GridExcelConverterControl = [New] Syncfusion.GridExcelConverter.GridExcelConverterControl()] |
|                                                                                                                                                                                                                                                                            |
| [gecc.ExcelToGrid([\"C:\\MyGC.xls\"], [Me].gridControl1.Model)]                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following code example illustrates how to transfer Excel content to the Grid Data Bound Grid.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [Syncfusion.GridExcelConverter.[GridExcelConverterControl] gecc = [new] Syncfusion.GridExcelConverter.[GridExcelConverterControl]();] |
|                                                                                                                                                                                                                                                |
| [gecc.ExcelToGrid([@\"C:\\MyGC.xls\"], [this].gridDataBoundGrid1.Model);]                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [Dim][ gecc [As] Syncfusion.GridExcelConverter.GridExcelConverterControl = [New] Syncfusion.GridExcelConverter.GridExcelConverterControl()] |
|                                                                                                                                                                                                                                                                            |
| [gecc.ExcelToGrid([\"C:\\MyGC.xls\"], [Me].gridDataBoundGrid1.Model)]                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p31} 

 

[]{#related-topics}

