---
title: showdatabindlabels1.md
original_path: WinForms_Docs/03_Data_Binding/showdatabindlabels1.md
created_at: 2025-08-05
---






#### ShowDataBindLabels {#showdatabindlabels style="tab-stops: 0pt"}

 

Indicates whether data bound labels are displayed in the chart.

 


+-------------------------------------+----------------------------------------------------------------------------+
| Details                                                                                                          |
+-------------------------------------+----------------------------------------------------------------------------+
| **Possible Values**                 | [·      ]True - Displays the databind labels. |
|                                     |                                                                            |
|                                     | [·      ]False - Hides the databind labels.   |
+-------------------------------------+----------------------------------------------------------------------------+
| **Default Value    **               | **False**                                                                  |
+-------------------------------------+----------------------------------------------------------------------------+
| **2D / 3D Limitations**             | No                                                                         |
+-------------------------------------+----------------------------------------------------------------------------+
| **Applies to Chart Element**        | All Series                                                                 |
+-------------------------------------+----------------------------------------------------------------------------+
| **Applies to Chart Types**          | Pie Chart, Doughnut Chart, Funnel Chart and Pyramid chart.                 |
+-------------------------------------+----------------------------------------------------------------------------+


 

Here is sample code snippet using ShowDataPointLabels.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [//For Pie Chart]                                                                                                                              |
|                                                                                                                                                                                                  |
| [this][.chartControl.Series\[0\].ConfigItems.PieItem.ShowDataBindLabels = [true];]     |
|                                                                                                                                                                                                  |
| [//For Funnel Chart]                                                                                                                           |
|                                                                                                                                                                                                  |
| [this][.chartControl.Series\[0\].ConfigItems.FunnelItem.ShowDataBindLabels = [true];]  |
|                                                                                                                                                                                                  |
| [//For Pyramid Chart]                                                                                                                          |
|                                                                                                                                                                                                  |
| [this][.chartControl.Series\[0\].ConfigItems.PyramidItem.ShowDataBindLabels = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                             |
| [\'For Pie Chart]                                                                                                                         |
|                                                                                                                                                                                             |
| [Me][.chartControl.Series(0).ConfigItems.PieItem.ShowDataBindLabels = [True]]     |
|                                                                                                                                                                                             |
| [\'For Funnel Chart]                                                                                                                      |
|                                                                                                                                                                                             |
| [Me][.chartControl.Series(0).ConfigItems.FunnelItem.ShowDataBindLabels = [True]]  |
|                                                                                                                                                                                             |
| [\'For Pyramid Chart]                                                                                                                     |
|                                                                                                                                                                                             |
| [Me][.chartControl.Series(0).ConfigItems.PyramidItem.ShowDataBindLabels = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 197: Doughnut Chart with Data-Bound Labels

 

{border="0"}

 

Figure 198: Funnel Chart with Data-Bound Labels

 

 

{border="0"}

 

Figure 199: Pyramid Chart with Data-Bound Labels

 

See Also

 

Pie Chart, Doughnut Chart, Funnel Chart, Pyramid Chart

 

[]{#p147} 

[]{#related-topics}

