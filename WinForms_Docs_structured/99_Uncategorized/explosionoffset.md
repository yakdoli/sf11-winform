---
title: explosionoffset.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\explosionoffset.md
created_at: 2025-07-03
---






#### ExplosionOffset {#explosionoffset style="tab-stops: 0pt"}

**[]** 

Gets / sets the offset value that is to be used when slices are to be exploded in a pie chart.

[] 


+--------------------------+---------------------------+
| Details                                              |
+--------------------------+---------------------------+
| Possible Values          | Float type values         |
+--------------------------+---------------------------+
| Default Value            | 20                        |
+--------------------------+---------------------------+
| 2D / 3D Limitations      | No                        |
+--------------------------+---------------------------+
| Applies to Chart Element | All series                |
+--------------------------+---------------------------+
| Applies to Chart Types   | Pie Chart, Doughnut Chart |
+--------------------------+---------------------------+


**[]** 

Here is some sample code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| **[]**                                                                                                              |
|                                                                                                                                                                       |
| [this][.ChartWebControl1.Series\[0\].ExplodedAll = [true];] |
|                                                                                                                                                                       |
| [this][.ChartWebControl1.Series\[0\].ExplosionOffset = 30f;]                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| **[]**                                                                                                           |
|                                                                                                                                                                    |
| [Me][.ChartWebControl1.Series\[0\].ExplodedAll = [True]] |
|                                                                                                                                                                    |
| [Me][.ChartWebControl1.Series(0).ExplosionOffset = 30f]                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 122: Exploded Pie Chart

**[]** 

See Also

**[]** 

[Pie Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Doughnut Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p102} 

[]{#related-topics}

