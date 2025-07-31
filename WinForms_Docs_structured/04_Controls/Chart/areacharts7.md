---
title: areacharts7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\areacharts7.md
created_at: 2025-07-03
---






#### Area Charts {#area-charts style="tab-stops: 0pt"}

The area chart connects the y points by using straight lines and forms an area bound by the above lines and x-axis. This area is then shaded with a specified color or gradient.

Multiple series can be plotted on the same chart and an alpha-blended interior color can be used on the exterior chart to make the interior chart show through.             

 

Chart Details


  ---------------------------------- -------------
  **Number of Y values per point**   1
  **Number of Series         **      One or more
  **Cannot be Combined with   **     Pie chart
  ---------------------------------- -------------


[] 

Area series can be added to the chart using the following code.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][      ][]**                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [        [Series] series = [new] [Series]([\"CompanyA\"]);]                                                             |
|                                                                                                                                                                                                                                                                       |
| [        series.Type = [SeriesType].Area;]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [        [MinMaxInfo] ass = [new] [MinMaxInfo](); ]                                                                                             |
|                                                                                                                                                                                                                                                                       |
| [        ass.Start =1940;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [        ass.End = 2005; ]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [        ass.Interval = 5;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [        [this].ChartAdv1.Axes\[[\"PrimaryX\"]\].RangeType = [RangeType].Set;]                                                                  |
|                                                                                                                                                                                                                                                                       |
| [        [this].ChartAdv1.Axes\[[\"PrimaryX\"]\].ValueType = [ChartAxisValueType].Double;]                                                      |
|                                                                                                                                                                                                                                                                       |
| [        [this].ChartAdv1.Axes\[[\"PrimaryX\"]\].Range = [new] [MinMaxInfo]() { Start = 1940, End = 2005, Interval = 5 };] |
|                                                                                                                                                                                                                                                                       |
| [      ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                       |
| [        series.Points.Add(1946, 0.011);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [        series.Points.Add(1945, 0.06);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                       |
| [        series.Points.Add(1947, 0.032);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [        . . .]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [        series.Style.Border.Width = 3;]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                       |
| [        series.DisplayText = [false];]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                       |
| [        series.Symbol.Visible = [true];]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [        series.Style.Opacity = 0.8f;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| [        series.Symbol.Shape = [SymbolShape].Star;]                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [this].ChartAdv1.Series.Add(series);]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [        [Series] series1 = [new] [Series]([\"CompanyB\"]);]                                                            |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [        series1.Points.Add(1950, 0.5);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                       |
| [        series1.Points.Add(1951, 0.25);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [        series1.Points.Add(1952, 0.50);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [        ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                       |
| [         . . .]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                       |
| [        series1.Type = [SeriesType].Area;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [        [this].ChartAdv1.Series.Add(series1);]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [        series1.Style.Border.Width = 3;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [        series1.Style.Opacity = 0.8f;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [        series1.DisplayText = [false];]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [        series1.Symbol.Visible = [true];]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [        series1.Symbol.Shape = [SymbolShape].Star;]                                                                                                                                         |
|                                                                                                                                                                                                                                                                       |
| [       ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| [      ][  [Dim] series [As] [New] [Series]([\"CompanyA\"])] |
|                                                                                                                                                                                                                                                                                            |
| [        series.Type = [SeriesType].Area]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [        ]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [        [Dim] ass [As] [New] [MinMaxInfo]()]                                                                                                      |
|                                                                                                                                                                                                                                                                                            |
| [        ass.Start = 1940]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [        ass.\[End\] = 2005]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                            |
| [        ass.Interval = 5]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [        [Me].ChartAdv1.Axes([\"PrimaryX\"]).RangeType = [RangeType].\[Set\]]                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [        [Me].ChartAdv1.Axes([\"PrimaryX\"]).ValueType = [ChartAxisValueType].\[Double\]]                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [        [Me].ChartAdv1.Axes([\"PrimaryX\"]).Range = [New] [MinMaxInfo]() [With]{.Start = 1940, .End=2005,.Interval=5}]    |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [        series.Points.Add(1946, 0.011)]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                            |
| [        series.Points.Add(1945, 0.06)]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                            |
| [        series.Points.Add(1947, 0.032)]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                            |
| [        ]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [        . . .]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| [        series.Style.Border.Width = 3]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                            |
| [        series.DisplayText = [False]]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                            |
| [        series.Symbol.Visible = [True]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [        series.Style.Opacity = 0.8F]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [        series.Symbol.Shape = [SymbolShape].Star]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [        [Me].ChartAdv1.Series.Add(series)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [        [Dim] series1 [As] [New] [Series]([\"CompanyB\"])]                                                                |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [        series1.Points.Add(1950, 0.5)]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                            |
| [        series1.Points.Add(1951, 0.25)]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                            |
| [        series1.Points.Add(1952, 0.5)]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                            |
| [        series1.Points.Add(1953, 0.12)]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                            |
| [        ]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [         . . .]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [        series1.Type = [SeriesType].Area]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [        [Me].ChartAdv1.Series.Add(series1)]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [        series1.Style.Border.Width = 3]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                            |
| [        series1.Style.Opacity = 0.8F]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [        series1.DisplayText = [False]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                            |
| [        series1.Symbol.Visible = [True]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [        series1.Symbol.Shape = [SymbolShape].Star]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [    ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [ ][ ][]                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 12: Area Chart

 

[]{#related-topics}

