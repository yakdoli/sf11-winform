---
title: addingsupportforlabelsandstrokealongtheoriginaxistoanapplication.md
original_path: WinForms_Docs/99_Uncategorized/addingsupportforlabelsandstrokealongtheoriginaxistoanapplication.md
created_at: 2025-08-05
---






##### Adding Support for Labels and Stroke along the Origin Axis to an Application {#adding-support-for-labels-and-stroke-along-the-origin-axis-to-an-application style="tab-stops: 0pt"}

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][sync][:][ChartAxis][ Header][=\"Stock ID\"][ ChartLabelPosition][=\"Inside\"][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                                   [ ChartTickLinesPosition][=\"Cross\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                                   [ TickSize][=\"15\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                                   [ ChartTickLinesRange][=\"1\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                                   [ HeaderPosition][=\"Cross\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                                    [LabelPosition][=\"Low\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                                 [ /\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                     |
|                                                                                                                                                                      |
| [            chart1.Areas\[0\].PrimaryAxis.ChartLabelPosition = [AxisPositions].Inside;]    |
|                                                                                                                                                                      |
| [            chart1.Areas\[0\].PrimaryAxis.ChartTickLinesPosition = [AxisPositions].Cross;] |
|                                                                                                                                                                      |
| [            chart1.Areas\[0\].PrimaryAxis.ChartTickLinesRange = 0.5d;]                                             |
|                                                                                                                                                                      |
| [            chart1.Areas\[0\].PrimaryAxis.HeaderPosition = [AxisPositions].Cross;]         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 125: TickPoistion, LabelPosition, and Header Position Set as Inside

 

{border="0"}

Figure 126: Header Position Set as Inside

 

{border="0"}

Figure 127: Axis Labels set to NextToAxis

 

[]{#related-topics}

