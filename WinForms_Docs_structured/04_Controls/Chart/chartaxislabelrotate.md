---
title: chartaxislabelrotate.md
original_path: WinForms_Docs/04_Controls/Chart/chartaxislabelrotate.md
created_at: 2025-08-05
---






##### Chart Axis Label Rotate {#chart-axis-label-rotate style="tab-stops: 0pt"}

ChartAxis labels could be rotated with custom angles. **Axis.LabelRotateAngle** property is used to define the angle in which the Axis Labels need to be rotated.

 

The below given code snippet could be used to customize the labels to be rotated with 90\'.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][sfchart][:][ChartArea.PrimaryAxis][\>]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][sfchart][:][ChartAxis][ LabelRotateAngle][=\"90\"][ LabelFormat][=\"0.000000\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][sfchart][:][ChartArea.PrimaryAxis][\>]                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                   |
|                                                                                                    |
| []                                                             |
|                                                                                                    |
| [//Sets the Label to be rotated with 90\' angle] |
|                                                                                                    |
| [ Area.PrimaryAxis.LabelRotateAngle = 90;           ]          |
+----------------------------------------------------------------------------------------------------+

[] 

Below given figure illustrates Chart with Primary Axis labels rotated with 90\' angle

[] 

{border="0"}

Figure 211: Primary Axis Labels rotated with 90 degrees Angle

 


{border="0"}Note: LabelRotateAngle property will not have effect when the Axis.IntersectAction property is set as Rotate.


[] 

See Also

[]

 

[]{#p142} 

 

[]{#related-topics}

