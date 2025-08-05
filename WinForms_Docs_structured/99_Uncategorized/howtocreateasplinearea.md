---
title: howtocreateasplinearea.md
original_path: WinForms_Docs/99_Uncategorized/howtocreateasplinearea.md
created_at: 2025-08-05
---






##### How to create a spline area? {#how-to-create-a-spline-area style="tab-stops: 0pt"}

[] 

Spline area chart is usually used in the case of approximating the intervals by using spline curve. It is often used when data points are in limited number.

The following illustration shows the Spline area chart:

[] 

{border="0"}

Figure 51: SplineArea Chart[]

[] 

The following code snippet shows how to select a Spline area chart:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ ChartType][=\"SplineArea\" /\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
|                                                                                                                   |
| olapChart.ChartType = [ChartTypes].SplineArea;                                            |
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
| olapChart.ChartType = [ChartTypes].SplineArea                                                                                                 |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample, which demonstrates all the available type of Area charts, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Types\\Area Chart Demo**

[] 

[]{#related-topics}

