---
title: columndrawmode1.md
original_path: WinForms_Docs/99_Uncategorized/columndrawmode1.md
created_at: 2025-08-05
---






#### ColumnDrawMode {#columndrawmode style="tab-stops: 0pt"}

 

Indicates the drawing mode of columns in charts when there are multiple series.

 


+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                |
|                                                                                                                                                                |
| Details                                                                                                                                                        |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **Possible Values**                 | [·      ]**InDepthMode** - Columns from different series are drawn at different depths.     |
|                                     |                                                                                                                          |
|                                     | [·      ]**PlaneMode** - Columns from all series are drawn side-by-side.                    |
|                                     |                                                                                                                          |
|                                     | [·      ]**ClusteredMode** - Columns from all series are drawn in depth with the same size. |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **Default Value    **               | **InDepthMode**                                                                                                          |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **2D / 3D Limitations**             | 3D only                                                                                                                  |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Element**        | All Series                                                                                                               |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Types**          | Column Chart, ColumnRange Chart,Bar Chart, BoxAndWhisker Chart, Gantt Chart                                              |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+


 

Here is the sample code snippet using **ColumnDrawMode** in Column Chart.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                     |
|                                                                                                                                                                                    |
| **[]**                                                                                                                           |
|                                                                                                                                                                                    |
| [this][.chartControl1.ColumnDrawMode = [ChartColumnDrawMode].PlaneMode;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                              |
|                                                                                                                                                                                 |
| **[]**                                                                                                                        |
|                                                                                                                                                                                 |
| [Me][.chartControl1.ColumnDrawMode = [ChartColumnDrawMode].PlaneMode] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 100: ColumnDrawMode set to \"PlaneMode\"

 

{border="0"}

 

Figure 101: ColumnDrawMode set to \"InDepthMode\"

 

{border="0"}

 

Figure 102: ColumnDrawMode set to \"ClusteredMode\"

 

See Also

 

[Column Chart]{.UGHyperlink}, [ColumnRange Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Bar Chart]{.UGHyperlink}, [BoxAndWhisker Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Gantt Chart]{.UGHyperlink}[]

 

[]{#p81} 

[]{#related-topics}

