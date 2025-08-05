---
title: kagichart3.md
original_path: WinForms_Docs/04_Controls/Chart/kagichart3.md
created_at: 2025-08-05
---






#### Kagi Chart {#kagi-chart style="tab-stops: 0pt"}

 

Kagi Charts are a Japanese invention and date since the late 1870\'s, but were popularized in the western world by Steven Nison. They contain a series of connecting vertical lines where the thickness and direction of those lines depend on price. If closing prices continue to move in the direction of the prior vertical Kagi line, then that line is extended. However, if the closing price reverses by a pre-determined \"reversal\" amount, a new Kagi line is drawn in the next column in the opposite direction.

 

The penetration of a prior column\'s high or low, by the latest closing price, alters the colors of the lines. These colors depict either a bullish or bearish pattern. Use the **PriceUpColor** and **PriceDownColor** properties to specify the colors for these two patterns. The wider the columns, the stronger the pattern.

 

{border="0"}

 

Figure 75: Chart displaying Kagi Series

 

**Chart Details**

 


+----------------------------------+-----------+
| Details                                      |
+----------------------------------+-----------+
| **Number of Y values per point** | 1\.       |
+----------------------------------+-----------+
| **Number of Series         **    | One.      |
+----------------------------------+-----------+
| **Cannot be Combined with   **   | Pie, Bar. |
+----------------------------------+-----------+


 

Kagi series can be added to the chart using the following code.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [// Create chart series and add data points into it.][  ][ ]                                                     |
|                                                                                                                                                                                                                                                             |
| [ChartSeries series = ][this][.chartControl1.Model.NewSeries (\"Series Name\", ChartSeriesType.Kagi);] |
|                                                                                                                                                                                                                                                             |
| [// Arguments: X value, closing price.]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(0, 23);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(1, 27);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(2, 24.7);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(3, 23);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(4, 21);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(5, 20);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(6, 22);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(7, 24);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(8, 26);]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [series.Text = series.Name;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [series.ReversalAmount = 1.0;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [series.PriceUpColor = Color.Green;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [series.PriceDownColor = Color.Red;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [// Add the series to the chart series collection.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series.Add (series);]                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Create chart series and add data points into it.]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Dim][ series ][As ][ChartSeries = ][Me][.chartControl1.Model.NewSeries (\"Series Name\", ChartSeriesType.Kagi)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Arguments: X value, closing price.]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.Points.Add(0, 23)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.Points.Add(1, 27)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.Points.Add(2, 24.7)]                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.Points.Add(3, 23)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.Points.Add(4, 21)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.Points.Add(5, 20)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.Points.Add(6, 22)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.Points.Add(7, 24)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.Points.Add(8, 26)]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.Text = series.Name]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.ReversalAmount = 1.0]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.PriceUpColor = Color.Green]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [series.PriceDownColor = Color.Red]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Add the series to the chart series collection.]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.chartControl1.Series.Add (series)]                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

If the ReversalAmount is 0.0 instead of 1.0 which is the default value, then the Kagi chart will look like the below image.

 

{border="0"}

**** 

Figure 76: Kagi Chart with ReversalAmount set to 0.0

 

+---------------------------------------------------------------------------------------------------------------------------------+
| []                                                                  |
|                                                                                                                                 |
| Customization Options                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------+
| DisplayShadow, DisplayText, DrawSeriesNameInDepth, PriceDownColor, PriceUpColor, ReversalAmount, Rotate, Spacing Between Series |
|                                                                                                                                 |
| ShadowInterior, ShadowOffset, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels,                 |
|                                                                                                                                 |
| Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible                                                      |
+---------------------------------------------------------------------------------------------------------------------------------+

[]{#p62} 

 

[]{#related-topics}

