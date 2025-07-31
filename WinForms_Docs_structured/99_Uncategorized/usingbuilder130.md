---
title: usingbuilder130.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder130.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The following steps explain how to set Syncfusion themes through the builder:**

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **AutoFormat** method with the desired theme as an argument.

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [        .Value(20)]                                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        **.AutoFormat([MobSkins].Spinach)**]                                                                                                                  |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [  ]                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                    |
|                                                                                                                                                                        |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                        |
| **[         ]** [.Value(20)]                                                                   |
|                                                                                                                                                                        |
| [        **.AutoFormat([MobSkins].Spinach)**]                                                              |
|                                                                                                                                                                        |
| [    .Render();]                                                                                                                   |
|                                                                                                                                                                        |
| [    [}]]                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in emulator.

 

[] 

[ {border="0"} ]

Figure 138: Slider with Spinach Theme[]

 

*[[ [] ]]{.underline}*  

[]{#related-topics}

