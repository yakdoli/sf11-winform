---
title: showdatabindlabels.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\showdatabindlabels.md
created_at: 2025-07-03
---






#### ShowDataBindLabels {#showdatabindlabels style="tab-stops: 0pt"}

[] 

Indicates whether data bound labels are displayed in the chart.

[] 


+-------------------------------------+------------------------------------------------------------+
| Details                                                                                          |
+-------------------------------------+------------------------------------------------------------+
| Possible Values                     | True - Displays the databind labels.                       |
|                                     |                                                            |
|                                     | False - Hides the databind labels.                         |
+-------------------------------------+------------------------------------------------------------+
| Default Value                       | False                                                      |
+-------------------------------------+------------------------------------------------------------+
| 2D / 3D Limitations                 | No                                                         |
+-------------------------------------+------------------------------------------------------------+
| Applies to Chart Element            | All Series                                                 |
+-------------------------------------+------------------------------------------------------------+
| Applies to Chart Types              | Pie Chart, Doughnut Chart, Funnel Chart and Pyramid chart. |
+-------------------------------------+------------------------------------------------------------+


**[]** 

Here is sample code snippet using ShowDataPointLabels.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [//For Pie Chart]                                                                                                                                  |
|                                                                                                                                                                                                      |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.PieItem.ShowDataBindLabels = [true];]     |
|                                                                                                                                                                                                      |
| [//For Funnel Chart]                                                                                                                               |
|                                                                                                                                                                                                      |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.FunnelItem.ShowDataBindLabels = [true];]  |
|                                                                                                                                                                                                      |
| [//For Pyramid Chart]                                                                                                                              |
|                                                                                                                                                                                                      |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.PyramidItem.ShowDataBindLabels = [true];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [\'For Pie Chart]                                                                                                                             |
|                                                                                                                                                                                                 |
| [Me][.ChartWebControl1.Series(0).ConfigItems.PieItem.ShowDataBindLabels = [True]]     |
|                                                                                                                                                                                                 |
| [\'For Funnel Chart]                                                                                                                          |
|                                                                                                                                                                                                 |
| [Me][.ChartWebControl1.Series(0).ConfigItems.FunnelItem.ShowDataBindLabels = [True]]  |
|                                                                                                                                                                                                 |
| [\'For Pyramid Chart]                                                                                                                         |
|                                                                                                                                                                                                 |
| [Me][.ChartWebControl1.Series(0).ConfigItems.PyramidItem.ShowDataBindLabels = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 191: Doughnut Chart with Databound Labels

**[]** 

{border="0"}

**[]** 

Figure 192: Funnel Chart with Databound Labels

**[]** 

{border="0"}

**[]** 

Figure 193: Pyramid Chart with Databound Labels

**[]** 

See Also

[] 

[Pie Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Doughnut Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Funnel Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Pyramid Chart]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p148} 

[]{#related-topics}

