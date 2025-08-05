---
title: howtotogglethevisibilityofthelegendcheckbox.md
original_path: WinForms_Docs/99_Uncategorized/howtotogglethevisibilityofthelegendcheckbox.md
created_at: 2025-08-05
---






##### How to toggle the visibility of the legend check box? {#how-to-toggle-the-visibility-of-the-legend-check-box style="tab-stops: 0pt"}

[] 

The visibility of the legend check box can be toggled by using the CheckBoxVisibility property in the ChartLegend. The following code snippet shows how to toggle the visibility of the check box in the legend of an OlapChart:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][OlapChart.Legend][\>]\                                                                                  |
| [    ][\<][baseChart][:][ChartLegend][ CheckBoxVisibility][=\"Collapsed\" /\>]\ |
| [\</][syncfusion][:][OlapChart.Legend][\>]                                                                                  |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                       |
|                                                                                                                                  |
|                                                                                                                                  |
|                                                                                                                                  |
| [this].olapChart.Legend.CheckBoxVisibility = System.Windows.[Visibility].Collapsed; |
|                                                                                                                                  |
|                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                    |
|                                                                                                                               |
|                                                                                                                               |
|                                                                                                                               |
| [Me].olapChart.Legend.CheckBoxVisibility = System.Windows.[Visibility].Collapsed |
|                                                                                                                               |
|                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

