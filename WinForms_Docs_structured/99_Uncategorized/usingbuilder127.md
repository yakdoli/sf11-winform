---
title: usingbuilder127.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder127.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The following steps explain how to enable or disable the slider control through the builder:**

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the Enable method with the desired value as an argument.

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [        .Value(20)]                                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        **.Enable([false])**]                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Razor\]]**                                                                                                                   |
|                                                                                                                                                                        |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                        |
| [.Value(20)]                                                                                                                       |
|                                                                                                                                                                        |
| [        **.Enable([false])**]                                                                                |
|                                                                                                                                                                        |
| [    .Render();]                                                                                                                   |
|                                                                                                                                                                        |
| [    [}]]                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in emulator.

 

[] 

[ {border="0"} ]

Figure 132: Disabled Slider[]

 

*[[ [] ]]{.underline}*  

[]{#related-topics}

