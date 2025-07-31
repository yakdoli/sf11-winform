---
title: howtocreatealinechart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtocreatealinechart.md
created_at: 2025-07-03
---






##### How to create a line chart? {#how-to-create-a-line-chart style="tab-stops: 0pt"}

[] 

Line chart is a simple form of chart, which connects a series of data points. Usually, it is used for Trend analysis, Forcasting, or in the case of large data points.

The following illustration shows the Line chart:

 

{border="0"}

Figure 53: Line Chart[]

[] 

The following code snippet shows how to select a Line chart:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"Line\" /\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].Line;                                                  |
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
| olapChart.ChartType = [ChartTypes].Line                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample, which demonstrates all the available type of Line charts, can be found in the following installation location.

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Line Chart Demo**

[] 

[]{#related-topics}

