---
title: rangeareachart3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\rangeareachart3.md
created_at: 2025-07-03
---






#### Range Area Chart {#range-area-chart style="tab-stops: 0pt"}

 

RangeArea chart is similar to the Area charts; the only difference is, we need to give two y values (Start & End). RangeArea chart will be rendered from the start value of the x axis(Lower bounds), to end value of the y axis(upper bounds) above, on the corresponding x axis values.

 

This chart type gives a clear look and it may be used in cases, where we have to display range of values, per single x point. For ex: if we have to display the range of temperature per day in a chart, RangeArea Chart will be the most convenient type of chart.

 

{border="0"}

Figure 61: RangeArea Chart

 

Chart Details

 


+---------------------------------------+-----------+
| Details                                           |
+---------------------------------------+-----------+
| **Number of Y values per point**      | 2         |
+---------------------------------------+-----------+
| **Maximum Number of Series         ** | Unlimited |
+---------------------------------------+-----------+
| **Minimum Number of Series         ** | 1         |
+---------------------------------------+-----------+


 

Step Area series can be added to the chart using the following code.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                        |
| [ChartSeries][ series1 = [this].chartControl1.Model.NewSeries([\"Profit Range\"], [ChartSeriesType].RangeArea);] |
|                                                                                                                                                                                                                                                                        |
| [series1.Points.Add(0, 18, 50);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [series1.Points.Add(1,20,49);]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| [series1.Points.Add(2,18 , 52);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [series1.Points.Add(3,20, 50);]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                        |
| [series1.Points.Add(4, 18.5,53);]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                        |
| [series1.Points.Add(5, 21, 51);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [series1.Points.Add(6, 17.7, 54);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [series1.Points.Add(7, 19, 52);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [this][.chartControl1.Series.Add(series1); ]                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ series1 ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries (\"][Profit Range][\", ChartSeriesType.][RangeArea[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series1.Points.Add(0, 18, 50)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series1.Points.Add(1,20,49)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series1.Points.Add(2,18 , 52)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series1.Points.Add(3,20, 50)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series1.Points.Add(4, 18.5,53)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series1.Points.Add(5, 21, 51)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series1.Points.Add(6, 17.7, 54)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series1.Points.Add(7, 19, 52)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.chartControl1.Series.Add (series1)]                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                               |
|                                                                                                                                                              |
| Customization Options                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Border[, ]DisplayShadow, DisplayText, DrawSeriesNameInDepth, ElementBorders, HighlightInterior, ImageIndex, Rotate, SeriesToolTipFormat |
|                                                                                                                                                              |
| Spacing Between Series, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels,                                                    |
|                                                                                                                                                              |
| Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p51} 

 

[]{#related-topics}

