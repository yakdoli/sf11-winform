---
title: howtoshowhidechartlegend.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtoshowhidechartlegend.md
created_at: 2025-07-03
---






##### How to Show/Hide chart legend? {#how-to-showhide-chart-legend style="tab-stops: 0pt"}

[] 

The ChartLegend has a visibility property using which you can show or hide the ChartLegend in an OlapChart. The following code snippets show how you can collapse the visibility of the ChartLegend:

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][OlapChart.Legend][\>]                                                                               |
|                                                                                                                                                                                                                                        |
| [        ][\<][baseChart][:][ChartLegend][ Visibility][=\"Collapsed\" /\>]\ |
| [\</][syncfusion][:][OlapChart.Legend][\>]                                                                              |
|                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                               |
|                                                                                                                          |
|                                                                                                                          |
|                                                                                                                          |
| [this].olapChart.Legend.Visibility = System.Windows.[Visibility].Collapsed; |
|                                                                                                                          |
|                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                  |
|                                                                                             |
|                                                                                             |
|                                                                                             |
| [Me].olapChart.Legend.Visibility = System.Windows.Visibility.Collapsed |
|                                                                                             |
|                                                                                             |
+---------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

