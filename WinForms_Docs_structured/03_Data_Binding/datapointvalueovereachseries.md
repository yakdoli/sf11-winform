---
title: datapointvalueovereachseries.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\datapointvalueovereachseries.md
created_at: 2025-07-03
---






#### Data-point Value Over Each Series {#data-point-value-over-each-series style="tab-stops: 0pt"}

 

The data-point values are displayed over each chart series, mentioning its value from database in numerical format. The orientation and format can be set in order to avoid clustering of data.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [foreach][ ([ChartSeries] series [in] [this].olapChart1.Series)] |
|                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [series.Style.TextFormat = [\"{0:n}\"];]                                                                                                                    |
|                                                                                                                                                                                                                         |
| [series.Style.DisplayText = ][true][;]                                                         |
|                                                                                                                                                                                                                         |
| [series.Style.TextOrientation = [ChartTextOrientation].Up;]                                                                                                 |
|                                                                                                                                                                                                                         |
| [}][]                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [For][ [Each] series [As] ChartSeries [In] [Me].olapChart1.Series] |
|                                                                                                                                                                                                                                             |
| [series.Style.TextFormat = [\"{0:n}\"]]                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [series.Style.DisplayText = ][true][]                                                                              |
|                                                                                                                                                                                                                                             |
| [series.Style.TextOrientation = [ChartTextOrientation].Up]                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [Next][ series][]                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 12: Data-Point Values

[]{#related-topics}

