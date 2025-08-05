---
title: darklightpower1.md
original_path: WinForms_Docs/99_Uncategorized/darklightpower1.md
created_at: 2025-08-05
---






#### DarkLightPower {#darklightpower style="tab-stops: 0pt"}

 

Gets or sets the intensity of the dark and light colors used in DarkLight color mode.

 


+-------------------------------------+-------------------------------------+
|                                                                           |
|                                                                           |
| Details                                                                   |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Possible Values**                 | Ranges from 0 to 255 bytes          |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Default Value    **               | **100**                             |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **2D / 3D Limitations**             | No                                  |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Applies to Chart Element**        | All series                          |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Applies to Chart Types**          | Renko Chart (Financial Charts)      |
+-------------------------------------+-------------------------------------+


 

Here is some sample code.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [// Setting ColorsMode as DarkLight]                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [this][.chartControl1.Series\[0\].ConfigItems.FinancialItem.ColorsMode = [ChartFinancialColorMode].DarkLight;] |
|                                                                                                                                                                                                                          |
| [// Setting the power value of the darklight]                                                                                                                          |
|                                                                                                                                                                                                                          |
| [this][.chartControl1.Series\[0\].ConfigItems.FinancialItem.DarkLightPower = 200;]                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [\' Setting ColorsMode as DarkLight]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [Me][.chartControl1.Series(0).ConfigItems.FinancialItem.ColorsMode =[ ][ChartFinancialColorMode][.]DarkLight] |
|                                                                                                                                                                                                                                                                   |
| [\' Setting the power value of the darklight]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [Me][.chartControl1.Series(0).ConfigItems.FinancialItem.DarkLightPower = 200]                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{hspace="12" align="left"}\

**[]** 

Figure 110: Renko Chart with DarkLightPower set to 200**[]**

**[]** 

See Also

 

[Renko Chart]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p86} 

 

[]{#related-topics}

