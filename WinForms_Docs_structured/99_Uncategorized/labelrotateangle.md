---
title: labelrotateangle.md
original_path: WinForms_Docs/99_Uncategorized/labelrotateangle.md
created_at: 2025-08-05
---






##### Label Rotate Angle {#label-rotate-angle style="tab-stops: 0pt"}

[]{#p96}[] 

The axis label can be rotated to a custom angle using the LabelRotateAngle property. The following code describes setting rotation angle for the axis label to 45 degree.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][syncfusion:ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [  \<][syncfusion:ChartAxis][ ][LabelRotateAngle][=][\"[45]\"[\>\</][syncfusion:ChartAxis][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\</][syncfusion:ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][syncfusion:ChartArea.SecondaryAxis][\>]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [  \<][syncfusion:ChartAxis][ ][LabelRotateAngle][=][\"[45]\"[\>\</][syncfusion:ChartAxis][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\</][syncfusion:ChartArea.SecondaryAxis][\>]                                                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                       |
|                                                                                                                    |
| []                                                                             |
|                                                                                                                    |
| [//Intialize the Chart Area and Axis]                            |
|                                                                                                                    |
| [ChartArea area = [new] ChartArea();]                     |
|                                                                                                                    |
| [ChartAxis primary = [new] ChartAxis();]                  |
|                                                                                                                    |
| [ChartAxis secondary = [new] ChartAxis();]                |
|                                                                                                                    |
| []                                                                             |
|                                                                                                                    |
| [//Initialize the primary and secondary axis Label rotate angle] |
|                                                                                                                    |
| [primary.LabelRotateAngle = 45;]                                               |
|                                                                                                                    |
| [secondary.LabelRotateAngle = 45;]                                             |
|                                                                                                                    |
| []                                                                             |
|                                                                                                                    |
| [area.PrimaryAxis = primary;]                                                  |
|                                                                                                                    |
| [area.SecondaryAxis = secondary;]                                              |
+--------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

Figure 98: LabelRotateAngle = \"45\"

[]{#related-topics}

