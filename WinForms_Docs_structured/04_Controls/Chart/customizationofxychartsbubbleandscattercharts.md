---
title: customizationofxychartsbubbleandscattercharts.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\customizationofxychartsbubbleandscattercharts.md
created_at: 2025-07-03
---






##### Customization of XY Charts (Bubble and Scatter Charts) {#customization-of-xy-charts-bubble-and-scatter-charts style="tab-stops: 0pt"}

The following table lists the customization details for the Bubble and Scatter charts:

**[]** 

Properties:

 


+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+---------------------------------------------------------------------------+
|      Property        | Description                                                                                                                                                         | Type of Property | Value it Accepts          | Any Other Dependencies/Sub-properties Associated                          |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+---------------------------------------------------------------------------+
| ScatterConnectType   | Specifies the connection type of the Scatter charts. Optionally, you can connect the points in the series through straight lines or splines by using this property. | Enum             | ScatterConnectType.None   | SeriesType should be a Scatter chart.                                     |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  | ScatterConnectType.Line   |                                                                           |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  | ScatterConnectType.Spline |                                                                           |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+---------------------------------------------------------------------------+
| ScatterSplineTension | Sets the tension required for the Scatter Spline chart.                                                                                                             | Integer          | Any integer value.        | ScatterConnecttype must be Spline and seriestype must be a Scatter chart. |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+---------------------------------------------------------------------------+
| BubbleType           | Specifies whether to render the data point symbols as a circle, a square, or an image.                                                                              | Enum             | ChartBubbleType.Image     | Series Type must be a Scatter chart or Bubble chart.                      |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  | ChartBubbleType.Circle    |                                                                           |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  |                           |                                                                           |
|                      |                                                                                                                                                                     |                  | ChartBubbleType.Square    |                                                                           |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+---------------------------------------------------------------------------+


[] 

[]{#related-topics}

