---
title: howtodisableverticalgridlines.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtodisableverticalgridlines.md
created_at: 2025-07-03
---






##### How to disable vertical grid lines? {#how-to-disable-vertical-grid-lines style="tab-stops: 0pt"}

[] 

In general, for column type charts, the ***vertical grid line belongs to*** ***the primary axis***. To disable the vertical grid lines for these types of charts, you need to use the ShowGridLines property of the primary axis.

The following illustration describes how the chart will look after the vertical grid lines are disabled:

 

{border="0"}

Figure 36: An OlapChart with vertical grid lines disabled[]

***[]*** 

The following code snippet describes how to disable the horizontal grid lines:

[] 

+-------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                      |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
| [      this].olapChart.Series\[0\].Area.PrimaryAxis.SetValue(              |
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
|           [Me].olapChart.Series(0).Area.PrimaryAxis.SetValue(             |
|                                                                                                |
|       [ChartArea].ShowGridLinesProperty, [False]) |
|                                                                                                |
|                                                                                                |
+------------------------------------------------------------------------------------------------+


 

[{border="0"}]Note: For bar type charts, such as Bar, Stacking bar, and Stacking100 Bar you can disable the vertical grid lines by using the ShowGridLinesProperty of the SecondaryAxis.


[] 

[]{#related-topics}

