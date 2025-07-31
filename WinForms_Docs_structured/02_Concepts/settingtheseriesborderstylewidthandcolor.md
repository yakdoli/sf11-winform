---
title: settingtheseriesborderstylewidthandcolor.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\settingtheseriesborderstylewidthandcolor.md
created_at: 2025-07-03
---






#### Setting the Series Border Style, Width and Color {#setting-the-series-border-style-width-and-color style="tab-stops: 0pt"}

 

The style, width and color for the series border are set based on the following properties:

[·      ]DashStyle

[·      ]Width

[·      ]Color

[] 

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
| [series.Style.Border.Color = [Color].Black;            ]                                                                                                    |
|                                                                                                                                                                                                                         |
| [}][]                                                                                                                                  |
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
| [series.Style.Border.Color = [Color].Black            ]                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [Next][ series][]                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

 

Figure 11: Chart Series Style

[]{#related-topics}

