---
title: howtotogglethevisibilityofthelegendicon.md
original_path: WinForms_Docs/99_Uncategorized/howtotogglethevisibilityofthelegendicon.md
created_at: 2025-08-05
---






##### How to toggle the visibility of the legend icon? {#how-to-toggle-the-visibility-of-the-legend-icon style="tab-stops: 0pt"}

[] 

The visibility of the legend icon can be toggled by using the IconVisibility property in the ChartLegend. The following code snippet shows how to toggle the visibility of the icons in an OlapChart legend:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                        |
| \                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][OlapChart.Legend][\>]\                                                                              |
| [    ][\<][baseChart][:][ChartLegend][ IconVisibility][=\"Collapsed\" /\>]\ |
| [\</][syncfusion][:][OlapChart.Legend][\>]                                                                              |
|                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                   |
|                                                                                                                              |
|                                                                                                                              |
|                                                                                                                              |
| [this].olapChart.Legend.IconVisibility = System.Windows.[Visibility].Collapsed; |
|                                                                                                                              |
|                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                |
|                                                                                                                           |
|                                                                                                                           |
|                                                                                                                           |
| [Me].olapChart.Legend.IconVisibility = System.Windows.[Visibility].Collapsed |
|                                                                                                                           |
|                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

