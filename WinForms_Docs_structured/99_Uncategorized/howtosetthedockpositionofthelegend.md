---
title: howtosetthedockpositionofthelegend.md
original_path: WinForms_Docs/99_Uncategorized/howtosetthedockpositionofthelegend.md
created_at: 2025-08-05
---






##### How to set the dock position of the legend? {#how-to-set-the-dock-position-of-the-legend style="tab-stops: 0pt"}

[] 

ChartLegend contains an enum property called *ChartDock*, which has the following values *Floating, Right, Left, Top, and Bottom.* You can choose the required docking position to dock the chart. The following code snippets explain how to set the docking position for an OlapChart legend:

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                 |
|                                                                                                                                            |
|                                                                                                                                            |
|                                                                                                                                            |
| [ChartDockPanel].SetDock([this].olapChart.Legend, [ChartDock].Right); |
|                                                                                                                                            |
|                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                              |
|                                                                                                                                         |
|                                                                                                                                         |
|                                                                                                                                         |
| [ChartDockPanel].SetDock([Me].olapChart.Legend, [ChartDock].Right) |
|                                                                                                                                         |
|                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

