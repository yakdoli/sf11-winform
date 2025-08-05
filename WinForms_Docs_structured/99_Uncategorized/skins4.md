---
title: skins4.md
original_path: WinForms_Docs/99_Uncategorized/skins4.md
created_at: 2025-08-05
---






##### Skins {#skins style="tab-stops: 0pt"}

 

Gauge MVC now comes with fourteen stunning skins for better and professional representation of gauges. You can now easily modify the look and feel of the gauge component by using the built-in visual styles color schemes.

[] 

 


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

###### 5.4.3.1.1.1 Through View Customization {#through-view-customization style="tab-stops: 0pt"}

**[]** 

Step 1:

View:

Add the below code in your aspx file.

The skins for the Rolling Gauge can be set by using its **GaugeSkins** property.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().RollingGauge([\"Gauge\"])] |
|                                                                                                                                                                                                                            |
| [         .Height(65)]                                                                                                                                                                 |
|                                                                                                                                                                                                                            |
| [         .Width(460)]                                                                                                                                                                 |
|                                                                                                                                                                                                                            |
| [         .SegmentCount(5)]                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [         .Value([\"Gauge\"])]                                                                                                                                 |
|                                                                                                                                                                                                                            |
| [         .FontSize(30)]                                                                                                                                                               |
|                                                                                                                                                                                                                            |
| [         .SpaceBetWeenSegment(2)]                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [         //Setting skins for the Rolling Gauge.][]                                                                                  |
|                                                                                                                                                                                                                            |
| [         **.GaugeSkins([GaugeSkins]. Midnight)**]                                                                                                             |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                    |
|                                                                                                                                                                         |
| [\@{][ Html.Syncfusion().RollingGauge([\"Gauge\"])] |
|                                                                                                                                                                         |
| [         .Height(65)]                                                                                                              |
|                                                                                                                                                                         |
| [         .Width(460)]                                                                                                              |
|                                                                                                                                                                         |
| [         .SegmentCount(5)]                                                                                                         |
|                                                                                                                                                                         |
| [         .Value([\"Gauge\"])]                                                                              |
|                                                                                                                                                                         |
| [         .FontSize(30)]                                                                                                            |
|                                                                                                                                                                         |
| [         .SpaceBetWeenSegment(2)]                                                                                                  |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [         //Setting skins for the Rolling Gauge.][]                               |
|                                                                                                                                                                         |
| [         **.GaugeSkins([GaugeSkins]. Midnight).**Render();]                                                |
|                                                                                                                                                                         |
| [    [}]]                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 2:

Controller:

Add the below code in your controller.

 

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

Run the Code. You will get the below output.

 

{border="0"}

Figure 142: Rolling Gauge with Midnight Skin**[]**

[                               ]

###### 5.4.3.1.1.2 Through RollingGaugeModel {#through-rollinggaugemodel style="tab-stops: 0pt"}

**[]** 

View:

Step 1:

Add the below code in your aspx file.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]  ]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]  ]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [@][Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])][] |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

Controller:

Add the below code in the controller. The skins for the Rolling Gauge can be set by using its **GaugeSkins** property.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [public][ [ActionResult] Index()]                                    |
|                                                                                                                                                                                   |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                   |
| [            [RollingGaugeModel] r_Gauge = [new] [RollingGaugeModel]();] |
|                                                                                                                                                                                   |
| [            r_Gauge.Height = 65;]                                                                                                            |
|                                                                                                                                                                                   |
| [            r_Gauge.Width = 460;]                                                                                                            |
|                                                                                                                                                                                   |
| [            r_Gauge.SegmentCount = 5;]                                                                                                       |
|                                                                                                                                                                                   |
| [            r_Gauge.Value = [\"Gauge\"];]                                                                            |
|                                                                                                                                                                                   |
| [            r_Gauge.FontSize = 30;]                                                                                                          |
|                                                                                                                                                                                   |
| [            r_Gauge.SpaceBetWeenSegment = 2;]                                                                                                |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [    //Setting skins for the Rolling Gauge.][]                                              |
|                                                                                                                                                                                   |
| [            **r_Gauge.GaugeSkins = [GaugeSkins].Midnight;**]                                                         |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            ViewData\[[\"GaugeModel\"]\] = r_Gauge;]                                                                 |
|                                                                                                                                                                                   |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                   |
| [        }]                                                                                                                                   |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [    }]                                                                                                                                       |
|                                                                                                                                                                                   |
| [}]                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the Code. You will get the following output.

 

{border="0"}

Figure 143: Rolling Gauge with Midnight Skin**[]**

[                                 ]

The following are the skins available:

**[]** 

{border="0"}

Figure 144:Rolling Gauge-Skins

[] 

[]{#related-topics}

