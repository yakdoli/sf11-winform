---
title: howtocreateasteplinechart.md
original_path: WinForms_Docs/04_Controls/Chart/howtocreateasteplinechart.md
created_at: 2025-08-05
---






##### How to create a step line chart? {#how-to-create-a-step-line-chart style="tab-stops: 0pt"}

[] 

StepLine chart is another form of chart, which connects the series of data points by using horizontal and vertical lines.

The following illustration shows the StepLine chart:

 

{border="0"}

Figure 56: StepLine Chart[]

[] 

The following code snippet shows how to select a StepLine chart:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"StepLine\" /\>] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].StepLine;                                              |
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
| olapChart.ChartType = [ChartTypes].StepLine                                                                                                   |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample, which demonstrates all the available type of Line charts, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Line Chart Demo**

[] 

[]{#related-topics}

