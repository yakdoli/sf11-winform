---
title: stackingbarchart3.md
original_path: WinForms_Docs/04_Controls/Chart/stackingbarchart3.md
created_at: 2025-08-05
---






#### Stacking Bar Chart {#stacking-bar-chart style="tab-stops: 0pt"}

 

Stacking Bar Charts are similar to regular bar charts except that the Y values stack on top of each other in the specified series order. This helps visualizing the relationship of parts to the whole.

 

The following image shows a sample Stacking Bar Chart.

 

{border="0"}

 

Figure 47: Chart displaying Stacking Bar Series

 

Chart Details

 


+----------------------------------+--------------------------------------------------------+
| Details                                                                                   |
+----------------------------------+--------------------------------------------------------+
| **Number of Y values per point** | 1                                                      |
+----------------------------------+--------------------------------------------------------+
| **Number of Series         **    | Two or More (Single series is rendered just as a bar). |
+----------------------------------+--------------------------------------------------------+
| **Cannot be Combined with   **   | Any chart type except Bar and Stacked Bar charts.      |
+----------------------------------+--------------------------------------------------------+


 

Stacking bar series can be added to the chart using the following code.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [// Create chart series and add data point into it.]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [ChartSeries series = ][this][.chartControl1.Model.NewSeries(\"Series Name\",ChartSeriesType.StackingBar);]  |
|                                                                                                                                                                                                                                                                   |
| [series.Points.Add(0, 1);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
| [series.Points.Add(1, 3);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
| [series.Points.Add(2, 4);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                   |
| [ChartSeries series2 = ][this][.chartControl1.Model.NewSeries(\"Series Name\",ChartSeriesType.StackingBar);] |
|                                                                                                                                                                                                                                                                   |
| [series2.Points.Add(0, 2);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [series2.Points.Add(1, 1);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [series2.Points.Add(2, 1);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                   |
| [// Add the series to the chart series collection.]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                   |
| [this][.chartControl1.Series.Add(series);]                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [this][.chartControl1.Series.Add(series2);]                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\' Create chart series and add data points into it.]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ series ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries(\"Series Name\", ChartSeriesType.StackingBar)]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [series.Points.Add(0, 1)]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [series.Points.Add(1, 3)]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [series.Points.Add(2, 4)]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ series2 ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries(\"Series Name\", ChartSeriesType.StackingBar)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [series2.Points.Add(0, 2)]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [series2.Points.Add(1, 1)]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [series2.Points.Add(2, 1)]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\' Add the series to the chart series collection.]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Me][.chartControl1.Series.Add(series)]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Me][.chartControl1.Series.Add(series2)]                                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                  |
| Customization Options                                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Border[, ]ColumnDrawMode, DisplayText, DrawSeriesNameInDepth, ElementBorders, HighlightInterior, ImageIndex, Images                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| LightAngle, LightColor, Rotate, Spacing, Spacing Between Series, ShadingMode, ShadowInterior, ShadowOffset, ZOrder, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

See Also

 

[Stacking Area Chart]{.UGHyperlink}[,]{.UGHyperlink} [Stacking Column Chart]{.UGHyperlink}[]

 

[]{#p35} 

[]{#related-topics}

