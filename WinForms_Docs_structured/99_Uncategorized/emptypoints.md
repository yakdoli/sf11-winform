---
title: emptypoints.md
original_path: WinForms_Docs/99_Uncategorized/emptypoints.md
created_at: 2025-08-05
---








  









### Empty Points {#empty-points style="tab-stops: 0pt"}

[] 

Essential Chart lets you prevent certain points from getting plotted in the resultant chart. Such points are termed \"Empty Points\".

 

Empty Points can be implemented by setting the **IsEmpty** property of the **ChartPoint** class to **true**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                   |
| [// This sets the specified point as empty point.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [this][.][ChartWebControl1[.Series\[1\].Points\[0\].IsEmpty = ][true][;]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [\' This sets the specified point as empty point.]                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [Me][.][ChartWebControl1[.Series\[1\].Points\[0\].IsEmpty = ][True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following images illustrate the same. The second image displays after setting Point1 as an empty point.

[] 

{border="0"}

**[]** 

Figure 236: Chart without Empty Point

**[]** 

{border="0"}

[] 

Figure 237: Chart with Point1 as Empty Point

[] 

Showing Empty Point without any gap between Data Points

[] 

It is possible to set some data point as empty point and still show the chart without any gap between the points. You need to set **AllowGapForEmptyPoints** property to **false** to enable this feature. By default it is set to **true**.

***[]*** 


{border="0"}Note: You need to set ChartWebControl.Indexed property to true for the above setting to be effective.


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
| **[]**                                                                                                                      |
|                                                                                                                                                                               |
| [this][.ChartWebControl1.Series\[0\].Points\[3\].IsEmpty = [true];] |
|                                                                                                                                                                               |
| [this][.ChartWebControl1.Series\[0\].Points\[4\].IsEmpty = [true];] |
|                                                                                                                                                                               |
| [this][.ChartWebControl1.Series\[0\].Points\[5\].IsEmpty = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                        |
| **[]**                                                                                                               |
|                                                                                                                                                                        |
| [Me][.ChartWebControl1.Series(0).Points(3).IsEmpty = [True]] |
|                                                                                                                                                                        |
| [Me][.ChartWebControl1.Series(0).Points(4).IsEmpty = [True]] |
|                                                                                                                                                                        |
| [Me][.ChartWebControl1.Series(0).Points(5).IsEmpty = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 238: Fourth, fifth and sixth data points set as Empty Points

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                                      |
| **[]**                                                                                                             |
|                                                                                                                                                                      |
| [this][.ChartWebControl1.Indexed = [true];]                |
|                                                                                                                                                                      |
| [this][.ChartWebControl1.AllowGapForEmptyPoints = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                |
|                                                                                                                                                                   |
| **[]**                                                                                                          |
|                                                                                                                                                                   |
| [Me][.ChartWebControl1.Indexed = [True]]                |
|                                                                                                                                                                   |
| [Me][.ChartWebControl1.AllowGapForEmptyPoints = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 239: Fourth, fifth and sixth data points set as Empty Points; AllowGapForEmptyPoints = True

[]{#p174} 

[]{#related-topics}

