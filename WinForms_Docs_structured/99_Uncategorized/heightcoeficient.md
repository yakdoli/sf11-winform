---
title: heightcoeficient.md
original_path: WinForms_Docs/99_Uncategorized/heightcoeficient.md
created_at: 2025-08-05
---






#### HeightCoeficient {#heightcoeficient style="tab-stops: 0pt"}

**[]** 

When in **3D** mode, the relative height of the pie chart can be specified via the property. Note that the **HeightByAreaDepth** property should be set as **false** for this to take effect.

[] 


+---------------------------------------+---------------------------------------+
| **[]**      |
|                                                                               |
| Details                                                                       |
+---------------------------------------+---------------------------------------+
| Possible Values                       | Valid Ranges From 0 to 1              |
+---------------------------------------+---------------------------------------+
| Default Value                         | 0.2                                   |
+---------------------------------------+---------------------------------------+
| 2D / 3D Limitations                   | 3D Only                               |
+---------------------------------------+---------------------------------------+
| Applies to Chart Element              | All series                            |
+---------------------------------------+---------------------------------------+
| Applies to Chart Types                | Pie Chart                             |
+---------------------------------------+---------------------------------------+


[] 

Here is the sample code.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| **[]**                                                                                                                                         |
|                                                                                                                                                                                                  |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.PieItem.HeightByAreaDepth = [false];] |
|                                                                                                                                                                                                  |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.PieItem.HeightCoeficient = 0.1f;]                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                             |
| [Me][.ChartWebControl1.Series(0).ConfigItems.PieItem.HeightByAreaDepth = [False]] |
|                                                                                                                                                                                             |
| [Me][.ChartWebControl1.Series(0).ConfigItems.PieItem.HeightCoeficient = 0.1f]                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 142: Pie Chart with HeightCoeficient property set to \"0.1f\"

**[]** 

See Also

[] 

[Pie Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p113} 

[]{#related-topics}

