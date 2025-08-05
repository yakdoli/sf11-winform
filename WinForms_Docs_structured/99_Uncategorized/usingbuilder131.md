---
title: usingbuilder131.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder131.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The following steps explain how to handle events using Builder.**

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **ClientSideOnChange**, **ClientSideOnSlide**, **ClientSideOnStart**, **ClientSideOnStop** and **ClientSideOnLoad** methods with the desired handlers as arguments.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [        .Value(20)]                                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [                **.ClientSideOnChange([\"OnChange\"])**]                                                                                                      |
|                                                                                                                                                                                                                            |
| **[                .ClientSideOnLoad([\"OnLoad\"])]**                                                                                                          |
|                                                                                                                                                                                                                            |
| **[                .ClientSideOnSlide([\"OnSlide\"])]**                                                                                                        |
|                                                                                                                                                                                                                            |
| **[                .ClientSideOnStart([\"OnStart\"])]**                                                                                                        |
|                                                                                                                                                                                                                            |
| **[                .ClientSideOnStop([\"OnStop\"])]**                                                                                                          |
|                                                                                                                                                                                                                            |
| [        [%\>]] []                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Razor\]]**                                                                                                                   |
|                                                                                                                                                                        |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                        |
| [.Value(20)]                                                                                                                       |
|                                                                                                                                                                        |
| [                **.ClientSideOnChange([\"OnChange\"])**]                                                  |
|                                                                                                                                                                        |
| **[                .ClientSideOnLoad([\"OnLoad\"])]**                                                      |
|                                                                                                                                                                        |
| **[                .ClientSideOnSlide([\"OnSlide\"])]**                                                    |
|                                                                                                                                                                        |
| **[                .ClientSideOnStart([\"OnStart\"])]**                                                    |
|                                                                                                                                                                        |
| **[                .ClientSideOnStop([\"OnStop\"])]**                                                      |
|                                                                                                                                                                        |
| [    .Render();]                                                                                                                   |
|                                                                                                                                                                        |
| [    [}]]                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In JavaScript, define the handlers.

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| [        [function] OnChange(event, data) {]                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [//data:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  value   - current value of the slider]]                                                                                                            |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnSlide(event, data) {]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [//data:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  value   - current value of the slider]]                                                                                                            |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnStart(event, data) {]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [//data:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//  value   - current value of the slider]]                                                                                                            |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] OnStop(event, data) {]                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [//event     - object sent by jQuery event trigger]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [//data:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [                        [//  value   - current value of the slider]]                                                                                                |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [      [\</][script][\>]]                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application in emulator.

**[]**  

[]{#related-topics}

