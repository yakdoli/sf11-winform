---
title: intersectinglabels.md
original_path: WinForms_Docs/99_Uncategorized/intersectinglabels.md
created_at: 2025-08-05
---






#### Intersecting Labels {#intersecting-labels style="tab-stops: 0pt"}

**[]** 

Sometimes the chart dimensions could cause the labels to intersect. The chart will, by default, render those texts one over the other. But, it also has some built-in capabilities to workaround this overlap and lets you dictate the technique to follow. Refer to the properties below.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ChartAxis Properties              | Description                                                                                                                                                                                                                 |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LabelIntersectAction              | Specifies the action to take when labels texts intersect.                                                                                                                                                                   |
|                                   |                                                                                                                                                                                                                             |
|                                   | **MultipleRows** - Will render the labels in multiple rows.                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                             |
|                                   | **None** - Do nothing (default value)                                                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                             |
|                                   | **Rotate** - Rotates text so as to avoid overlap                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                             |
|                                   | **Wrap** - wraps text.                                                                                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EdgeLabelsDrawingMode             | Affects the labels that get rendered at the edges of the axis. Possible values:                                                                                                                                             |
|                                   |                                                                                                                                                                                                                             |
|                                   | Center - Centers the label at the interval. Default setting.                                                                                                                                                                |
|                                   |                                                                                                                                                                                                                             |
|                                   | Shift - Shifts the labels so that it\'s within the interval boundaries                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                             |
|                                   | ClippingProtection - Uses some intelligent logic to avoid clipping.                                                                                                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HidePartialLabels                 | When this property is set to true and when label overlap occurs, the chart will selectively hide certain labels (usually the min and max labels to begin with) to keep the rest of labels readable. Default value is false. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| **[]**                                                                                                                                                    |
|                                                                                                                                                                                                             |
| [this][.ChartWebControl1.PrimaryXAxis.HidePartialLabels = [true];]                                |
|                                                                                                                                                                                                             |
| [this][.ChartWebControl1.PrimaryXAxis.LabelIntersectAction = [ChartLabelIntersectAction].Rotate;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                         |
|                                                                                                                                                                                                          |
| **[]**                                                                                                                                                               |
|                                                                                                                                                                                                          |
| [Me][.ChartWebControl1.PrimaryXAxis.HidePartialLabels = [True]]                                |
|                                                                                                                                                                                                          |
| [Me][.ChartWebControl1.PrimaryXAxis.LabelIntersectAction = [ChartLabelIntersectAction].Rotate] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

{border="0"}**[]**

Figure 255: Intersecting Labels

 

 

[]{#p186} 

[]{#related-topics}

