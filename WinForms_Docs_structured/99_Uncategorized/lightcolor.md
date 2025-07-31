---
title: lightcolor.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\lightcolor.md
created_at: 2025-07-03
---






#### LightColor {#lightcolor style="tab-stops: 0pt"}

**[]** 

Specifies the color of light for all shading modes except ChartColumnShadingMode.FlatRectangle.

[] 


+--------------------------+----------------------------------------------------------------------------------------------------------+
| Details                                                                                                                             |
+--------------------------+----------------------------------------------------------------------------------------------------------+
| Possible Values          | A Color object                                                                                           |
+--------------------------+----------------------------------------------------------------------------------------------------------+
| Default Value            | Color.White                                                                                              |
+--------------------------+----------------------------------------------------------------------------------------------------------+
| 2D / 3D Limitations      | No                                                                                                       |
+--------------------------+----------------------------------------------------------------------------------------------------------+
| Applies to Chart Element | Any Series                                                                                               |
+--------------------------+----------------------------------------------------------------------------------------------------------+
| Applies to Chart Types   | Column Chart, Bar Chart, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Radar Chart |
+--------------------------+----------------------------------------------------------------------------------------------------------+


**[]** 

Here is sample code snippet using **LightColor** in Column Chart.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                 |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.ColumnItem.LightColor = ][Color][.Blue;] |
|                                                                                                                                                                                                                                                                                                 |
| [this][.ChartWebControl1.Series\[1\].ConfigItems.ColumnItem.LightColor =][Color][.Green;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [Private Me][.ChartWebControl1.Series(0).ConfigItems.ColumnItem.LightColor = ][Color][.Blue]  |
|                                                                                                                                                                                                                                                                                                     |
| [Private Me][.ChartWebControl1.Series(1).ConfigItems.ColumnItem.LightColor = ][Color][.Green] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 156: LightColor applied to Chart Series

***[]*** 

See Also

[Pyramid Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Funnel Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Area Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Bar Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Bubble Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Column Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Candle Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Renko chart]{.UGHyperlink}[, ]{.UGHyperlink}[Three Line Break Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Box and Whisker Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Gantt Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Histogram Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Tornado Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Polar and Radar Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Pie Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p124} 

[]{#related-topics}

