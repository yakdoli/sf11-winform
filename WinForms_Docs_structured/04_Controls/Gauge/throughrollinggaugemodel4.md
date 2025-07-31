---
title: throughrollinggaugemodel4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\throughrollinggaugemodel4.md
created_at: 2025-07-03
---






##### Through RollingGaugeModel {#through-rollinggaugemodel style="tab-stops: 0pt"}

 

Step 1:

View:

Add the below code in the aspx file.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [    [\<%][\--Rendering the rolling gauge\--][%\>]]                                                                          |
|                                                                                                                                                                                                                                                    |
| [     [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [    [@\*][\--Rendering the rolling gauge\--][\*@]]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                    |
| [@][Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])][] |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 2:

Controller:

**[]** 

Add the below code in the controller. To automatically update the segment count value dynamically, set its **IsAutomaticSegmentCountEnabled** property to True.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [public][ [ActionResult] Index()]                                      |
|                                                                                                                                                                                     |
| [        {]                                                                                                                                     |
|                                                                                                                                                                                     |
| [           [RollingGaugeModel] roll_Gauge = [new] [RollingGaugeModel]();] |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [            roll_Gauge.Value = [\"Gauge\"];]                                                                           |
|                                                                                                                                                                                     |
| [            [//Enabling the IsAutomaticSegmentCountEnabled property to update.]]                                         |
|                                                                                                                                                                                     |
| [            [//The segment count is automatically based on the gauge value.]]                                            |
|                                                                                                                                                                                     |
| [            roll_Gauge.IsAutomaticSegmentCountEnabled = [true];]                                                          |
|                                                                                                                                                                                     |
| [            roll_Gauge.Height = 50;]                                                                                                           |
|                                                                                                                                                                                     |
| [            roll_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                              |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [            ViewData\[[\"GaugeModel\"]\] = roll_Gauge;]                                                                |
|                                                                                                                                                                                     |
| [            [return] View();]                                                                                             |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [        }]                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 3:

Run the code to achieve the below output.

 

{border="0"}

Figure 154: AutomaticSegment count Enabled-Rolling Gauge**[]**

[                                                       ]

[]{#related-topics}

