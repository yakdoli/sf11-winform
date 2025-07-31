---
title: features55.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\features55.md
created_at: 2025-07-03
---






##### Features {#features style="tab-stops: 0pt"}

There are three options for exporting a Grid control:

 

[·      ]Converting the entire content of a grid

[·      ]Converting a selected content of the grid

[·      ]Pass the Excel Engine

[] 

###### 4.1.9.1.1.1 Entire Content {#entire-content style="tab-stops: 0pt"}

You can convert the entire content of a GridData control to an Excel Spreadsheet. You can also avail the option for specifying the version of the Excel file using the ExcelVersion enum. The version can be one of the following:

 

[·      ]ExcelVersion.Excel97to2003 

[·      ]ExcelVersion.Excel2007

 

The following code illustrates the conversion of the entire Grid content to an Excel Spreadsheet:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                              |
|                                                                                                                                                                         |
| []                                                                                                                     |
|                                                                                                                                                                         |
| [gridControl.Model.ExportToExcel([@\"Sample.xls\"], [ExcelVersion].Excel97to2003);] |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [(or)]                                                                                                                              |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [gridControl.Model.ExportToExcel([@\"Sample.xlsx\"], [ExcelVersion].Excel2007);]    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 125: Grid to be exported

***[]*** 

{border="0"}

Figure 126: Exported Grid control content in Excel Spreadsheet

***[]*** 

 

The images above show how the entire content of the Grid control is exported to an Excel spreadsheet.

 

###### 4.1.9.1.1.2 Selected Content {#selected-content style="tab-stops: 0pt"}

You can convert a selected content of the grid to the specified range in an Excel spreadsheet. It will be very useful, when you have some data like picture, chart, etc., in your spreadsheet and you want to fill a particular range, for example-the remaining part of the spreadsheet using the Grid cell data.

 

Use-Case Scenario

Consider that you have a chart in a spreadsheet in the range \[A1:I19\] and you wish to populate a part of the Spreadsheet starting from E21, with the selected cell data of Grid control. You can use the following code, to achieve the scenario above mentioned:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                           |
|                                                                                                                                                                                                      |
| []                                                                                                                                                  |
|                                                                                                                                                                                                      |
| [ExcelEngine][ excelEngine = [new] [ExcelEngine]();]            |
|                                                                                                                                                                                                      |
| [IApplication][ application = excelEngine.Excel;]                                                            |
|                                                                                                                                                                                                      |
| [IWorkbook][ myWorkbook = excelEngine.Excel.Workbooks.Add();]                                                |
|                                                                                                                                                                                                      |
| [IWorksheet][ mySheet = myWorkbook.Worksheets\[1\];]                                                         |
|                                                                                                                                                                                                      |
| [IChart][ chartShape = mySheet.Charts.Add();]                                                                |
|                                                                                                                                                                                                      |
| [IChartSeries][ series1 = chartShape.Series.Add();]                                                          |
|                                                                                                                                                                                                      |
| [series1.SerieType = [ExcelChartType].Column_Clustered;]                                                                                 |
|                                                                                                                                                                                                      |
| [chartShape.ChartTitle = [\"Column_Clustered\"];]                                                                                        |
|                                                                                                                                                                                                      |
| [series1.Values = mySheet.Range\[[\"B1:B5\"]\];]                                                                                         |
|                                                                                                                                                                                                      |
| [series1.CategoryLabels = mySheet.Range\[[\"A1:A5\"]\];]                                                                                 |
|                                                                                                                                                                                                      |
| [Random][ r = [new] [Random]();]                                |
|                                                                                                                                                                                                      |
| [for][ ([int] i = 1; i \<= 4; i++)]                                                        |
|                                                                                                                                                                                                      |
| [{]                                                                                                                                                              |
|                                                                                                                                                                                                      |
| [    mySheet.Range\[i, 1\].Number = i;]                                                                                                                          |
|                                                                                                                                                                                                      |
| [    mySheet.Range\[i, 2\].Number = r.Next(4000, 6000);]                                                                                                         |
|                                                                                                                                                                                                      |
| [}]                                                                                                                                                              |
|                                                                                                                                                                                                      |
| [for][ ([int] i = 1; i \<= 4; i++)]                                                        |
|                                                                                                                                                                                                      |
| [{]                                                                                                                                                              |
|                                                                                                                                                                                                      |
| [    mySheet.Range\[i + 5, 1\].Number = i;]                                                                                                                      |
|                                                                                                                                                                                                      |
| [    mySheet.Range\[i + 5, 2\].Number = r.Next(4000, 6000);]                                                                                                     |
|                                                                                                                                                                                                      |
| [}]                                                                                                                                                              |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [IRange][ excelRange = mySheet.Range\[21, 5\];]                                                              |
|                                                                                                                                                                                                      |
| [GridRangeInfoList][ rangeList = gridControl.Model.SelectedRanges;]                                          |
|                                                                                                                                                                                                      |
| [GridRangeInfo][ range = rangeList\[0\];]                                                                    |
|                                                                                                                                                                                                      |
| [gridControl.Model.ExportToExcel(range, mySheet, excelRange, [@\"Sample2.xls\"], [ExcelVersion].Excel97to2003);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

***[]*** 

{border="0"}

Figure 127: Grid showing the selected range to be exported

***[]*** 

{border="0"}

Figure 128: Exported Grid control in Excel Spreadsheet

 

The above images shows how a part of the Grid control is exported to a specific range on an Excel Spreadsheet.

 

###### 4.1.9.1.1.3 Using the Excel Engine (XlsIO) {#using-the-excel-engine-xlsio style="tab-stops: 0pt"}

You can also pass the Excel Engine with the worksheet number, as illustrated by the code below:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                   |
| [ExcelEngine][ excelEngine = [new] [ExcelEngine]();]                         |
|                                                                                                                                                                                                                   |
| [IApplication][ application = excelEngine.Excel;]                                                                         |
|                                                                                                                                                                                                                   |
| [IWorkbook][ myWorkbook = excelEngine.Excel.Workbooks.Add();]                                                             |
|                                                                                                                                                                                                                   |
| [IWorksheet][  mySheet = myWorkbook.Worksheets\[0\];]                                                                     |
|                                                                                                                                                                                                                   |
| [gridControl.Model.ExportToExcel(range, excelEngine, 0, mySheet.Range\[5,5\], [@\"Sample.xlsx\"], [ExcelVersion].Excel2007);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 129: GridData control

[] 

{border="0"}

Figure 130: Exported Grid control in Excel Spreadsheet

[] 


{border="0"}Note: For more details, refer the following browser sample:


 

***\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\ExcelExport\\GridControl Excel Export Demo***

 

 

[]{#related-topics}

