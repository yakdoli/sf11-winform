---
title: usingbuilder122.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder122.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how to set the range of the slider through the builder:

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **Minimum**, **Maximum**, **Step**, and **Value** methods with the desired values as arguments.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [    **.Value(2)**]                                                                                                                                                                    |
|                                                                                                                                                                                                                            |
| **[    .Maximum(10)]**                                                                                                                                                                 |
|                                                                                                                                                                                                                            |
| **[    .Minimum(0)]**                                                                                                                                                                  |
|                                                                                                                                                                                                                            |
| **[    .Step(2)]**                                                                                                                                                                     |
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
| [    **.Value(2)**]                                                                                                                |
|                                                                                                                                                                        |
| **[    .Maximum(10)]**                                                                                                             |
|                                                                                                                                                                        |
| **[    .Minimum(0)]**                                                                                                              |
|                                                                                                                                                                        |
| **[    .Step(2)]**                                                                                                                 |
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

Figure 124: Slider with Customized Range

**[]**  

[]{#related-topics}

