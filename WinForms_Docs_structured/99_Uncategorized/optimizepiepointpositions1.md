---
title: optimizepiepointpositions1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\optimizepiepointpositions1.md
created_at: 2025-07-03
---






#### OptimizePiePointPositions {#optimizepiepointpositions style="tab-stops: 0pt"}

 

Specifies if the data points with smaller values are grouped together and ordered. By default, they are ordered in the order in which the points are added to the series.

 


+-------------------------------------+---------------------------------------------------------------------+
|                                                                                                           |
|                                                                                                           |
| **Details**                                                                                               |
+-------------------------------------+---------------------------------------------------------------------+
| **Possible Values**                 |                                                                     |
|                                     |                                                                     |
|                                     | [·      ]True  - Enables optimization  |
|                                     |                                                                     |
|                                     | [·      ]False - Disables optimization |
|                                     |                                                                     |
|                                     |                                                                     |
+-------------------------------------+---------------------------------------------------------------------+
| **Default Value    **               | **True**                                                            |
+-------------------------------------+---------------------------------------------------------------------+
| **2D / 3D Limitations**             | No.                                                                 |
+-------------------------------------+---------------------------------------------------------------------+
| **Applies to Chart Element**        | Any Series.                                                         |
+-------------------------------------+---------------------------------------------------------------------+
| **Applies to Chart Types**          | Pie Chart.                                                          |
+-------------------------------------+---------------------------------------------------------------------+


 

Here is the code snippet using OptimizePiePointPositions.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [ChartSeries][ series = [this].chartControl1.Model.NewSeries([\"Series Name\"], [ChartSeriesType].Pie);] |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(0, 20);]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(1, 28);]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(2, 23);]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(3, 10);]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(4, 12);]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(5, 3);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [series.Points.Add(6, 2);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [series.ExplodedIndex = 2;]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [series.OptimizePiePointPositions = [false];]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [this][.chartControl1.Series.Add(series);]                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ ][series[ ][As][ ChartSeries = ][Me][.chartControl1.Model.NewSeries(\"][Series Name][\",][ChartSeriesType][.]Pie[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.Points.Add(0, 20)]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.Points.Add(1, 28)]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.Points.Add(2, 23)]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.Points.Add(3, 10)]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.Points.Add(4, 12)]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.Points.Add(5, 3)]                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.Points.Add(6, 2)]                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.ExplodedIndex = 2]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [series.OptimizePiePointPositions = [False]]                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.chartControl1.Series.Add(][series[)]]                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 167: OptimizePiePointPositions set to True

 

{border="0"}

 

Figure 168: OptimizePiePointPositions set to False

 

See Also

[[]]

[[Pie Chart]]{.UGHyperlink}

 

[]{#p127} 

 

[]{#related-topics}

