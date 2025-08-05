---
title: exportingtoexcel1.md
original_path: WinForms_Docs/99_Uncategorized/exportingtoexcel1.md
created_at: 2025-08-05
---








  









### Exporting to Excel {#exporting-to-excel style="tab-stops: 0pt"}

 

Essential Chart data can be exported into an Excel document and an Excel chart can be created to use the above data using **Essential XlsIO**. Though there is no built-in support for this, this can be easily implemented with a very intuitive XlsIO API.

 

{border="0"}

 

Figure 352: Essential Chart translated into an Excel Chart by using Essential XlsIO

 

Given below are the steps that will guide you through this process.

 

1.   Add the Syncfusion.XLsIO.Base and Syncfusion.XLsIO.Windows assemblies.

 

2.   Add the namespace Syncfusion.XLsIO in your form.

 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| **[]**                                                                       |
|                                                                                                                                |
| [using][ Syncfusion.XlsIO;] |
+--------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]** |
|                                                                                                                                                                            |
| **[]**                                                                                                                   |
|                                                                                                                                                                            |
| [Imports][ Syncfusion.XlsIO]                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Add the code snippet that is given below in your form.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [string][ exportFileName = Application.StartupPath+\"\\\\chartexport\" + \".xls\";                                    ]                        |
|                                                                                                                                                                                                                                                   |
| [                ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// A new workbook with a worksheet should be created.]                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [IWorkbook chartBook = ExcelUtils.CreateWorkbook(1);]                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [IWorksheet sheet = chartBook.Worksheets\[0\];]                                                                                                                                                 |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [   // Fill the worksheet with chart data.]                                                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [for][(][int][ i=1;i\<=5;i++)]              |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [sheet.Range\[i,1\].Number = ][this][.chartControl1.Series\[0\].Points\[i-1\].X;]            |
|                                                                                                                                                                                                                                                   |
| [sheet.Range\[i,2\].Number = ][this][.chartControl1.Series\[0\].Points\[i-1\].YValues\[0\];] |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [  // Create a chart worksheet.]                                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [IChart chart = chartBook.Charts.Add(\"Essential Chart\");]                                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [   // Specify the title of the Chart.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [chart.ChartTitle = \"Essential Chart\";]                                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// Initialize a new series instance and add it to the series collection of the chart.]                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [IChartSerie series = chart.Series.Add();]                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [ // Specify the chart type of the series.]                                                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [series.SerieType = ExcelChartType.Column_Clustered;]                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// Specify the name of the series. This will be displayed as the text of the legend.]                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [series.Name = \"Sample Series\";]                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [                 ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [ // Specify the value ranges for the series.]                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [series.Values = sheet.Range\[\"B1:B5\"\];]                                                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [                                        ]                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [ // Specify the Category labels for the series.]                                                                                                                                               |
|                                                                                                                                                                                                                                                   |
| [series.CategoryLabels = sheet.Range\[\"A1:A5\"\];]                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [                ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [ // Make the chart as active sheet.]                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [chart.Activate();]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [  // Save the Chart book.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| [chartBook.SaveAs(exportFileName);]                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [chartBook.Close();]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [ExcelUtils.Close();]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [ // Launches the file.]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [System.Diagnostics.Process.Start(exportFileName);]                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ exportFileName ][As String][ = Application.StartupPath & \"\\chartexport\" & \".xls\"]                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [  \' A new workbook with a worksheet should be created.]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ chartBook ][As][ IWorkbook = ExcelUtils.CreateWorkbook(1)]                                                                        |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ sheet ][As][ IWorksheet = chartBook.Worksheets(0)]                                                                                |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [ \' Fill the worksheet with chart data.]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                |
| [For][ i ][As Integer][ = 1 ][To][ 5] |
|                                                                                                                                                                                                                                                                                                                                                |
| [sheet.Range(i,1).Number = ][Me][.chartControl1.Series(0).Points(i-1).X]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                |
| [sheet.Range(i,2).Number = ][Me][.chartControl1.Series(0).Points(i-1).YValues(0)]                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [Next][ i]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [\' Create a chart worksheet.]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ chart ][As][ IChart = chartBook.Charts.Add(\"Essential Chart\")]                                                                  |
|                                                                                                                                                                                                                                                                                                                                                |
| [\' Specify the title of the Chart.]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [chart.ChartTitle = \"Essential Chart\"]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [ \' Initialize a new series instance and add it to the series collection of the chart.]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ series ][As][ IChartSerie = chart.Series.Add()]                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [    \' Specify the chart type of the series.]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                |
| [series.SerieType = ExcelChartType.Column_Clustered]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [ \' Specify the name of the series. This will be displayed as the text of the legend.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                |
| [series.Name = \"Sample Series\"]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                |
| [                        ][\' Specify the value ranges for the series.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                |
| [series.Values = sheet.Range(\"B1:B5\")]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                |
| [\' Specify the Category labels for the series.]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| [series.CategoryLabels = sheet.Range(\"A1:A5\")]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [\' Make the chart as active sheet.]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [chart.Activate()]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [ \' Save the Chart book.]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                |
| [chartBook.SaveAs(exportFileName)]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [chartBook.Close()]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                |
| [ExcelUtils.Close()]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [                        ]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                |
| [ \' Launches the file. ]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                |
| [System.Diagnostics.Process.Start(exportFileName)]                                                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Sample

 

A sample demonstrating the above functionality is available in our installation at the following location:

 

\"[My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Chart.Windows\\Samples\\2.0\\Export\\Chart Export Data]{.UGHyperlink}\"

[]{#p256} 

[]{#related-topics}

