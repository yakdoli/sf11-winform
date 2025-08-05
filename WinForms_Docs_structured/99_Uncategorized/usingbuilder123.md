---
title: usingbuilder123.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder123.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how to set slider orientation using Builder:**

1.   In **View**, invoke the slider helper with the control ID as an argument, followed by the **Orientation** method with the desired orientation as an argument.

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [    .Value(20)]                                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [    .Height(400)]                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    .Width(10)]                                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [    **.Orientation([SliderOrientation].Vertical)**]                                                                                                           |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                    |
|                                                                                                                                                                        |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                        |
| [    .Value(20)]                                                                                                                   |
|                                                                                                                                                                        |
| [    .Height(400)]                                                                                                                 |
|                                                                                                                                                                        |
| [    .Width(10)]                                                                                                                   |
|                                                                                                                                                                        |
| [    **.Orientation([SliderOrientation].Vertical)**]                                                       |
|                                                                                                                                                                        |
| [    .Render();]                                                                                                                   |
|                                                                                                                                                                        |
| [    [}]]                                                                                              |
|                                                                                                                                                                        |
| []                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


Note: For vertical orientation, you need to register the stylesheet for the SliderVertical Component as in the below code snippets.


 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                          |
|                                                                                                                                             |
| [\<%] [{]                                       |
|                                                                                                                                             |
| [          Html.MobSyncfusion().StyleManager()]                                                         |
|                                                                                                                                             |
| [          .Register(stylesheets =\>]                                                                   |
|                                                                                                                                             |
| [                  {]                                                                                   |
|                                                                                                                                             |
| [                      **stylesheets.Add([MobComponentType].SliderVertical);**] |
|                                                                                                                                             |
| [                  }).Render();]                                                                        |
|                                                                                                                                             |
| [      }[%\>]]                                                              |
|                                                                                                                                             |
| []                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                         |
|                                                                                                                                             |
| [\@{] [ Html.MobSyncfusion().StyleManager()]    |
|                                                                                                                                             |
| [          .Register(stylesheets =\>]                                                                   |
|                                                                                                                                             |
| [                  {]                                                                                   |
|                                                                                                                                             |
| [                      **stylesheets.Add([MobComponentType].SliderVertical);**] |
|                                                                                                                                             |
| [                  }).Render();]                                                                        |
|                                                                                                                                             |
| [    [}]]                                                                   |
|                                                                                                                                             |
| []                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

2.   Build and run the application in the emulator.

 

[ {border="0"} ]

Figure 125: Vertical Slider[]

 

[]{#related-topics}

