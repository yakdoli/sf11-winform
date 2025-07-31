---
title: usingbuilder125.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder125.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The following steps explain how to animate slider handle through the builder:**

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **Animate** method with the desired value as an argument.

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [         .Value(20)]                                                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [         **.Animate([true])**]                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                    |
|                                                                                                                                                                        |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                        |
| [         .Value(20)]                                                                                                              |
|                                                                                                                                                                        |
| [         **.Animate([true])**]                                                                               |
|                                                                                                                                                                        |
| [    .Render();]                                                                                                                   |
|                                                                                                                                                                        |
| [    [}]]                                                                                              |
|                                                                                                                                                                        |
| []                                                                                                             |
|                                                                                                                                                                        |
| []                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in the emulator.

*[[ [] ]]{.underline}*  

 

{border="0"}

Figure 128:Slider

*[[ [] ]]{.underline}*  

[]{#related-topics}

