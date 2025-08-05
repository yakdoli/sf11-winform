---
title: changetheseriesstyleandshowthedisplayedtext.md
original_path: WinForms_Docs/02_Concepts/changetheseriesstyleandshowthedisplayedtext.md
created_at: 2025-08-05
---








  









## Change the Series Style and Show the Displayed Text? {#change-the-series-style-and-show-the-displayed-text style="tab-stops: 0pt"}

 

The following code snippet sets a different style to the chart series:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [foreach][ ([ChartSeries] series [in] [this].olapChart1.Series)] |
|                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [series.Style.Border.Width = 1;            ]                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [series.Style.Border.DashStyle = [DashStyle].DashDot;           ]                                                                                           |
|                                                                                                                                                                                                                         |
| [ series.Style.Border.Color = [Color].Black;            ]                                                                                                   |
|                                                                                                                                                                                                                         |
| [series.Style.DisplayShadow = [true];            ]                                                                                                             |
|                                                                                                                                                                                                                         |
| [series.Style.Symbol.Shape = [ChartSymbolShape].Diamond;            ]                                                                                       |
|                                                                                                                                                                                                                         |
| [series.Style.Symbol.Color = [Color].Lime;]                                                                                                                 |
|                                                                                                                                                                                                                         |
| [series.Style.DisplayText = [true];]                                                                                                                           |
|                                                                                                                                                                                                                         |
| [this][.olapChart1.Refresh();]                                                                                                     |
|                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [For][ [Each] series [As] ChartSeries [In] [Me].olapChart1.Series] |
|                                                                                                                                                                                                                                             |
| [series.Style.Border.Width = 1            ]                                                                                                                                                             |
|                                                                                                                                                                                                                                             |
| [series.Style.Border.DashStyle = [DashStyle].DashDot          ]                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [ series.Style.Border.Color = [Color].Black            ]                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [series.Style.DisplayShadow = [true]           ]                                                                                                                                   |
|                                                                                                                                                                                                                                             |
| [series.Style.Symbol.Shape = [ChartSymbolShape].Diamond           ]                                                                                                             |
|                                                                                                                                                                                                                                             |
| [ series.Style.Symbol.Color = [Color].Lime]                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [series.Style.DisplayText = [true]]                                                                                                                                                |
|                                                                                                                                                                                                                                             |
| [Me][.olapChart1.Refresh()]                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [Next][ series]                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 58: Series Style

[]{#related-topics}

