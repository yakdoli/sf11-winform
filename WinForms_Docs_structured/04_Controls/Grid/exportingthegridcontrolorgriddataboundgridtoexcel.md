---
title: exportingthegridcontrolorgriddataboundgridtoexcel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\exportingthegridcontrolorgriddataboundgridtoexcel.md
created_at: 2025-07-03
---






#### Exporting the Grid Control or Grid Data Bound Grid To Excel {#exporting-the-grid-control-or-grid-data-bound-grid-to-excel style="tab-stops: 0pt"}

[] 

The **GridExcelConverter** class provides support for exporting data from a Grid control or Grid Data Bound Grid into an Excel spreadsheet for verification and/or computation. This control automatically copies the Grid\'s styles and formats to Excel. The **GridExcelConverter** control is derived from the **GridExcelConverterBase**. The XlsIO libraries support the conversion of Grid content to Excel.

 

To make use of the GridExcelConverter class, the following assemblies should be added along with the default assemblies present in the **References** folder of your application: **Syncfusion.GridConverter.Base** and **Syncfusion.XlsIO.Base**.

 

The **GridToExcel** method is used to export the grid to an Excel sheet. The following code example illustrates how to convert the Grid content to Excel.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [Syncfusion.GridExcelConverter.[GridExcelConverterControl] gecc = [new] Syncfusion.GridExcelConverter.[GridExcelConverterControl]();] |
|                                                                                                                                                                                                                                                |
| [gecc.GridToExcel([this].gridControl1.Model, [@\"C:\\MyGC.xls\"]);]                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [Dim][ gecc [As] Syncfusion.GridExcelConverter.GridExcelConverterControl = [New] Syncfusion.GridExcelConverter.GridExcelConverterControl()] |
|                                                                                                                                                                                                                                                                            |
| [gecc.GridToExcel([Me].gridControl1.Model, [\"C:\\MyGC.xls\"])]                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following code example illustrates how to convert the Grid Data Bound Grid content to Excel.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [Syncfusion.GridExcelConverter.[GridExcelConverterControl] gecc = [new] Syncfusion.GridExcelConverter.[GridExcelConverterControl]();] |
|                                                                                                                                                                                                                                                |
| [gecc.GridToExcel([this].gridDataBoundGrid1.Model, [@\"C:\\MyGC.xls\"]);]                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [Dim][ gecc [As] Syncfusion.GridExcelConverter.GridExcelConverterControl = [New] Syncfusion.GridExcelConverter.GridExcelConverterControl()] |
|                                                                                                                                                                                                                                                                            |
| [gecc.GridToExcel([Me].gridDataBoundGrid1.Model, [\"C:\\MyGC.xls\"])]                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

More:





