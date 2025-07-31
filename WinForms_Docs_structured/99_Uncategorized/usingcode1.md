---
title: usingcode1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingcode1.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Using code {#using-code style="tab-stops: 0pt"}

The linear gauge control can be created through code, in ASP.NET if you followed the given steps:

1.   Create a new ASP.NET Web application.

2.   In the .cs file include the following directory.

 

+------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                             |
|                                                                                                                                          |
| []                                                                                                   |
|                                                                                                                                          |
| [using  ] [Syncfusion.Web.UI.WebControls.Gauge;] |
|                                                                                                                                          |
| []                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                              |
|                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                           |
| [Imports  ] [Syncfusion.Web.UI.WebControls.Gauge] |
|                                                                                                                                           |
| []                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   In code view, the control is instantiated and added as shown in the following code:

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                           |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [protected] [ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                            |
|                                                                                                                                                                                                                        |
| [        BuildLinearGauge();]                                                                                                                                                      |
|                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                            |
|                                                                                                                                                                                                                        |
| [    [private][void] BuildLinearGauge()]                                                                                                 |
|                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                            |
|                                                                                                                                                                                                                        |
| [        [LinearGauge] gauge1 = [new][LinearGauge]();]                                                        |
|                                                                                                                                                                                                                        |
| [        gauge1.FrameType = [LinearGaugeFrameType].RoundedRectangle;]                                                                                      |
|                                                                                                                                                                                                                        |
| [        gauge1.AutoFormat = [GaugeSkins].Blend;]                                                                                                          |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [LinearScale] scale1 = [new][LinearScale]();]                                                        |
|                                                                                                                                                                                                                        |
| [        scale1.ScaleBarSize = 20;]                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [        gauge1.Scales.Add(scale1);]                                                                                                                                               |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [LinearGaugeLabel] label1 = [new][LinearGaugeLabel]();]                                              |
|                                                                                                                                                                                                                        |
| [        label1.LabelPlacement = [ScalePlacement].Near;]                                                                                                   |
|                                                                                                                                                                                                                        |
| [        label1.XDistanceFromScale = -10;]                                                                                                                                         |
|                                                                                                                                                                                                                        |
| [        scale1.Labels.Add(label1);]                                                                                                                                               |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [LinearGaugeTick] tick1 = [new][LinearGaugeTick]();]                                                 |
|                                                                                                                                                                                                                        |
| [        scale1.Ticks.Add(tick1);]                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [LinearBarPointer] barPointer1 = [new][LinearBarPointer]();]                                         |
|                                                                                                                                                                                                                        |
| [        barPointer1.Value = 50;]                                                                                                                                                  |
|                                                                                                                                                                                                                        |
| [        scale1.BarPointers.Add(barPointer1);]                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [LinearMarkerPointer] markerPointer1 = [new][LinearMarkerPointer]();]                                |
|                                                                                                                                                                                                                        |
| [        markerPointer1.Value = 50;]                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [        markerPointer1.PointerPlacement = [ScalePlacement].Far;]                                                                                          |
|                                                                                                                                                                                                                        |
| [        scale1.MarkerPointers.Add(markerPointer1);]                                                                                                                               |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [this].form1.Controls.Add(gauge1);]                                                                                                                  |
|                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Private] [ [Sub] Page_Load([ByVal] sender [As][Object], [ByVal] e [As] System.EventArgs) [Handles][MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        BuildCircularGauge()]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [End] [ [Sub] ]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Public] [ [Sub] BuildCircularGauge ()]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        ] [Dim] [ gauge1 [As][New][LinearGauge]()]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        gauge1.FrameType = [LinearGaugeFrameType].RoundedRectangle]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        gauge1.AutoFormat = [GaugeSkins].Blend]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        ] [Dim] [ scale1 [As][New][LinearScale]()]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.ScaleBarSize = 20]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        gauge1.Scales.Add(scale1)]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        ] [Dim] [ label1 [As][New][LinearGaugeLabel]()]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        label1.LabelPlacement = [ScalePlacement].Near]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        label1.XDistanceFromScale = -10]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.Labels.Add(label1)]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        ] [Dim] [ tick1 [As][New][LinearGaugeTick]()]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.Ticks.Add(tick1)]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        ] [Dim] [ barPointer1 [As][New][LinearBarPointer]()]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        barPointer1.Value = 50]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.BarPointers.Add(barPointer1)]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        ] [Dim] [ markerPointer1 [As][New][LinearMarkerPointer]()]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        markerPointer1.Value = 50]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        markerPointer1.PointerPlacement = [ScalePlacement].Far]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.MarkerPointers.Add(markerPointer1)]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        [Me].form1.Controls.Add(gauge1)]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [End] [ [Sub] ]                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   Build and run the application. The result will be displayed as follows:

{border="0"}

 

 

[]{#related-topics}

