---
title: hidepartiallabels.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\hidepartiallabels.md
created_at: 2025-07-03
---






##### Hide Partial Labels {#hide-partial-labels style="tab-stops: 0pt"}

[]{#p95}[] 

The HidePartialLabel property can be used to hide the axis labels that appear partially in the chart area. Usually labels in the edges are affected. If this property is set to True, the partially displayed labels will be hidden.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion:ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [  \<][syncfusion:ChartAxis][ ][HidePartialLabel][=][\"[True]\"[\>\</][syncfusion:ChartAxis][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][syncfusion:ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                   |
|                                                                                                |
| []                                                         |
|                                                                                                |
| [ChartArea area = [new] ChartArea();] |
|                                                                                                |
| [ChartAxis axis = [new] ChartAxis();] |
|                                                                                                |
| [axis.HidePartialLabel = [true];]     |
|                                                                                                |
| [area.PrimaryAxis = axis;]                                 |
+------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

Figure 97: HidePartialLabel = \"True\"

[]{#related-topics}

