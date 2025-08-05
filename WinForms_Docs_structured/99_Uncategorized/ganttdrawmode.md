---
title: ganttdrawmode.md
original_path: WinForms_Docs/99_Uncategorized/ganttdrawmode.md
created_at: 2025-08-05
---






#### GanttDrawMode {#ganttdrawmode style="tab-stops: 0pt"}

[] 

Specifies the drawing mode of Gantt chart.

[] 


+---------------------------------------+-------------------------------------------------------------+
| **[]**                            |
|                                                                                                     |
| Details                                                                                             |
+---------------------------------------+-------------------------------------------------------------+
| Possible Values                       | AutoSizeMode - Plots the Gantt Chart side by side.          |
|                                       |                                                             |
|                                       | CustomPointWidthMode - Plots the Gantt Chart as Overlapped. |
+---------------------------------------+-------------------------------------------------------------+
| Default Value                         | CustomPointWidthMode                                        |
+---------------------------------------+-------------------------------------------------------------+
| 2D / 3D Limitations                   | None                                                        |
+---------------------------------------+-------------------------------------------------------------+
| Applies to Chart Element              | All series                                                  |
+---------------------------------------+-------------------------------------------------------------+
| Applies to Chart Types                | Gantt Chart                                                 |
+---------------------------------------+-------------------------------------------------------------+


**[]** 

Here is some sample code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                   |
|                                                                                                                                                                                                            |
| **[ ]**[// Specifies GenttDrawMode as CustomPointWidthMode]                                            |
|                                                                                                                                                                                                            |
| [this][.ChartWebControl1.Series\[0\].GanttDrawMode = [ChartGanttDrawMode].CustomPointWidthMode;] |
|                                                                                                                                                                                                            |
| [this][.ChartWebControl1.Series\[0\].Style.PointWidth = 0.7f;]                                                        |
|                                                                                                                                                                                                            |
| [this][.ChartWebControl1.Series\[1\].GanttDrawMode = [ChartGanttDrawMode].CustomPointWidthMode;] |
|                                                                                                                                                                                                            |
| [this][.ChartWebControl1.Series\[1\].Style.PointWidth = 1f;]                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                    |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                                              |
|                                                                                                                                                                                                       |
| [\' Specifies GenttDrawMode as CustomPointWidthMode]                                                                                                |
|                                                                                                                                                                                                       |
| [Me][.ChartWebControl1.Series(0).GanttDrawMode = [ChartGanttDrawMode].CustomPointWidthMode] |
|                                                                                                                                                                                                       |
| [Me][.ChartWebControl1.Series(0).Style.PointWidth = 0.7f]                                                        |
|                                                                                                                                                                                                       |
| [Me][.ChartWebControl1.Series(1).GanttDrawMode = ChartGanttDrawMode.CustomPointWidthMode]                        |
|                                                                                                                                                                                                       |
| [Me][.ChartWebControl1.Series(1).Style.PointWidth = 1f]                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| **[]**                                                                                                                                           |
|                                                                                                                                                                                                    |
| [// Specifies GenttDrawMode as AutoSizeMode]                                                                                                     |
|                                                                                                                                                                                                    |
| [this][.ChartWebControl1.Series\[0\].GanttDrawMode = [ChartGanttDrawMode].AutoSizeMode;] |
|                                                                                                                                                                                                    |
| [this][.ChartWebControl1.Series\[1\].GanttDrawMode = [ChartGanttDrawMode].AutoSizeMode;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| **[]**                                                                                                                                      |
|                                                                                                                                                                                               |
| [\' Specifies GenttDrawMode as AutoSizeMode]                                                                                                |
|                                                                                                                                                                                               |
| [Me][.ChartWebControl1.Series(0).GanttDrawMode = [ChartGanttDrawMode].AutoSizeMode] |
|                                                                                                                                                                                               |
| [Me][.ChartWebControl1.Series(1).GanttDrawMode = [ChartGanttDrawMode].AutoSizeMode] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 133: Gantt Chart with AutoSizeMode

**[]** 

{border="0"}

**[]** 

Figure 134: Gantt Chart with CustomPointWidthMode

**[]** 

See Also

[] 

[Gantt Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p108} 

[]{#related-topics}

