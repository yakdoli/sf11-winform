---
title: areachart3.md
original_path: WinForms_Docs/04_Controls/Chart/areachart3.md
created_at: 2025-08-05
---






#### Area Chart {#area-chart style="tab-stops: 0pt"}

 

The Area Chart connects the y points using straight lines and forms an area covered by the above lines and x-axis. This area is then shaded with a specified color or gradient.

 

Multiple series can be plotted on the same chart and alpha-blended interior color can be used on the exterior chart to make the interior chart show through.

 

The following image shows a multi series Area Chart.

 

{border="0"}

 

Figure 56: Chart displaying Area Series in 3D View

 

**Chart Details**

 


+----------------------------------+--------------------------------------------+
| **Details**                                                                   |
+----------------------------------+--------------------------------------------+
| **Number of Y values per point** | 1                                          |
+----------------------------------+--------------------------------------------+
| **Number of Series         **    | One or More                                |
+----------------------------------+--------------------------------------------+
| **Cannot be Combined with   **   | Pie, Bar, Polar, Radar, Gantt, Stacked Bar |
+----------------------------------+--------------------------------------------+


 

An Area series can be added to the chart using the following code.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                           |
| [// Create a chart series and add data points into it.]                                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [ChartSeries series = ][this][.chartControl1.Model.NewSeries(\"Series Name\",ChartSeriesType.Area);] |
|                                                                                                                                                                                                                                                           |
| [series.Points.Add(0, 4.5);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
| [series.Points.Add(1, 3);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| [series.Points.Add(2, 4);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| [series.Points.Add(3, 3);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [// Add the series to the chart series collection.]                                                                                                                                                     |
|                                                                                                                                                                                                                                                           |
| [this][.chartControl1.Series.Add(series);]                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\' Create a chart series and add data points into it.]                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Dim][ series ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries(\"Series Name\", ChartSeriesType.Area)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [ChartSeries series = ][this][.chartControl1.Model.NewSeries(\"Series Name\",ChartSeriesType.Area);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [series.Points.Add(0, 4.5)]                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [series.Points.Add(1, 3)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [series.Points.Add(2, 4)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [series.Points.Add(3, 3)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\' Add the series to the chart series collection.]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Me][.chartControl1.Series.Add(series)]                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                              |
|                                                                                                                                                              |
| Customization Options                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Border[, ]DisplayShadow, DisplayText, DrawSeriesNameInDepth, ElementBorders, HighlightInterior, ImageIndex, Rotate, SeriesToolTipFormat |
|                                                                                                                                                              |
| Spacing Between Series, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels,                                                    |
|                                                                                                                                                              |
| Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p46} 

[]{#related-topics}

