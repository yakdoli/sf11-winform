---
title: howtoconvertthecontentsofagridcontrolorgriddataboundgridcontroltoexcel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtoconvertthecontentsofagridcontrolorgriddataboundgridcontroltoexcel.md
created_at: 2025-07-03
---








  









### How to convert the contents of a GridControl or GridDataBoundGridControl to Excel {#how-to-convert-the-contents-of-a-gridcontrol-or-griddataboundgridcontrol-to-excel style="tab-stops: 0pt"}

[] 

The Contents of the GridControl and GridDataBoundGrid can be transferred to Excel by using the GridToExcel method of the GridExcelConverter class. Here is the code snippet.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                          |
| [Syncfusion.GridExcelConverter.GridExcelConverterControl gecc = ][new][ Syncfusion.GridExcelConverter.GridExcelConverterControl();] |
|                                                                                                                                                                                                                                                                                          |
| [gecc.GridToExcel(][this][.gridControl1.Model,@\"C:\\MyGC.xls\");]                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                       |
| [Dim][ gecc ][As New][ Syncfusion.GridExcelConverter.GridExcelConverterControl] |
|                                                                                                                                                                                                                                                                                       |
| [gecc.GridToExcel(][Me][.gridControl1.Model, \"C:\\MyGC.xls\")]                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following dll files should be added, along with the default dll files in the reference folder: Syncfusion.GridConverter.Base and Syncfusion.XlsIO.Base.

 

[]{#p616} 

 

[]{#related-topics}

