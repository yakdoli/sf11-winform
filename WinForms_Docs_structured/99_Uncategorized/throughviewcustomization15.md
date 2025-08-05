---
title: throughviewcustomization15.md
original_path: WinForms_Docs/99_Uncategorized/throughviewcustomization15.md
created_at: 2025-08-05
---






#### Through View Customization {#through-view-customization style="tab-stops: 0pt"}

 

Step 1:

View:

 

Add the below code in your aspx file.

The Height and Width of the Digital Gauge can be controlled using its Height and Width properties.  The Width of the first and second frame can be customized by its **FirstFrameThickness** and **SecondFrameThickness** properties. The segments and Characters of the digital gauge can be customized.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().DigitalGauge([\"Gauge\"], gauge=\>] |
|                                                                                                                                                                                                                                     |
| [         {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                     |
| [        gauge]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            [//Setting the height and width for the digital gauge.     ]]                                                                                                |
|                                                                                                                                                                                                                                     |
| [            .Height(100)]                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| [            .Width(350)   ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                     |
| [            [//Setting first, second and center frame colors.]]                                                                                                          |
|                                                                                                                                                                                                                                     |
| [            .FirstFrameFillColor([Brushes].LightGray)]                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            .SecondFrameFillColor([Brushes].DarkGray)]                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            .CenterFrameFillColor([Brushes].Gray)]                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            [//Setting first and second frame thickness.]]                                                                                                               |
|                                                                                                                                                                                                                                     |
| [            .FirstFrameThickness([new] System.Windows.[Thickness](8))]                                                                            |
|                                                                                                                                                                                                                                     |
| [            .SecondFrameThickness([new] System.Windows.[Thickness](6))]                                                                           |
|                                                                                                                                                                                                                                     |
| [            [//Sets the color for the bright segments.]]                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            .Foreground([Brushes].Red)]                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [            [//Sets color for the dimmed segments.]]                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            .DimmedBrush([Brushes].DarkGray)]                                                                                                                          |
|                                                                                                                                                                                                                                     |
| [            .Value([\"10000\"])]                                                                                                                                       |
|                                                                                                                                                                                                                                     |
| [            [//Setting the frame type for the Digital Gauge.    ]]                                                                                                       |
|                                                                                                                                                                                                                                     |
| [            .FrameType([DigitalGaugeFrameType].CroppedRectangle)]                                                                                                      |
|                                                                                                                                                                                                                                     |
| [            [//Setting the space between the segments.]]                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [            .SegmentSpacing(0.8)]                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [            [//setting the character type.]]                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [            .CharacterType([CharacterType].SegmentFourteen)]                                                                                                           |
|                                                                                                                                                                                                                                     |
| [            .CharacterSpacing(5)]                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [            [//Setting character height and character count.]]                                                                                                           |
|                                                                                                                                                                                                                                     |
| [            .CharacterCount(10)]                                                                                                                                                               |
|                                                                                                                                                                                                                                     |
| [            .CharacterHeight(28)]                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [            [//Setting the segment width.]]                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [            .SegmentWidth(2.5)]                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [            [//Setting the value for the gauge.]]                                                                                                                        |
|                                                                                                                                                                                                                                     |
| [            .Value([\"Syncfusion\"]);]                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [               ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                     |
| [                  })]                                                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| [                 [%\>]]                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                               |
|                                                                                                                                                                        |
| **[]**                                                                                                                             |
|                                                                                                                                                                        |
| [  [@]Html.Syncfusion().DigitalGauge([\"Gauge\"], gauge=\>]       |
|                                                                                                                                                                        |
| [         {]                                                                                                          |
|                                                                                                                                                                        |
| [        gauge]                                                                                                       |
|                                                                                                                                                                        |
| [            [//Setting the height and width for the digital gauge.     ]]                      |
|                                                                                                                                                                        |
| [            .Height(100)]                                                                                            |
|                                                                                                                                                                        |
| [            .Width(350)   ]                                                                                          |
|                                                                                                                                                                        |
| [            [//Setting first, second and center frame colors.]]                                |
|                                                                                                                                                                        |
| [            .FirstFrameFillColor([Brushes].LightGray)]                                       |
|                                                                                                                                                                        |
| [            .SecondFrameFillColor([Brushes].DarkGray)]                                       |
|                                                                                                                                                                        |
| [            .CenterFrameFillColor([Brushes].Gray)]                                           |
|                                                                                                                                                                        |
| [            [//Setting first and second frame thickness.]]                                     |
|                                                                                                                                                                        |
| [            .FirstFrameThickness([new] System.Windows.[Thickness](8))]  |
|                                                                                                                                                                        |
| [            .SecondFrameThickness([new] System.Windows.[Thickness](6))] |
|                                                                                                                                                                        |
| [            [//Sets the color for the bright segments.]]                                       |
|                                                                                                                                                                        |
| [            .Foreground([Brushes].Red)]                                                      |
|                                                                                                                                                                        |
| [            [//Sets color for the dimmed segments.]]                                           |
|                                                                                                                                                                        |
| [            .DimmedBrush([Brushes].DarkGray)]                                                |
|                                                                                                                                                                        |
| [            .Value([\"10000\"])]                                                             |
|                                                                                                                                                                        |
| [            [//Setting the frame type for the Digital Gauge.    ]]                             |
|                                                                                                                                                                        |
| [            .FrameType([DigitalGaugeFrameType].CroppedRectangle)]                            |
|                                                                                                                                                                        |
| [            [//Setting the space between the segments.]]                                       |
|                                                                                                                                                                        |
| [            .SegmentSpacing(0.8)]                                                                                    |
|                                                                                                                                                                        |
| [            [//setting the character type.]]                                                   |
|                                                                                                                                                                        |
| [            .CharacterType([CharacterType].SegmentFourteen)]                                 |
|                                                                                                                                                                        |
| [            .CharacterSpacing(5)]                                                                                    |
|                                                                                                                                                                        |
| [            [//Setting character height and character count.]]                                 |
|                                                                                                                                                                        |
| [            .CharacterCount(10)]                                                                                     |
|                                                                                                                                                                        |
| [            .CharacterHeight(28)]                                                                                    |
|                                                                                                                                                                        |
| [            [//Setting the segment width.]]                                                    |
|                                                                                                                                                                        |
| [            .SegmentWidth(2.5)]                                                                                      |
|                                                                                                                                                                        |
| [            [//Setting the value for the gauge.]]                                              |
|                                                                                                                                                                        |
| [            .Value([\"Syncfusion\"]);]                                                       |
|                                                                                                                                                                        |
| [               ]                                                                                                     |
|                                                                                                                                                                        |
| [                  })]                                                                                                |
|                                                                                                                                                                        |
| []                                                                                                                    |
|                                                                                                                                                                        |
| [      ]                                                                                                              |
|                                                                                                                                                                        |
| []                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Step 2:

Controller:

 

Add the below code in your controller.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [using][ System;]                                                                               |
|                                                                                                                                                                                      |
| [using][ System.Collections.Generic;]                                                           |
|                                                                                                                                                                                      |
| [using][ System.Linq;]                                                                          |
|                                                                                                                                                                                      |
| [using][ System.Web;]                                                                           |
|                                                                                                                                                                                      |
| [using][ System.Web.Mvc;]                                                                       |
|                                                                                                                                                                                      |
| [using][ Syncfusion.Mvc.Gauge;]                                                                 |
|                                                                                                                                                                                      |
| [using][ Syncfusion.Mvc.Shared;]                                                                |
|                                                                                                                                                                                      |
| [using][ System.Windows.Media;]                                                                 |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [namespace][ CircularGauge.Controllers]                                                         |
|                                                                                                                                                                                      |
| [{]                                                                                                                                              |
|                                                                                                                                                                                      |
| [    \[[HandleError]\]]                                                                                                  |
|                                                                                                                                                                                      |
| [    [public] [class] [HomeController] : [Controller]] |
|                                                                                                                                                                                      |
| [    {]                                                                                                                                          |
|                                                                                                                                                                                      |
| [        [public] [ActionResult] Index()]                                                           |
|                                                                                                                                                                                      |
| [        {]                                                                                                                                      |
|                                                                                                                                                                                      |
| [           ]                                                                                                                                    |
|                                                                                                                                                                                      |
| [            [return] View();]                                                                                              |
|                                                                                                                                                                                      |
| [        }]                                                                                                                                      |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [    }]                                                                                                                                          |
|                                                                                                                                                                                      |
| [}]                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Step 3:

Run the code. You will get the below output.

 

{border="0"}

Figure 121: Digital Gauge

[                             ]

[]{#related-topics}

