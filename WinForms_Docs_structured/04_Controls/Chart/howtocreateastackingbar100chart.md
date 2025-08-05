---
title: howtocreateastackingbar100chart.md
original_path: WinForms_Docs/04_Controls/Chart/howtocreateastackingbar100chart.md
created_at: 2025-08-05
---






##### How to create a stacking bar 100 chart? {#how-to-create-a-stacking-bar-100-chart style="tab-stops: 0pt"}

[] 

StackingBar100 chart is the same as the StackingColumn100 chart, the variation is it is rotated 90 degree in the clockwise direction. This chart type is widely used for proportional analysis over a particular period of time.

The following illustration shows the StackingBar100 chart:

 

{border="0"}

Figure 48: StackingBar100 Chart[]

 

The following code snippet shows how to select a bar chart:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"StackingBar100\" /\>] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].StackingBar100;                                        |
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
| olapChart.ChartType = [ChartTypes].StackingBar100                                                                                             |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample, which demonstrates all the available type of Bar charts, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Bar Chart Demo**

[] 

[]{#related-topics}

