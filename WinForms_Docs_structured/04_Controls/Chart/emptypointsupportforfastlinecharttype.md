---
title: emptypointsupportforfastlinecharttype.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\emptypointsupportforfastlinecharttype.md
created_at: 2025-07-03
---






##### Empty point support for FastLine Chart type {#empty-point-support-for-fastline-chart-type style="tab-stops: 0pt"}

Essential chart WPF is now supports Empty point for  Fast Line Chart type.

The data collection that is passed to the chart may have **NaN** values, this is an empty points.

If data points bounded with chart does not give any value then chart renders empty points in chart series.

[] 

This feature is useful when you are not able to get exact value for a particular data.

e.g.  In population analysis if you do not get the result for previous years then we can use Empty data value.

**[]** 

Adding Empty Point

Add Empty Point to the Chart, by using the following code.

Set **ShowEmptyPoints** to **True** to enable Empty Point.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Xaml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [  ][\<][syncfusion][:][ChartSeries][ Name][=\"series1\"][ ShowEmptyPoints][=\"True\"][ ]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Type][=\"FastLine\"][ Interior][=\"Red\"][ Stroke][=\"Black\"][ DataSource][=\"{][Binding][}\"/\>] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                            |
|                                                                                              |
| **[]**                                                   |
|                                                                                              |
| [Series1.ShowEmptyPoints = [true];] |
+----------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 109: Empty Point[]{#p69}

[]{#related-topics}

