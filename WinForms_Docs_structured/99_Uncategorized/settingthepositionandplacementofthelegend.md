---
title: settingthepositionandplacementofthelegend.md
original_path: WinForms_Docs/99_Uncategorized/settingthepositionandplacementofthelegend.md
created_at: 2025-08-05
---






#### Setting the Position and Placement of the Legend {#setting-the-position-and-placement-of-the-legend style="tab-stops: 0pt"}

 

The legend can be positioned possibly on top, bottom, left or right based on the value assigned to the Position property of legend as well as inside or outside the chart area, which is set using the LegendsPlacement property. ShowLegend property enables the appearance of Legend.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                           |
| [this][.olapChart1.ShowLegend = [true];][] |
|                                                                                                                                                                                                           |
| [this][. olapChart1.Legend.Position = ChartDock.Top;][]            |
|                                                                                                                                                                                                           |
| [this][.olapChart1.LegendsPlacement = [ChartPlacement].Inside;]                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
| [Me][.olapChart1.ShowLegend = [True]][]                                 |
|                                                                                                                                                                                                                                        |
| [Me][. olapChart1.Legend.Position = ChartDock.Top]                                                                                                |
|                                                                                                                                                                                                                                        |
| [Me][.olapChart1.LegendsPlacement = [ChartPlacement].Inside][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"} 

 

Figure 15: Legend Position - Top

[]{#related-topics}

