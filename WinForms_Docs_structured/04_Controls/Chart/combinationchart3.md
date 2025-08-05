---
title: combinationchart3.md
original_path: WinForms_Docs/04_Controls/Chart/combinationchart3.md
created_at: 2025-08-05
---








  









### Combination Chart {#combination-chart style="tab-stops: 0pt"}

Combination charts refer to the ability to display multiple data series in the same chart with each series visualized by using different chart types. In Essential Chart, chart types that are compatible with each other may be combined in the same chart area.

Typically it is a combination of a line chart and column chart sharing a common x-axis but with separate y-axes, one on either side of the chart.

You can change an existing chart to a combination chart by selecting the data series you want to change and then changing the chart type for that series.    

[] 

Combination series can be added to the chart using the following code.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][      ][]**                                                                              |
|                                                                                                                                                                                                                              |
| [       [ ][Series] series = [new] [Series]([\"John\"]);] |
|                                                                                                                                                                                                                              |
| [        series.Type= [SeriesType].Column;]                                                                                                         |
|                                                                                                                                                                                                                              |
| [        series.Points.Add(1, 3);]                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [        series.Points.Add(2, 2);]                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [        series.Points.Add(3, 1);]                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [        series.Points.Add(4, 2);]                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [        series.Points.Add(5, 5);]                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [        [this].ChartAdv1.Series.Add(series);]                                                                                                         |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [         [Series] series1 = [new] [Series]([\"Andrew\"]);]                    |
|                                                                                                                                                                                                                              |
| [        series1.Type= [SeriesType].Column;]                                                                                                        |
|                                                                                                                                                                                                                              |
| [        series1.Points.Add(1, 2);]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [        series1.Points.Add(2, 3);]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [        series1.Points.Add(3, 5);]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [        series1.Points.Add(4, 7);]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [        series1.Points.Add(5, 6);]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [        [this].ChartAdv1.Series.Add(series1);]                                                                                                        |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [         [Series] series2 = [new] [Series]([\"Henry\"]);]                     |
|                                                                                                                                                                                                                              |
| [        series2.Type= [SeriesType].Column;]                                                                                                        |
|                                                                                                                                                                                                                              |
| [        series2.Points.Add(1, 4);]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [        series2.Points.Add(2, 3);]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [        series2.Points.Add(3, 3);]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [        series2.Points.Add(4, 9);]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [        series2.Points.Add(5, 3);]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [        [this].ChartAdv1.Series.Add(series2);]                                                                                                        |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [         [Series] series4 = [new] [Series]([\"Average\"]);]                   |
|                                                                                                                                                                                                                              |
| [        series4.Type= [SeriesType].Line;]                                                                                                          |
|                                                                                                                                                                                                                              |
| [        series4.Points.Add(1, 3); ]                                                                                                                                        |
|                                                                                                                                                                                                                              |
| [        series4.Points.Add(2, 2.67);]                                                                                                                                      |
|                                                                                                                                                                                                                              |
| [        series4.Points.Add(3, 3); ]                                                                                                                                        |
|                                                                                                                                                                                                                              |
| [        series4.Points.Add(4, 6.33);]                                                                                                                                      |
|                                                                                                                                                                                                                              |
| [        series4.Points.Add(5, 3.33);]                                                                                                                                      |
|                                                                                                                                                                                                                              |
| [        [this].ChartAdv1.Series.Add(series4);]                                                                                                        |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [  ]                                                                                                                                                                        |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]][      ][]**                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [       [ Dim] series [As] [Series] = [New] [Series]([\"John\"])]     |
|                                                                                                                                                                                                                                                               |
| [        series.Type = [SeriesType].Column]                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [        series.Points.Add(1, 3)]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [        series.Points.Add(2, 2)]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [        series.Points.Add(3, 1)]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [        series.Points.Add(4, 2)]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [        series.Points.Add(5, 5)]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [        [Me].ChartAdv1.Series.Add(series)]                                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        [Dim] series1 [As] [Series] = [New] [Series]([\"Andrew\"])]  |
|                                                                                                                                                                                                                                                               |
| [        series1.Type = [SeriesType].Column]                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [        series1.Points.Add(1, 2)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series1.Points.Add(2, 3)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series1.Points.Add(3, 5)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series1.Points.Add(4, 7)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series1.Points.Add(5, 6)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        [Me].ChartAdv1.Series.Add(series1)]                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        [Dim] series2 [As] [Series] = [New] [Series]([\"Henry\"])]   |
|                                                                                                                                                                                                                                                               |
| [        series2.Type = [SeriesType].Column]                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [        series2.Points.Add(1, 4)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series2.Points.Add(2, 3)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series2.Points.Add(3, 3)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series2.Points.Add(4, 9)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series2.Points.Add(5, 3)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        [Me].ChartAdv1.Series.Add(series2)]                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        [Dim] series4 [As] [Series] = [New] [Series]([\"Average\"])] |
|                                                                                                                                                                                                                                                               |
| [        series4.Type = [SeriesType].Line]                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series4.Points.Add(1, 3)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series4.Points.Add(2, 2.67)]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [        series4.Points.Add(3, 3)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [        series4.Points.Add(4, 6.33)]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [        series4.Points.Add(5, 3.33)]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [        [Me].ChartAdv1.Series.Add(series4)]                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [         ]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [  ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

{border="0"}

Figure 17: Combination Chart

 

[]{#related-topics}

