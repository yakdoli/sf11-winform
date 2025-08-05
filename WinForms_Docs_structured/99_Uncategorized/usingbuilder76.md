---
title: usingbuilder76.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder76.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the restriction of the end-user interaction over the dialog using Builder:

1.   In **View**, create the contents of the dialog and invoke the dialog helper with the Control IDas the first argument followed by the **Draggable,** and **Modal** methods with the desired options as arguments.

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
| [              .AllowDrag([true])]                                                                          |
|                                                                                                                                                                      |
| [              .Modal([true])]                                                                              |
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
| []                                                                                                                               |
|                                                                                                                                                                      |
| []                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                       |
|                                                                                                                                                                           |
| **[]**                                                                                                                                |
|                                                                                                                                                                           |
| [    [\@{]]                                                                                               |
|                                                                                                                                                                           |
| [        Html.MobSyncfusion().Dialog([\"MobDialog\"])]                                                        |
|                                                                                                                                                                           |
| [            .Modal([true])]                                                                                     |
|                                                                                                                                                                           |
| [            .AllowDrag([true])]                                                                                 |
|                                                                                                                                                                           |
| [            .Template([@][\<][div][\>]] |
|                                                                                                                                                                           |
| [                This is the Syncfusion Mobile Dialog control]                                                                        |
|                                                                                                                                                                           |
| [            [\</][div][\>]]                                         |
|                                                                                                                                                                           |
| [).Render();]                                                                                                                         |
|                                                                                                                                                                           |
| [    [}]] []                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application in emulator.

 

[]{#related-topics}

