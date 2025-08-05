---
title: throughlineargaugemodel2.md
original_path: WinForms_Docs/04_Controls/Gauge/throughlineargaugemodel2.md
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
| [\<%][\--Rendering the Linear Gauge\--][%\>][]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<%][=]Html.Syncfusion().LinearGauge([\"Gauge\"], ([LinearGaugeModel])ViewData\[[\"GaugeModel\"]\])[%\>]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][asp][:][Content][\>][]                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                 |
| [\<][div][\>][]                                                                                        |
|                                                                                                                                                                                                                                                                                                 |
| [@\*][\--Rendering the Linear Gauge\--][\*@][]                                        |
|                                                                                                                                                                                                                                                                                                 |
| [@][Html.Syncfusion().LinearGauge([\"Gauge\"], ([LinearGaugeModel])ViewData\[[\"GaugeModel\"]\])] |
|                                                                                                                                                                                                                                                                                                 |
| [    ]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                 |
| [\</][div][\>][]                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

Controller:

 

Add the below code in your controller. Using the **LinearScale** class, you can create the scale element.

By using **Scales** collection of **LinearGaugeModel** class, you can add the scale elemet.

 

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
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [namespace][ LinearGauge.Controllers]                                                           |
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
| [            [LinearGaugeModel] model = [new] [LinearGaugeModel]();]        |
|                                                                                                                                                                                      |
| [            model.FrameType = [LinearGaugeFrameType].CroppedRectangle;]                                                 |
|                                                                                                                                                                                      |
| [            model.GaugeSkins = [GaugeSkins].VS2010;]                                                                    |
|                                                                                                                                                                                      |
| [            model.Height = 420;]                                                                                                                |
|                                                                                                                                                                                      |
| [            model.Width = 130;]                                                                                                                 |
|                                                                                                                                                                                      |
| [            model.Orientation = [GaugeOrientation].Vertical;]                                                           |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Creating Linear scale element.]]                                                                           |
|                                                                                                                                                                                      |
| [            [LinearScale] l_Scale = [new] [LinearScale]();]                |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Specifying maximum and minimum values for the linear scale.]]                                              |
|                                                                                                                                                                                      |
| [            l_Scale.Maximum = 100;]                                                                                                             |
|                                                                                                                                                                                      |
| [            l_Scale.Minimum = 0;]                                                                                                               |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Setting major and minor interval values for the linear scale.]]                                            |
|                                                                                                                                                                                      |
| [            l_Scale.MinorIntervalValue = 2;]                                                                                                    |
|                                                                                                                                                                                      |
| [            l_Scale.MajorIntervalValue = 10;]                                                                                                   |
|                                                                                                                                                                                      |
| [            l_Scale.BackgroundBrush = [Brushes].White;]                                                                 |
|                                                                                                                                                                                      |
| [            l_Scale.ScaleBarSize = 24;]                                                                                                         |
|                                                                                                                                                                                      |
| [            l_Scale.ScaleBarLength = 290;]                                                                                                      |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Setting the scale direction.]]                                                                             |
|                                                                                                                                                                                      |
| [            l_Scale.ScaleDirection = [ScaleDirection].CounterClockwise;]                                                |
|                                                                                                                                                                                      |
| [            l_Scale.BorderWidth = 4;]                                                                                                           |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Adding the scale element to the linear gauge.]]                                                            |
|                                                                                                                                                                                      |
| [            model.Scales.Add(l_Scale);]                                                                                                         |
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

 

Run the Code. You will get the following output.

 

{border="0"}

Figure 98: Linear Gauge-Scale**[]**

[                          ]

[]{#related-topics}

