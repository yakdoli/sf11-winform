---
title: optimizepiepointpositions.md
original_path: WinForms_Docs/99_Uncategorized/optimizepiepointpositions.md
created_at: 2025-08-05
---






#### OptimizePiePointPositions {#optimizepiepointpositions style="tab-stops: 0pt"}

**[]** 

Specifies if the data points with smaller values are grouped together and ordered. By default, they are ordered in the order in which the points are added to the series.

[] 


+---------------------------------------+---------------------------------------+
| **[]**      |
|                                                                               |
| Details                                                                       |
+---------------------------------------+---------------------------------------+
| Possible Values                       | True - Enables optimization           |
|                                       |                                       |
|                                       | False - Disables optimization         |
+---------------------------------------+---------------------------------------+
| Default Value                         | True                                  |
+---------------------------------------+---------------------------------------+
| 2D / 3D Limitations                   | No.                                   |
+---------------------------------------+---------------------------------------+
| Applies to Chart Element              | Any Series.                           |
+---------------------------------------+---------------------------------------+
| Applies to Chart Types                | Pie Chart.                            |
+---------------------------------------+---------------------------------------+


**[]** 

Here is the code snippet using OptimizePiePointPositions.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [ChartSeries][ series = [this].ChartWebControl1.Model.NewSeries([\"Series Name\"], [ChartSeriesType].Pie);] |
|                                                                                                                                                                                                                                                                   |
| [series.Points.Add(0, 20);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [series.Points.Add(1, 28);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [series.Points.Add(2, 23);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [series.Points.Add(3, 10);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [series.Points.Add(4, 12);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [series.Points.Add(5, 3);]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| [series.Points.Add(6, 2);]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| [series.ExplodedIndex = 2;]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [series.OptimizePiePointPositions = [false];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [this][.ChartWebControl1.Series.Add(series);]                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ ][series[ ][As][ ChartSeries = ][Me][.ChartWebControl1.Model.NewSeries(\"][Series Name][\",][ChartSeriesType][.]Pie[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [series.Points.Add(0, 20)]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [series.Points.Add(1, 28)]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [series.Points.Add(2, 23)]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [series.Points.Add(3, 10)]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [series.Points.Add(4, 12)]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [series.Points.Add(5, 3)]                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [series.Points.Add(6, 2)]                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [series.ExplodedIndex = 2]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [series.OptimizePiePointPositions = [False]]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.ChartWebControl1.Series.Add(][series[)]]                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 162: OptimizePiePointPositions Enabled in Chart (Default)

**[]** 

{border="0"}

**[]** 

Figure 163: OptimizePiePointPositions Disabled in Chart

**[]** 

See Also

[] 

[Pie Chart]{.UGHyperlink}

[]{#p128} 

[]{#related-topics}

