---
title: usingbuilder129.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder129.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The following steps explain how to customize the slider handle through the builder:**

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the ShowThumb and ThumbStyle method with the desired value as an argument.

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [        .Value(20)]                                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        **.ShowThumb([true])**]                                                                                                                                  |
|                                                                                                                                                                                                                            |
| **[        .ThumbStyle([ThumbStyle].Diamond)]**                                                                                                                |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                    |
|                                                                                                                                                                        |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                        |
| [       .Value(20)]                                                                                                                |
|                                                                                                                                                                        |
| [        **.ShowThumb([true])**]                                                                              |
|                                                                                                                                                                        |
| **[        .ThumbStyle([ThumbStyle].Diamond)]**                                                            |
|                                                                                                                                                                        |
| [    .Render();]                                                                                                                   |
|                                                                                                                                                                        |
| [    [}]]                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in an emulator.

*[[ [] ]]{.underline}*  

[ {border="0"} ]

Figure 136: Slider with Diamond Thumb style[]

*[[ [] ]]{.underline}*  

[]{#related-topics}

