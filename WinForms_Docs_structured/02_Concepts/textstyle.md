---
title: textstyle.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\textstyle.md
created_at: 2025-07-03
---






#### Text (Style) {#text-style style="tab-stops: 0pt"}

**[]** 

Series Wide Setting

**[]** 

Datapoint labels for a series can be specified using **Series.Style.Text** property.

[] 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                              |
|                                                                                                                             |
| **[]**                                                                    |
|                                                                                                                             |
| [//labels for the series]                                                 |
|                                                                                                                             |
| [ChartWebControl1.Series\[0\].Style.DisplayText = [true];]         |
|                                                                                                                             |
| [ChartWebControl1.Series\[0\].Style.Text = [\"Series1 Point\"];] |
+-----------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                       |
|                                                                                                                          |
| **[]**                                                                 |
|                                                                                                                          |
| [\'labels for the series]                                              |
|                                                                                                                          |
| [ChartWebControl1.Series\[0\].Style.DisplayText = [True]]       |
|                                                                                                                          |
| [ChartWebControl1.Series(0).Style.Text = [\"Series1 Point\"]] |
+--------------------------------------------------------------------------------------------------------------------------+

[                                                                                 ]

{border="0"}

**[]** 

Figure 208: DataPoint Labels displayed for the Series

[                                                                                 ]

Specific Data Point Setting

**[]** 

Labels for specific data points can be specified through **Series.Styles\[0\].Text** property.

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                                           |
|                                                                                                                                  |
| [//labels for the individual datapoints in the series]                         |
|                                                                                                                                  |
| [ChartWebControl1.Series\[0\].Style.DisplayText = [true];]              |
|                                                                                                                                  |
| [ChartWebControl1.Series\[0\].Styles\[0\].Text = [\"First Point\"];]  |
|                                                                                                                                  |
| [ChartWebControl1.Series\[0\].Styles\[1\].Text = [\"Second Point\"];] |
|                                                                                                                                  |
| [ChartWebControl1.Series\[0\].Styles\[2\].Text = [\"Third Point\"];]  |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                          |
|                                                                                                                             |
| **[]**                                                                    |
|                                                                                                                             |
| [\'labels for the individual datapoints in the series]                    |
|                                                                                                                             |
| [ChartWebControl1.Series\[0\].Style.DisplayText = [True]]          |
|                                                                                                                             |
| [ChartWebControl1.Series(0).Styles(0).Text = [\"First Point\"]]  |
|                                                                                                                             |
| [ChartWebControl1.Series(0).Styles(1).Text = [\"Second Point\"]] |
|                                                                                                                             |
| [ChartWebControl1.Series(0).Styles(2).Text = [\"Third Point\"]]  |
+-----------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 209: Using Series.Styles\[0\].Text in Column Chart

**[]** 

   {border="0"}         

**[]** 

Figure 210: Using Series.Styles\[0\].Text in Pie Chart

**[]** 

See Also

**[]** 

[Chart Types]{.UGHyperlink}[]{.UGHyperlink}

[]{#p159} 

 

[]{#related-topics}

