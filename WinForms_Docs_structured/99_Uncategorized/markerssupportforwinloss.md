---
title: markerssupportforwinloss.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\markerssupportforwinloss.md
created_at: 2025-07-03
---






##### Markers Support for WinLoss {#markers-support-for-winloss style="tab-stops: 0pt"}

This marker feature supports High Points, Low Points, Start Point, End point and Negative Point of WinLoss Sparkline. You can choose the highlight color for data points. The markers feature of WinLoss is the same as Column markers. 

 

Refer to the following code snippets to enable the marker in column sparkline.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]]**                                                                                                                  |
|                                                                                                                                                                       |
| [//To enable marker to sparkline high,low,start,end,negative data points]**[]** |
|                                                                                                                                                                       |
| [this][.sparkLine1.IsHighPointHighlighted = [true];]        |
|                                                                                                                                                                       |
| [this][.sparkLine1.IsLowPointHighlighted = [true];]         |
|                                                                                                                                                                       |
| [this][.sparkLine1.IsFirstPointHighlighted = [true];]       |
|                                                                                                                                                                       |
| [this][.sparkLine1.IsLastPointHighlighted = [true];]        |
|                                                                                                                                                                       |
| [this][.sparkLine1.IsNegativePointHighlighted = [true];]    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                  |
|                                                                                                                                                                       |
| [//To enable marker to sparkline high,low,start,end,negative data points]**[]** |
|                                                                                                                                                                       |
| [Me][.sparkLine1.IsHighPointHighlighted = [true];]          |
|                                                                                                                                                                       |
| [Me][.sparkLine1.IsLowPointHighlighted = [true];]           |
|                                                                                                                                                                       |
| [Me][.sparkLine1.IsFirstPointHighlighted = [true];]         |
|                                                                                                                                                                       |
| [Me][.sparkLine1.IsLastPointHighlighted = [true];]          |
|                                                                                                                                                                       |
| [Me][.sparkLine1.IsNegativePointHighlighted = [true];]      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[{border="0"}]

Figure 284: Markers for WinLoss SparkLine[]

 

[]{#related-topics}

