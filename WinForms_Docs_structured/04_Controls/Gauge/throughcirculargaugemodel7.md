---
title: throughcirculargaugemodel7.md
original_path: WinForms_Docs/04_Controls/Gauge/throughcirculargaugemodel7.md
created_at: 2025-08-05
---






##### Through CircularGaugeModel {#through-circulargaugemodel style="tab-stops: 0pt"}

 

Step 1:

View:

 

Add the below code in your aspx file.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][@][ [Page] [Language][=\"C#\"] [MasterPageFile][=\"\~/Views/Shared/Site.Master\"] [Inherits][=\"System.Web.Mvc.ViewPage\"] [%\>]]                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][asp][:][Content][ [ID][=\"Content1\"] [ContentPlaceHolderID][=\"TitleContent\"] [runat][=\"server\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [    HalfCircular Gauge]                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][asp][:][Content][\>][]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][asp][:][Content][ [ID][=\"Content2\"] [ContentPlaceHolderID][=\"MainContent\"] [runat][=\"server\"\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][\--Rendering the Half-Circular Gauge\--][%\>][]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<%][=]Html.Syncfusion().CircularGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][asp][:][Content][\>][]                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                     |
| [\<][div][\>][]                                                        |
|                                                                                                                                                                                                                                                                                                     |
| [@\*][\--Rendering the Half-Circular Gauge\--][\*@][] |
|                                                                                                                                                                                                                                                                                                     |
| [@][Html.Syncfusion().CircularGauge([\"Gauge\"],([CircularGaugeModel])ViewData\[[\"GaugeModel\"]\])]  |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                     |
| [\</][div][\>][]                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 2:

Controller:

 

Add the below code in HomeController.cs file.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| [using][ System;]                                                                      |
|                                                                                                                                                                                               |
| [using][ System.Collections.Generic;]                                                  |
|                                                                                                                                                                                               |
| [using][ System.Linq;]                                                                 |
|                                                                                                                                                                                               |
| [using][ System.Web;]                                                                  |
|                                                                                                                                                                                               |
| [using][ System.Web.Mvc;]                                                              |
|                                                                                                                                                                                               |
| [using][ System.Web.Mvc.Ajax;]                                                         |
|                                                                                                                                                                                               |
| [using][ Syncfusion.Mvc.Gauge;]                                                        |
|                                                                                                                                                                                               |
| [using][ System.Windows;]                                                              |
|                                                                                                                                                                                               |
| [using][ Syncfusion.Mvc.Shared;]                                                       |
|                                                                                                                                                                                               |
| [using][ System.Windows.Media;]                                                        |
|                                                                                                                                                                                               |
| [namespace][ CircularGauge.Controllers]                                                |
|                                                                                                                                                                                               |
| [{]                                                                                                                                              |
|                                                                                                                                                                                               |
| [    \[[HandleError]\]]                                                                                                  |
|                                                                                                                                                                                               |
| [    [public] [class] [HomeController] : [Controller]] |
|                                                                                                                                                                                               |
| [    {]                                                                                                                                          |
|                                                                                                                                                                                               |
| [        [public] [ActionResult] Index()]                                                           |
|                                                                                                                                                                                               |
| [        {]                                                                                                                                      |
|                                                                                                                                                                                               |
| [            [CircularGaugeModel] gauge = [new] [CircularGaugeModel]();]    |
|                                                                                                                                                                                               |
| [            gauge.Radius = 180;]                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| [            [//Setting the FrameType to HalfCircle.]]                                                                     |
|                                                                                                                                                                                               |
| [            gauge.FrameType = [GaugeFrameType].HalfCircle;]                                                             |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| [            gauge.HalfCircleInnerRadius = 0;]                                                                                                   |
|                                                                                                                                                                                               |
| [            gauge.FirstFrameThickness = [new] [Thickness](8);]                                     |
|                                                                                                                                                                                               |
| [            gauge.SecondFrameThickness = [new] [Thickness](6);]                                    |
|                                                                                                                                                                                               |
| [            gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                                    |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| [            [CircularScale] c_Scale = [new] [CircularScale]();]            |
|                                                                                                                                                                                               |
| [            c_Scale.Maximum = 100;]                                                                                                             |
|                                                                                                                                                                                               |
| [            c_Scale.Minimum = 0;]                                                                                                               |
|                                                                                                                                                                                               |
| [            c_Scale.MinorIntervalValue = 5;]                                                                                                    |
|                                                                                                                                                                                               |
| [            c_Scale.MajorIntervalValue = 10;]                                                                                                   |
|                                                                                                                                                                                               |
| [            c_Scale.GapSweepAngle = 180;]                                                                                                       |
|                                                                                                                                                                                               |
| [            c_Scale.Radius = 120;]                                                                                                              |
|                                                                                                                                                                                               |
| [            c_Scale.StartAngle = 180;]                                                                                                          |
|                                                                                                                                                                                               |
| [            c_Scale.PointerCapRadius = 9;]                                                                                                      |
|                                                                                                                                                                                               |
| [            c_Scale.Location = [new] [Point](50, 83);]                                             |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| [            [GaugeLabelTick] c_LabelTick = [new] [GaugeLabelTick]();]      |
|                                                                                                                                                                                               |
| [            c_LabelTick.TickStyle = [TickStyle].MajorTick;]                                                             |
|                                                                                                                                                                                               |
| [            c_LabelTick.FontSize = 15;]                                                                                                         |
|                                                                                                                                                                                               |
| [            c_LabelTick.DistanceFromScale = 10;]                                                                                                |
|                                                                                                                                                                                               |
| [            c_LabelTick.TickPlacement = [ScalePlacement].Inside;]                                                       |
|                                                                                                                                                                                               |
| [            c_LabelTick.Angle = 0;]                                                                                                             |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| [            [TickMark] \_minor = [new] [TickMark]();]                      |
|                                                                                                                                                                                               |
| [            \_minor.TickShape = [TickShape].Triangle;]                                                                  |
|                                                                                                                                                                                               |
| [            \_minor.TickStyle = [TickStyle].MinorTick;]                                                                 |
|                                                                                                                                                                                               |
| [            \_minor.TickWidth = 2.5;]                                                                                                           |
|                                                                                                                                                                                               |
| [            \_minor.TickHeight = 6.5;]                                                                                                          |
|                                                                                                                                                                                               |
| [            \_minor.TickPlacement = [ScalePlacement].Cross;]                                                            |
|                                                                                                                                                                                               |
| [            \_minor.Angle = 180;]                                                                                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| [            [TickMark] \_major = [new] [TickMark]();]                      |
|                                                                                                                                                                                               |
| [            \_major.TickShape = [TickShape].Triangle;]                                                                  |
|                                                                                                                                                                                               |
| [            \_major.TickStyle = [TickStyle].MajorTick;]                                                                 |
|                                                                                                                                                                                               |
| [            \_major.TickWidth = 4.5;]                                                                                                           |
|                                                                                                                                                                                               |
| [            \_major.TickHeight = 11;]                                                                                                           |
|                                                                                                                                                                                               |
| [            \_major.TickPlacement = [ScalePlacement].Cross;]                                                            |
|                                                                                                                                                                                               |
| [            \_major.Angle = 180;]                                                                                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| [            [CircularPointer] c_Pointer = [new] [CircularPointer]();]      |
|                                                                                                                                                                                               |
| [            c_Pointer.PointerLength = 110;]                                                                                                     |
|                                                                                                                                                                                               |
| [            c_Pointer.PointerWidth = 8;]                                                                                                        |
|                                                                                                                                                                                               |
| [            c_Pointer.PointerNeedleType = [PointerNeedleType].Needle;]                                                  |
|                                                                                                                                                                                               |
| [            c_Pointer.Value = 10;]                                                                                                              |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| [            c_Scale.Ticks.Add(\_minor);]                                                                                                        |
|                                                                                                                                                                                               |
| [            c_Scale.Ticks.Add(\_major);]                                                                                                        |
|                                                                                                                                                                                               |
| [            c_Scale.Pointers.Add(c_Pointer);]                                                                                                   |
|                                                                                                                                                                                               |
| [            c_Scale.Labels.Add(c_LabelTick);]                                                                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                               |
|                                                                                                                                                                                               |
| [            gauge.Scales.Add(c_Scale);]                                                                                                         |
|                                                                                                                                                                                               |
| [            ViewData\[[\"GaugeModel\"]\] = gauge;]                                                                      |
|                                                                                                                                                                                               |
| [            [return] View();]                                                                                              |
|                                                                                                                                                                                               |
| [        }]                                                                                                                                      |
|                                                                                                                                                                                               |
| [    }]                                                                                                                                          |
|                                                                                                                                                                                               |
| [}]                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

 

Run the code to achieve the below output.

 

{border="0"}

Figure 86: HalfCircular Gauge**[]**

**[                         ]**

[]{#related-topics}

