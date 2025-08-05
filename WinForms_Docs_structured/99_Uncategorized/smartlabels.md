---
title: smartlabels.md
original_path: WinForms_Docs/99_Uncategorized/smartlabels.md
created_at: 2025-08-05
---






#### SmartLabels {#smartlabels style="tab-stops: 0pt"}

**[]** 

Specifies the behavior of the labels. If set to true, the labels will be rendered to avoid overlap with other labels.

[] 


+---------------------------------------+---------------------------------------+
| **[]**      |
|                                                                               |
| Details                                                                       |
+---------------------------------------+---------------------------------------+
| Possible Values                       | True  -  Enables smart labels         |
|                                       |                                       |
|                                       | False -  Disables smart labels        |
+---------------------------------------+---------------------------------------+
| Default Value                         | False                                 |
+---------------------------------------+---------------------------------------+
| 2D / 3D Limitations                   | No                                    |
+---------------------------------------+---------------------------------------+
| Applies to Chart Element              | Any Series                            |
+---------------------------------------+---------------------------------------+
| Applies to Chart Types                | All chart types                       |
+---------------------------------------+---------------------------------------+


**[]** 

[] 

Here is sample code snippet using Smart Labels in ColumnChart.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [this][.ChartWebControl1.Series\[0\].Style.DisplayText = [true];]                                                                                         |
|                                                                                                                                                                                                                                                                     |
| [series.Styles\[0\].Text = series.Name;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [this][.ChartWebControl1.Series\[0\].SmartLabels = ][true][;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [Me][.ChartWebControl1.Series(0).Style.DisplayText = [True]]                                             |
|                                                                                                                                                                                                                    |
| [series.Styles(0).Text = series.Name]                                                                                                                                          |
|                                                                                                                                                                                                                    |
| [Private Me][.ChartWebControl1.Series(0).SmartLabels = ][True] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[                                             ]**

{border="0"}

**[]** 

***[]*** 

Figure 198: Chart with Smart Labels Disabled

**[]** 

{border="0"}

**[]** 

***[]*** 

Figure 199: Chart with Smart Labels Enabled

**[]** 

**[]** 

Custom borders for smart Labels

[] 

Smart labels can be made more smarter by displaying with customized borders. The color and the width of the border can be changed using the appearance properties available. **SmartLabelsBorderColor** property is used to set color for the border and **SmartLabelsBorderWidth** property is used to set the width of the border.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [this][.ChartWebControl1.[Series\[0\].SmartLabelsBorderColor = ][Color][.Yellow;]] |
|                                                                                                                                                                                                                                          |
| [this][.ChartWebControl1.[Series\[0\].SmartLabelsBorderWidth = 2]]                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [Me][.ChartWebControl1.[Series(0).SmartLabelsBorderColor = ][Color][.Yellow]] |
|                                                                                                                                                                                                                                     |
| [Me][.ChartWebControl1.[Series(0).SmartLabelsBorderWidth = 2]]                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Chart Types]{.UGHyperlink}[]{.UGHyperlink}

[]{#p151} 

[]{#related-topics}

