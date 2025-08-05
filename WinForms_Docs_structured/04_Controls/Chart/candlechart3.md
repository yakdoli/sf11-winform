---
title: candlechart3.md
original_path: WinForms_Docs/04_Controls/Chart/candlechart3.md
created_at: 2025-08-05
---






#### Candle Chart {#candle-chart style="tab-stops: 0pt"}

 

A Candle chart displays stock information using the High, Low, Open and Close values. The Hi and Lo values are represented by the wick of a candle. The candle represents open and close values.

 

The following image shows a CandleChart displaying a single series.

 

{border="0"}

 

Figure 72: Chart displaying Candle Series

 

Chart Details

 


+----------------------------------+----------------------------------------------+
| Details                                                                         |
+----------------------------------+----------------------------------------------+
| **Number of Y values per point** | 4 (High, Low , Open and Close respectively). |
+----------------------------------+----------------------------------------------+
| **Number of Series         **    | One or More.                                 |
+----------------------------------+----------------------------------------------+
| **Cannot be Combined with   **   | Pie, Bar, Stacked Bar charts, Polar, Radar.  |
+----------------------------------+----------------------------------------------+


 

Candle series can be added to the chart using the following code.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [// Create chart series and add data point into it.]**[ ]**[ ]                                        |
|                                                                                                                                                                                                                                                             |
| [ChartSeries series = ][this][.chartControl1.Model.NewSeries(\"Series Name\",ChartSeriesType.Candle);] |
|                                                                                                                                                                                                                                                             |
| [// Arguments: X value, High, Low, Open, Close]                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(0, 5, 1, 3, 4);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(1, 8, 7, 4, 7);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(2, 8, 4, 5, 6);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [// Add the series to the chart series collection.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series.Add(series);]                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Create chart series and add data point into it.]**[ ]**[ ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ series ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries(\"Series Name\", ChartSeriesType.Candle)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Arguments: X value, High, Low, Open, Close]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [series.Points.Add(0, 5, 1, 3, 4)]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [series.Points.Add(1, 8, 7, 4, 7)]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [series.Points.Add(2, 8, 4, 5, 6)]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Add the series to the chart series collection.]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.chartControl1.Series.Add(series)]                                                                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                              |
|                                                                                                                              |
| Customization Options                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------+
| Border, DisplayShadow, DisplayText, DrawSeriesNameInDepth, ImageIndex, Images, PhongAlpha, Rotate, Spacing Between Series    |
|                                                                                                                              |
| ShadingMode, ShadowInterior, ShadowOffset, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels, |
|                                                                                                                              |
| Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible                                                   |
+------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p59} 

 

[]{#related-topics}

