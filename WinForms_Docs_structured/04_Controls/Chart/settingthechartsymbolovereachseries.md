---
title: settingthechartsymbolovereachseries.md
original_path: WinForms_Docs/04_Controls/Chart/settingthechartsymbolovereachseries.md
created_at: 2025-08-05
---






#### Setting the Chart Symbol Over Each Series {#setting-the-chart-symbol-over-each-series style="tab-stops: 0pt"}

 

The chart symbol is set at the top of each chart series by assigning a proper value to the Shape property.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [foreach][ ([ChartSeries] series [in] [this].olapChart1.Series)] |
|                                                                                                                                                                                                                         |
| [    series.Style.Symbol.Shape = [ChartSymbolShape].Diamond;            ]                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [For][ [Each] series [As] ChartSeries [In] [Me].olapChart1.Series] |
|                                                                                                                                                                                                                                             |
| [series.Style.Symbol.Shape = [ChartSymbolShape].Diamond           ]                                                                                                             |
|                                                                                                                                                                                                                                             |
| [Next][ series][]                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 14: Symbol over chart series

[]{#related-topics}

