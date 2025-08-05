---
title: howtodisplayinsecondaryaxis.md
original_path: WinForms_Docs/99_Uncategorized/howtodisplayinsecondaryaxis.md
created_at: 2025-08-05
---






##### How to display % in secondary axis? {#how-to-display-in-secondary-axis style="tab-stops: 0pt"}

[] 

To display the '%' symbol in secondary axis, you need to set the secondary axis label format property. The following code snippet describes the usage of '%' in the secondary axis label:

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [       \<][syncfusion][:][OlapChart.SecondaryAxis][\>]                                                                   |
|                                                                                                                                                                                                                                          |
| [              ][\<][syncfusion][:][ChartAxis][ LabelFormat][=\"00.00%\" /\>] |
|                                                                                                                                                                                                                                          |
| [       ][\</][syncfusion][:][OlapChart.SecondaryAxis][\>]                                        |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

