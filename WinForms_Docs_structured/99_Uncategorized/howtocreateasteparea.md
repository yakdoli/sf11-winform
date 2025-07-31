---
title: howtocreateasteparea.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocreateasteparea.md
created_at: 2025-07-03
---






##### How to create a step area? {#how-to-create-a-step-area style="tab-stops: 0pt"}

[] 

In the Step area chart, the points are plotted instead of a straight line tracing the shortest path between points; the values are connected by continuous vertical and horizontal lines.

 

The following illustration shows the Step area chart:

 

{border="0"}

Figure 52: StepArea Chart[]

[] 

The following code snippet shows how to select a Step area chart:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"StepArea\" /\>] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].StepArea;                                              |
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
| olapChart.ChartType = [ChartTypes].StepArea                                                                                                   |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample, which demonstrates all the available type of Area charts, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Area Chart Demo**

[] 

[]{#related-topics}

