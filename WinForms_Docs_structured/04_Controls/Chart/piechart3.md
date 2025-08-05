---
title: piechart3.md
original_path: WinForms_Docs/04_Controls/Chart/piechart3.md
created_at: 2025-08-05
---








  









### Pie Chart {#pie-chart style="tab-stops: 0pt"}

 

A Pie Chart renders y values as slices in a pie. These slices are rendered in proportion to the whole, which is simply the sum of all the y values in the series. Consequently, Pie Charts are used to visualize the proportional contribution (in terms of percentage or fraction) of categories of data to the whole data set. The x values in the data series will only be treated as nominal (categorical, qualitative) data. The Pie Chart can display only one Data Series at a time.

 

{border="0"}

 

Figure 81: Chart displaying Pie Series

 

Chart Details

 


+----------------------------------+------------------------+
| Details                                                   |
+----------------------------------+------------------------+
| **Number of Y values per point** | 1                      |
+----------------------------------+------------------------+
| **Number of Series         **    | One.                   |
+----------------------------------+------------------------+
| **Cannot be Combined with   **   | Any other chart types. |
+----------------------------------+------------------------+


 

Pie series can be added to the chart using the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [// Create chart series and add data points into it.]                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [ChartSeries series = ][this][.chartControl1.Model.NewSeries(\"Series Name\",ChartSeriesType.Pie);] |
|                                                                                                                                                                                                                                                          |
| [series.Points.Add(0, 1);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [series.Points.Add(1, 3);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [series.Points.Add(2, 4);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [// Add the series to the chart series collection.]                                                                                                                                                    |
|                                                                                                                                                                                                                                                          |
| [this][.chartControl1.Series.Add(series);]                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\' Create chart series and add data points into it.]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ series ][As][ ChartSeries =][ Me][.chartControl1.Model.NewSeries(\"Series Name\", ChartSeriesType.Pie)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series.Points.Add(0, 1)]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series.Points.Add(1, 3)]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [series.Points.Add(2, 4)]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [// Add the series to the chart series collection.]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.chartControl1.Series.Add(series)]                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                |
|                                                                                                                                                                                |
| Customization Options                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AngleOffset[, ]Border, DisplayShadow, DisplayText, DoughnutCoeficient, DrawSeriesNameInDepth, ElementBorders, ExplodedAll, ExplodedIndex, ExplosionOffset |
|                                                                                                                                                                                |
| FillMode, Gradient, HeightByAreaDepth, HeightCoeficient, HighlightInterior, InSideRadius, OptimizePiePointPositions, PieType, ShadowInterior, ShadowOffset                     |
|                                                                                                                                                                                |
| ShowTicks, VisibleAllPies, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels,                                                                   |
|                                                                                                                                                                                |
| Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible, ShowDataBindLabels                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**See Also**

 

More:





