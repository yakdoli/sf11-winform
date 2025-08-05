---
title: throughrollinggaugemodel.md
original_path: WinForms_Docs/04_Controls/Gauge/throughrollinggaugemodel.md
created_at: 2025-08-05
---






#### Through RollingGaugeModel : {#through-rollinggaugemodel style="tab-stops: 0pt"}

 

Step 1:

View:

 

Add the below code in your aspx file.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the Rolling Gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [     [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                               |
| [@\*][\--Rendering the Rolling Gauge\--][\*@][]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [     ][@][Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])][] |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

Controller:[ ]

[] 

Add the below code in the controller.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [public][ [ActionResult] Index()]                                    |
|                                                                                                                                                                                   |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                   |
| [            [//Creating a Rolling Gauge.]]                                                                             |
|                                                                                                                                                                                   |
| [            [RollingGaugeModel] r_Gauge = [new] [RollingGaugeModel]();] |
|                                                                                                                                                                                   |
| [            [//Specifying the height and width of the gauge.]]                                                         |
|                                                                                                                                                                                   |
| [            r_Gauge.Height = 55;]                                                                                                            |
|                                                                                                                                                                                   |
| [            r_Gauge.Width = 500;]                                                                                                            |
|                                                                                                                                                                                   |
| [            [//Setting the segment count value.]]                                                                      |
|                                                                                                                                                                                   |
| [            r_Gauge.SegmentCount = 5;]                                                                                                       |
|                                                                                                                                                                                   |
| [            [//Specifying the value for the gauge.]]                                                                   |
|                                                                                                                                                                                   |
| [            r_Gauge.Value = [\"10000\"];]                                                                            |
|                                                                                                                                                                                   |
| [            [//Setting the font-size.]]                                                                                |
|                                                                                                                                                                                   |
| [            r_Gauge.FontSize = 20;]                                                                                                          |
|                                                                                                                                                                                   |
| [            [//Setting the border width for the segments.]]                                                            |
|                                                                                                                                                                                   |
| [            r_Gauge.SegmentBorderWidth = 1;]                                                                                                 |
|                                                                                                                                                                                   |
| [            [//Specifying the space between the segments.]]                                                            |
|                                                                                                                                                                                   |
| [            r_Gauge.SpaceBetWeenSegment = 2;]                                                                                                |
|                                                                                                                                                                                   |
| [            [//Setting the skins for the gauge.]]                                                                      |
|                                                                                                                                                                                   |
| [            r_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                               |
|                                                                                                                                                                                   |
| [            [//Setting RadiusX and RadiusY values to get the rounded corner.]]                                         |
|                                                                                                                                                                                   |
| [            r_Gauge.RadiusX = 8;]                                                                                                            |
|                                                                                                                                                                                   |
| [            r_Gauge.RadiusY = 8;]                                                                                                            |
|                                                                                                                                                                                   |
| [            [//Setting the unit value.]]                                                                               |
|                                                                                                                                                                                   |
| [            r_Gauge.Unit = [\"KM\"];]                                                                                |
|                                                                                                                                                                                   |
| [            [//Passing the gauge model to the view.]]                                                                  |
|                                                                                                                                                                                   |
| [            ViewData\[[\"GaugeModel\"]\] = r_Gauge;]                                                                 |
|                                                                                                                                                                                   |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                   |
| [        }]                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

[] 

Run the Code. You will get the below output.

 

{border="0"}

Figure 140: Rolling Gauge**[]**

[                                      ]

A sample which [demonstrates a Rolling ]Gauge control can be downloaded from the below mentioned link.

[] 


[ASPX Application](http://files2.syncfusion.com/support/ASP%20MVC/UG/Gauge/Rolling%20Gauge%20(ASPX).zip)

[Razor Application](http://files2.syncfusion.com/support/ASP%20MVC/UG/Gauge/Rolling%20Gauge%20(Razor).zip)


[[]]{.UGHyperlink} 


{border="0"} Note: The version number for the assemblies has been set to 9.4.0.62 in the Web.config file of the attached sample


**[]** 

[]{#related-topics}

