---
title: usingbuilder121.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder121.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how to set the dimensions of the slider through the builder:

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **Height** and **Width** methods with the desired values as arguments.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [    .Value(20)]                                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [    **.Height(100)**]                                                                                                                                                                 |
|                                                                                                                                                                                                                            |
| **[    .Width(400)]**                                                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Razor\]]**                                                                                                                   |
|                                                                                                                                                                        |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                        |
| [    .Value(20)]                                                                                                                   |
|                                                                                                                                                                        |
| [    **.Height(100)**]                                                                                                             |
|                                                                                                                                                                        |
| **[    .Width(400)]**                                                                                                              |
|                                                                                                                                                                        |
| [    .Render();]                                                                                                                   |
|                                                                                                                                                                        |
| [    [}]]                                                                                              |
|                                                                                                                                                                        |
| []                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in the emulator.

**[]**  

[ {border="0"} ]

Figure 122: Slider[]

**[]**  

[]{#related-topics}

