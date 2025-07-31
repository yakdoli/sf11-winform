---
title: howtoaddchartlabelstoscatterpoints.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtoaddchartlabelstoscatterpoints.md
created_at: 2025-07-03
---








  









### How to add chart labels to scatter points? {#how-to-add-chart-labels-to-scatter-points style="tab-stops: 0pt"}

 

The following code illustrates adding chart labels to the scatter points of the chart.

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                       |
| []                                                                                                                            |
|                                                                                                                                                       |
| [//Get the chart from the charts collection]                                                        |
|                                                                                                                                                       |
| [IChart][ chart = sheet.Charts\[0\];[]] |
|                                                                                                                                                       |
| []                                                                                                                |
|                                                                                                                                                       |
| [//Get the first series from the Series collection]                                                 |
|                                                                                                                                                       |
| [IChartSerie][ serieOne = chart.Series\[0\];]                 |
|                                                                                                                                                       |
| [          ]                                                                                                      |
|                                                                                                                                                       |
| [//Set the Series name to the Data Labels through Data Points]                                      |
|                                                                                                                                                       |
| [serieOne.DataPoints\[0\].DataLabels.IsSeriesName = [true];]                                 |
|                                                                                                                                                       |
| []                                                                                                                |
|                                                                                                                                                       |
| [//Set the Value to the Data Labels through Data Points]                                            |
|                                                                                                                                                       |
| [serieOne.DataPoints\[0\].DataLabels.IsValue = [true];[]]              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                              |
|                                                                                                                                                               |
| []                                                                                                                                    |
|                                                                                                                                                               |
| [\'Get the chart from the charts collection]                                                                |
|                                                                                                                                                               |
| [Dim][ chart [As] IChart = sheet.Charts(0)]         |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [\'Get the first series from the Series collection][]                   |
|                                                                                                                                                               |
| [Dim][ serieOne [As] IChartSerie = chart.Series(0)] |
|                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                               |
| [\'Set the Series name to the Data Labels through Data Points][]        |
|                                                                                                                                                               |
| [serieOne.DataPoints(0).DataLabels.IsSeriesName = [True]]                                            |
|                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                               |
| [\'Set the Value to the Data Labels through Data Points][]              |
|                                                                                                                                                               |
| [serieOne.DataPoints(0).DataLabels.IsValue = [True]]                                                 |
|                                                                                                                                                               |
| []                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

