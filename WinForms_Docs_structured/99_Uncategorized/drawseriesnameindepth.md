---
title: drawseriesnameindepth.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drawseriesnameindepth.md
created_at: 2025-07-03
---






#### DrawSeriesNameInDepth {#drawseriesnameindepth style="tab-stops: 0pt"}

**[]** 

This indicates whether to draw series name at opposed position to origin, along x-axis.

[] 


+---------------------------------------+---------------------------------------+
| **[]**      |
|                                                                               |
| Details                                                                       |
+---------------------------------------+---------------------------------------+
| Possible Values                       | True or False                         |
+---------------------------------------+---------------------------------------+
| Default Value                         | False                                 |
+---------------------------------------+---------------------------------------+
| 2D / 3D Limitations                   | 3D Only                               |
+---------------------------------------+---------------------------------------+
| Applies to Chart Element              | All series                            |
+---------------------------------------+---------------------------------------+
| Applies to Chart Types                | All chart types                       |
+---------------------------------------+---------------------------------------+


**[]** 

Here is some sample code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [// Specified 3D View]                                                                                                                       |
|                                                                                                                                                                                                |
| [this][.ChartWebControl1.Series3D = [true];]                                         |
|                                                                                                                                                                                                |
| [// Setting Text Format]                                                                                                                     |
|                                                                                                                                                                                                |
| [this][.ChartWebControl1.Series\[0\].Style.Font.FontStyle = [FontStyle].Underline;]  |
|                                                                                                                                                                                                |
| [this][.ChartWebControl1.Series\[0\].Style.TextColor = [Color].Black;]               |
|                                                                                                                                                                                                |
| [this][.ChartWebControl1.Series\[0\].Style.Font.Size = 7;]                                                |
|                                                                                                                                                                                                |
| [this][.ChartWebControl1.Series\[0\].Style.Font.Facename = [\"Times New Roman\"];] |
|                                                                                                                                                                                                |
| [// Set SeriesNameDepth as True]                                                                                                             |
|                                                                                                                                                                                                |
| [this][.ChartWebControl1.Series\[0\].DrawSeriesNameInDepth = [true];]                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                 |
|                                                                                                                                                                                                    |
| **[]**                                                                                                                                           |
|                                                                                                                                                                                                    |
| [\' Specified 3D View]                                                                                                                           |
|                                                                                                                                                                                                    |
| [Me][.ChartWebControl1.Series3D = [True]]                                                |
|                                                                                                                                                                                                    |
| [\' Setting Text Format]                                                                                                                         |
|                                                                                                                                                                                                    |
| [Me][.ChartWebControl1.Series(0).Style.Font.FontStyle = [FontStyle].Underline]           |
|                                                                                                                                                                                                    |
| [Me][.ChartWebControl1.Series(0).Style.TextColor = [Color][.]Black] |
|                                                                                                                                                                                                    |
| [Me][.ChartWebControl1.Series(0).Style.Font.Size = 7]                                                         |
|                                                                                                                                                                                                    |
| [Me][.ChartWebControl1.Series(0).Style.Font.Facename = [\"Times New Roman\"]]          |
|                                                                                                                                                                                                    |
| [\' Set SeriesNameDepth as True]                                                                                                                 |
|                                                                                                                                                                                                    |
| [Me][.ChartWebControl1.Series(0).DrawSeriesNameInDepth = [True]]                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 116: DrawSeriesNameInDepth in BarChart

**[]** 

See Also

[] 

[Chart Types]{.UGHyperlink}[]{.UGHyperlink}

[]{#p95} 

[]{#related-topics}

