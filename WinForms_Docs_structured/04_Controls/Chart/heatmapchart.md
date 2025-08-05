---
title: heatmapchart.md
original_path: WinForms_Docs/04_Controls/Chart/heatmapchart.md
created_at: 2025-08-05
---








  









### Heat Map Chart {#heat-map-chart style="tab-stops: 0pt"}

A heat map chart is a graphical representation of data where the values taken by a variable in two-dimensional map are represented as colors.

[] 

{border="0"}

[] 

Figure 85: Chart displaying Heat Map Series

**[]** 

Chart Details

**[]** 


+------------------------------+------------------------+
| Details                                               |
+------------------------------+------------------------+
| Number of Y values per point | 2                      |
+------------------------------+------------------------+
| Number of Series             | One.                   |
+------------------------------+------------------------+
| Cannot be Combined with      | Any other chart types. |
+------------------------------+------------------------+


[] 

Combination series can be added to the chart using the following code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [ChartSeries][ Stocks = [new] [ChartSeries]([\"Stocks\"], ChartSeriesType.HeatMap);] |
|                                                                                                                                                                                                                                             |
| [Stocks.Points.Add(7,4, 10000);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [Stocks.Points.Add(6,3, 5541);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [Stocks.Points.Add(5,2, 6007);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [Stocks.Points.Add(4,2, 5022);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [Stocks.Points.Add(3,2.5, 6882);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [Stocks.Points.Add(2,1.5, 6584);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [Stocks.Points.Add(1,1, 2799);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series.Add(Stocks);]                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ ][Stocks[ As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries (][\"Stocks\"][, ChartSeriesType.Line)]] |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Stocks.Points.Add(7,4, 10000)]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Stocks.Points.Add(6,3, 5541)]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Stocks.Points.Add(5,2, 6007)]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Stocks.Points.Add(4,2, 5022)]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Stocks.Points.Add(3,2.5, 6882)]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Stocks.Points.Add(2,1.5, 6584)]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Stocks.Points.Add(1,1, 2799)]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [\' Add the series to the chart series collection.]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.chartControl1.Series.Add (Stocks)]                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Features

[] 

The following table lists the properties of heat map chart with descriptions.

[] 


  -------------------- -------------------------------------------------------------------------------------------
  Property             Description
  HeatMapStyle         Specifies styles of heat maps. The types are Rectangular, Vertical and Horizontal styles.
  DisplayColorSwatch   Enables the color swatch of the heat map.
  DisplayTitle         Enables or disables the series title in the left corner of the swatch.
  StartText            Sets the text for the left label in the color swatch.
  EndText              Sets the text for the right label in the color swatch.
  LowestValueColor     Sets the lowest value color of the heat map chart.
  HighestValueColor    Sets the highest value color of the heat map chart.
  MiddleValueColor     Sets the middle value color of the heat map chart.
  LabelMargin          Sets the margin for the left and right side labels.
  -------------------- -------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [//Sets the Heat map style.]                                                                                                                             |
|                                                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].ConfigItems.HeatMapItem.HeatMapStyle = ChartHeatMapLayoutStyle.Rectangular;]        |
|                                                                                                                                                                                                            |
| [//Display color swatch.]                                                                                                                                |
|                                                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].ConfigItems.HeatMapItem.DisplayColorSwatch = [true];]          |
|                                                                                                                                                                                                            |
| [//Sets the Series Title.]                                                                                                                               |
|                                                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].ConfigItems.HeatMapItem.DisplayTitle = [true];]                |
|                                                                                                                                                                                                            |
| [//Sets the left and right label text.]                                                                                                                  |
|                                                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].ConfigItems.HeatMapItem.StartText = [\"US\"];]              |
|                                                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].ConfigItems.HeatMapItem.EndText = [\"Utah\"];]              |
|                                                                                                                                                                                                            |
| [//Sets the lowest, highest and middle value color.]                                                                                                     |
|                                                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].ConfigItems.HeatMapItem.LowestValueColor = [Color].Red;]    |
|                                                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].ConfigItems.HeatMapItem.HighestValueColor = [Color].Blue;]  |
|                                                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].ConfigItems.HeatMapItem.MiddleValueColor = [Color].Yellow;] |
|                                                                                                                                                                                                            |
| [//Sets the value for the left and right labels.]                                                                                                        |
|                                                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].ConfigItems.HeatMapItem.LabelMargins = 15;]                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                                                      |
|                                                                                                                                                                                               |
| [\'Sets the Heat map style.]                                                                                                                |
|                                                                                                                                                                                               |
| [Me][.chartControl1.Series(0).ConfigItems.HeatMapItem.HeatMapStyle =ChartHeatMapLayoutStyle.Rectangular] |
|                                                                                                                                                                                               |
| [\'Display color swatch.  ]                                                                                                                 |
|                                                                                                                                                                                               |
| [Me][.chartControl1.Series(0).ConfigItems.HeatMapItem.DisplayColorSwatch = [True]]  |
|                                                                                                                                                                                               |
| [\'Sets the display title.      ]                                                                                                           |
|                                                                                                                                                                                               |
| [Me][.chartControl1.Series(0).ConfigItems.HeatMapItem.DisplayTitle = [True]]        |
|                                                                                                                                                                                               |
| [\'Sets the start and end text.]                                                                                                            |
|                                                                                                                                                                                               |
| [series.ConfigItems.HeatMapItem.StartText = [\"US\"]            ]                                                                  |
|                                                                                                                                                                                               |
| [series.ConfigItems.HeatMapItem.EndText = [\"Utah\"]]                                                                              |
|                                                                                                                                                                                               |
| [\'Sets the lowest, highest and middle value color.]                                                                                        |
|                                                                                                                                                                                               |
| [series.ConfigItems.HeatMapItem.LowestValueColor = Color.FromArgb(255, 23, 0)]                                                                            |
|                                                                                                                                                                                               |
| [series.ConfigItems.HeatMapItem.HighestValueColor = Color.FromArgb(81, 168, 0)]                                                                           |
|                                                                                                                                                                                               |
| [series.ConfigItems.HeatMapItem.MiddleValueColor = Color.Gold]                                                                                            |
|                                                                                                                                                                                               |
| [\'Sets the margin for the left and right labels.]                                                                                          |
|                                                                                                                                                                                               |
| [series.ConfigItems.HeatMapItem.LabelMargins = 15]                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p75} 

[]{#related-topics}

