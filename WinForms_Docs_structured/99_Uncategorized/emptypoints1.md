---
title: emptypoints1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\emptypoints1.md
created_at: 2025-07-03
---








  









### Empty Points {#empty-points style="tab-stops: 0pt"}

 

Essential Chart lets you prevent certain points from getting plotted in the resultant chart. Such points are termed **Empty Points**.

 

Empty Points can be implemented by setting the **IsEmpty** property of the **ChartPoint** class to **true**.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| [// This sets the specified point as empty point.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [this][.chartControl1.Series\[1\].Points\[0\].IsEmpty = ][true][;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                          |
|                                                                                                                                                                                                                   |
| [\' This sets the specified point as empty point.]                                                                                                              |
|                                                                                                                                                                                                                   |
| [Me][.chartControl1.Series\[1\].Points\[0\].IsEmpty = ][True] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following images illustrates the same. The second image displays after setting Point1 as an empty point.

 

{border="0"}

 

Figure 242: Chart without Empty Point

 

{border="0"}

 

Figure 243: Chart with Point1 as Empty Point

 

Showing Empty Point without any gap between Data Points

 

It is possible to set some data point as empty point and still show the chart without any gap between the points. You need to set **AllowGapForEmptyPoints** property to **false** to enable this feature. By default it is set to **true**.

**** 


{border="0"}Note: You need to set ChartControl.Indexed property to true for the above setting to be effective.


 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| **[]**                                                                                                                   |
|                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].Points\[3\].IsEmpty = [true];] |
|                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].Points\[4\].IsEmpty = [true];] |
|                                                                                                                                                                            |
| [this][.chartControl1.Series\[0\].Points\[5\].IsEmpty = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                  |
|                                                                                                                                                                     |
| **[]**                                                                                                            |
|                                                                                                                                                                     |
| [Me][.chartControl1.Series(0).Points(3).IsEmpty = [True]] |
|                                                                                                                                                                     |
| [Me][.chartControl1.Series(0).Points(4).IsEmpty = [True]] |
|                                                                                                                                                                     |
| [Me][.chartControl1.Series(0).Points(5).IsEmpty = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 244: 4th, 5th and 6th Data Points set as Empty Points

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| **[]**                                                                                                          |
|                                                                                                                                                                   |
| [this][.chartControl1.Indexed = [true];]                |
|                                                                                                                                                                   |
| [this][.chartControl1.AllowGapForEmptyPoints = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
| **[]**                                                                                                       |
|                                                                                                                                                                |
| [Me][.chartControl1.Indexed = [True]]                |
|                                                                                                                                                                |
| [Me][.chartControl1.AllowGapForEmptyPoints = [True]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 245: 4th, 5th and 6th Data Points set as Empty Points; AllowGapForEmptyPoints = \"True\"

 

[]{#p172} 

 

[]{#related-topics}

