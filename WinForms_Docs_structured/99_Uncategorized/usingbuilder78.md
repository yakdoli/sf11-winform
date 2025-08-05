---
title: usingbuilder78.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder78.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the setting of the Syncfusion themes to Dialog using Builder:

1.   In **View**, create the contents of the dialog and invoke the dialog helper with the Control ID as first argument followed by the **AutoFormat** method with the desired theme as the argument.

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
| [                    .AutoFormat([MobSkins].DarkNight)]                   |
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
| []                                                                            |
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
| [                    .AutoFormat([MobSkins].DarkNight)]                                                               |
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

