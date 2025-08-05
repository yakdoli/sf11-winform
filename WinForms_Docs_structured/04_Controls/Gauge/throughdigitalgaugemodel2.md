---
title: throughdigitalgaugemodel2.md
original_path: WinForms_Docs/04_Controls/Gauge/throughdigitalgaugemodel2.md
created_at: 2025-08-05
---






##### Through DigitalGaugeModel {#through-digitalgaugemodel style="tab-stops: 0pt"}

[] 

Step 1:

View:

 

Add the below code in your aspx file.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the Digital Gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [     [\<%][=]Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                              |
| [@\*][\--Rendering the Digital Gauge\--][\*@][]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                              |
| [     ][@][Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel")]][] |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 2:

Controller:

 

Add the below code in your controller.

The character count and character height can be set using its **CharacterCount** and **CharacterHeight properties.** The character type can be set using its **CharacterType property**. The space between the characters can be set using its **CharacterSpacing** property**.**

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                            |
|                                                                                                                                                                                                   |
| [DigitalGaugeModel][ d_Gauge = [new] [DigitalGaugeModel]();] |
|                                                                                                                                                                                                   |
| [            d_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                                               |
|                                                                                                                                                                                                   |
| [            d_Gauge.FrameType = [DigitalGaugeFrameType].CroppedRectangle;]                                                           |
|                                                                                                                                                                                                   |
| [            d_Gauge.Value = [\"10:30\"];]                                                                                            |
|                                                                                                                                                                                                   |
| [            [//Sets the character count value]]                                                                                        |
|                                                                                                                                                                                                   |
| [            d_Gauge.CharacterCount = 5;]                                                                                                                     |
|                                                                                                                                                                                                   |
| [            d_Gauge.SegmentSpacing = 0.5;]                                                                                                                   |
|                                                                                                                                                                                                   |
| [            d_Gauge.SegmentWidth = 4;]                                                                                                                       |
|                                                                                                                                                                                                   |
| [            [//Sets the space between each characters]]                                                                                |
|                                                                                                                                                                                                   |
| [            d_Gauge.CharacterSpacing = 15;]                                                                                                                  |
|                                                                                                                                                                                                   |
| [            [//Sets the character type]]                                                                                               |
|                                                                                                                                                                                                   |
| [            d_Gauge.CharacterType = [CharacterType].SegmentSeven;]                                                                   |
|                                                                                                                                                                                                   |
| [            [//Sets the character height]]                                                                                             |
|                                                                                                                                                                                                   |
| [            d_Gauge.CharacterHeight = 35;]                                                                                                                   |
|                                                                                                                                                                                                   |
| [            ViewData\[[\"GaugeModel\"]\] = d_Gauge;]                                                                                 |
|                                                                                                                                                                                                   |
| [            [return] View();]                                                                                                           |
|                                                                                                                                                                                                   |
| [        }]                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code. You will get the following output.

 

{border="0"}

Figure 136: Digital Gauge-Character Customization**[]**

[                                   ]

[]{#related-topics}

