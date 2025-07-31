---
title: throughcirculargaugemodel2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\throughcirculargaugemodel2.md
created_at: 2025-07-03
---






##### Through CircularGaugeModel {#through-circulargaugemodel style="tab-stops: 0pt"}

 

View:

Step 1:

 

Add the below code in your aspx file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ View\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%][@][ [Page] [Language][=\"C#\"] [MasterPageFile][=\"\~/Views/Shared/Site.Master\"] [Inherits][=\"System.Web.Mvc.ViewPage\"] [%\>]]                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][asp][:][Content][ [ID][=\"Content1\"] [ContentPlaceHolderID][=\"TitleContent\"] [runat][=\"server\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    Circular Gauge]                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][Content][\>][]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][asp][:][Content][ [ID][=\"Content2\"] [ContentPlaceHolderID][=\"MainContent\"] [runat][=\"server\"\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<%][\--Rendering the Circular Gauge \--][%\>][]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<%][=]Html.Syncfusion().CircularGauge([\"Gauge\"],([CircularGaugeModel])ViewData\[[\"GaugeModel\"]\])[%\>]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][Content][\>][]                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                    |
| [\@{]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                    |
| [Layout=[\"\~/Views/Shared/\_Layout.cshtml\"];  ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                    |
| [}][]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                    |
| [\<][div][\>]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| [@\*][\--Rendering the Circular Gauge \--][\*@][]                                        |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [@][Html.Syncfusion().CircularGauge([\"Gauge\"],([CircularGaugeModel])ViewData\[[\"GaugeModel\"]\])] |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [\</][div][\>][]                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

***[]*** 

Controller:

Step 2:

 

Add the below code in your controller.

 Using the **CircularScale** class, Scale element can be created.

And Using **Scales** collection of **CircularGaugeModel** class, you can add the Circular Scale element.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [using][ System;]                                                                               |
|                                                                                                                                                                                      |
| [using][ System.Collections.Generic;]                                                           |
|                                                                                                                                                                                      |
| [using][ System.Linq;]                                                                          |
|                                                                                                                                                                                      |
| [using][ System.Web;]                                                                           |
|                                                                                                                                                                                      |
| [using][ System.Web.Mvc;]                                                                       |
|                                                                                                                                                                                      |
| [using][ Syncfusion.Mvc.Gauge;]                                                                 |
|                                                                                                                                                                                      |
| [using][ Syncfusion.Mvc.Shared;]                                                                |
|                                                                                                                                                                                      |
| [using][ System.Windows.Media;]                                                                 |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [namespace][ CircularGauge.Controllers]                                                         |
|                                                                                                                                                                                      |
| [{]                                                                                                                                              |
|                                                                                                                                                                                      |
| [    \[[HandleError]\]]                                                                                                  |
|                                                                                                                                                                                      |
| [    [public] [class] [HomeController] : [Controller]] |
|                                                                                                                                                                                      |
| [    {]                                                                                                                                          |
|                                                                                                                                                                                      |
| [        [public] [ActionResult] Index()]                                                           |
|                                                                                                                                                                                      |
| [        {]                                                                                                                                      |
|                                                                                                                                                                                      |
| [            [CircularGaugeModel] model = [new] [CircularGaugeModel]();]    |
|                                                                                                                                                                                      |
| [            model.Radius = 160;]                                                                                                                |
|                                                                                                                                                                                      |
| [            model.GaugeSkins = [GaugeSkins].VS2010;]                                                                    |
|                                                                                                                                                                                      |
| [            model.FrameType = [GaugeFrameType].CircularWithInnerTopGradient;]                                           |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Creating a Scale element.]]                                                                                |
|                                                                                                                                                                                      |
| [           ]                                                                                                                                    |
|                                                                                                                                                                                      |
| [            [CircularScale] c_Scale = [new] [CircularScale]();]            |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Setting maximum and minimum values for the scale.]]                                                        |
|                                                                                                                                                                                      |
| [            c_Scale.Maximum = 100;]                                                                                                             |
|                                                                                                                                                                                      |
| [            c_Scale.Minimum = 0;]                                                                                                               |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Setting major and minor interval values for the scale.]]                                                   |
|                                                                                                                                                                                      |
| [            c_Scale.MinorIntervalValue = 2;]                                                                                                    |
|                                                                                                                                                                                      |
| [            c_Scale.MajorIntervalValue = 10;]                                                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Setting GapSweepAngle and StartAngle of the scale.]]                                                       |
|                                                                                                                                                                                      |
| [            c_Scale.GapSweepAngle = 300;]                                                                                                       |
|                                                                                                                                                                                      |
| [            c_Scale.StartAngle = 120;]                                                                                                          |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Setting radius of the scale.]]                                                                             |
|                                                                                                                                                                                      |
| [            c_Scale.Radius = 110;]                                                                                                              |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            c_Scale.ScaleBarSize = 4.5;]                                                                                                        |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Setting pointer cap radius.]]                                                                              |
|                                                                                                                                                                                      |
| [            c_Scale.PointerCapRadius = 8;]                                                                                                      |
|                                                                                                                                                                                      |
| [            c_Scale.BackgroundBrush = [Brushes].LightGray;]                                                             |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [GaugeLabelTick] c_LabelTick = [new] [GaugeLabelTick]();]      |
|                                                                                                                                                                                      |
| [            c_LabelTick.TickStyle = [TickStyle].MajorTick;]                                                             |
|                                                                                                                                                                                      |
| [            c_LabelTick.FontSize = 16;]                                                                                                         |
|                                                                                                                                                                                      |
| [            c_LabelTick.DistanceFromScale = 1;]                                                                                                 |
|                                                                                                                                                                                      |
| [            c_LabelTick.TickPlacement = [ScalePlacement].Outside;]                                                      |
|                                                                                                                                                                                      |
| [            c_LabelTick.Angle = 0;]                                                                                                             |
|                                                                                                                                                                                      |
| [            c_LabelTick.BackgroundBrush = [Brushes].White;]                                                             |
|                                                                                                                                                                                      |
| [            c_LabelTick.IncludeFirstValue = [true];]                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            c_Scale.Labels.Add(c_LabelTick);]                                                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Adding Scale element in Circular Gauge.]]                                                                  |
|                                                                                                                                                                                      |
| [            model.Scales.Add(c_Scale);]                                                                                                         |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            ViewData\[[\"GaugeModel\"]\] = model;]                                                                      |
|                                                                                                                                                                                      |
| [            [return] View();]                                                                                              |
|                                                                                                                                                                                      |
| [        }]                                                                                                                                      |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [    }]                                                                                                                                          |
|                                                                                                                                                                                      |
| [}]                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code. It will generate the following output.

*[]* 

{border="0"}

Figure 62: Circular Gauge-Scale[         ]

[]{#related-topics}

