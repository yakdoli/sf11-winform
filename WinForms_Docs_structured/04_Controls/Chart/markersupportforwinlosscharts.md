---
title: markersupportforwinlosscharts.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\markersupportforwinlosscharts.md
created_at: 2025-07-03
---






##### Marker Support for Win-Loss charts {#marker-support-for-win-loss-charts style="tab-stops: 0pt"}

This marker feature supports High Points, Low Points, Start Point and Negative Point of Win-Loss Sparkline.

The markers feature of Win-Loss is the same as Column markers. You can choose the marker color for data points.

To enable the marker in the Win-Loss Sparkline, refer to the following code snippets:

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

Figure 92: Markers for Win-Loss Sparkline

 

[]{#related-topics}

