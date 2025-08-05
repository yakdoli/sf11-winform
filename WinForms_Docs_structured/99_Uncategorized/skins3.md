---
title: skins3.md
original_path: WinForms_Docs/99_Uncategorized/skins3.md
created_at: 2025-08-05
---






##### Skins {#skins style="tab-stops: 0pt"}

[] 

Gauge MVC now comes with fourteen stunning skins for better and professional representation of gauges. You can now easily modify the look and feel of the gauge component by using the built-in visual styles color schemes.

[] 

Properties

 


+-------------+-------------------------------+-----------------------------+-------------------------------------------------------+--------------------------------------------------+
| Property    | Description                   | Type of Property            | Value It Accepts                                      | Any other dependencies/Sub properties associated |
+-------------+-------------------------------+-----------------------------+-------------------------------------------------------+--------------------------------------------------+
| GaugeSkins  | Sets the Skins for the Gauge. | [enum] | [GaugeSkins].Almond           | NA                                               |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Blueberry        |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Monochrome       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].VS2010           |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Office2007Blue   |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Office2007Black  |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Blend            |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Midnight         |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Marble           |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Office2007Silver |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Sandune          |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Olive            |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Vista            |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Turquoise        |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             |                                                       |                                                  |
|             |                               |                             | [GaugeSkins].Default          |                                                  |
+-------------+-------------------------------+-----------------------------+-------------------------------------------------------+--------------------------------------------------+


[] 

###### 5.3.3.1.1.1 Through View Customization {#through-view-customization style="tab-stops: 0pt"}

[] 

Step 1:

View:

Using the **GaugeSkins** property of Digital Gauge, we can set the skins.

Add the below code in your aspx file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().DigitalGauge([\"Gauge\"], gauge=\>] |
|                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [        gauge]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            .FrameType([DigitalGaugeFrameType].CroppedRectangle)]                                                                                                      |
|                                                                                                                                                                                                                                     |
| [            ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| [            [//Setting Skins for the Digital Gauge.]]                                                                                                                    |
|                                                                                                                                                                                                                                     |
| [             .GaugeSkins([GaugeSkins].Midnight);]                                                                                                                      |
|                                                                                                                                                                                                                                     |
| [                  })]                                                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [                 [%\>]]                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                           |
|                                                                                                                                                                                                |
| []                                                                                                                                            |
|                                                                                                                                                                                                |
| [@][Html.Syncfusion().DigitalGauge([\"Gauge\"],] |
|                                                                                                                                                                                                |
| [       gauge=\>]                                                                                                                             |
|                                                                                                                                                                                                |
| [    {]                                                                                                                                       |
|                                                                                                                                                                                                |
| [        gauge]                                                                                                                               |
|                                                                                                                                                                                                |
| [            .FrameType([DigitalGaugeFrameType].CroppedRectangle)]                                                    |
|                                                                                                                                                                                                |
| [            ]                                                                                                                                |
|                                                                                                                                                                                                |
| [            [//Setting Skins for the Digital Gauge.]]                                                                  |
|                                                                                                                                                                                                |
| [             .GaugeSkins([GaugeSkins].Midnight);]                                                                    |
|                                                                                                                                                                                                |
| [                  })]                                                                                                                        |
|                                                                                                                                                                                                |
| [              ]                                                                                                                              |
|                                                                                                                                                                                                |
| [                  ]                                                                                                                          |
|                                                                                                                                                                                                |
| [                  []]                                                                                            |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

Controller:

**[]** 

Add the below code in your controller.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                     |
|                                                                                                                                     |
| [        [public] [ActionResult] Index()] |
|                                                                                                                                     |
| [        {]                                                                            |
|                                                                                                                                     |
| [            [return] View();]                                    |
|                                                                                                                                     |
| [        }]                                                                            |
|                                                                                                                                     |
| [}]                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code. You will get the below output.

 

{border="0"}

Figure 124: Digital Gauge with Midnight skin**[]**

[                                       ]

###### 5.3.3.1.1.2 Through DigitalGaugeModel {#through-digitalgaugemodel style="tab-stops: 0pt"}

 

Step 1:

View:

Add the following code in your aspx file.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the Digital Gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| [     [\<%][=]Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\][]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| [@\*][\--Rendering the Digital Gauge\--][\*@][]              |
|                                                                                                                                                                                                                                                                        |
| [@][Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel\"])[]] |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 2:

Controller:

**[]** 

Add the following code in your controller. Using the **GaugeSkins** property of Digital Gauge, you can set the skins.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                            |
|                                                                                                                                                                                            |
| []                                                                                                                                            |
|                                                                                                                                                                                            |
| [        [public] [ActionResult] Index()]                                                        |
|                                                                                                                                                                                            |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                            |
| [            [DigitalGaugeModel] d_Gauge = [new] [DigitalGaugeModel]();] |
|                                                                                                                                                                                            |
| []                                                                                                                                            |
|                                                                                                                                                                                            |
| [            [//Setting Skins for the Digital Gauge.]]                                                                  |
|                                                                                                                                                                                            |
| [            d_Gauge.GaugeSkins = [GaugeSkins].Midnight;]                                                             |
|                                                                                                                                                                                            |
| [            d_Gauge.FrameType = [DigitalGaugeFrameType].CroppedRectangle;]                                           |
|                                                                                                                                                                                            |
| [            ViewData\[[\"GaugeModel\"]\] = d_Gauge;]                                                                 |
|                                                                                                                                                                                            |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                            |
| [        }]                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code. You will get the following output.

 

{border="0"}

Figure 125: Digital Gauge with Midnight skin**[]**

[] 

[                                  ]

The following are the skins available:

**[                                                ]**

{border="0"}

Figure 126: DigitalGauge Skins

**[]** 

[]{#related-topics}

