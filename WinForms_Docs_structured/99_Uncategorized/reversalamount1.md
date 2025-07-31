---
title: reversalamount1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\reversalamount1.md
created_at: 2025-07-03
---






#### ReversalAmount {#reversalamount style="tab-stops: 0pt"}

 

Gets or sets the reversal amount for financial charts.

 


+-------------------------------------+-------------------------------------------------------------------------+
|                                                                                                               |
|                                                                                                               |
| Details                                                                                                       |
+-------------------------------------+-------------------------------------------------------------------------+
| **Possible Values**                 | Any numeric value                                                       |
+-------------------------------------+-------------------------------------------------------------------------+
| **Default Value    **               | **1**                                                                   |
+-------------------------------------+-------------------------------------------------------------------------+
| **2D / 3D Limitations**             | No                                                                      |
+-------------------------------------+-------------------------------------------------------------------------+
| **Applies to Chart Element**        | Any Series                                                              |
+-------------------------------------+-------------------------------------------------------------------------+
| **Applies to Chart Types**          | Kagi Chart, Three Line Break Chart, Point and Figure Chart, Renko Chart |
+-------------------------------------+-------------------------------------------------------------------------+


 

Here is code snippet using ReversalAmount in Renko Chart.

 

{border="0"}

 

Figure 185: Renko Chart with default ReversalAmount = \"1\"

 

+--------------------------------------------------------------------------------+
| **[\[C#\]]**                 |
|                                                                                |
| **[]**                       |
|                                                                                |
| [series.ReversalAmount = 3;] |
+--------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                       |
|                                                                                                                                          |
| **[]**                                                                                 |
|                                                                                                                                          |
| [Private][ series.ReversalAmount = 3] |
+------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 186: Renko Chart with ReversalAmount = \"3\"

 

 

See Also

 

[]{#p139}[[Kagi Chart]]{.UGHyperlink}, [Point and Figure Chart]{.UGHyperlink}, [Three Line Break Chart]{.UGHyperlink}, [Renko Chart]{.UGHyperlink}

 

 

[]{#related-topics}

