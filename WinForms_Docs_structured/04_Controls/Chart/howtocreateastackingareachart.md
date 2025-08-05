---
title: howtocreateastackingareachart.md
original_path: WinForms_Docs/04_Controls/Chart/howtocreateastackingareachart.md
created_at: 2025-08-05
---






##### How to create a stacking area chart? {#how-to-create-a-stacking-area-chart style="tab-stops: 0pt"}

[] 

StackingArea chart fills the quantitative data over a period of time just like the line Area chart. The variation in the StackingArea is while plotting the series. Each series is plotted on the top of the previous series rather than starting from 0 of the horizontal axis. It is mainly used to compare the quantity plotted over two or more series.

The following illustration shows the StackingArea chart:

[] 

{border="0"}

Figure 50: StackingArea Chart[]

[] 

The following code snippet shows how to select a StackingArea chart:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"StackingArea\" /\>] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].StackingArea;                                          |
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
| olapChart.ChartType = [ChartTypes].StackingArea                                                                                               |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample, which demonstrates all the available type of Area charts, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Area Chart Demo**

[] 

[]{#related-topics}

