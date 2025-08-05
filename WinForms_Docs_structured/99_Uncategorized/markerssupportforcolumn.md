---
title: markerssupportforcolumn.md
original_path: WinForms_Docs/99_Uncategorized/markerssupportforcolumn.md
created_at: 2025-08-05
---






##### Markers Support for Column {#markers-support-for-column style="tab-stops: 0pt"}

This marker feature supports high point, low point, start point, end point and negative points of column sparkline.  You can choose the highlight color for data points.

 

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

 

[{border="0"}]

Figure 283: Markers for Column SparkLine[]

 

[] 

[] 

[]{#related-topics}

