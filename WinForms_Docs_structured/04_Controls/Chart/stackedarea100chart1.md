---
title: stackedarea100chart1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\stackedarea100chart1.md
created_at: 2025-07-03
---






#### StackedArea100 Chart {#stackedarea100-chart style="tab-stops: 0pt"}

 

This chart type displays multiple series of data as stacked areas ensuring that the cumulative proportion of each stacked element always totals 100 percent. The y axis will hence always be rendered with the range 0 - 100.

 

{border="0"}

 

Figure 59: A 100 percent StackedArea Chart

 


+----------------------------------+------------------------+
| Details                                                   |
+----------------------------------+------------------------+
| **Number of Y values per point** | 1                      |
+----------------------------------+------------------------+
| **Number of Series         **    | One.                   |
+----------------------------------+------------------------+
| **SupportMarker**                | No                     |
+----------------------------------+------------------------+
| **Cannot be Combined with   **   | Any other chart types. |
+----------------------------------+------------------------+


 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [ChartSeries][ series1=chartControl1.Model.NewSeries([\"Series1\"],[ChartSeriesType].StackingArea100);] |
|                                                                                                                                                                                                                                          |
| [series1.Points.Add(1,20);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series1.Points.Add(2,30);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series1.Points.Add(3,10);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series1.Points.Add(4,15);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series1.Points.Add(5,25);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [this][.chartControl1.Series.Add(series1);]                                                                                                         |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [ChartSeries][ series2=chartControl1.Model.NewSeries([\"Series2\"],[ChartSeriesType].StackingArea100);] |
|                                                                                                                                                                                                                                          |
| [series2.Points.Add(1,20);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series2.Points.Add(2,10);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series2.Points.Add(3,50);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series2.Points.Add(4,15);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series2.Points.Add(5,5);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| [this][.chartControl1.Series.Add(series2);]                                                                                                         |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [ChartSeries][ series3=chartControl1.Model.NewSeries([\"Series3\"],[ChartSeriesType].StackingArea100);] |
|                                                                                                                                                                                                                                          |
| [series3.Points.Add(1,20);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series3.Points.Add(2,40);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series3.Points.Add(3,10);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [series3.Points.Add(4,5);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| [series3.Points.Add(5,20);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [this][.chartControl1.Series.Add(series3);]                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [Dim][ series1 [As] ChartSeries = chartControl1.Model.NewSeries([\"Series1\"], ChartSeriesType.StackingArea100)] |
|                                                                                                                                                                                                                                                   |
| [series1.Points.Add(0, 20)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series1.Points.Add(1, 30)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series1.Points.Add(2, 10)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series1.Points.Add(3, 15)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series1.Points.Add(4, 25)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [Me][.chartControl1.Series.Add(series1)]                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [Dim][ series2 [As] ChartSeries = chartControl1.Model.NewSeries([\"Series2\"], ChartSeriesType.StackingArea100)] |
|                                                                                                                                                                                                                                                   |
| [series2.Points.Add(0, 20)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series2.Points.Add(1, 10)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series2.Points.Add(2, 50)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series2.Points.Add(3, 15)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series2.Points.Add(4, 5)]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [Me][.chartControl1.Series.Add(series2)]                                                                                                                     |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [Dim][ series3 [As] ChartSeries = chartControl1.Model.NewSeries([\"Series3\"], ChartSeriesType.StackingArea100)] |
|                                                                                                                                                                                                                                                   |
| [series3.Points.Add(0, 20)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series3.Points.Add(1, 40)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series3.Points.Add(2, 10)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [series3.Points.Add(3, 5)]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [series3.Points.Add(4, 20)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [Me][.chartControl1.Series.Add(series3)]                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                 |
|                                                                                                                                                |
| Customization Options                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------+
| Border, DisplayText, DrawSeriesNameInDepth, ElementBorders, HighlightInterior, ImageIndex, Rotate, SeriesToolTipFormat, Spacing Between Series |
|                                                                                                                                                |
| , ZOrder, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels,                                                    |
|                                                                                                                                                |
| Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+

 

**See Also**

 

[StackedBar100 Chart]{.UGHyperlink}, [StackedColumn100Chart]{.UGHyperlink}[]

 

[]{#p49} 

 

[]{#related-topics}

