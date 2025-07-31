---
title: name.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\name.md
created_at: 2025-07-03
---






#### Name {#name style="tab-stops: 0pt"}

**[]** 

Specifies the name of the Series. This name can also be used to retrieve the series by name from the series collection.

[] 


+--------------------------+-------------------------+
| Details                                            |
+--------------------------+-------------------------+
| Possible Values          | Any user defined string |
+--------------------------+-------------------------+
| Default Value            | Null                    |
+--------------------------+-------------------------+
| 2D / 3D Limitations      | No                      |
+--------------------------+-------------------------+
| Applies to Chart Element | Any Series points       |
+--------------------------+-------------------------+
| Applies to Chart Types   | All chart types         |
+--------------------------+-------------------------+


**[]** 

Here is the code snippet using **Name** in Column Chart.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                      |
| [//This Code Snippet gives the name of the series as Product1]                                                                                                                     |
|                                                                                                                                                                                                                                      |
| [ChartSeries][ s1 = [this].ChartWebControl1.Model.NewSeries(); ]                                                           |
|                                                                                                                                                                                                                                      |
| [s1.Type = Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Column;          ]                                                                                              |
|                                                                                                                                                                                                                                      |
| [s1.Name=\"[Product1]\";]                                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [// Points to be added]                                                                                                                                                            |
|                                                                                                                                                                                                                                      |
| [this][.ChartWebControl1.Series.Add(s1);]                                                                                                       |
|                                                                                                                                                                                                                                      |
| [  ]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                      |
| [//Series retrieved using Name]                                                                                                                                                    |
|                                                                                                                                                                                                                                      |
| [this][.ChartWebControl1.Series\[[\"Product1\"]\].Style.Symbol.Shape = [ChartSymbolShape.Diamond];] |
|                                                                                                                                                                                                                                      |
| [this][.ChartWebControl1.Series\[[\"Product1\"]\].Style.Symbol.Color = [Color].Red;]                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                             |
| [\' This Code Snippet gives the name of the series as Product]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                             |
| [s1 ][As][ ChartSeries =][ Me][.ChartWebControl1.Model.NewSeries()] |
|                                                                                                                                                                                                                                                                                                                             |
| [s1.Type = Syncfusion.Windows.Forms.Chart.][ChartSeriesType][.Column]                                                                                                  |
|                                                                                                                                                                                                                                                                                                                             |
| [s1.Name=\"][Product1][\"]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                             |
| [\' Points to be added]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                             |
| [Me][.ChartWebControl1.Series.Add(s1) ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                             |
| [  ]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                             |
| [\'Series retrieved using Name]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                             |
| [Me][.ChartWebControl1.Series\[[\"Product1\"]\].Style.Symbol.Shape = [ChartSymbolShape.Diamond ]]                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| [Me][.ChartWebControl1.Series\[[\"Product1\"]\].Style.Symbol.Color = [Color].Red ]                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 157: Chart with Legend for the Series

[] 

See Also

[] 

[Chart Types]{.UGHyperlink}[]{.UGHyperlink}

[]{#p125} 

[]{#related-topics}

