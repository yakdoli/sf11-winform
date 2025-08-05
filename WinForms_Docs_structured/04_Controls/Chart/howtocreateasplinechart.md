---
title: howtocreateasplinechart.md
original_path: WinForms_Docs/04_Controls/Chart/howtocreateasplinechart.md
created_at: 2025-08-05
---






##### How to create a spline chart? {#how-to-create-a-spline-chart style="tab-stops: 0pt"}

 

Spline chart is a simple form of chart, which connects the series of data points with an arc rather than a straight line.

The following illustration shows the Spline chart:

 

{border="0"}

Figure 54: Spline Chart[]

[] 

[] 

The following code snippet shows how to select a Spline chart:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"Spline\" /\>] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].Spline;                                                |
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
| olapChart.ChartType = [ChartTypes].Spline                                                                                                     |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample, which demonstrates all the available type of Line charts, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Line Chart Demo**

[] 

[]{#related-topics}

