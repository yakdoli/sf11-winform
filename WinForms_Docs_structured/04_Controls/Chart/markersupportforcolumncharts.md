---
title: markersupportforcolumncharts.md
original_path: WinForms_Docs/04_Controls/Chart/markersupportforcolumncharts.md
created_at: 2025-08-05
---






##### Marker Support for Column charts {#marker-support-for-column-charts style="tab-stops: 0pt"}

This marker feature supports High Points, Low Points, Start Point and Negative Point of column Sparkline.

You can choose the marker color for data points.

To enable the marker in column Sparkline, use the following code snippets:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#.NET\]]**                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [//To enable marker to sparkline high,low,start,end,negative data points]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                         |
| [this][.sparkLine1.Markers.ShowHighPoint = [true];]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                         |
| [this][.sparkLine1.Markers.ShowLowPoint = [true];]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [this][.sparkLine1.Markers.ShowStartPoint = [true];]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                         |
| [this][.sparkLine1.Markers.ShowEndPoint = [true];]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [this][.sparkLine1.Markers.ShowNegativePoint= [true];]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                         |
| [//To customize the marker color to low points]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                         |
| [this][.sparkLine1.Markers.LowPointColor = [new] [BrushInfo]([GradientStyle].BackwardDiagonal, [Color].Blue, [Color].Wheat);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [//To enable marker to sparkline high,low,start,end,negative data points]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                      |
| [Me][.sparkLine1.Markers.ShowHighPoint = [True]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                      |
| [Me][.sparkLine1.Markers.ShowLowPoint = [True]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                      |
| [Me][.sparkLine1.Markers.ShowStartPoint = [True]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                      |
| [Me][.sparkLine1.Markers.ShowEndPoint = [True]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                      |
| [Me][.sparkLine1.Markers.ShowNegativePoint= [True]]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                      |
| [//To customize the marker color to low points]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                      |
| [Me][.sparkLine1.Markers.LowPointColor = [new] [BrushInfo]([GradientStyle].BackwardDiagonal, [Color].Blue, [Color].Wheat)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 91: Markers for Column SparkLine

[]{#related-topics}

