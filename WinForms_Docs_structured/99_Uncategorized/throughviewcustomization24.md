---
title: throughviewcustomization24.md
original_path: WinForms_Docs/99_Uncategorized/throughviewcustomization24.md
created_at: 2025-08-05
---






##### Through View Customization {#through-view-customization style="tab-stops: 0pt"}

[] 

Step 1:

View:

 

Rolling Gauge can be restricted to display only the numeric values.

 

This can be done by setting its **IsNumeric** property to True. Also maximum and Minimum value can be set for the rolling gauge when the **IsNumeric** property is set to True. This can be done by setting its **MaxValue** and **MinValue** properties.

 

If you set the value for the rolling gauge higher than the maximum value, it will take the maximum value and if you set the value lesser than the mnimum value, then it will take the minimum value.

Add the below code in the aspx file.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the rolling gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| [    [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                    |
|                                                                                                                                                                                                                                                           |
| [         .Value([\"10000\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Sets to display only the numeric values.]]                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [            **.IsNumeric([true])**]                                                                                                                                                             |
|                                                                                                                                                                                                                                                           |
| [            [//Setting the maximum and minimum values for the rolling gauge.]]                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| **[           .MaxValue(1000)]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| **[           .MinValue(500)]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [          .IsAutomaticSegmentCountEnabled([true])]                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [           .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [           .Height(50)]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [         ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [    [%\>]]                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [@\*][\--Rendering the rolling gauge\--][\*@][] |
|                                                                                                                                                                                                                                                           |
| [    [\@{] Html.Syncfusion().RollingGauge([\"Gauge\"])]                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [         .Value([\"10000\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [            [//Sets to display only the numeric values.]]                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [            **.IsNumeric([true])**]                                                                                                                                                             |
|                                                                                                                                                                                                                                                           |
| [            [//Setting maximum and minimum values for the rolling gauge.]]                                                                                                                     |
|                                                                                                                                                                                                                                                           |
| **[           .MaxValue(1000)]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| **[           .MinValue(500)]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [          .IsAutomaticSegmentCountEnabled([true])]                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [           .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [           .Height(50).Render();         ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [    [}]]                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 2:

Controller:

 

Add the code below in the controller.

 

+----------------------------------------------------------------------------------------------------------------------------+
| []                                                                                     |
|                                                                                                                            |
| [        [public] [ActionResult] Index()] |
|                                                                                                                            |
| [        {]                                                                            |
|                                                                                                                            |
| [            [return] View();]                                    |
|                                                                                                                            |
| [        }]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code to achieve the below output.

 

{border="0"}

Figure 157: RollingGauge with Numeric Value**[]**

[                                                                        ]


{border="0"} Note: In the above example, the rolling gauge displays the value "1000" eventhough its value is set as "10000", because the Maximum value is set as "1000".


[]{#related-topics}

