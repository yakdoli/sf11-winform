---
title: throughlineargaugemodel4.md
original_path: WinForms_Docs/04_Controls/Gauge/throughlineargaugemodel4.md
created_at: 2025-08-05
---






##### Through LinearGaugeModel {#through-lineargaugemodel style="tab-stops: 0pt"}

 

Step 1:

View:

 

Add the below code in your aspx file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%][@][ [Page] [Language][=\"C#\"] [MasterPageFile][=\"\~/Views/Shared/Site.Master\"] [Inherits][=\"System.Web.Mvc.ViewPage\"] [%\>]]                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][asp][:][Content][ [ID][=\"Content3\"] [ContentPlaceHolderID][=\"TitleContent\"] [runat][=\"server\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    Linear Gauge]                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][Content][\>][]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][asp][:][Content][ [ID][=\"Content4\"] [ContentPlaceHolderID][=\"MainContent\"] [runat][=\"server\"\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%][\--Rendering the Linear Gauge\--][%\>][]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<%][=]Html.Syncfusion().LinearGauge([\"Gauge\"], ([LinearGaugeModel])ViewData\[[\"GaugeModel\"]\])[%\>]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][Content][\>][]                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]][]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                 |
| [@\*][\--Rendering the Linear Gauge\--][\*@][]                                        |
|                                                                                                                                                                                                                                                                                                 |
| [@][Html.Syncfusion().LinearGauge([\"Gauge\"], ([LinearGaugeModel])ViewData\[[\"GaugeModel\"]\])] |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 2:

Controller:

 

Add the below code in your controller.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [using][ System;]                                                                                  |
|                                                                                                                                                                                         |
| [using][ System.Collections.Generic;]                                                              |
|                                                                                                                                                                                         |
| [using][ System.Linq;]                                                                             |
|                                                                                                                                                                                         |
| [using][ System.Web;]                                                                              |
|                                                                                                                                                                                         |
| [using][ System.Web.Mvc;]                                                                          |
|                                                                                                                                                                                         |
| [using][ Syncfusion.Mvc.Gauge;]                                                                    |
|                                                                                                                                                                                         |
| [using][ Syncfusion.Mvc.Shared;]                                                                   |
|                                                                                                                                                                                         |
| [using][ System.Windows.Media;]                                                                    |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [namespace][ LinearGauge.Controllers]                                                              |
|                                                                                                                                                                                         |
| [{]                                                                                                                                                 |
|                                                                                                                                                                                         |
| [    \[[HandleError]\]]                                                                                                     |
|                                                                                                                                                                                         |
| [    [public] [class] [HomeController] : [Controller]]    |
|                                                                                                                                                                                         |
| [    {]                                                                                                                                             |
|                                                                                                                                                                                         |
| [        [public] [ActionResult] Index()]                                                              |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            [LinearGaugeModel] model = [new] [LinearGaugeModel]();]           |
|                                                                                                                                                                                         |
| [            model.FrameType = [LinearGaugeFrameType].CroppedRectangle;]                                                    |
|                                                                                                                                                                                         |
| [            model.GaugeSkins = [GaugeSkins].VS2010;]                                                                       |
|                                                                                                                                                                                         |
| [            model.Height = 420;]                                                                                                                   |
|                                                                                                                                                                                         |
| [            model.Width = 130;]                                                                                                                    |
|                                                                                                                                                                                         |
| [            model.Orientation = [GaugeOrientation].Vertical;]                                                              |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [LinearScale] l_Scale = [new] [LinearScale]();]                   |
|                                                                                                                                                                                         |
| [            l_Scale.Maximum = 100;]                                                                                                                |
|                                                                                                                                                                                         |
| [            l_Scale.Minimum = 0;]                                                                                                                  |
|                                                                                                                                                                                         |
| [            l_Scale.MinorIntervalValue = 2;]                                                                                                       |
|                                                                                                                                                                                         |
| [            l_Scale.MajorIntervalValue = 10;]                                                                                                      |
|                                                                                                                                                                                         |
| [            l_Scale.BackgroundBrush = [Brushes].White;]                                                                    |
|                                                                                                                                                                                         |
| [            l_Scale.ScaleBarSize = 24;]                                                                                                            |
|                                                                                                                                                                                         |
| [            l_Scale.ScaleBarLength = 290;]                                                                                                         |
|                                                                                                                                                                                         |
| [            l_Scale.ScaleDirection = [ScaleDirection].CounterClockwise;]                                                   |
|                                                                                                                                                                                         |
| [            l_Scale.BorderWidth = 4;]                                                                                                              |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [GaugeLabelTick] c_LabelTick = [new] [GaugeLabelTick]();]         |
|                                                                                                                                                                                         |
| [            c_LabelTick.TickStyle = [TickStyle].MajorTick;]                                                                |
|                                                                                                                                                                                         |
| [            c_LabelTick.FontSize = 15;]                                                                                                            |
|                                                                                                                                                                                         |
| [            c_LabelTick.DistanceFromScale = 5;]                                                                                                    |
|                                                                                                                                                                                         |
| [            c_LabelTick.TickPlacement = [ScalePlacement].Inside;]                                                          |
|                                                                                                                                                                                         |
| [            c_LabelTick.Angle = 0;]                                                                                                                |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [TickMark] \_minor = [new] [TickMark]();]                         |
|                                                                                                                                                                                         |
| [            \_minor.TickShape = [TickShape].Rectangle;]                                                                    |
|                                                                                                                                                                                         |
| [            \_minor.TickStyle = [TickStyle].MinorTick;]                                                                    |
|                                                                                                                                                                                         |
| [            \_minor.TickWidth = 4;]                                                                                                                |
|                                                                                                                                                                                         |
| [            \_minor.TickHeight = 6;]                                                                                                               |
|                                                                                                                                                                                         |
| [            \_minor.DistanceFromScale = -24;]                                                                                                      |
|                                                                                                                                                                                         |
| [            \_minor.TickPlacement = [ScalePlacement].Outside;]                                                             |
|                                                                                                                                                                                         |
| [            \_minor.Angle = 180;]                                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [TickMark] \_major = [new] [TickMark]();]                         |
|                                                                                                                                                                                         |
| [            \_major.TickShape = [TickShape].Rectangle;]                                                                    |
|                                                                                                                                                                                         |
| [            \_major.TickStyle = [TickStyle].MajorTick;]                                                                    |
|                                                                                                                                                                                         |
| [            \_major.TickWidth = 4;]                                                                                                                |
|                                                                                                                                                                                         |
| [            \_major.TickHeight = 10;]                                                                                                              |
|                                                                                                                                                                                         |
| [            \_major.DistanceFromScale = -24;]                                                                                                      |
|                                                                                                                                                                                         |
| [            \_major.TickPlacement = [ScalePlacement].Outside;]                                                             |
|                                                                                                                                                                                         |
| [            \_major.Angle = 180;]                                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [LinearMarkerPointer] m_Pointer = [new] [LinearMarkerPointer]();] |
|                                                                                                                                                                                         |
| [            m_Pointer.Value = 32;]                                                                                                                 |
|                                                                                                                                                                                         |
| [            m_Pointer.MarkerStyle = [MarkerStyle].Diamond;]                                                                |
|                                                                                                                                                                                         |
| [            m_Pointer.PointerPlacement = [ScalePlacement].Outside;]                                                        |
|                                                                                                                                                                                         |
| [            m_Pointer.PointerLength = 17;]                                                                                                         |
|                                                                                                                                                                                         |
| [            m_Pointer.PointerWidth = 12;]                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [LinearBarPointer] b_Pointer = [new] [LinearBarPointer]();]       |
|                                                                                                                                                                                         |
| [            b_Pointer.Value = 32;]                                                                                                                 |
|                                                                                                                                                                                         |
| [            b_Pointer.Opacity = 0.7;]                                                                                                              |
|                                                                                                                                                                                         |
| [            b_Pointer.BarStyle = [BarStyle].Rectangle;]                                                                    |
|                                                                                                                                                                                         |
| [            b_Pointer.PointerWidth = 18;]                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Creating Range.]]                                                                                             |
|                                                                                                                                                                                         |
| [            [LinearRange] l_Range = [new] [LinearRange]();]                   |
|                                                                                                                                                                                         |
| [            [//Setting the start and end values for the range.]]                                                             |
|                                                                                                                                                                                         |
| [            l_Range.StartValue = 60;]                                                                                                              |
|                                                                                                                                                                                         |
| [            l_Range.EndValue = 90;]                                                                                                                |
|                                                                                                                                                                                         |
| [            [//Setting the start and end widths for the range.]]                                                             |
|                                                                                                                                                                                         |
| [            l_Range.StartWidth = 0;]                                                                                                               |
|                                                                                                                                                                                         |
| [            l_Range.EndWidth = 13;]                                                                                                                |
|                                                                                                                                                                                         |
| [            l_Range.BackgroundBrush = [Brushes].Red;]                                                                      |
|                                                                                                                                                                                         |
| [            l_Range.Opacity = 0.4;]                                                                                                                |
|                                                                                                                                                                                         |
| [            l_Range.BorderWidth = 0;]                                                                                                              |
|                                                                                                                                                                                         |
| [            [//Setting the position of the range.]]                                                                          |
|                                                                                                                                                                                         |
| [            l_Range.RangePosition = [ScalePlacement].Outside;]                                                             |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            l_Scale.Ticks.Add(\_minor);]                                                                                                           |
|                                                                                                                                                                                         |
| [            l_Scale.Ticks.Add(\_major);]                                                                                                           |
|                                                                                                                                                                                         |
| [            l_Scale.Pointers.Add(b_Pointer);]                                                                                                      |
|                                                                                                                                                                                         |
| [            l_Scale.Pointers.Add(m_Pointer);]                                                                                                      |
|                                                                                                                                                                                         |
| [            l_Scale.Labels.Add(c_LabelTick);]                                                                                                      |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Adding the range element to the linear scale.]]                                                               |
|                                                                                                                                                                                         |
| [            l_Scale.Ranges.Add(l_Range);]                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            model.Scales.Add(l_Scale);]                                                                                                            |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            ViewData\[[\"GaugeModel\"]\] = model;]                                                                         |
|                                                                                                                                                                                         |
| [            [return] View();]                                                                                                 |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| [    }]                                                                                                                                             |
|                                                                                                                                                                                         |
| [}]                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the Code. You will get the following output.

 

{border="0"}

Figure 106: Linear Gauge with Range**[]**

[                             ]

[]{#related-topics}

