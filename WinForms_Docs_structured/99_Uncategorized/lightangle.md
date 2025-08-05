---
title: lightangle.md
original_path: WinForms_Docs/99_Uncategorized/lightangle.md
created_at: 2025-08-05
---






#### LightAngle {#lightangle style="tab-stops: 0pt"}

**[     ]**

Specifies the light angle in horizontal plane.

[] 


+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                                |
| Details                                                                                                                                                                                                        |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Possible Values                       | Any double value                                                                                                                                                       |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default Value                         | -0.785398163397448                                                                                                                                                     |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2D / 3D Limitations                   | No                                                                                                                                                                     |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Applies to Chart Element              | Any Series                                                                                                                                                             |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Applies to Chart Types                | Column Charts , Bar Charts, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart, Candle Chart, Hilo Chart(3D), HiloOpenClose(3D) |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

Here is code snippet using **LightAngle** in Column Chart.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| **[]**                                                                                                                         |
|                                                                                                                                                                                  |
| [// Specifies light angle of both the series]                                                                                  |
|                                                                                                                                                                                  |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.ColumnItem.LightAngle = 45;] |
|                                                                                                                                                                                  |
| [this][.ChartWebControl1.Series\[1\].ConfigItems.ColumnItem.LightAngle = 45;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                  |
|                                                                                                                                                                                     |
| **[]**                                                                                                                            |
|                                                                                                                                                                                     |
| [\' Specifies light angle of both the series]                                                                                     |
|                                                                                                                                                                                     |
| [Private Me][.ChartWebControl1.Series(0).ConfigItems.ColumnItem.LightAngle =45]  |
|                                                                                                                                                                                     |
| [Private Me][.ChartWebControl1.Series(1).ConfigItems.ColumnItem.LightAngle = 45] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 154: Light Angle set to \"45\" with 3D Effect

[] 

{border="0"}

**[]** 

Figure 155: Light Angle set to \"30\" with 3D Effect

**[]** 

See Also

**[]** 

[Pyramid Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Funnel Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Area Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Bar Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Bubble Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Column Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Candle Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Renko chart]{.UGHyperlink}[, ]{.UGHyperlink}[Three Line Break Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Box and Whisker Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Gantt Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Histogram Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Tornado Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Polar and Radar Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Pie Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p123} 

[]{#related-topics}

