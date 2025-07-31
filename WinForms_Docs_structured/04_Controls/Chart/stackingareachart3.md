---
title: stackingareachart3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\stackingareachart3.md
created_at: 2025-07-03
---






#### Stacking Area Chart {#stacking-area-chart style="tab-stops: 0pt"}

 

Stacking Area Charts are similar to regular area charts except that the y values stack on top of each other in the specified series order. This helps visualize the relationship of parts to the whole.

 

The following image shows a sample Stacking Area Chart.

 

{border="0"}

 

Figure 58: Chart displaying Stacking Area Series in 3D

 

Chart Details

 


+-------------------------------------+------------------------------------------------+
|                                                                                      |
|                                                                                      |
| Details                                                                              |
+-------------------------------------+------------------------------------------------+
|                                     |                                                |
|                                     |                                                |
| **Number of Y values per point**    | 1                                              |
+-------------------------------------+------------------------------------------------+
|                                     |                                                |
|                                     |                                                |
| **Number of Series         **       | One or More                                    |
+-------------------------------------+------------------------------------------------+
|                                     |                                                |
|                                     |                                                |
| **Cannot be Combined with   **      | Pie, Bar, Stacked Bar charts, Polar and Radar. |
+-------------------------------------+------------------------------------------------+


 

Stacking area series can be added to the chart using the following code.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [// Create chart series and add data points into it.]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [ChartSeries series = ][this][.chartControl1.Model.NewSeries(\"Series Name\",ChartSeriesType.StackingArea);]  |
|                                                                                                                                                                                                                                                                    |
| [series.Points.Add(0, 1);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [series.Points.Add(1, 3);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [series.Points.Add(2, 4);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [ChartSeries series2 = ][this][.chartControl1.Model.NewSeries(\"Series Name\",ChartSeriesType.StackingArea);] |
|                                                                                                                                                                                                                                                                    |
| [series2.Points.Add(0, 2);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [series2.Points.Add(1, 1);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [series2.Points.Add(2, 1);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [// Add the series to the chart series collection.]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                    |
| [this][.chartControl1.Series.Add(series);]                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [this][.chartControl1.Series.Add(series2);]                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' Create chart series and add data points into it.]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ series ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries(\"Series Name\", ChartSeriesType.StackingArea)]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [series.Points.Add(0, 1)]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [series.Points.Add(1, 3)]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [series.Points.Add(2, 4)]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ series2 ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries(\"Series Name\", ChartSeriesType.StackingArea)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [series2.Points.Add(0, 2)]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [series2.Points.Add(1, 1)]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [series2.Points.Add(2, 1)]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\' Add the series to the chart series collection.]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Me][.chartControl1.Series.Add(series)]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Me][.chartControl1.Series.Add(series2)]                                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                             |
| Customization Options                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Border, DisplayText, DrawSeriesNameInDepth, ElementBorders, HighlightInterior, ImageIndex, Rotate, SeriesToolTipFormat, Spacing Between Series                                                                                                                                              |
|                                                                                                                                                                                                                                                                                             |
| , [ZOrder], [FancyToolTip], [Font], [Interior], [LegendItem], [Name], [PointsToolTipFormat], [SmartLabels], |
|                                                                                                                                                                                                                                                                                             |
| [Summary], [Text], [TextColor], [TextFormat], [TextOffset], [TextOrientation], [Visible]                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

See Also

 

[Stacking Bar Chart]{.UGHyperlink}, [Stacking Column Chart]{.UGHyperlink}[]

[[]]{.UGHyperlink} 

[]{#p48} 

 

[]{#related-topics}

