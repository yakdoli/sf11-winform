---
title: doughnutcoeficient1.md
original_path: WinForms_Docs/99_Uncategorized/doughnutcoeficient1.md
created_at: 2025-08-05
---






#### DoughnutCoeficient {#doughnutcoeficient style="tab-stops: 0pt"}

 

Specifies the percentage of the overall radius of the chart that will be used for the Doughnut center hole. For example, if it is set to 0, the doughnut hole will not exist, therefore, the chart will look like a Pie chart.

 


+-------------------------------------+-------------------------------------+
|                                                                           |
|                                                                           |
| Details                                                                   |
+-------------------------------------+-------------------------------------+
| **Possible Values**                 | Ranges from 0.0 to 0.9              |
+-------------------------------------+-------------------------------------+
| **Default Value    **               | **0**                               |
+-------------------------------------+-------------------------------------+
| **2D / 3D Limitations**             | No.                                 |
+-------------------------------------+-------------------------------------+
| **Applies to Chart Element**        | All series.                         |
+-------------------------------------+-------------------------------------+
| **Applies to Chart Types**          | Doughnut Chart, Pie Chart.          |
+-------------------------------------+-------------------------------------+


 

PieCharts with a **DoughnutCoeficient** specified will be rendered as doughnuts. By default, this value is set to 0.0 and hence the chart will be rendered as a full pie.

 

The DoughnutCoeficient property specifies the fraction of the radius occupied by the doughnut whole. Hence the value can range from 0.0 to 0.9.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| **[]**                                                                                                               |
|                                                                                                                                                                        |
| [this][.chartControl1.Series\[0\].ConfigItems.PieItem.DoughnutCoeficient = 0.5f;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                |
|                                                                                                                                                                   |
| **[]**                                                                                                          |
|                                                                                                                                                                   |
| [Me][.chartControl1.Series(0).ConfigItems.PieItem.DoughnutCoeficient = 0.5f] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 114: Pie Chart with DoughnutCoeficient Property Set

 

See Also

 

[Doughnut Chart]{.UGHyperlink}, [Pie Chart]{.UGHyperlink}[]

 

[]{#p89} 

[]{#related-topics}

