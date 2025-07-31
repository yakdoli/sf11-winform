---
title: stackedarea100chart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\stackedarea100chart.md
created_at: 2025-07-03
---






#### Stacked Area 100 Chart {#stacked-area-100-chart style="tab-stops: 0pt"}

[] 

This chart type displays multiple series of data as stacked areas ensuring that the cumulative proportion of each stacked element always totals 100%. The y axis will hence always be rendered with the range 0 - 100.

[] 

{border="0"}

[] 

Figure 57: 100% Stacked Area Chart

[] 


+------------------------------+------------------------+
| Details                                               |
+------------------------------+------------------------+
| Number of Y values per point | 1                      |
+------------------------------+------------------------+
| Number of Series             | One.                   |
+------------------------------+------------------------+
| SupportMarker                | No                     |
+------------------------------+------------------------+
| Cannot be Combined with      | Any other chart types. |
+------------------------------+------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| [ChartSeries][ series1= [this].ChartWebControl1.Model.NewSeries([\"Series1\"],[ChartSeriesType].StackingArea100);] |
|                                                                                                                                                                                                                                                                          |
| [series1.Points.Add(1,20);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series1.Points.Add(2,30);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series1.Points.Add(3,10);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series1.Points.Add(4,15);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series1.Points.Add(5,25);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [this][.ChartWebControl1.Series.Add(series1);]                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [ChartSeries][ series2= [this].ChartWebControl1.Model.NewSeries([\"Series2\"],[ChartSeriesType].StackingArea100);] |
|                                                                                                                                                                                                                                                                          |
| [series2.Points.Add(1,20);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series2.Points.Add(2,10);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series2.Points.Add(3,50);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series2.Points.Add(4,15);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series2.Points.Add(5,5);]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| [this][.ChartWebControl1.Series.Add(series2);]                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [ChartSeries][ series3= [this].ChartWebControl1.Model.NewSeries([\"Series3\"],[ChartSeriesType].StackingArea100);] |
|                                                                                                                                                                                                                                                                          |
| [series3.Points.Add(1,20);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series3.Points.Add(2,40);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series3.Points.Add(3,10);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [series3.Points.Add(4,5);]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| [series3.Points.Add(5,20);]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [this][.ChartWebControl1.Series.Add(series3);]                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                |
| [Dim][ series1 [As] ChartSeries = [Me].ChartWebControl1.Model.NewSeries([\"Series1\"], ChartSeriesType.StackingArea100)] |
|                                                                                                                                                                                                                                                                                |
| [series1.Points.Add(0, 20)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series1.Points.Add(1, 30)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series1.Points.Add(2, 10)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series1.Points.Add(3, 15)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series1.Points.Add(4, 25)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [Me][.ChartWebControl1.Series.Add(series1)]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [Dim][ series2 [As] ChartSeries = [Me].ChartWebControl1.Model.NewSeries([\"Series2\"], ChartSeriesType.StackingArea100)] |
|                                                                                                                                                                                                                                                                                |
| [series2.Points.Add(0, 20)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series2.Points.Add(1, 10)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series2.Points.Add(2, 50)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series2.Points.Add(3, 15)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series2.Points.Add(4, 5)]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [Me][.ChartWebControl1.Series.Add(series2)]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [Dim][ series3 [As] ChartSeries = [Me].ChartWebControl1.Model.NewSeries([\"Series3\"], ChartSeriesType.StackingArea100)] |
|                                                                                                                                                                                                                                                                                |
| [series3.Points.Add(0, 20)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series3.Points.Add(1, 40)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series3.Points.Add(2, 10)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [series3.Points.Add(3, 5)]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| [series3.Points.Add(4, 20)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [Me][.ChartWebControl1.Series.Add(series3)]                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                             |
| Customization Options[]                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Border, DisplayShadow, DisplayText, DrawSeriesNameInDepth, ElementBorders, HighlightInterior, ImageIndex, Rotate, SeriesToolTipFormat, Spacing Between Series, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible]{.UGHyperlink} |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

See Also

[] 

{target="Stacking column"}[]{.UGHyperlink}

[]{#p51} 

[]{#related-topics}

