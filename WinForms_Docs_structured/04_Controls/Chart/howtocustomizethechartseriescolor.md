---
title: howtocustomizethechartseriescolor.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtocustomizethechartseriescolor.md
created_at: 2025-07-03
---






##### How to customize the chart series color? {#how-to-customize-the-chart-series-color style="tab-stops: 0pt"}

[] 

You can set a custom color for each series in the OlapChart. The following code snippet explains this. To apply different colors to different series iterate through the series and apply the custom brush to the series.

[] 

+----------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                     |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
| [       this].olapChart1.Series\[0\].Interior = [Brushes].Orange; |
|                                                                                                                |
|                                                                                                                |
+----------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                               |
|                                                                                                          |
|                                                                                                          |
|                                                                                                          |
| [      Me].olapChart1.Series(0).Interior = [Brushes].Orange |
|                                                                                                          |
|                                                                                                          |
+----------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

