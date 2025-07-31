---
title: heightbyareadepth1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\heightbyareadepth1.md
created_at: 2025-07-03
---






#### HeightByAreaDepth {#heightbyareadepth style="tab-stops: 0pt"}

 

Indicates whether to draw series using the **ChartArea.Depth** property.

 


+-------------------------------------+-------------------------------------+
|                                                                           |
|                                                                           |
| Details                                                                   |
+-------------------------------------+-------------------------------------+
| **Possible Values**                 | True or False                       |
+-------------------------------------+-------------------------------------+
| **Default Value    **               | **False**                           |
+-------------------------------------+-------------------------------------+
| **2D / 3D Limitations**             | 3D Only                             |
+-------------------------------------+-------------------------------------+
| **Applies to Chart Element**        | All series                          |
+-------------------------------------+-------------------------------------+
| **Applies to Chart Types**          | Pie Chart                           |
+-------------------------------------+-------------------------------------+


 

Here is some sample code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| **[]**                                                                                                                                     |
|                                                                                                                                                                                              |
| [this][.chartControl1.Series\[0\].ConfigItems.PieItem.HeightByAreaDepth = [true];] |
|                                                                                                                                                                                              |
| [this][.chartControl1.ChartArea.Depth = 25f;]                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                      |
|                                                                                                                                                                                         |
| **[]**                                                                                                                                |
|                                                                                                                                                                                         |
| [Me][.chartControl1.Series(0).ConfigItems.PieItem.HeightByAreaDepth = [True]] |
|                                                                                                                                                                                         |
| [Me][.chartControl1.ChartArea.Depth = 25f]                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 145: Pie Chart with Default Dimension

 

{border="0"}

 

Figure 146: Pie Chart with HeightByAreaDepth Enabled

 

See Also

 

[Pie Chart]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p111} 

[]{#related-topics}

