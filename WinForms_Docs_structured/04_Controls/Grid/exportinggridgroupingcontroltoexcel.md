---
title: exportinggridgroupingcontroltoexcel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\exportinggridgroupingcontroltoexcel.md
created_at: 2025-07-03
---






#### Exporting Grid Grouping Control To Excel {#exporting-grid-grouping-control-to-excel style="tab-stops: 0pt"}

[] 

The **GroupingGridExcelConverter** class provides support for exporting data from a Grouping Grid control into an Excel spreadsheet for verification and/or computation. This control automatically copies the Grid\'s styles, formats, groups, summary rows and expression fields to Excel. The **GroupingGridExcelConverter** control is derived from the **GridExcelConverterBase**. The XlsIO libraries support the conversion of Grid content to Excel.

 

To make use of the GroupingGridExcelConverter class, the following assemblies must be added along with the default assemblies present in the **References** folder of your application: **Syncfusion.XlsIO.Base** and **Syncfusion.GridConverter.Windows**.

 

The content of the Grid Grouping control can be transferred to Excel by using the **GroupingGridToExcel** method in the **GroupingGridExcelConverterControl** class. There are two export options provided by the Grid Grouping control: first option converts the entire content in the grid to Excel, and the second option converts only the visible content in the grid to Excel.

 

The following code example illustrates how to convert the entire Grid content to Excel.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| [Syncfusion.GroupingGridExcelConverter.[GroupingGridExcelConverterControl] converter = [new] Syncfusion.GroupingGridExcelConverter.[GroupingGridExcelConverterControl]();] |
|                                                                                                                                                                                                                                                                                     |
| [converter.GroupingGridToExcel([this].gridGroupingControl1, [@\"C:\\MyGGC.xls\"], Syncfusion.GridExcelConverter.[ConverterOptions].Default); ]                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                 |
| [Dim][ converter [As] Syncfusion.GroupingGridExcelConverter.GroupingGridExcelConverterControl = [New] Syncfusion.GroupingGridExcelConverter.GroupingGridExcelConverterControl()] |
|                                                                                                                                                                                                                                                                                                                 |
| [converter.GroupingGridToExcel([Me].gridGroupingControl1, [\"C:\\MyGGC.xls\"], Syncfusion.GridExcelConverter.ConverterOptions.Default);]                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can export the visible, or expanded records or groups alone by using the following code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                         |
| [converter.GroupingGridToExcel([this].gridGroupingControl1, [@\"C:\\MyGGC.xls\"], Syncfusion.GridExcelConverter.[ConverterOptions].Visible); ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                   |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [converter.GroupingGridToExcel(this.gridGroupingControl1, [\"C:\\MyGGC.xls\"], Syncfusion.GridExcelConverter.ConverterOptions.Visible);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p33} 

 

[]{#related-topics}

