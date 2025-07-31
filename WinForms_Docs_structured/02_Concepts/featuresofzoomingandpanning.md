---
title: featuresofzoomingandpanning.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\featuresofzoomingandpanning.md
created_at: 2025-07-03
---








  









### Features of Zooming and Panning {#features-of-zooming-and-panning style="tab-stops: 0pt"}

 

Zooming and Panning using Pinch Operation:

The chart can be zoomed in and out using the pinch (Touch) in the device. This operation is very similar to zooming an image file in the device. Similarly, the zoom out operation can be performed. To perform Zoom and Pan operation through Pinch operations, "IsZoomAllAxes" property has to be set to "True" and "SwitchZooming ()" method should be invoked on Chart Area loaded event.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                |
|  [ ][//event handler for Chart Area Loaded]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                |
|  [this][.Chart1.Areas\[0\].Loaded += ][new][ ][RoutedEventHandler][(Charts_Loaded);]                             |
|                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [ ][void][ Charts_Loaded(][object][ sender, ][RoutedEventArgs][ e)] |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [ {]                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [    ][this][.Chart1.Areas\[0\].IsZoomAllAxes = ][true][;]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [     ][this][.Chart1.Areas\[0\].SwitchZooming();             ]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [ }  ]                                                                                                                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Zooming and Panning using Code

Zoom in and Zoom out can be performed using code by calling the "ZoomInCommand()" and "ZoomOutCommand(); methods. Panning can be done by using the property "ZoomPosition".

The following code snippets explain enabling Zooming/ Panning using XAML and C# code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<!\--Sets IsEnabledZoom,ZoomPosition and ZoomFactor properties\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][syncfusion][:][ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][syncfusion][:][ChartAxis][ EnableZooming][=\"True\"][ ZoomPosition][=\"5\"][ ZoomFactor][=\"0.5\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][syncfusion][:][ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<!\--Sets IsZoomAllAxes property\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][syncfusion][:][ChartArea][ IsZoomAllAxes][=\"True\"\>]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<!\--Chart code\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][syncfusion][:][ChartArea][\>][]                                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------+
| \[C#\]                                                                      |
|                                                                             |
| [//Enabling the zooming feature]                      |
|                                                                             |
| MyChart.Areas\[0\].PrimaryAxis.IsEnabledZoom = [true]; |
|                                                                             |
| [//Setting the zoom factor]                           |
|                                                                             |
| MyChart.Areas\[0\].PrimaryAxis.ZoomFactor = 0.5;                            |
|                                                                             |
| [// Setting the zoom positioning]                     |
|                                                                             |
| MyChart.Areas\[0\].PrimaryAxis.ZoomPosition = 5;                            |
|                                                                             |
| [//Setting IsZoomAllAxes property]                    |
|                                                                             |
| MyChart.Areas\[0\].IsZoomAllAxes = [true];             |
+-----------------------------------------------------------------------------+

 

 

[]{#related-topics}

