---
title: throughviewcustomization25.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughviewcustomization25.md
created_at: 2025-07-03
---






##### Through View Customization {#through-view-customization style="tab-stops: 0pt"}

 

Step 1:

View:

 

The segments of the rolling gauge can be customized using its **SegmentBorderWidth**, **SpaceBetWeenSegment**,etc. If you set these properties, it will be applied for all segments. But if we want to customize the particular segments, then this can be done using the **Segments** mapper by setting its **CharacterIndex** property.

 

In the below code, CharacterIndex is specified as 2. Then the third segment will be customized. The specified segments has their own properties to customize it. 

 

 You can customize the background and border color for the specified segments using the **BackgroundColor** and **BorderColor** properties.  The font color, font family and font size can be customized using its **FontColor**, **FontSize** and **FontFamily** properties. The value for the specified segment can be given by using its **Value** property.

 

Add the below code in your aspx file.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().RollingGauge([\"Gauge\"])] |
|                                                                                                                                                                                                                            |
| [            .Height(50)]                                                                                                                                                              |
|                                                                                                                                                                                                                            |
| [            .Width(300)]                                                                                                                                                              |
|                                                                                                                                                                                                                            |
| [            .FontFamily([new] System.Drawing.[FontFamily]([\"Calibri\"]))]                                       |
|                                                                                                                                                                                                                            |
| [              [//Setting the segment count.]]                                                                                                                   |
|                                                                                                                                                                                                                            |
| [            **.SegmentCount(5)**]                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [            [//Setting the space between each segments.]]                                                                                                       |
|                                                                                                                                                                                                                            |
| [            **.SpaceBetWeenSegment(2)**]                                                                                                                                              |
|                                                                                                                                                                                                                            |
| [              [//Setting the border width for the segments.]]                                                                                                   |
|                                                                                                                                                                                                                            |
| [            **.SegmentBorderWidth(1)**]                                                                                                                                               |
|                                                                                                                                                                                                                            |
| [            .BorderWidth(10)]                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [            .Value([\"Gauge\"])]                                                                                                                              |
|                                                                                                                                                                                                                            |
| [             .Direction([Direction].Clockwise)]                                                                                                               |
|                                                                                                                                                                                                                            |
| [            .UnitPosition([UnitPosition].End)]                                                                                                                |
|                                                                                                                                                                                                                            |
| [            .MaxValue(10000)]                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [            .MinValue(100)]                                                                                                                                                           |
|                                                                                                                                                                                                                            |
| [            .AnimationDelay(500)]                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [            .FontSize(30)]                                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [            .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                 |
|                                                                                                                                                                                                                            |
| [              [//Customizing the particular segments by specifying the index values.]]                                                                          |
|                                                                                                                                                                                                                            |
| [              **.Segments(seg=\>**]                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [                {]                                                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [                  seg.Add()]                                                                                                                                                          |
|                                                                                                                                                                                                                            |
| [                    [//Setting the character index.]]                                                                                                           |
|                                                                                                                                                                                                                            |
| [                **.CharacterIndex(2)**]                                                                                                                                               |
|                                                                                                                                                                                                                            |
| [                    [//Setting border and background color for the segment specified by the CharacterIndex property.]]                                          |
|                                                                                                                                                                                                                            |
| [                .BackgroundColor(System.Drawing.[Color].LightBlue)]                                                                                           |
|                                                                                                                                                                                                                            |
| [                  .BorderColor(System.Drawing.[Color].Pink)]                                                                                                  |
|                                                                                                                                                                                                                            |
| [                    [//Setting the font color for the segment specified by the CharacterIndex property.]]                                                       |
|                                                                                                                                                                                                                            |
| [                .FontColor(System.Drawing.[Color].White)]                                                                                                     |
|                                                                                                                                                                                                                            |
| [                    [//Setting the border width for the segment specified by the CharacterIndex property.]]                                                     |
|                                                                                                                                                                                                                            |
| [                .BorderWidth(3)]                                                                                                                                                      |
|                                                                                                                                                                                                                            |
| [                    [//Setting the font size for the segment specified by the CharacterIndex property.]]                                                        |
|                                                                                                                                                                                                                            |
| [                .FontSize(20)]                                                                                                                                                        |
|                                                                                                                                                                                                                            |
| [                    [//Setting the value for the segment specified by the CharacterIndex property.]]                                                            |
|                                                                                                                                                                                                                            |
| [                  .Value([\'u\']);]                                                                                                                           |
|                                                                                                                                                                                                                            |
| [            })]                                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [            ]                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                 |
|                                                                                                                                                                                      |
| [\@{][ Html.Syncfusion().RollingGauge([\"Gauge\"])]              |
|                                                                                                                                                                                      |
| [            .Height(50)]                                                                                                                        |
|                                                                                                                                                                                      |
| [            .Width(300)]                                                                                                                        |
|                                                                                                                                                                                      |
| [            .FontFamily([new] System.Drawing.[FontFamily]([\"Calibri\"]))] |
|                                                                                                                                                                                      |
| [              [//Setting the segment count.]]                                                                             |
|                                                                                                                                                                                      |
| [            **.SegmentCount(5)**]                                                                                                               |
|                                                                                                                                                                                      |
| [            [//Setting the space between each segments.]]                                                                 |
|                                                                                                                                                                                      |
| [            **.SpaceBetWeenSegment(2)**]                                                                                                        |
|                                                                                                                                                                                      |
| [              [//Setting the border width for the segments.]]                                                             |
|                                                                                                                                                                                      |
| [            **.SegmentBorderWidth(1)**]                                                                                                         |
|                                                                                                                                                                                      |
| [            .BorderWidth(10)]                                                                                                                   |
|                                                                                                                                                                                      |
| [            .Value([\"Gauge\"])]                                                                                        |
|                                                                                                                                                                                      |
| [             .Direction([Direction].Clockwise)]                                                                         |
|                                                                                                                                                                                      |
| [            .UnitPosition([UnitPosition].End)]                                                                          |
|                                                                                                                                                                                      |
| [            .MaxValue(10000)]                                                                                                                   |
|                                                                                                                                                                                      |
| [            .MinValue(100)]                                                                                                                     |
|                                                                                                                                                                                      |
| [            .AnimationDelay(500)]                                                                                                               |
|                                                                                                                                                                                      |
| [            .FontSize(30)]                                                                                                                      |
|                                                                                                                                                                                      |
| [            .GaugeSkins([GaugeSkins].VS2010)]                                                                           |
|                                                                                                                                                                                      |
| [              [//Customizing the particular segments by specifying the index value.]]                                     |
|                                                                                                                                                                                      |
| [              **.Segments(seg=\>**]                                                                                                             |
|                                                                                                                                                                                      |
| [                {]                                                                                                                              |
|                                                                                                                                                                                      |
| [                  seg.Add()]                                                                                                                    |
|                                                                                                                                                                                      |
| [                    [//Setting the character index.]]                                                                     |
|                                                                                                                                                                                      |
| [                **.CharacterIndex(2)**]                                                                                                         |
|                                                                                                                                                                                      |
| [                    [//Setting border and background color for the segment specified by the CharacterIndex property.]]    |
|                                                                                                                                                                                      |
| [                .BackgroundColor(System.Drawing.[Color].LightBlue)]                                                     |
|                                                                                                                                                                                      |
| [                  .BorderColor(System.Drawing.[Color].Pink)]                                                            |
|                                                                                                                                                                                      |
| [                    [//Setting the font color for the segment specified by the CharacterIndex property.]]                 |
|                                                                                                                                                                                      |
| [                .FontColor(System.Drawing.[Color].White)]                                                               |
|                                                                                                                                                                                      |
| [                    [//Setting the border width for the segment specified by the CharacterIndex property.]]               |
|                                                                                                                                                                                      |
| [                .BorderWidth(3)]                                                                                                                |
|                                                                                                                                                                                      |
| [                    [//Setting the font size for the segment specified by the CharacterIndex property.]]                  |
|                                                                                                                                                                                      |
| [                .FontSize(20)]                                                                                                                  |
|                                                                                                                                                                                      |
| [                    [//Setting the value for the segment specified by the CharacterIndex property.]]                      |
|                                                                                                                                                                                      |
| [                  .Value([\'u\']);]                                                                                     |
|                                                                                                                                                                                      |
| [            }).Render();            ]                                                                                                           |
|                                                                                                                                                                                      |
| [    [}]]                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Controller:

Step 2:

 

Add the below code in your controller.

 

+----------------------------------------------------------------------------------------------------------------------------+
| []                                                                                     |
|                                                                                                                            |
| [        [public] [ActionResult] Index()] |
|                                                                                                                            |
| [        {]                                                                            |
|                                                                                                                            |
| []                                                                                     |
|                                                                                                                            |
| [            [return] View();]                                    |
|                                                                                                                            |
| [        }]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 3:

Run the code. You will get the below output.

 

{border="0"}

Figure 159: Rolling Gauge-Segment Customization**[]**

[                                                          ]

**[]** 

[]{#related-topics}

