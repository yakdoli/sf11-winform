---
title: editcharts.md
original_path: WinForms_Docs/04_Controls/Chart/editcharts.md
created_at: 2025-08-05
---






#### Edit Charts {#edit-charts style="tab-stops: 0pt"}

**[]** 

The properties of the Chart in an existing workbook can be opened and edited by using Essential XlsIO. Following code example illustrates how an existing workbook with a chart is opened, and how the chart properties are modified.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// Opening the Existing Worksheet from a Workbook.]                                                                       |
|                                                                                                                                                                              |
| [IWorkbook workbook = application.Workbooks.Open(@\"..\\..\\..\\..\\..\\Data\\EditChartsTemplate.xls\");]                  |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// The first worksheet object in the worksheets collection is accessed.]                                                  |
|                                                                                                                                                                              |
| [IWorksheet sheet = workbook.Worksheets\[0\];]                                                                             |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// Editing the Existing Chart.]                                                                                           |
|                                                                                                                                                                              |
| [IChart chart = sheet.Charts\[0\];]                                                                                        |
|                                                                                                                                                                              |
| [chart.ChartTitle = \"Texas Books Unit Sales\";]                                                                           |
|                                                                                                                                                                              |
| [chart.PrimaryCategoryAxis.Title = \"City\";]                                                                              |
|                                                                                                                                                                              |
| [chart.PrimaryValueAxis.Title = \"Sales (in Dollars)\";]                                                                   |
|                                                                                                                                                                              |
| [chart.Legend.Position = ExcelLegendPosition.Top;]                                                                         |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// Setting the Series Names in a Legend.]                                                                                 |
|                                                                                                                                                                              |
| [IChartSerie serieOne = chart.Series\[0\];]                                                                                |
|                                                                                                                                                                              |
| [serieOne.Name = \"Jan\";]                                                                                                 |
|                                                                                                                                                                              |
| [IChartSerie serietwo = chart.Series\[1\];]                                                                                |
|                                                                                                                                                                              |
| [serietwo.Name = \"Feb\";]                                                                                                 |
|                                                                                                                                                                              |
| [IChartSerie seriethree = chart.Series\[2\];]                                                                              |
|                                                                                                                                                                              |
| [seriethree.Name = \"March\";]                                                                                             |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// Setting the Title Area text.]                                                                                          |
|                                                                                                                                                                              |
| [IChartTextArea Area = chart.ChartTitleArea;]                                                                              |
|                                                                                                                                                                              |
| [Area.Bold = ][true][;] |
|                                                                                                                                                                              |
| [Area.Underline = ExcelUnderline.Single;]                                                                                  |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// Setting the Minimum and Maximum Value for Value Axis.]                                                                 |
|                                                                                                                                                                              |
| [chart.PrimaryValueAxis.MinimumValue = 10;]                                                                                |
|                                                                                                                                                                              |
| [chart.PrimaryValueAxis.MaximumValue = 100;]                                                                               |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// Setting the Height of the chart.]                                                                                      |
|                                                                                                                                                                              |
| [chart.Height = 1/10;]                                                                                                     |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// Setting the Width of the chart.]                                                                                       |
|                                                                                                                                                                              |
| [chart.Width = 1/72;]                                                                                                      |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// Saving the workbook to disk.]                                                                                          |
|                                                                                                                                                                              |
| [workbook.SaveAs(\"Sample.xls\");]                                                                                         |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// Closing the workbook.]                                                                                                 |
|                                                                                                                                                                              |
| [workbook.Close();][ ]                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                            |
| [\' Opening the Existing Worksheet from a Workbook.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ workbook ][As][ IWorkbook = application.Workbooks.Open(\"..\\..\\..\\..\\..\\Data\\EditChartsTemplate.xls\")] |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [\' The first worksheet object in the worksheets collection is accessed.]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ sheet ][As][ IWorksheet = workbook.Worksheets(0)]                                                             |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [\' Editing the Existing Chart.]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ chart ][As][ IChart = sheet.Charts(0)]                                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| [chart.ChartTitle = \"Texas Books Unit Sales\"]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                            |
| [chart.PrimaryCategoryAxis.Title = \"City\"]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                            |
| [chart.PrimaryValueAxis.Title = \"Sales (in Dollars)\"]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                            |
| [chart.Legend.Position = ExcelLegendPosition.Top]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| [\' Setting the Series Names in a Legend.]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ serieOne ][As][ IChartSerie = chart.Series(0)]                                                                |
|                                                                                                                                                                                                                                                                                                                            |
| [serieOne.Name = \"Jan\"]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ serietwo ][As][ IChartSerie = chart.Series(1)]                                                                |
|                                                                                                                                                                                                                                                                                                                            |
| [serietwo.Name = \"Feb\"]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ seriethree ][As][ IChartSerie = chart.Series(2)]                                                              |
|                                                                                                                                                                                                                                                                                                                            |
| [seriethree.Name = \"March\"]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [\' Setting the Title Area text.]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| [Dim][ Area ][As][ IChartTextArea = chart.ChartTitleArea]                                                            |
|                                                                                                                                                                                                                                                                                                                            |
| [Area.Bold = ][True]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                            |
| [Area.Underline = ExcelUnderline.Single]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [\' Setting the Minimum and Maximum Value for the Value Axis.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                            |
| [chart.PrimaryValueAxis.MinimumValue = 10]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                            |
| [chart.PrimaryValueAxis.MaximumValue = 100]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [\' Setting the Height of the chart.]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                            |
| [chart.Height = 1 / 10]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [\' Setting the Width of the chart.]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [chart.Width = 1 / 72]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [\' Saving the workbook to disk.]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| [workbook.SaveAs(\"Sample.xls\")]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [\' Closing the workbook.]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                            |
| [workbook.Close()]                                                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

More:









