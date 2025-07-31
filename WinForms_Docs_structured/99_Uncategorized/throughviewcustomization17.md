---
title: throughviewcustomization17.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughviewcustomization17.md
created_at: 2025-07-03
---






##### Through View Customization {#through-view-customization style="tab-stops: 0pt"}

[] 

Step 1:

View:

Add the below code in your aspx file. The character count and character height can be set using its **CharacterCount** and **CharacterHeight properties.** The character type can be set using its **CharacterType property**. The space between the characters can be set using its **CharacterSpacing** property**.**

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[ASPX\]]                                                                                                                                                                                                                         |
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
| [            .FrameType([DigitalGaugeFrameType].CroppedRectangle)]                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [            .SegmentSpacing(0.5)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [            [//Sets the character type.]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| **[            .CharacterType([CharacterType].SegmentSeven)]**                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| **[            [//Sets the space between each characters.]]**                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| **[            .CharacterSpacing(15)]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| **[            [//Sets the character count value.]]**                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| **[            .CharacterCount(5)]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| **[            [//Sets the character height.]]**                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| **[            .CharacterHeight(35)]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [            .SegmentWidth(4)]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [            .Value([\"10:30\"]);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [               ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [                  })]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [                 [%\>]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [View\[cshtml\]]                                                                                                                                                    |
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
| [            .FrameType([DigitalGaugeFrameType].CroppedRectangle)]                                                             |
|                                                                                                                                                                                                         |
| [            .SegmentSpacing(0.5)]                                                                                                                     |
|                                                                                                                                                                                                         |
| [            [//Sets the character type.]]                                                                                       |
|                                                                                                                                                                                                         |
| [            .CharacterType([CharacterType].SegmentSeven)]                                                                     |
|                                                                                                                                                                                                         |
| [            [//Sets the space between each characters.]]                                                                        |
|                                                                                                                                                                                                         |
| [            .CharacterSpacing(15)]                                                                                                                    |
|                                                                                                                                                                                                         |
| [            [//Sets the character count value.]]                                                                                |
|                                                                                                                                                                                                         |
| [            .CharacterCount(5)]                                                                                                                       |
|                                                                                                                                                                                                         |
| [            [//Sets the character height.]]                                                                                     |
|                                                                                                                                                                                                         |
| [            .CharacterHeight(35)]                                                                                                                     |
|                                                                                                                                                                                                         |
| [            .SegmentWidth(4)]                                                                                                                         |
|                                                                                                                                                                                                         |
| [            .Value([\"10:30\"]);               ]                                                                              |
|                                                                                                                                                                                                         |
| [                  })]                                                                                                                                 |
|                                                                                                                                                                                                         |
| []                                                                                                                                                     |
|                                                                                                                                                                                                         |
| []                                                                                                                                                     |
|                                                                                                                                                                                                         |
| []                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

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
| [           ]                                                                          |
|                                                                                                                            |
| [            [return] View();]                                    |
|                                                                                                                            |
| [        }]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------+

**[]** 

Step 3:

Run the code. You will get the below output.

 

{border="0"}

Figure 135: Digital Gauge-Character Customization**[]**

[                                       ]

[]{#related-topics}

