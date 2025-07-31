---
title: howtospecifythepositionforafloatinglegend1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtospecifythepositionforafloatinglegend1.md
created_at: 2025-07-03
---








  









## How to specify the position for a Floating Legend {#how-to-specify-the-position-for-a-floating-legend style="tab-stops: 0pt"}

  

When the **LegendPosition** property of the ChartControl is set to **ChartDock.Floating**, the position of the legend defaults to the top-right corner of the ChartArea. Once this is done, you can specify the coordinates via the **Legend.Location** property of the ChartLegend.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                       |
|                                                                                                                                                                            |
| [this][.chartControl1.LegendPosition = [ChartDock].Floating;] |
|                                                                                                                                                                            |
| [this][.chartControl1.Legend.Location = [new] Point(20,20);]     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                  |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [Me][.ChartControl1.LegendPosition = ChartDock.Floating]                       |
|                                                                                                                                                                     |
| [Me][.ChartControl1.Legend.Location = [New] Point(20,20)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

See Also

 

[Chart Legend]{.UGHyperlink}[]{.UGHyperlink}

[]{#p293} 

[]{#related-topics}

