---
title: howtoaddlegendtotheolapchart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtoaddlegendtotheolapchart.md
created_at: 2025-07-03
---






##### How to add legend to the OlapChart {#how-to-add-legend-to-the-olapchart style="tab-stops: 0pt"}

[] 

The ChartLegend can be added to an OlapChart by adding the ChartLegend of the Essential Chart WPF, which is found under the *Syncfusion.Windows.Chart* namespace. The following code snippets explain how to add a legend to an OlapChart:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                             |
| [       \<][syncfusion][:][OlapChart.Legend][\>]\                                                                            |
| [            ][\<][baseChart][:][ChartLegend][ Background][=\"Transparent\"/\>]\ |
| [       ][\</][syncfusion][:][OlapChart.Legend][\>]                                                  |
|                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                |
|                                                                                                                           |
|                                                                                                                           |
|                                                                                                                           |
| [       this].olapChart.Legend = [new] [ChartLegend](); |
|                                                                                                                           |
|                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                            |
|                                                                                                                       |
|                                                                                                                       |
|                                                                                                                       |
| [      Me].olapChart.Legend = [New] [ChartLegend]() |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

