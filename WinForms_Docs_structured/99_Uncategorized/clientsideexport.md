---
title: clientsideexport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideexport.md
created_at: 2025-07-03
---






##### ClientSide Export {#clientside-export style="tab-stops: 0pt"}

 

Refer to the below code to export the gauge in client side.

Step 1:

Controller:

 

Add the below code in your controller.

By setting the **GaugeExport** property to **ClientSide** and calling the **GenerateGaugeImage()** function, you can export the gauge in client side .

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                               |
|                                                                                                                                                                                   |
| [public][ [ActionResult] Index()]                                    |
|                                                                                                                                                                                   |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                   |
| [            [CircularGaugeModel] model = [new] [CircularGaugeModel]();] |
|                                                                                                                                                                                   |
| [            model.Radius = 160;]                                                                                                             |
|                                                                                                                                                                                   |
| [            model.GaugeSkins = [GaugeSkins].VS2010;]                                                                 |
|                                                                                                                                                                                   |
| [            model.FrameType = [GaugeFrameType].FullCircle;]                                                          |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            [CircularScale] c_Scale = [new] [CircularScale]();]         |
|                                                                                                                                                                                   |
| [            c_Scale.PointerCapRadius = 8;]                                                                                                   |
|                                                                                                                                                                                   |
| [            c_Scale.BackgroundBrush = [Brushes].Gray;]                                                               |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            [GaugeLabelTick] c_LabelTick = [new] [GaugeLabelTick]();]   |
|                                                                                                                                                                                   |
| [            c_LabelTick.FontSize = 15;]                                                                                                      |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            [TickMark] \_minor = [new] [TickMark]();]                   |
|                                                                                                                                                                                   |
| [            \_minor.TickStyle = [TickStyle].MinorTick;]                                                              |
|                                                                                                                                                                                   |
| [            \_minor.TickWidth = 1;]                                                                                                          |
|                                                                                                                                                                                   |
| [            \_minor.TickHeight = 9;]                                                                                                         |
|                                                                                                                                                                                   |
| [            \_minor.TickPlacement = [ScalePlacement].Outside;]                                                       |
|                                                                                                                                                                                   |
| [            \_minor.BackgroundBrush = [Brushes].White;]                                                              |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            [TickMark] \_major = [new] [TickMark]();]                   |
|                                                                                                                                                                                   |
| [            \_major.TickStyle = [TickStyle].MajorTick;]                                                              |
|                                                                                                                                                                                   |
| [            \_major.TickWidth = 3;]                                                                                                          |
|                                                                                                                                                                                   |
| [            \_major.TickHeight = 14;]                                                                                                        |
|                                                                                                                                                                                   |
| [            \_major.TickPlacement = [ScalePlacement].Outside;]                                                       |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            [CircularPointer] c_Pointer = [new] [CircularPointer]();]   |
|                                                                                                                                                                                   |
| [            c_Pointer.PointerLength = 100;]                                                                                                  |
|                                                                                                                                                                                   |
| [            c_Pointer.PointerWidth = 10;]                                                                                                    |
|                                                                                                                                                                                   |
| [            c_Pointer.BorderWidth = 2;]                                                                                                      |
|                                                                                                                                                                                   |
| [            c_Pointer.PointerPlacement = [ScalePlacement].Inside;]                                                   |
|                                                                                                                                                                                   |
| [            c_Pointer.MarkerStyle = [MarkerStyle].Trapezoid;]                                                        |
|                                                                                                                                                                                   |
| [            c_Pointer.Value = 0;]                                                                                                            |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            c_Scale.Ticks.Add(\_minor);]                                                                                                     |
|                                                                                                                                                                                   |
| [            c_Scale.Ticks.Add(\_major);]                                                                                                     |
|                                                                                                                                                                                   |
| [            c_Scale.Pointers.Add(c_Pointer);]                                                                                                |
|                                                                                                                                                                                   |
| [            c_Scale.Labels.Add(c_LabelTick);]                                                                                                |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            model.Scales.Add(c_Scale);]                                                                                                      |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            [//Sets for client side export.]]                                                                          |
|                                                                                                                                                                                   |
| [            model.GaugeExport = [GaugeExport].ClientSide;]                                                           |
|                                                                                                                                                                                   |
| [            [//Function to generate the gauge in Server or client side in Gif format.]]                                |
|                                                                                                                                                                                   |
| [            model.GenerateGaugeImage(model, [\"Gauge\"], [ImageFormat].Gif);]                |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            ViewData\[[\"GaugeModel\"]\] = model;]                                                                   |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                   |
| [        }]                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

View:

 

Add the below code in view page.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                             |
| [\<%][\--Rendering the linear gauge\--][%\>][]                                                    |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [   [\<%][=]Html.Syncfusion().CircularGauge([\"Gauge\"], ([CircularGaugeModel])ViewData\[[\"GaugeModel\"]\])[%\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [@\*][\--Rendering the linear gauge\--][\*@][]                                           |
|                                                                                                                                                                                                                                                                                                    |
| [@][Html.Syncfusion().CircularGauge([\"Gauge\"],([CircularGaugeModel])ViewData\[[\"GaugeModel\"]\])] |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 3:

[] 

Run the code. Then the below Save dialog window will open . Then you can save the image.

 

{border="0"}

Figure 84: Client Side-Save Dialog Box[                                ]


 

{border="0"} Note: On Ajax call, you can't export the gauge in client-side.

 


[]{#related-topics}

