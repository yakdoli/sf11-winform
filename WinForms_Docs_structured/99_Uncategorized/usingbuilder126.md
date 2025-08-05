---
title: usingbuilder126.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder126.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The following steps explain how to display the tick mark through the builder:**

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **EnableTickMark, SliderTickPosition, TickFrequency and** **ShowLabel** methods with the desired value as an argument.

[] 

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [        .Value(20)]                                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        .Maximum(100)]                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        **.EnableTickMark([true])**]                                                                                                                             |
|                                                                                                                                                                                                                            |
| **[        .TickFrequency(20)]**                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| **[        .SliderTickPosition([TickPosition].BottomRight)]**                                                                                                  |
|                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                    |
|                                                                                                                                                                        |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                        |
| [        .Value(20)]                                                                                                               |
|                                                                                                                                                                        |
| [        .Maximum(100)]                                                                                                            |
|                                                                                                                                                                        |
| [        **.EnableTickMark([true])**]                                                                         |
|                                                                                                                                                                        |
| **[        .TickFrequency(20)]**                                                                                                   |
|                                                                                                                                                                        |
| **[        .SliderTickPosition([TickPosition].BottomRight)]**                                              |
|                                                                                                                                                                        |
| [    .Render();]                                                                                                                   |
|                                                                                                                                                                        |
| [    [}]]                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in the emulator.

*[[ [] ]]{.underline}*  

*[[ [] ]]{.underline}*  

[ {border="0"} ]

Figure 130: Slider with TickMark[]

*[[ [] ]]{.underline}*  

[]{#related-topics}

