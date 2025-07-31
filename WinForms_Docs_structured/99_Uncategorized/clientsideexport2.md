---
title: clientsideexport2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideexport2.md
created_at: 2025-07-03
---






##### ClientSide Export {#clientside-export style="tab-stops: 0pt"}

[] 

Refer to the below code to export the gauge in client side.

Step 1:

Controller:

 

Add the below code in your controller.

 By setting the **GaugeExport** property to **ClientSide** and calling the **GenerateGaugeImage()** function, you can export the gauge in client side .

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [public][ [ActionResult] Index()]                                    |
|                                                                                                                                                                                   |
| [        {]                                                                                                                                   |
|                                                                                                                                                                                   |
| [            [DigitalGaugeModel] d_Gauge = [new] [DigitalGaugeModel]();] |
|                                                                                                                                                                                   |
| [            d_Gauge.Height = 105;]                                                                                                           |
|                                                                                                                                                                                   |
| [            d_Gauge.Width = 350;]                                                                                                            |
|                                                                                                                                                                                   |
| [            d_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                               |
|                                                                                                                                                                                   |
| [            d_Gauge.FrameType = [DigitalGaugeFrameType].CroppedRectangle;]                                           |
|                                                                                                                                                                                   |
| [            d_Gauge.SegmentSpacing = 0.8;]                                                                                                   |
|                                                                                                                                                                                   |
| [            d_Gauge.CharacterType = [CharacterType].SegmentFourteen;]                                                |
|                                                                                                                                                                                   |
| [            d_Gauge.CharacterHeight = 28;]                                                                                                   |
|                                                                                                                                                                                   |
| [            d_Gauge.CharacterSpacing = 5;]                                                                                                   |
|                                                                                                                                                                                   |
| [            d_Gauge.SegmentWidth = 2.5;]                                                                                                     |
|                                                                                                                                                                                   |
| [            d_Gauge.Value = [\"Syncfusion\"];]                                                                       |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [            [//Sets for client side export.]]                                                                          |
|                                                                                                                                                                                   |
| [            d_Gauge.GaugeExport = [GaugeExport].ClientSide;]                                                         |
|                                                                                                                                                                                   |
| [            [//Function to generate the gauge in Server or client side in Gif format.]]                                |
|                                                                                                                                                                                   |
| [            d_Gauge.GenerateGaugeImage(d_Gauge, [\"Gauge\"], [ImageFormat].Gif);]            |
|                                                                                                                                                                                   |
| [            ViewData\[[\"GaugeModel\"]\] = d_Gauge;]                                                                 |
|                                                                                                                                                                                   |
| [            [return] View();]                                                                                           |
|                                                                                                                                                                                   |
| [        }]                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 2:

View:

**[]** 

Add the below code in view page.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the Digital Gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [     [\<%][=]Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [@\*][\--Rendering the Digital Gauge\--][\*@][]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [     ][@][Html.Syncfusion().DigitalGauge([\"Gauge\"], [\"GaugeModel\"])][] |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 3:

Run the code. Then the below save dialog window will open . Then you can save the image.

 

{border="0"}

Figure 138: Client Side Exporting-Save Dialog Box**[]**

**[                         ]**

[]{#related-topics}

