---
title: howtospecifythepositionforafloatinglegend.md
original_path: WinForms_Docs/99_Uncategorized/howtospecifythepositionforafloatinglegend.md
created_at: 2025-08-05
---








  









## How to specify the position for a Floating Legend? {#how-to-specify-the-position-for-a-floating-legend style="tab-stops: 0pt"}

[   ]

When the **LegendPosition** property of the ChartControl is set to **ChartDock.Floating**, the position of the legend defaults to the top-right corner of the ChartArea. Once this is done, you can specify the coordinates via the **Legend.Location** property of the ChartLegend.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [this][.ChartWebControl1.LegendPosition = [ChartDock].Floating;] |
|                                                                                                                                                                               |
| [this][.ChartWebControl1.Legend.Location = [new] Point(20,20);]     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                        |
| []                                                                                                                   |
|                                                                                                                                                                        |
| [Me][.ChartWebControl1.LegendPosition = ChartDock.Floating]                       |
|                                                                                                                                                                        |
| [Me][.ChartWebControl1.Legend.Location = [New] Point(20,20)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[See Also]**

[] 

[Chart Legend]{.UGHyperlink}[]{.UGHyperlink}

[]{#p285} 

[]{#related-topics}

