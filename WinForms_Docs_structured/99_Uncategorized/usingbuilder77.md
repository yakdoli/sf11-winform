---
title: usingbuilder77.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder77.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the addition of animations to the Dialog using Builder:

1.   In **View**, create the contents of the Dialog and invoke the Dialog Helper with the control ID as the first argument followed by the **ShowAnimation** and **HideAnimation** methods with the desired animations as arguments.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                    |
|                                                                                                                                       |
| **[]**                                                                                            |
|                                                                                                                                       |
| [            [\<%]{]                                                  |
|                                                                                                                                       |
| [                  Html.MobSyncfusion().Dialog([\"MobDialog\"])]          |
|                                                                                                                                       |
| [                    .ShowAnimation([MobAnimations].Scale)]               |
|                                                                                                                                       |
| [                    .HideAnimation([MobAnimations].Blind)]               |
|                                                                                                                                       |
| [                    .Title([\"Syncfusion Essential Studio\"])]           |
|                                                                                                                                       |
| [                    .DialogIconUrl([\"\~/Content/Images/favicon.ico\"])] |
|                                                                                                                                       |
| [                    .Template(() =\>]                                                            |
|                                                                                                                                       |
| [                      {[%\>]]                                        |
|                                                                                                                                       |
| [            [\<][div][\>]]      |
|                                                                                                                                       |
| [                This is the Syncfusion Mobile Dialog control]                                    |
|                                                                                                                                       |
| [            [\</][div][\>]]     |
|                                                                                                                                       |
| [            [\<%]})]                                                 |
|                                                                                                                                       |
| [            .Render();]                                                                          |
|                                                                                                                                       |
| [              }[%\>]]                                                |
|                                                                                                                                       |
| []                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                               |
|                                                                                                                                                                                   |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                   |
| [            [\@{]]                                                                                               |
|                                                                                                                                                                                   |
| [                Html.MobSyncfusion().Dialog([\"MobDialog\"])]                                                        |
|                                                                                                                                                                                   |
| [                    .ShowAnimation([MobAnimations].Scale)]                                                           |
|                                                                                                                                                                                   |
| [                    .HideAnimation([MobAnimations].Blind)]                                                           |
|                                                                                                                                                                                   |
| [                    .Title([\"Syncfusion Essential Studio\"])]                                                       |
|                                                                                                                                                                                   |
| [                    .DialogIconUrl([\"\~/Content/Images/favicon.ico\"])]                                             |
|                                                                                                                                                                                   |
| [                    .Template([@][\<][div][\>]] |
|                                                                                                                                                                                   |
| [                        This is the Syncfusion Mobile Dialog control]                                                                        |
|                                                                                                                                                                                   |
| [                    [\</][div][\>]]                                         |
|                                                                                                                                                                                   |
| [            ).Render();[}]]                                                                                      |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application in emulator.

**[]**  

[]{#related-topics}

