---
title: throughrollinggaugemodel7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\throughrollinggaugemodel7.md
created_at: 2025-07-03
---






##### Through RollingGaugeModel {#through-rollinggaugemodel style="tab-stops: 0pt"}

**[]** 

Step 1:

View:

Add the below code in your aspx file.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [\<%][\--Rendering the rolling gauge\--][%\>][] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [  [\<%][=]Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"])[%\>]]           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                              |
| [@\*][\--Rendering the rolling gauge\--][\*@][]                                                    |
|                                                                                                                                                                                                                                                                                                              |
| [@][Html.Syncfusion().RollingGauge([\"Gauge\"], [\"GaugeModel\"]][)[]] |
|                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 2:

Controller:

 

The segments of the rolling gauge can be customized using its **SegmentBorderWidth**, **SpaceBetWeenSegment**,etc. If you set these properties, it will be applied for all segments. But if you want to customize the particular segments, then this can be done initializing the **RollingCharacter** class and setting its **CharacterIndex** property.

 

In the below code, CharacterIndex is specified as 2. Then the third segment will be customized. The specified segments can be customized through **RollingCharacter** class properties. 

 

You can customize the background and border color for the specified segments using the **BackgroundColor** and **BorderColor** properties.  The font color, font family and font size can be customized using its **FontColor, FontSize** and **FontFamily** properties. The value for the specified segment can be given by using its **Value** property.

 

You can specify the index of the character to be customized using the RollingCharacter class's property named CharacterIndex  and you can customize the specified segment by using its other properties

Add the below code in your controller.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [public][ [ActionResult] Index()]                                        |
|                                                                                                                                                                                       |
| [        {]                                                                                                                                       |
|                                                                                                                                                                                       |
| [           [RollingGaugeModel] roll_Gauge = [new] [RollingGaugeModel]();]   |
|                                                                                                                                                                                       |
| [            roll_Gauge.Height = 50;]                                                                                                             |
|                                                                                                                                                                                       |
| [            roll_Gauge.Width = 300;]                                                                                                             |
|                                                                                                                                                                                       |
| [            roll_Gauge.GaugeSkins = [GaugeSkins].VS2010;]                                                                |
|                                                                                                                                                                                       |
| [            roll_Gauge.FontSize = 30;]                                                                                                           |
|                                                                                                                                                                                       |
| [            [//Setting the space between each segments.]]                                                                  |
|                                                                                                                                                                                       |
| [            roll_Gauge.SpaceBetWeenSegment = 2;]                                                                                                 |
|                                                                                                                                                                                       |
| [            [//Setting the segment count.]]                                                                                |
|                                                                                                                                                                                       |
| [            roll_Gauge.SegmentCount = 5;]                                                                                                        |
|                                                                                                                                                                                       |
| [            roll_Gauge.Value = [\"Gauge\"];]                                                                             |
|                                                                                                                                                                                       |
| [            roll_Gauge.BorderWidth = 10;]                                                                                                        |
|                                                                                                                                                                                       |
| [            [//Setting the border width for the segments.]]                                                                |
|                                                                                                                                                                                       |
| [            roll_Gauge.SegmentBorderWidth = 1;]                                                                                                  |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [            [//Using the RollingCharacter class, we can customize the particular segments by specifying the index value.]] |
|                                                                                                                                                                                       |
| [            [RollingCharacter] seg1 = [new] [RollingCharacter]();]          |
|                                                                                                                                                                                       |
| [            [//Setting the character index.]]                                                                              |
|                                                                                                                                                                                       |
| [            seg1.CharacterIndex = 2;]                                                                                                            |
|                                                                                                                                                                                       |
| [            [//Setting the value for the segment specified by the CharacterIndex property.]]                               |
|                                                                                                                                                                                       |
| [            seg1.Value = [\'u\'];]                                                                                       |
|                                                                                                                                                                                       |
| [            [//Setting border and background color for the segment specified by the CharacterIndex property.]]             |
|                                                                                                                                                                                       |
| [            seg1.BackgroundColor = System.Drawing.[Color].LightBlue;]                                                    |
|                                                                                                                                                                                       |
| [            seg1.BorderColor = System.Drawing.[Color].Pink;]                                                             |
|                                                                                                                                                                                       |
| [            [//setting the border width for the segment specified by the CharacterIndex property.]]                        |
|                                                                                                                                                                                       |
| [            seg1.BorderWidth = 3;]                                                                                                               |
|                                                                                                                                                                                       |
| [            [//Setting the font size for the segment specified by the CharacterIndex property.]]                           |
|                                                                                                                                                                                       |
| [            seg1.FontSize = 20;]                                                                                                                 |
|                                                                                                                                                                                       |
| [            [//Setting the font color for the segment specified by the CharacterIndex property.]]                          |
|                                                                                                                                                                                       |
| [            seg1.FontColor = System.Drawing.[Color].White;]                                                              |
|                                                                                                                                                                                       |
| [            [//Adding the rolling character to be customized in the segments collection.]]                                 |
|                                                                                                                                                                                       |
| [            roll_Gauge.Segments.Add(seg1);]                                                                                                      |
|                                                                                                                                                                                       |
| [            ViewData\[[\"GaugeModel\"]\] = roll_Gauge;]                                                                  |
|                                                                                                                                                                                       |
| [            [return] View();]                                                                                               |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [        }]                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code. You will get the below output.

 

{border="0"}

Figure 160: Rolling Gauge-Segment Customization

**[]** 

[]{#related-topics}

