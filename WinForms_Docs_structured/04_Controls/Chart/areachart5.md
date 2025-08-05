---
title: areachart5.md
original_path: WinForms_Docs/04_Controls/Chart/areachart5.md
created_at: 2025-08-05
---








  









### Area Chart {#area-chart style="tab-stops: 0pt"}

Area charts emphasize the degree of change of the values over a period of time. Instead of rendering data as discreet bars or columns, an Area chart renders them in a continuous ebb and flow pattern as defined against the y-axis.

 

There is support for alpha-blending multiple series areas. The look and feel is also easily customizable by the user.

 

This Area chart connects the y-points by using straight lines and forms, which is an area covered by the above lines and x-axis. This area is then shaded with a specified color or gradient.

Multiple series can be plotted on the same chart and alpha-blended interior color can be used on the exterior chart to make the interior chart show through.

 

The following code snippet shows how to select this chart type.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][sfchart][:][OlapChart][ OlapChartType][=\"Area\" /\>]**[]** |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                               |
| [this][.olapChart1.OlapChartType = [OlapChartTypes].Area;][] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [Me][.olapChart1.OlapChartType = ][OlapChartTypes][.Area][] |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image shows a simple Area chart:

[] 

{border="0"}

 

Figure 18: Area chart

[]{#related-topics}

