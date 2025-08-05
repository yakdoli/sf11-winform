---
title: drawseriesnameindepth1.md
original_path: WinForms_Docs/99_Uncategorized/drawseriesnameindepth1.md
created_at: 2025-08-05
---






#### DrawSeriesNameInDepth {#drawseriesnameindepth style="tab-stops: 0pt"}

 

Indicates whether to draw series name at opposed position to origin, along x-axis.

 


+-------------------------------------+-------------------------------------+
|                                                                           |
|                                                                           |
| Details                                                                   |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Possible Values**                 | True or False                       |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Default Value    **               | **False**                           |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **2D / 3D Limitations**             | 3D Only                             |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Applies to Chart Element**        | All series                          |
+-------------------------------------+-------------------------------------+
|                                     |                                     |
|                                     |                                     |
| **Applies to Chart Types**          | All chart types                     |
+-------------------------------------+-------------------------------------+


 

Here is some sample code.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                             |
| [// Specified 3D View]                                                                                                                    |
|                                                                                                                                                                                             |
| [this][.chartControl1.Series3D = [true];]                                         |
|                                                                                                                                                                                             |
| [// Setting Text Format]                                                                                                                  |
|                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].Style.Font.FontStyle = [FontStyle].Underline;]  |
|                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].Style.TextColor = [Color].Black;]               |
|                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].Style.Font.Size = 7;]                                                |
|                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].Style.Font.Facename = [\"Times New Roman\"];] |
|                                                                                                                                                                                             |
| [// Set SeriesNameDepth as True]                                                                                                          |
|                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].DrawSeriesNameInDepth = [true];]                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [\' Specified 3D View]                                                                                                                        |
|                                                                                                                                                                                                 |
| [Me][.chartControl1.Series3D = [True]]                                                |
|                                                                                                                                                                                                 |
| [\' Setting Text Format]                                                                                                                      |
|                                                                                                                                                                                                 |
| [Me][.chartControl1.Series(0).Style.Font.FontStyle = [FontStyle].Underline]           |
|                                                                                                                                                                                                 |
| [Me][.chartControl1.Series(0).Style.TextColor = [Color][.]Black] |
|                                                                                                                                                                                                 |
| [Me][.chartControl1.Series(0).Style.Font.Size = 7]                                                         |
|                                                                                                                                                                                                 |
| [Me][.chartControl1.Series(0).Style.Font.Facename = [\"Times New Roman\"]]          |
|                                                                                                                                                                                                 |
| [\' Set SeriesNameDepth as True]                                                                                                              |
|                                                                                                                                                                                                 |
| [Me][.chartControl1.Series(0).DrawSeriesNameInDepth = [True]]                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 120: DrawSeriesNameInDepth in BarChart

**[]** 

See Also

 

[Chart Types]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p93} 

[]{#related-topics}

