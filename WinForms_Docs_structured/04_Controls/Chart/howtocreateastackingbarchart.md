---
title: howtocreateastackingbarchart.md
original_path: WinForms_Docs/04_Controls/Chart/howtocreateastackingbarchart.md
created_at: 2025-08-05
---






##### How to create a stacking bar chart? {#how-to-create-a-stacking-bar-chart style="tab-stops: 0pt"}

[] 

StackingBar chart is the same as the StackingColumn chart, the variation is it is rotated 90 degrees in the clockwise direction. This chart type is widely used for proportional analysis over a particular period of time.

The following illustration shows the simple bar chart:

 

{border="0"}

Figure 47: StackingBar Chart[]

[] 

The following code snippet shows how to select a bar chart:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"StackingBar\" /\>] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].StackingBar;                                           |
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
| olapChart.ChartType = [ChartTypes].StackingBar                                                                                                |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample, which demonstrates all the available type of Bar charts, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Bar Chart Demo**

 

[]{#related-topics}

