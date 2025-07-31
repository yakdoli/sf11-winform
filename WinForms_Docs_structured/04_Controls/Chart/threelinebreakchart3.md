---
title: threelinebreakchart3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\threelinebreakchart3.md
created_at: 2025-07-03
---






#### Three Line Break Chart {#three-line-break-chart style="tab-stops: 0pt"}

 

Three Line Break Chart is similar in concept to point and figure charts. The Three Line Break charting method is so-named because of the number of lines typically used. It displays a series of vertical boxes (\"lines\") that are based on changes in prices. It ignores the passage of time.

 

The three-line break chart looks like a series of rising and falling lines of varying heights. Each new line, like the X\'s and O\'s of a point and figure chart, occupies a new column. Based on closing prices (or highs and lows), a new rising line is drawn if the previous high is exceeded and a new falling line is drawn if the price hits a new low. Change in price trends are highlighted by changing colors. Use the **PriceUpColor** to indicate bullish trend and **PriceDownColor** to indicate bearish trend.

 

The **ReversalAmount** specifies the threshold amount by which the price should change to begin rendering a new vertical box in the appropriate direction.

 

{border="0"}

 

Figure 79: Chart displaying Three Line Break Series

 

**Chart Details**

 


+-------------------------------------+-------------------------------------+
|                                                                           |
|                                                                           |
| Details                                                                   |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Number of Y values per point**    | 1                                   |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Number of Series         **       | One                                 |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Cannot be Combined with   **      | Pie, Bar                            |
+-------------------------------------+-------------------------------------+


 

Three Line Break series can be added to the chart using the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                      |
| [// Create chart series and add data points into it.][  ][ ]                                                              |
|                                                                                                                                                                                                                                                                      |
| [ChartSeries series = ][this][.chartControl1.Model.NewSeries (\"Series Name\",ChartSeriesType.ThreeLineBreak);] |
|                                                                                                                                                                                                                                                                      |
| [series.Points.Add (0, 1);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                      |
| [series.Points.Add (1, 3);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                      |
| [series.Points.Add (2, 4);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [// Add series to the chart series collection.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                      |
| [this][.chartControl1.Series.Add (series);]                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\' Create chart series and add data points into it.][ ][  ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Dim][ series ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries (\"Series Name\", ChartSeriesType.ThreeLineBreak)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [series.Points.Add (0, 1)]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [series.Points.Add (1, 3)]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [series.Points.Add (2, 4)]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\' Add series to the chart series collection.]                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.chartControl1.Series.Add (series)]                                                                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                              |
|                                                                                                                                             |
| Customization Options                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------+
| DisplayShadow, DisplayText, DrawSeriesNameInDepth, ElementBorders, ImageIndex, Images, PriceDownColor, PriceUpColor, Spacing Between Series |
|                                                                                                                                             |
| ShadowInterior, ShadowOffset, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels,                             |
|                                                                                                                                             |
| Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p65} 

 

[]{#related-topics}

