---
title: howtocreatearotatesplinechart.md
original_path: WinForms_Docs/04_Controls/Chart/howtocreatearotatesplinechart.md
created_at: 2025-08-05
---






##### How to create a rotate spline chart? {#how-to-create-a-rotate-spline-chart style="tab-stops: 0pt"}

[] 

RotatedSpline chart is similar to the Spline chart, but is rotated 90 degrees in the clockwise direction.

The following illustration shows the RotatedSpline chart:

 

{border="0"}

[] 

Figure 55: RotatedSpline Chart

 

The following code snippet shows how to select a RotatedSpline chart.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"RotatedSpline\" /\>] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].RotatedSpline;                                         |
|                                                                                                                   |
|                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                                            |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
| [Dim] olapChart [As] [OlapChart] = [New] [OlapChart]() |
|                                                                                                                                                                       |
| olapChart.ChartType = [ChartTypes].RotatedSpline                                                                                              |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample, which demonstrates all the available type of Line charts, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Line Chart Demo**

[] 

[]{#related-topics}

