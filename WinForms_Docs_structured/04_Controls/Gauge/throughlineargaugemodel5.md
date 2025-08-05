---
title: throughlineargaugemodel5.md
original_path: WinForms_Docs/04_Controls/Gauge/throughlineargaugemodel5.md
created_at: 2025-08-05
---






##### Through LinearGaugeModel {#through-lineargaugemodel style="tab-stops: 0pt"}

 

Step 1:

View:

 

Add the below code in your aspx file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                              |
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
| [    [\<%][=]Html.Syncfusion().LinearGauge([\"Gauge\"], ([LinearGaugeModel])ViewData\[[\"GaugeModel\"]\])[%\>]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][Content][\>][]                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                 |
| [@][Html.Syncfusion().LinearGauge([\"Gauge\"], ([LinearGaugeModel])ViewData\[[\"GaugeModel\"]\])] |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

Controller:

**[]** 

Add the below code in your controller.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [using][ System;]                                                                                                |
|                                                                                                                                                                                                       |
| [using][ System.Collections.Generic;]                                                                            |
|                                                                                                                                                                                                       |
| [using][ System.Linq;]                                                                                           |
|                                                                                                                                                                                                       |
| [using][ System.Web;]                                                                                            |
|                                                                                                                                                                                                       |
| [using][ System.Web.Mvc;]                                                                                        |
|                                                                                                                                                                                                       |
| [using][ Syncfusion.Mvc.Gauge;]                                                                                  |
|                                                                                                                                                                                                       |
| [using][ Syncfusion.Mvc.Shared;]                                                                                 |
|                                                                                                                                                                                                       |
| [using][ System.Windows.Media;]                                                                                  |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [namespace][ LinearGauge.Controllers]                                                                            |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [    \[[HandleError]\]]                                                                                                                   |
|                                                                                                                                                                                                       |
| [    [public] [class] [HomeController] : [Controller]]                  |
|                                                                                                                                                                                                       |
| [    {]                                                                                                                                                           |
|                                                                                                                                                                                                       |
| [        [public] [ActionResult] Index()]                                                                            |
|                                                                                                                                                                                                       |
| [        {]                                                                                                                                                       |
|                                                                                                                                                                                                       |
| [            [LinearGaugeModel] model = [new] [LinearGaugeModel]();]                         |
|                                                                                                                                                                                                       |
| [            model.FrameType = [LinearGaugeFrameType].CroppedRectangle;]                                                                  |
|                                                                                                                                                                                                       |
| [            model.GaugeSkins = [GaugeSkins].VS2010;]                                                                                     |
|                                                                                                                                                                                                       |
| [            model.Height = 420;]                                                                                                                                 |
|                                                                                                                                                                                                       |
| [            model.Width = 130;]                                                                                                                                  |
|                                                                                                                                                                                                       |
| [            model.Orientation = [GaugeOrientation].Vertical;]                                                                            |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            [LinearScale] l_Scale = [new] [LinearScale]();]                                 |
|                                                                                                                                                                                                       |
| [            l_Scale.Maximum = 100;]                                                                                                                              |
|                                                                                                                                                                                                       |
| [            l_Scale.Minimum = 0;]                                                                                                                                |
|                                                                                                                                                                                                       |
| [            l_Scale.MinorIntervalValue = 2;]                                                                                                                     |
|                                                                                                                                                                                                       |
| [            l_Scale.MajorIntervalValue = 10;]                                                                                                                    |
|                                                                                                                                                                                                       |
| [            l_Scale.BackgroundBrush = [Brushes].White;]                                                                                  |
|                                                                                                                                                                                                       |
| [            l_Scale.ScaleBarSize = 24;]                                                                                                                          |
|                                                                                                                                                                                                       |
| [            l_Scale.ScaleBarLength = 290;]                                                                                                                       |
|                                                                                                                                                                                                       |
| [            l_Scale.ScaleDirection = [ScaleDirection].CounterClockwise;]                                                                 |
|                                                                                                                                                                                                       |
| [            l_Scale.BorderWidth = 4;]                                                                                                                            |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            [GaugeLabelTick] c_LabelTick = [new] [GaugeLabelTick]();]                       |
|                                                                                                                                                                                                       |
| [            c_LabelTick.TickStyle = [TickStyle].MajorTick;]                                                                              |
|                                                                                                                                                                                                       |
| [            c_LabelTick.FontSize = 15;]                                                                                                                          |
|                                                                                                                                                                                                       |
| [            c_LabelTick.DistanceFromScale = 5;]                                                                                                                  |
|                                                                                                                                                                                                       |
| [            c_LabelTick.TickPlacement = [ScalePlacement].Inside;]                                                                        |
|                                                                                                                                                                                                       |
| [            c_LabelTick.Angle = 0;]                                                                                                                              |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            [TickMark] \_minor = [new] [TickMark]();]                                       |
|                                                                                                                                                                                                       |
| [            \_minor.TickShape = [TickShape].Rectangle;]                                                                                  |
|                                                                                                                                                                                                       |
| [            \_minor.TickStyle = [TickStyle].MinorTick;]                                                                                  |
|                                                                                                                                                                                                       |
| [            \_minor.TickWidth = 4;]                                                                                                                              |
|                                                                                                                                                                                                       |
| [            \_minor.TickHeight = 6;]                                                                                                                             |
|                                                                                                                                                                                                       |
| [            \_minor.DistanceFromScale = -24;]                                                                                                                    |
|                                                                                                                                                                                                       |
| [            \_minor.TickPlacement = [ScalePlacement].Outside;]                                                                           |
|                                                                                                                                                                                                       |
| [            \_minor.Angle = 180;]                                                                                                                                |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            [TickMark] \_major = [new] [TickMark]();]                                       |
|                                                                                                                                                                                                       |
| [            \_major.TickShape = [TickShape].Rectangle;]                                                                                  |
|                                                                                                                                                                                                       |
| [            \_major.TickStyle = [TickStyle].MajorTick;]                                                                                  |
|                                                                                                                                                                                                       |
| [            \_major.TickWidth = 4;]                                                                                                                              |
|                                                                                                                                                                                                       |
| [            \_major.TickHeight = 10;]                                                                                                                            |
|                                                                                                                                                                                                       |
| [            \_major.DistanceFromScale = -24;]                                                                                                                    |
|                                                                                                                                                                                                       |
| [            \_major.TickPlacement = [ScalePlacement].Outside;]                                                                           |
|                                                                                                                                                                                                       |
| [            \_major.Angle = 180;]                                                                                                                                |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            [LinearMarkerPointer] m_Pointer = [new] [LinearMarkerPointer]();]               |
|                                                                                                                                                                                                       |
| [            m_Pointer.Value = 32;]                                                                                                                               |
|                                                                                                                                                                                                       |
| [            m_Pointer.MarkerStyle = [MarkerStyle].Diamond;]                                                                              |
|                                                                                                                                                                                                       |
| [            m_Pointer.PointerPlacement = [ScalePlacement].Outside;]                                                                      |
|                                                                                                                                                                                                       |
| [            m_Pointer.PointerLength = 17;]                                                                                                                       |
|                                                                                                                                                                                                       |
| [            m_Pointer.PointerWidth = 12;]                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            [LinearBarPointer] b_Pointer = [new] [LinearBarPointer]();]                     |
|                                                                                                                                                                                                       |
| [            b_Pointer.Value = 32;]                                                                                                                               |
|                                                                                                                                                                                                       |
| [            b_Pointer.Opacity = 0.7;]                                                                                                                            |
|                                                                                                                                                                                                       |
| [            b_Pointer.BarStyle = [BarStyle].Rectangle;]                                                                                  |
|                                                                                                                                                                                                       |
| [            b_Pointer.PointerWidth = 18;]                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            [//Adding the State Indicator in Linear Gauge.]]                                                                               |
|                                                                                                                                                                                                       |
| [            [StateIndicator] s_Indicator = [new] [StateIndicator]();]                       |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            [//Specifying the height and width for the state indicator.]]                                                                  |
|                                                                                                                                                                                                       |
| [            s_Indicator.IndicatorHeight = 15;]                                                                                                                   |
|                                                                                                                                                                                                       |
| [            s_Indicator.IndicatorWidth = 15;]                                                                                                                    |
|                                                                                                                                                                                                       |
| [            [//Setting the value property, which is used to bind with pointer value, ]]                                                    |
|                                                                                                                                                                                                       |
| [            [//to set active and inactive states of the indicator.]]                                                                       |
|                                                                                                                                                                                                       |
| [            s_Indicator.Value = 32;]                                                                                                                             |
|                                                                                                                                                                                                       |
| [            [//Setting the style for the indicator.]]                                                                                      |
|                                                                                                                                                                                                       |
| [            s_Indicator.IndicatorStyle = [IndicatorStyle].CircularLED;]                                                                  |
|                                                                                                                                                                                                       |
| [            s_Indicator.Location = [new] System.Windows.[Point](50, 89);]                                           |
|                                                                                                                                                                                                       |
| [            s_Indicator.BackgroundBrush = [Brushes].LightBlue;]                                                                          |
|                                                                                                                                                                                                       |
| [            [//Setting the background brush for the indicator when it is in active state.]]                                                |
|                                                                                                                                                                                                       |
| [            s_Indicator.ActiveBackGroundBrush = [Brushes].Red;]                                                                          |
|                                                                                                                                                                                                       |
| [            [//Adding state ranges in which active start value and Active End value can be specified. If the pointer]]                     |
|                                                                                                                                                                                                       |
| [            [//value is between the state range value, then the indicator is in active state. You can customize the active              ]] |
|                                                                                                                                                                                                       |
| [            [// state indicator, using its ActiveBackground and ActiveBorderBrush properties.]]                                            |
|                                                                                                                                                                                                       |
| [            s_Indicator.StateRanges.Add([new] [StateRange](60, 90));]                                               |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            [LinearRange] l_Range = [new] [LinearRange]();]                                 |
|                                                                                                                                                                                                       |
| [            l_Range.StartValue = 60;]                                                                                                                            |
|                                                                                                                                                                                                       |
| [            l_Range.EndValue = 90;]                                                                                                                              |
|                                                                                                                                                                                                       |
| [            l_Range.StartWidth = 0;]                                                                                                                             |
|                                                                                                                                                                                                       |
| [            l_Range.EndWidth = 13;]                                                                                                                              |
|                                                                                                                                                                                                       |
| [            l_Range.BackgroundBrush = [Brushes].Red;]                                                                                    |
|                                                                                                                                                                                                       |
| [            l_Range.Opacity = 0.4;]                                                                                                                              |
|                                                                                                                                                                                                       |
| [            l_Range.BorderWidth = 0;]                                                                                                                            |
|                                                                                                                                                                                                       |
| [            l_Range.RangePosition = [ScalePlacement].Outside;]                                                                           |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            l_Scale.Ticks.Add(\_minor);]                                                                                                                         |
|                                                                                                                                                                                                       |
| [            l_Scale.Ticks.Add(\_major);]                                                                                                                         |
|                                                                                                                                                                                                       |
| [            l_Scale.Pointers.Add(b_Pointer);]                                                                                                                    |
|                                                                                                                                                                                                       |
| [            l_Scale.Pointers.Add(m_Pointer);]                                                                                                                    |
|                                                                                                                                                                                                       |
| [            l_Scale.Labels.Add(c_LabelTick);]                                                                                                                    |
|                                                                                                                                                                                                       |
| [            l_Scale.Ranges.Add(l_Range);]                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            model.Scales.Add(l_Scale);]                                                                                                                          |
|                                                                                                                                                                                                       |
| [            [//Adding state indicators in linear gauge.]]                                                                                  |
|                                                                                                                                                                                                       |
| [            model.StateIndicators.Add(s_Indicator);]                                                                                                             |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [            ViewData\[[\"GaugeModel\"]\] = model;]                                                                                       |
|                                                                                                                                                                                                       |
| [            [return] View();]                                                                                                               |
|                                                                                                                                                                                                       |
| [        }]                                                                                                                                                       |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [    }]                                                                                                                                                           |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code.  You will get the below Output for State Indicator InActive State.

 

{border="0"}

Figure 109: State Indicator-Inactive state**[]**

[                                 ]

Step 4:

 

In the above codes, you have mentioned that the State Range is between (60-90) and the Pointer Value is 32. Hence the state Indicator is in Inactive state. Now change the Pointer value to 72 and bind it with state Indicator value and then see the State Indicator in Active State. You can see the difference in the color of the Indicator.

**[]** 

{border="0"}

Figure 110: State Indicator-Active state**[]**

[                                      ]

[]{#related-topics}

