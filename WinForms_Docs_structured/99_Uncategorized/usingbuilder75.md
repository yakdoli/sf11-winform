---
title: usingbuilder75.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder75.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the setting of the dimensions of the dialog using Builder:

1.   In **View**, create the contents of the dialog and invoke the dialog helper with the Control ID as the first argument followed by the **Height** and **Width** methods with the desired dimensions as arguments.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                   |
|                                                                                                                                                                      |
| **[]**                                                                                                                           |
|                                                                                                                                                                      |
| [    [\<%]{]                                                                                         |
|                                                                                                                                                                      |
| [          Html.MobSyncfusion().Dialog([\"MobDialog\"])]                                                 |
|                                                                                                                                                                      |
| [              .Height(100)]                                                                                                     |
|                                                                                                                                                                      |
| [              .Width(400)]                                                                                                      |
|                                                                                                                                                                      |
| [              .Title([\"Syncfusion Essential Studio\"])]                                                |
|                                                                                                                                                                      |
| [              .DialogIconUrl([\"\~/Content/Images/favicon.ico\"])]                                      |
|                                                                                                                                                                      |
| [              .Template(() =\>]                                                                                                 |
|                                                                                                                                                                      |
| [              {[%\>][\<][div][\>]] |
|                                                                                                                                                                      |
| [                  This is the Syncfusion Mobile Dialog control]                                                                 |
|                                                                                                                                                                      |
| [              [\</][div][\>]]                                  |
|                                                                                                                                                                      |
| [    [\<%]})]                                                                                        |
|                                                                                                                                                                      |
| [            .Render();]                                                                                                         |
|                                                                                                                                                                      |
| [      }[%\>]]                                                                                       |
|                                                                                                                                                                      |
| []                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                       |
|                                                                                                                                                                           |
| **[]**                                                                                                                                |
|                                                                                                                                                                           |
| [    [\@{]]                                                                                               |
|                                                                                                                                                                           |
| [        Html.MobSyncfusion().Dialog([\"MobDialog\"])]                                                        |
|                                                                                                                                                                           |
| [            .Height(100)]                                                                                                            |
|                                                                                                                                                                           |
| [            .Width(400)]                                                                                                             |
|                                                                                                                                                                           |
| [            .Title([\"Syncfusion Essential Studio\"])]                                                       |
|                                                                                                                                                                           |
| [            .DialogIconUrl([\"\~/Content/Images/favicon.ico\"])]                                             |
|                                                                                                                                                                           |
| [            .Template([@][\<][div][\>]] |
|                                                                                                                                                                           |
| [                This is the Syncfusion Mobile Dialog control]                                                                        |
|                                                                                                                                                                           |
| [            [\</][div][\>]]                                         |
|                                                                                                                                                                           |
| [).Render();]                                                                                                                         |
|                                                                                                                                                                           |
| [    [}]] []                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in emulator.

**[]**  

[]{#related-topics}

