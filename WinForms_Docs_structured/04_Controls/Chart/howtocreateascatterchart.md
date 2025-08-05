---
title: howtocreateascatterchart.md
original_path: WinForms_Docs/04_Controls/Chart/howtocreateascatterchart.md
created_at: 2025-08-05
---






##### How to create a scatter chart? {#how-to-create-a-scatter-chart style="tab-stops: 0pt"}

[] 

Scatter chart is a collection of points plotted in the rectangular co-ordinate system. It is often used in relationship analysis upto one independent variable.

The following illustration shows the Scatter chart:

 

{border="0"}

Figure 57: Scatter Chart[]

[] 

The following code snippet shows how to select a Scatter chart:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                  |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"Scatter\" /\>] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].Scatter;                                               |
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
| olapChart.ChartType = [ChartTypes].Scatter                                                                                                    |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample, which demonstrates the Scatter chart, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Scatter Chart Demo**

 

[]{#related-topics}

