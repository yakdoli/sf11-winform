---
title: throughdigitalgaugemodel1.md
original_path: WinForms_Docs/04_Controls/Gauge/throughdigitalgaugemodel1.md
created_at: 2025-08-05
---






##### Through DigitalGaugeModel {#through-digitalgaugemodel style="tab-stops: 0pt"}

[] 

Step 1:

View:

Add the following code in your aspx file.

 

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

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                           |
| [@\*][\--Rendering the Digital Gauge\--][\*@][] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [@][Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel\"])]                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

 

Step 2:

Controller:

 

Add the below code in your controller.

The  space between the segments can be customized using its **SegmentSpacing** property and the segment width can be customized using its **SegmentWidth** property.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [        [public] [ActionResult] Index()]                                                        |
|                                                                                                                                                                                   |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                   |
| [            [DigitalGaugeModel] d_Gauge = [new] [DigitalGaugeModel]();] |
|                                                                                                                                                                                   |
| [            d_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                               |
|                                                                                                                                                                                   |
| [            d_Gauge.FrameType = [DigitalGaugeFrameType].CroppedRectangle;]                                           |
|                                                                                                                                                                                   |
| [            d_Gauge.Value = [\"10:30 PM\"];]                                                                         |
|                                                                                                                                                                                   |
| [            d_Gauge.CharacterCount = 8;]                                                                                                     |
|                                                                                                                                                                                   |
| [           //Setting the segment space.][]                                                 |
|                                                                                                                                                                                   |
| **[            d_Gauge.SegmentSpacing = 0.5;]**                                                                                               |
|                                                                                                                                                                                   |
| [            [//Setting the segment width.]]                                                                            |
|                                                                                                                                                                                   |
| **[            d_Gauge.SegmentWidth = 2;]**                                                                                                   |
|                                                                                                                                                                                   |
| [            d_Gauge.DimmedBrush = [Brushes].Gray;]                                                                   |
|                                                                                                                                                                                   |
| [            ViewData\[[\"GaugeModel\"]\] = d_Gauge;]                                                                 |
|                                                                                                                                                                                   |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                   |
| [        }]                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code. You will get the following output.

[] 

{border="0"}

Figure 134: Digital Gauge-Segment customization**[]**

[                             ]

[]{#related-topics}

