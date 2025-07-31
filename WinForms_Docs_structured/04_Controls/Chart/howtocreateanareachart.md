---
title: howtocreateanareachart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtocreateanareachart.md
created_at: 2025-07-03
---






##### How to create an Area chart? {#how-to-create-an-area-chart style="tab-stops: 0pt"}

[] 

Area chart fills the quantitative data over a period of time. It is mainly used to compare the quantity plotted over two or more series.

 

The following illustration shows the simple Area chart:

[] 

{border="0"}

Figure 49: Area Chart[]

[] 

The following code snippet shows how to select an Area chart:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"Area\" /\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].Area;                                                  |
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
| olapChart.ChartType = [ChartTypes].Area                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample, which demonstrates all the available type of Area charts, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Area Chart Demo**

[] 

[]{#related-topics}

