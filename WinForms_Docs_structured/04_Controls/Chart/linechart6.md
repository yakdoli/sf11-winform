---
title: linechart6.md
original_path: WinForms_Docs/04_Controls/Chart/linechart6.md
created_at: 2025-08-05
---






#### Line Chart {#line-chart style="tab-stops: 0pt"}

Line charts join points on a plot by using straight lines showing trends in data at equal intervals. Line charts treat the input as non-numeric, categorical information, and equally space it along the x-axis. This is appropriate for categorical data such as text labels, but can produce unexpected results when the x values consist of numbers.

When rendered in 3-D, the plot looks like a ribbon. Hence such types are also referred as ribbon or strip charts.

The appearance of the lines and the points can be configured with options such as the colors used, thickness of the lines, and the symbols displayed.

 

Chart Details


  ---------------------------------- -------------
  **Number of Y Values per Point**   1
  **Number of Series         **      One or more
  **Cannot be Combined with   **     Pie chart
  ---------------------------------- -------------


[] 

Line series can be added to the chart using the following code.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                             |
| [            [Series] series = [new] [Series]([\"Banana\"]);] |
|                                                                                                                                                                                                             |
| []                                                                                                                                                         |
|                                                                                                                                                                                                             |
| [            series.Points.Add(1991, 3.9);]                                                                                                                |
|                                                                                                                                                                                                             |
| [            series.Points.Add(1992, 5.3);]                                                                                                                |
|                                                                                                                                                                                                             |
| [            series.Points.Add(1993, 8.8);]                                                                                                                |
|                                                                                                                                                                                                             |
| [            \...]                                                                                                                                         |
|                                                                                                                                                                                                             |
| [            series.Symbol.Visible = [true];]                                                                                         |
|                                                                                                                                                                                                             |
| [            series.Symbol.Shape = [SymbolShape].Triangle;]                                                                        |
|                                                                                                                                                                                                             |
| []                                                                                                                                                         |
|                                                                                                                                                                                                             |
| []                                                                                                                                                         |
|                                                                                                                                                                                                             |
| [            series.Type = [SeriesType].Line;]                                                                                     |
|                                                                                                                                                                                                             |
| [            [this].ChartAdv1.Series.Add(series);]                                                                                    |
|                                                                                                                                                                                                             |
| []                                                                                                                                                         |
|                                                                                                                                                                                                             |
| [            [Series] series1 = [new] [Series]([\"Apple\"]);] |
|                                                                                                                                                                                                             |
| [            series1.Points.Add(1991, 3.9);]                                                                                                               |
|                                                                                                                                                                                                             |
| [            series1.Points.Add(1992, 4.2);]                                                                                                               |
|                                                                                                                                                                                                             |
| [            series1.Points.Add(1993, 5.7);]                                                                                                               |
|                                                                                                                                                                                                             |
| [             . . .]                                                                                                                                       |
|                                                                                                                                                                                                             |
| []                                                                                                                                                         |
|                                                                                                                                                                                                             |
| [            series1.Symbol.Visible = [true];]                                                                                        |
|                                                                                                                                                                                                             |
| [            series1.Symbol.Shape = [SymbolShape].Diamond;]                                                                        |
|                                                                                                                                                                                                             |
| [            series1.Type = [SeriesType].Line;]                                                                                    |
|                                                                                                                                                                                                             |
| [            [this].ChartAdv1.Series.Add(series1);]                                                                                   |
|                                                                                                                                                                                                             |
| []                                                                                                                                                         |
|                                                                                                                                                                                                             |
| [            ]                                                                                                                                             |
|                                                                                                                                                                                                             |
| [        ]                                                                                                                                                 |
|                                                                                                                                                                                                             |
| [          ][ ][]                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ** [\[VB\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                 |
| [            [Dim] series [As] [Series] = [New] [Series]([\"Banana\"])] |
|                                                                                                                                                                                                                                                                 |
| [            ]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [            series.Points.Add(1991, 4.9)]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [            series.Points.Add(1992, 7.3)]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [            series.Points.Add(1993, 9.8)]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [            . . .]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [            series.Symbol.Visible = [True]]                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| [            series.Symbol.Shape = [SymbolShape].Triangle]                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [            series.Type = [SeriesType].Line]                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            [Me].ChartAdv1.Series.Add(series)]                                                                                                                                           |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [            [Dim] series1 [As] [Series] = [New] [Series]([\"Apple\"])] |
|                                                                                                                                                                                                                                                                 |
| [            series1.Points.Add(1991, 7.9)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [            series1.Points.Add(1992, 6.2)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [            series1.Points.Add(1993, 5.7)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| [            . . .]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [            series1.Symbol.Visible = [True]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [            series1.Symbol.Shape = [SymbolShape].Diamond]                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [            series1.Type = [SeriesType].Line]                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [            [Me].ChartAdv1.Series.Add(series1)][   ][]                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 9: Line Chart

 

[]{#related-topics}

