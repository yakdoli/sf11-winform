---
title: throughlineargaugemodel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\throughlineargaugemodel.md
created_at: 2025-07-03
---






#### Through LinearGaugeModel: {#through-lineargaugemodel style="tab-stops: 0pt"}

 

Step 1:

View:

 

Add the below code in your aspx file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
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

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                 |
| [\<][div][\>][]                                                                                        |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                 |
| [@\*][\--Rendering the Linear Gauge\--][\*@][]                                        |
|                                                                                                                                                                                                                                                                                                 |
| [@][Html.Syncfusion().LinearGauge([\"Gauge\"], ([LinearGaugeModel])ViewData\[[\"GaugeModel\"]\])] |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                 |
| [\</][div][\>][]                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 2:

Controller:

 

Add the below code in your controller.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                              |
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
| [            [//Creating a linear gauge.]]                                                                                    |
|                                                                                                                                                                                         |
| [            [LinearGaugeModel] model = [new] [LinearGaugeModel]();]           |
|                                                                                                                                                                                         |
| [            model.FrameType = [LinearGaugeFrameType].CroppedRectangle;]                                                    |
|                                                                                                                                                                                         |
| [            [//Setting the skins for the linear gauge.]]                                                                     |
|                                                                                                                                                                                         |
| [            model.GaugeSkins = [GaugeSkins].VS2010;]                                                                       |
|                                                                                                                                                                                         |
| [            [//Specifying the height and width for the linear gauge.]]                                                       |
|                                                                                                                                                                                         |
| [            model.Height = 420;]                                                                                                                   |
|                                                                                                                                                                                         |
| [            model.Width = 130;]                                                                                                                    |
|                                                                                                                                                                                         |
| [            [//Setting the orientation of the linear gauge.]]                                                                |
|                                                                                                                                                                                         |
| [            model.Orientation = [GaugeOrientation].Vertical;]                                                              |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Creating the scale element in linear gauge.]]                                                                 |
|                                                                                                                                                                                         |
| [            [LinearScale] l_Scale = [new] [LinearScale]();]                   |
|                                                                                                                                                                                         |
| [            [//Setting maximum and minimum values for the scale.]]                                                           |
|                                                                                                                                                                                         |
| [            l_Scale.Maximum = 100;]                                                                                                                |
|                                                                                                                                                                                         |
| [            l_Scale.Minimum = 0;]                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Setting major and minor interval values for the scale.]]                                                      |
|                                                                                                                                                                                         |
| [            l_Scale.MinorIntervalValue = 2;]                                                                                                       |
|                                                                                                                                                                                         |
| [            l_Scale.MajorIntervalValue = 10;]                                                                                                      |
|                                                                                                                                                                                         |
| [            l_Scale.BackgroundBrush = [Brushes].White;]                                                                    |
|                                                                                                                                                                                         |
| [            l_Scale.ScaleBarSize = 24;]                                                                                                            |
|                                                                                                                                                                                         |
| [            [//Setting the length of the scale.]]                                                                            |
|                                                                                                                                                                                         |
| [            l_Scale.ScaleBarLength = 290;]                                                                                                         |
|                                                                                                                                                                                         |
| [            l_Scale.ScaleDirection = [ScaleDirection].CounterClockwise;]                                                   |
|                                                                                                                                                                                         |
| [            l_Scale.BorderWidth = 4;]                                                                                                              |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Creating the label element in scale.]]                                                                        |
|                                                                                                                                                                                         |
| [            [GaugeLabelTick] c_LabelTick = [new] [GaugeLabelTick]();]         |
|                                                                                                                                                                                         |
| [            c_LabelTick.TickStyle = [TickStyle].MajorTick;]                                                                |
|                                                                                                                                                                                         |
| [            [//Setting the font size for the labels.]]                                                                       |
|                                                                                                                                                                                         |
| [            c_LabelTick.FontSize = 15;]                                                                                                            |
|                                                                                                                                                                                         |
| [            c_LabelTick.DistanceFromScale = 5;]                                                                                                    |
|                                                                                                                                                                                         |
| [            [//Setting the location of the label.]]                                                                          |
|                                                                                                                                                                                         |
| [            c_LabelTick.TickPlacement = [ScalePlacement].Inside;]                                                          |
|                                                                                                                                                                                         |
| [            c_LabelTick.Angle = 0;]                                                                                                                |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Adding the minor tick elements in linear scale.]]                                                             |
|                                                                                                                                                                                         |
| [            [TickMark] \_minor = [new] [TickMark]();]                         |
|                                                                                                                                                                                         |
| [           [//Setting the tick shape.]]                                                                                      |
|                                                                                                                                                                                         |
| [            \_minor.TickShape = [TickShape].Rectangle;]                                                                    |
|                                                                                                                                                                                         |
| [            [//Setting the tick serle.]]                                                                                     |
|                                                                                                                                                                                         |
| [            \_minor.TickStyle = [TickStyle].MinorTick;]                                                                    |
|                                                                                                                                                                                         |
| [            [//Setting the height and width of the ticks.]]                                                                  |
|                                                                                                                                                                                         |
| [            \_minor.TickWidth = 4;]                                                                                                                |
|                                                                                                                                                                                         |
| [            \_minor.TickHeight = 6;]                                                                                                               |
|                                                                                                                                                                                         |
| [            [//Setting the position of the ticks.]]                                                                          |
|                                                                                                                                                                                         |
| [            \_minor.DistanceFromScale = -24;]                                                                                                      |
|                                                                                                                                                                                         |
| [            \_minor.TickPlacement = [ScalePlacement].Outside;]                                                             |
|                                                                                                                                                                                         |
| [            \_minor.Angle = 180;]                                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Adding the major tick elements in linear scale.]]                                                             |
|                                                                                                                                                                                         |
| [            [TickMark] \_major = [new] [TickMark]();]                         |
|                                                                                                                                                                                         |
| [            [//Setting the tick shape.]]                                                                                     |
|                                                                                                                                                                                         |
| [            \_major.TickShape = [TickShape].Rectangle;]                                                                    |
|                                                                                                                                                                                         |
| [            \_major.TickStyle = [TickStyle].MajorTick;]                                                                    |
|                                                                                                                                                                                         |
| [            [//Setting the height and width of the ticks.]]                                                                  |
|                                                                                                                                                                                         |
| [            \_major.TickWidth = 4;]                                                                                                                |
|                                                                                                                                                                                         |
| [            \_major.TickHeight = 10;]                                                                                                              |
|                                                                                                                                                                                         |
| [            [//Setting the position of the ticks.]]                                                                          |
|                                                                                                                                                                                         |
| [            \_major.DistanceFromScale = -24;]                                                                                                      |
|                                                                                                                                                                                         |
| [            \_major.TickPlacement = [ScalePlacement].Outside;]                                                             |
|                                                                                                                                                                                         |
| [            \_major.Angle = 180;]                                                                                                                  |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Creating the market pointer.]]                                                                                |
|                                                                                                                                                                                         |
| [            [LinearMarkerPointer] m_Pointer = [new] [LinearMarkerPointer]();] |
|                                                                                                                                                                                         |
| [            [//Setting the value for the pointer.]]                                                                          |
|                                                                                                                                                                                         |
| [            m_Pointer.Value = 32;]                                                                                                                 |
|                                                                                                                                                                                         |
| [            [//Setting the marker style.]]                                                                                   |
|                                                                                                                                                                                         |
| [            m_Pointer.MarkerStyle = [MarkerStyle].Diamond;]                                                                |
|                                                                                                                                                                                         |
| [            [//Setting the position of the marker.]]                                                                         |
|                                                                                                                                                                                         |
| [            m_Pointer.PointerPlacement = [ScalePlacement].Outside;]                                                        |
|                                                                                                                                                                                         |
| [            [//Setting the length and width of the pointer.]]                                                                |
|                                                                                                                                                                                         |
| [            m_Pointer.PointerLength = 17;]                                                                                                         |
|                                                                                                                                                                                         |
| [            m_Pointer.PointerWidth = 12;]                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Creating the bar pointer.]]                                                                                   |
|                                                                                                                                                                                         |
| [            [LinearBarPointer] b_Pointer = [new] [LinearBarPointer]();]       |
|                                                                                                                                                                                         |
| [            [//Setting the value for the pointer.]]                                                                          |
|                                                                                                                                                                                         |
| [            b_Pointer.Value = 32;]                                                                                                                 |
|                                                                                                                                                                                         |
| [            b_Pointer.Opacity = 0.7;]                                                                                                              |
|                                                                                                                                                                                         |
| [            [//Setting the bar style.]]                                                                                      |
|                                                                                                                                                                                         |
| [            b_Pointer.BarStyle = [BarStyle].Rectangle;]                                                                    |
|                                                                                                                                                                                         |
| [            [//Setting the width of the bar pointer.]]                                                                       |
|                                                                                                                                                                                         |
| [            b_Pointer.PointerWidth = 18;]                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Creating the indicator.]]                                                                                     |
|                                                                                                                                                                                         |
| [            [StateIndicator] s_Indicator = [new] [StateIndicator]();]         |
|                                                                                                                                                                                         |
| [            [//Setting the height and width of the indicator.]]                                                              |
|                                                                                                                                                                                         |
| [            s_Indicator.IndicatorHeight = 15;]                                                                                                     |
|                                                                                                                                                                                         |
| [            s_Indicator.IndicatorWidth = 15;]                                                                                                      |
|                                                                                                                                                                                         |
| [            s_Indicator.Value = 32;]                                                                                                               |
|                                                                                                                                                                                         |
| [            [//Setting the indicator style.]]                                                                                |
|                                                                                                                                                                                         |
| [            s_Indicator.IndicatorStyle = [IndicatorStyle].CircularLED;]                                                    |
|                                                                                                                                                                                         |
| [            [//Setting the location of the indicators.]]                                                                     |
|                                                                                                                                                                                         |
| [            s_Indicator.Location = [new] System.Windows.[Point](50, 89);]                             |
|                                                                                                                                                                                         |
| [            s_Indicator.BackgroundBrush = [Brushes].LightBlue;]                                                            |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Creating the range.]]                                                                                         |
|                                                                                                                                                                                         |
| [            [LinearRange] l_Range = [new] [LinearRange]();]                   |
|                                                                                                                                                                                         |
| [            [//Setting the start value and end value for the range.]]                                                        |
|                                                                                                                                                                                         |
| [            l_Range.StartValue = 60;]                                                                                                              |
|                                                                                                                                                                                         |
| [            l_Range.EndValue = 90;]                                                                                                                |
|                                                                                                                                                                                         |
| [            [//Setting Start width and end width.]]                                                                          |
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
| [            [//Creating custom labels. ]]                                                                                    |
|                                                                                                                                                                                         |
| [            [GaugeCustomLabel] custom_Label = [new] [GaugeCustomLabel]();]    |
|                                                                                                                                                                                         |
| [            [//Setting the font size for the label.]]                                                                        |
|                                                                                                                                                                                         |
| [            custom_Label.FontSize = 15;]                                                                                                           |
|                                                                                                                                                                                         |
| [            [//Setting the label value for the linear gauge.]]                                                               |
|                                                                                                                                                                                         |
| [            custom_Label.LabelValue = [\"Gauge\"];]                                                                        |
|                                                                                                                                                                                         |
| [            [//Setting the position of the custom label.]]                                                                   |
|                                                                                                                                                                                         |
| [            custom_Label.Location = [new] System.Windows.[Point](50, 93);]                            |
|                                                                                                                                                                                         |
| [            custom_Label.BackgroundBrush = [Brushes].White;]                                                               |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [            [//Adding the tick elements in linear scale.]]                                                                   |
|                                                                                                                                                                                         |
| [            l_Scale.Ticks.Add(\_minor);]                                                                                                           |
|                                                                                                                                                                                         |
| [            l_Scale.Ticks.Add(\_major);]                                                                                                           |
|                                                                                                                                                                                         |
| [            [//Adding the bar pointer.]]                                                                                     |
|                                                                                                                                                                                         |
| [            l_Scale.Pointers.Add(b_Pointer);]                                                                                                      |
|                                                                                                                                                                                         |
| [            [//Adding the marker pointer.]]                                                                                  |
|                                                                                                                                                                                         |
| [            l_Scale.Pointers.Add(m_Pointer);]                                                                                                      |
|                                                                                                                                                                                         |
| [            l_Scale.Labels.Add(c_LabelTick);]                                                                                                      |
|                                                                                                                                                                                         |
| [            [//Adding the range element.]]                                                                                   |
|                                                                                                                                                                                         |
| [            l_Scale.Ranges.Add(l_Range);]                                                                                                          |
|                                                                                                                                                                                         |
| [            [//Adding the scale element.]]                                                                                   |
|                                                                                                                                                                                         |
| [            model.Scales.Add(l_Scale);]                                                                                                            |
|                                                                                                                                                                                         |
| [            [//Adding state indicators in linear gauge.]]                                                                    |
|                                                                                                                                                                                         |
| [            model.StateIndicators.Add(s_Indicator);]                                                                                               |
|                                                                                                                                                                                         |
| [            [//Adding the custom labels.]]                                                                                   |
|                                                                                                                                                                                         |
| [            model.CustomLabel.Add(custom_Label);]                                                                                                  |
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

 

Run the code. You will get the following output.

 

{border="0"}

Figure 88: Linear Gauge**[]**

[                                                ]

A sample which demonstrates a Linear Gauge control can be downloaded from the below mentioned link.

[] 


[ASPX Application](http://files2.syncfusion.com/support/ASP%20MVC/UG/Gauge/Linear%20Gauge%20(ASPX).zip)

[Razor Application](http://files2.syncfusion.com/support/ASP%20MVC/UG/Gauge/Linear%20Gauge%20(Razor).zip)

 

{border="0"} Note: The version number for the assemblies has been set to 9.4.0.62 in the Web.config file of the attached sample.


[]{#related-topics}

