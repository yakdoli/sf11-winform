---
title: howtodrawtheyaxisatthecenterofthexaxis.md
original_path: WinForms_Docs/99_Uncategorized/howtodrawtheyaxisatthecenterofthexaxis.md
created_at: 2025-08-05
---








  









## How to draw the Y-axis at the center of the X-axis {#how-to-draw-the-y-axis-at-the-center-of-the-x-axis style="tab-stops: 0pt"}

 

The y-axis can be drawn at any custom position using the **ChartAxisLocationType** class. This can be achieved by setting the value of the **LocationType** property of the PrimaryYAxis to **Set**.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| **[]**                                                                                                                                     |
|                                                                                                                                                                                              |
| [// Drawing Y-axis at the center of the X-axis.]                                                                                           |
|                                                                                                                                                                                              |
| [this][.chartControl1.PrimaryYAxis.LocationType = [ChartAxisLocationType].Set;] |
|                                                                                                                                                                                              |
| [this][.chartControl1.PrimaryYAxis.Location = [new] PointF(300, 352);]             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                            |
|                                                                                                                                                                               |
| **[]**                                                                                                                      |
|                                                                                                                                                                               |
| [// Drawing Y-axis at the center of the X-axis.]                                                                            |
|                                                                                                                                                                               |
| [Me][.chartControl1.PrimaryYAxis.LocationType=ChartAxisLocationType.Set]                 |
|                                                                                                                                                                               |
| [Me][.chartControl1.PrimaryYAxis.Location = [New] PointF(300, 352)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p283} 

[]{#related-topics}

