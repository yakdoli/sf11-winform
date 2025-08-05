---
title: fillmode.md
original_path: WinForms_Docs/99_Uncategorized/fillmode.md
created_at: 2025-08-05
---






#### FillMode {#fillmode style="tab-stops: 0pt"}

[] 

Specifies how the slice interior should be filled with gradient colors.

[] 


+-------------------------------------+----------------------------------------------------------------+
| Details                                                                                              |
+-------------------------------------+----------------------------------------------------------------+
| Possible Values                     | AllPie - Controls the interior shape style of All PieItem.     |
|                                     |                                                                |
|                                     | EveryPie - Controls the interior shape style of Every PieItem. |
+-------------------------------------+----------------------------------------------------------------+
| Default Value                       | AllPie                                                         |
+-------------------------------------+----------------------------------------------------------------+
| 2D / 3D Limitations                 | No                                                             |
+-------------------------------------+----------------------------------------------------------------+
| Applies to Chart Element            | All series                                                     |
+-------------------------------------+----------------------------------------------------------------+
| Applies to Chart Types              | Pie Chart                                                      |
+-------------------------------------+----------------------------------------------------------------+


**[]** 

Here is some sample code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| **[]**                                                                                                                                                    |
|                                                                                                                                                                                                             |
| [// Setting Pietype]                                                                                                                                      |
|                                                                                                                                                                                                             |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.PieItem.PieType = [ChartPieType].Round;]         |
|                                                                                                                                                                                                             |
| [// Setting the interiors of shapes in this GraphicsPath object are filled.]                                                                              |
|                                                                                                                                                                                                             |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.PieItem.FillMode = [ChartPieFillMode].EveryPie;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [\' Setting Pietype]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [Me][.ChartWebControl1.Series(0).ConfigItems.PieItem.PieType = [ChartPieType][.]Round]                                |
|                                                                                                                                                                                                                                                      |
| [\' Setting the interiors of shapes in this GraphicsPath object are filled.]                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| [Me][.ChartWebControl1.Series(0).ConfigItems.PieItem.FillMode =[ ][ChartPieFillMode][.]EveryPie] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 128: Pie Chart with \"EveryPie\" FillMode

**[]** 

{border="0"}

**[]** 

Figure 129: Pie Chart with \"AllPie\" FillMode

**[]** 

See Also

[] 

[Pie Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p105} 

[]{#related-topics}

