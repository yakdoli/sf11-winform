---
title: howtocreateasimplecolumnchart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtocreateasimplecolumnchart.md
created_at: 2025-07-03
---






##### How to create a simple column chart? {#how-to-create-a-simple-column-chart style="tab-stops: 0pt"}

[] 

Column chart is the most basic type of chart. Column charts are widely used for comparison analysis.

The following illustration shows the basic column chart:

 

{border="0"}

Figure 43: Simple Column Chart[]

[] 

The following code snippet shows how to select a simple column chart:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"Column\" /\>] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].Column;                                                |
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
| olapChart.ChartType = [ChartTypes].Column                                                                                                     |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample, which demonstrates all the available type of Column charts, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Column Chart Demo**

 

[]{#related-topics}

