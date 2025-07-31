---
title: howtodisablehorizontalgridlines.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtodisablehorizontalgridlines.md
created_at: 2025-07-03
---






##### How to disable horizontal grid lines? {#how-to-disable-horizontal-grid-lines style="tab-stops: 0pt"}

[] 

In general, for column type charts, the ***horizontal grid line belongs to*** ***the secondary axis***. To disable the horizontal grid lines for these types of charts, you need to use the ShowGridLines property of the secondary axis.

The following illustration describes how the chart will look after the horizontal grid lines are disabled:[]

[] 

{border="0"}

Figure 35: An OlapChart with horizontal grid lines disabled[]

***[]*** 

The following code snippet describes how to disable the horizontal grid lines:

[] 

+-------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                      |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
| [      this].olapChart.Series\[0\].Area.SecondaryAxis.SetValue(            |
|                                                                                                 |
| [      ChartArea].ShowGridLinesProperty, [false]); |
|                                                                                                 |
|                                                                                                 |
+-------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                     |
|                                                                                                |
|                                                                                                |
|                                                                                                |
|           [Me].olapChart.Series(0).Area.SecondaryAxis.SetValue(           |
|                                                                                                |
|       [ChartArea].ShowGridLinesProperty, [False]) |
|                                                                                                |
|                                                                                                |
+------------------------------------------------------------------------------------------------+

[] 


 

[{border="0"}]Note: For bar type charts, such as Bar, Stacking bar, and Stacking100 Bar you can disable the horizontal grid lines by using the ShowGridLinesProperty of the PrimaryAxis.


[] 

[]{#related-topics}

