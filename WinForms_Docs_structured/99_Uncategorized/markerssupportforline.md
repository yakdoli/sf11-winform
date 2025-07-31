---
title: markerssupportforline.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\markerssupportforline.md
created_at: 2025-07-03
---






##### Markers Support for Line {#markers-support-for-line style="tab-stops: 0pt"}

This marker feature supports data points of line sparkline. You can choose the marker color for data points. 

 

Refer to the following code snippets to enable the marker in line sparkline.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]]**                                                                                                                                             |
|                                                                                                                                                                                                  |
| [//To enable marker to sparkline for all data points]**[]**                                                |
|                                                                                                                                                                                                  |
| [this][.sparkLine1.Markers.ShowMarker  =[true];][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                          |
|                                                                                                                                                                                               |
| [\'To enable marker to sparkline for all data points]**[]**                                             |
|                                                                                                                                                                                               |
| [Me][.sparkLine1.Markers.ShowMarker  =[True]][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 282: Marker for Line SparkLine

***            ***

You can choose the highlight color for data points.

 

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

[]{#related-topics}

