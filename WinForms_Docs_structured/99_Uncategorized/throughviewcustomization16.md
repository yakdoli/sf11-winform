---
title: throughviewcustomization16.md
original_path: WinForms_Docs/99_Uncategorized/throughviewcustomization16.md
created_at: 2025-08-05
---






##### Through View Customization {#through-view-customization style="tab-stops: 0pt"}

 

Step 1:

**[]** 

The  space between the segments can be customized using its **SegmentSpacing** property and the segment width can be customized using its **SegmentWidth** property.

Add the below code in your aspx file.

View:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().DigitalGauge([\"Gauge\"], gauge=\>] |
|                                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [        gauge.Height(105)]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [            .Width(350)]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [            .GaugeSkins([GaugeSkins].VS2010)]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [            .DimmedBrush([Brushes].Gray)]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [            .FrameType([DigitalGaugeFrameType].CroppedRectangle)]                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [            [//Setting the segment space.]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [            .SegmentSpacing(0.5)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [            .CharacterCount(8)]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [            [//Setting the segment width.]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [            .SegmentWidth(2)]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [            .Value([\"10:30 PM\"]);]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [               ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [                  })]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [                 [%\>]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [@][Html.Syncfusion().DigitalGauge([\"Gauge\"], gauge=\>] |
|                                                                                                                                                                                                         |
| [    {]                                                                                                                                                |
|                                                                                                                                                                                                         |
| [        gauge.Height(105)]                                                                                                                            |
|                                                                                                                                                                                                         |
| [            .Width(350)]                                                                                                                              |
|                                                                                                                                                                                                         |
| [            .GaugeSkins([GaugeSkins].VS2010)]                                                                                 |
|                                                                                                                                                                                                         |
| [            .DimmedBrush([Brushes].Gray)]                                                                                     |
|                                                                                                                                                                                                         |
| [            .FrameType([DigitalGaugeFrameType].CroppedRectangle)]                                                             |
|                                                                                                                                                                                                         |
| [            [//Setting the segment space.]]                                                                                     |
|                                                                                                                                                                                                         |
| [            .SegmentSpacing(0.5)]                                                                                                                     |
|                                                                                                                                                                                                         |
| [            .CharacterCount(8)]                                                                                                                       |
|                                                                                                                                                                                                         |
| [            [//Setting the segment width.]]                                                                                     |
|                                                                                                                                                                                                         |
| [            .SegmentWidth(2)]                                                                                                                         |
|                                                                                                                                                                                                         |
| [            .Value([\"10:30 PM\"]);]                                                                                          |
|                                                                                                                                                                                                         |
| [               ]                                                                                                                                      |
|                                                                                                                                                                                                         |
| [                  })]                                                                                                                                 |
|                                                                                                                                                                                                         |
| []                                                                                                                                                     |
|                                                                                                                                                                                                         |
| []                                                                                                                                                     |
|                                                                                                                                                                                                         |
| []                                                                                                                                                     |
|                                                                                                                                                                                                         |
| []                                                                                                                                                     |
|                                                                                                                                                                                                         |
| []                                                                                                                                                     |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Step 2:

Controller:

 

Add the below code in your controller.

 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                         |
|                                                                                                                                                |
| [public][ [ActionResult] Index()] |
|                                                                                                                                                |
| [        {           ]                                                                                     |
|                                                                                                                                                |
| [            [return] View();]                                                        |
|                                                                                                                                                |
| [        }]                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

[] 

Run the code. You will get the following output.

 

{border="0"}

Figure 133: Digital Gauge-Segment customization**[]**

[                          ]

 

[]{#related-topics}

