---
title: radartype2.md
original_path: WinForms_Docs/99_Uncategorized/radartype2.md
created_at: 2025-08-05
---






#### Radar Type {#radar-type style="tab-stops: 0pt"}

 

Indicates the type of radar chart to be rendered.

 


+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                          |
|                                                                                                                                                                                          |
| Details                                                                                                                                                                                  |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Possible Values**                 | [·      ]**Area** - Renders the radar chart such that the points are connected and the enclosed region is not filled. |
|                                     |                                                                                                                                                    |
|                                     | [·      ]**Line** - Renders the radar chart such that the points are connected but the enclosed region is not filled. |
|                                     |                                                                                                                                                    |
|                                     | [·      ]**Symbol** - Points are rendered with the associated symbols                                                 |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default Value    **               | **Area**                                                                                                                                           |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **2D / 3D Limitations**             | No                                                                                                                                                 |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Element**        | Any series                                                                                                                                         |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Types**          | Polar and Radar Chart                                                                                                                              |
+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+


 

Here is code snippet using RadarType.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                      |
| [this][.chartControl1.Series\[0\].ConfigItems.RadarItem.Type = ][ChartRadarDrawType][.Symbol;] |
|                                                                                                                                                                                                                                                                                                      |
| [this][.chartControl1.Series\[1\].ConfigItems.RadarItem.Type = ][ChartRadarDrawType][.Symbol;] |
|                                                                                                                                                                                                                                                                                                      |
| [this][.chartControl1.Series\[0\].Style.Symbol.Shape = ][ChartSymbolShape][.Star;]             |
|                                                                                                                                                                                                                                                                                                      |
| [this][.chartControl1.Series\[1\].Style.Symbol.Shape = ][ChartSymbolShape][.Star;]             |
|                                                                                                                                                                                                                                                                                                      |
| [this][.chartControl1.Series\[0\].Style.Symbol.Color =][ Color][.Blue;]                        |
|                                                                                                                                                                                                                                                                                                      |
| [this][.chartControl1.Series\[1\].Style.Symbol.Color = ][Color][.Green;]                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                         |
| [Private Me][.chartControl1.Series(0).ConfigItems.RadarItem.Type = ][ChartRadarDrawType][.Symbol] |
|                                                                                                                                                                                                                                                                                                         |
| [Private Me][.chartControl1.Series(1).ConfigItems.RadarItem.Type = ][ChartRadarDrawType][.Symbol] |
|                                                                                                                                                                                                                                                                                                         |
| [Private Me][.chartControl1.Series(0).Style.Symbol.Shape = ][ChartSymbolShape][.Star]             |
|                                                                                                                                                                                                                                                                                                         |
| [Private Me][.chartControl1.Series(1).Style.Symbol.Shape =][ ChartSymbolShape][.Star]             |
|                                                                                                                                                                                                                                                                                                         |
| [Private Me][.chartControl1.Series(0).Style.Symbol.Color = ][Color][.Blue]                        |
|                                                                                                                                                                                                                                                                                                         |
| [Private Me][.chartControl1.Series(1).Style.Symbol.Color =][ Color][.Green]                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 181: Radar Chart

**[]** 

See Also

 

[Polar and Radar Charts]{.UGHyperlink}[]

 

[]{#p136} 

 

[]{#related-topics}

