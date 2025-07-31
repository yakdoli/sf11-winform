---
title: labelplacement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\labelplacement.md
created_at: 2025-07-03
---






#### LabelPlacement {#labelplacement style="tab-stops: 0pt"}

**[]** 

Gets or sets the Pyramid chart or Funnel chart data point label placement when **ChartAccumulationLabelStyle** is set as **Inside**.

[] 


+-------------------------------------+-------------------------------------------------------------------------------+
| Details                                                                                                             |
+-------------------------------------+-------------------------------------------------------------------------------+
| Possible Values                     | Center -- DataPoint labels are aligned to the center of the Pyramid segment.\ |
|                                     | Top - DataPoint labels are aligned to the top of the Pyramid segment.\        |
|                                     | Bottom -- DataPoint labels are aligned to the bottom of the Pyramid segment.  |
|                                     |                                                                               |
|                                     | Left - DataPoint labels are aligned to the Left of the Pyramid segment.       |
|                                     |                                                                               |
|                                     | Right - DataPoint labels are aligned to the Right of the Pyramid segment.     |
+-------------------------------------+-------------------------------------------------------------------------------+
| Default Value                       | Right                                                                         |
+-------------------------------------+-------------------------------------------------------------------------------+
| 2D / 3D Limitations                 | No                                                                            |
+-------------------------------------+-------------------------------------------------------------------------------+
| Applies to Chart Element            | Any Series                                                                    |
+-------------------------------------+-------------------------------------------------------------------------------+
| Applies to Chart Types              | Funnel and Pyramid Charts                                                     |
+-------------------------------------+-------------------------------------------------------------------------------+


[] 

Here is the code snippet using LabelPlacement in Pyramid Chart.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.PyramidItem.LabelPlacement = [ChartAccumulationLabelPlacement].Center;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                      |
|                                                                                                                                                                                                                               |
| [Me][.ChartWebControl1.Series(0).ConfigItems.PyramidItem.LabelPlacement = [ChartAccumulationLabelPlacement].Center] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 150: ChartAccumulationLabelPlacement as Center

**[]** 

Here is the code snippet using LabelPlacement in Funnel Chart.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.FunnelItem.LabelPlacement = [ChartAccumulationLabelPlacement].Center;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                     |
|                                                                                                                                                                                                                              |
| [Me][.ChartWebControl1.Series(0).ConfigItems.FunnelItem.LabelPlacement = [ChartAccumulationLabelPlacement].Center] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 151: ChartAccumulationLabelPlacement as Center

[] 

See Also

**[]** 

[Pyramid Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Funnel Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p120} 

[]{#related-topics}

