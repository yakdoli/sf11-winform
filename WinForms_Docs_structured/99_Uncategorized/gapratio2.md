---
title: gapratio2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\gapratio2.md
created_at: 2025-07-03
---






#### GapRatio {#gapratio style="tab-stops: 0pt"}

 

Gets or sets the gap size between funnel chart or pyramid chart segments. Default value is 0.0. The maximum gap size is limited by the number of points.

 


+------------------------------+-----------------------------+
| Details                                                    |
+------------------------------+-----------------------------+
| **Possible Values**          | Ranges from 0.0             |
+------------------------------+-----------------------------+
| **Default Value    **        | **0**                       |
+------------------------------+-----------------------------+
| **2D / 3D Limitations**      | No                          |
+------------------------------+-----------------------------+
| **Applies to Chart Element** | All series                  |
+------------------------------+-----------------------------+
| **Applies to Chart Types**   | Funnel Chart, Pyramid Chart |
+------------------------------+-----------------------------+


 

Here is some sample code.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| **[]**                                                                                                         |
|                                                                                                                                                                  |
| [// Setting GapRatio for Funnel Chart]                                                                         |
|                                                                                                                                                                  |
| [this][.chartControl1.Series\[0\].ConfigItems.FunnelItem.GapRatio = 0.1f;]  |
|                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                  |
| [// Setting GapRatio for Pyramid Chart]                                                                        |
|                                                                                                                                                                  |
| [this][.chartControl1.Series\[0\].ConfigItems.PyramidItem.GapRatio = 0.1f;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| **[]**                                                                                                    |
|                                                                                                                                                             |
| [\' Setting GapRatio for Funnel Chart]                                                                    |
|                                                                                                                                                             |
| [Me][.chartControl1.Series(0).ConfigItems.FunnelItem.GapRatio = 0.1f]  |
|                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                             |
| [\' Setting GapRatio for Pyramid Chart]                                                                   |
|                                                                                                                                                             |
| [Me][.chartControl1.Series(0).ConfigItems.PyramidItem.GapRatio = 0.1f] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 140: Funnel chart with 0.1 GapRatio

 

   {border="0"}

 

Figure 141: Pyramid chart with 0.1 GapRatio

 

See Also

 

[Pyramid Chart]{.UGHyperlink}, [Funnel Chart]{.UGHyperlink}[]

 

[]{#p108} 

[]{#related-topics}

