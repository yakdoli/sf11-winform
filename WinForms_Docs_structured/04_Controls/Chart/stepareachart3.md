---
title: stepareachart3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\stepareachart3.md
created_at: 2025-07-03
---






#### Step Area Chart {#step-area-chart style="tab-stops: 0pt"}

 

Step Area Charts are similar to regular area chart except that instead of a straight line tracing the shortest path between points, the values are connected by continuous vertical and horizontal lines forming a step like progression.

 

The following image shows a sample Step Area Chart.

 

{border="0"}

                                                                             

Figure 60: Chart displaying Step Area Series

 

Chart Details

 


+----------------------------------+------------------------------------------------+
| Details                                                                           |
+----------------------------------+------------------------------------------------+
| **Number of Y values per point** | 1                                              |
+----------------------------------+------------------------------------------------+
| **Number of Series         **    | One or More.                                   |
+----------------------------------+------------------------------------------------+
| **Cannot be Combined with   **   | Pie, Bar, Stacked Bar charts, Polar and Radar. |
+----------------------------------+------------------------------------------------+


 

Step Area series can be added to the chart using the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [// Create chart series and add data points into it.]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [ChartSeries series = ][this][.chartControl1.Model.NewSeries (\"Series Name\",ChartSeriesType.StepArea);] |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(0, 1);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(1, 3);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(2, 4);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(3, 2);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(4, 3);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [// Add the series to the chart series collection.]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [this][.chartControl1.Series.Add (series);]                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Create chart series and add data points into it.]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ series ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries (\"Series Name\", ChartSeriesType.StepArea)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series.Points.Add(0, 1)]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series.Points.Add(1, 3)]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series.Points.Add(2, 4)]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series.Points.Add(3, 2)]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series.Points.Add(4, 3)]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Add the series to the chart series collection.]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.chartControl1.Series.Add (series)]                                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                              |
| Customization Options                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Border, DisplayText, DrawSeriesNameInDepth, ElementBorders, ImageIndex, Rotate, SeriesToolTipFormat, Spacing Between Series, StepItem.Inverted, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p50} 

 

[]{#related-topics}

