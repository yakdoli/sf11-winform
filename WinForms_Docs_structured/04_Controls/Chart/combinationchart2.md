---
title: combinationchart2.md
original_path: WinForms_Docs/04_Controls/Chart/combinationchart2.md
created_at: 2025-08-05
---








  









### Combination Chart {#combination-chart style="tab-stops: 0pt"}

 

Combination Charts refers to the ability to display multiple data series in the same chart with each series visualized using different chart types. In Essential Chart, Chart types that are compatible with each other may be combined in the same Chart Area.

 

Typically it is a combination of a Line chart and a Column chart, sharing a common x-axis but with separate y-axes, one on either side of the chart.

 

One can change an existing chart to a combination chart by selecting the data series you want to change and then changing the chart type for that series.

 

{border="0"}

 

Figure 86: Chart displaying Line and Column Chart

 

 

Chart Details

 


+--------------------------------+-------------------------+
| Details                                                  |
+--------------------------------+-------------------------+
| **Number of Series         **  | One or more.            |
+--------------------------------+-------------------------+
| **Cannot be Combined with   ** | Pie, Bar, Polar, Radar. |
+--------------------------------+-------------------------+


 

Combination series can be added to the chart using the following code.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                               |
| [ChartSeries series = ][this][.chartControl1.Model.NewSeries (\"Series Name\",ChartSeriesType.Line);]    |
|                                                                                                                                                                                                                                                               |
| [series.Points.Add (0, 2);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [series.Points.Add (1, 1);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [series.Points.Add (2, 1);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [// Create chart series and add data points into it.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [ChartSeries series2 = ][this][.chartControl1.Model.NewSeries (\"Series Name\",ChartSeriesType.Column);] |
|                                                                                                                                                                                                                                                               |
| [series2.Points.Add (0, 1);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [series2.Points.Add (1, 3);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [series2.Points.Add (2, 4);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [// Add the series to the chart series collection.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [this][.chartControl1.Series.Add (series);]                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [this][.chartControl1.Series.Add (series2);]                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ series][ As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries (\"Series Name\", ChartSeriesType.Line)]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.Points.Add (0, 2)]                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.Points.Add (1, 1)]                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.Points.Add (2, 1)]                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\' Create chart series and add data points into it.]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ series2 ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries (\"Series Name\", ChartSeriesType.Column)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series2.Points.Add (0, 1)]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series2.Points.Add (1, 3)]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series2.Points.Add (2, 4)]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\' Add the series to the chart series collection.]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.chartControl1.Series.Add (series)]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.chartControl1.Series.Add (series2) ]                                                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                          |
| Customization Options                                                                                                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Border, DisplayShadow, DisplayText, DrawColumnSeparatingLines, ElementBorders, ImageIndex, Images, LightAngle, LightColor, PhongAlpha, Spacing Between Series, ShadowInterior ShadowOffset, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p72} 

[]{#related-topics}

