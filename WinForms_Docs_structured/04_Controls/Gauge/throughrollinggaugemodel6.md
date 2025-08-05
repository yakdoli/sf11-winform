---
title: throughrollinggaugemodel6.md
original_path: WinForms_Docs/04_Controls/Gauge/throughrollinggaugemodel6.md
created_at: 2025-08-05
---






##### Through RollingGaugeModel {#through-rollinggaugemodel style="tab-stops: 0pt"}

 

Step 1:

View:

Add the below code in the aspx file.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                               |
| [\<%][\--Rendering the rolling gauge\--][%\>][] |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                               |
| [    [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"],[\"GaugeModel\"])[%\>]]                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                            |
| [@\*][\--Rendering the rolling gauge\--][\*@][]              |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [@][Html.Syncfusion().RollingGauge([\"Gauge\"],[\"GaugeModel\"])][] |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 2:

Controller:

 

Add the code below in the controller. Rolling Gauge can be restricted to display only the numeric values.

This can be done by setting its **IsNumeric** property to True. Also maximum and minimum can be set for the rolling gauge when the **IsNumeric** property is set to True. This can be done by setting its **MaxValue** and **MinValue** properties.

 

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
| [            roll_Gauge.Value = [\"10000\"];]                                                                           |
|                                                                                                                                                                                     |
| [            [//Sets to display only the numeric values.]]                                                                |
|                                                                                                                                                                                     |
| **[            roll_Gauge.IsNumeric = [true];]**                                                                           |
|                                                                                                                                                                                     |
| [            [//Setting maximum and minimum values for the rolling gauge.]]                                               |
|                                                                                                                                                                                     |
| **[            roll_Gauge.MaxValue = 1000;]**                                                                                                   |
|                                                                                                                                                                                     |
| **[            roll_Gauge.MinValue = 500;]**                                                                                                    |
|                                                                                                                                                                                     |
| [            roll_Gauge.IsAutomaticSegmentCountEnabled = [true];]                                                          |
|                                                                                                                                                                                     |
| [            roll_Gauge.Height = 50;]                                                                                                           |
|                                                                                                                                                                                     |
| [            roll_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                              |
|                                                                                                                                                                                     |
| [            ViewData\[[\"GaugeModel\"]\] = roll_Gauge;]                                                                |
|                                                                                                                                                                                     |
| [            [return] View();]                                                                                             |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [        }]                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code to achieve the below output.

 

{border="0"}

Figure 158: RollingGauge with Numeric Value**[]**

[                                                           ]


{border="0"} Note: In the above example, the rolling gauge displays the value "1000" eventhough its value is set as "10000", because the Maximum value is set as "1000".


[]{#related-topics}

