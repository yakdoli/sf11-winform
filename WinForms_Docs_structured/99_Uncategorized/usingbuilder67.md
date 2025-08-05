---
title: usingbuilder67.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder67.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Using Builder {#using-builder style="tab-stops: 0pt"}

[The following steps explain the addition of a date picker to an application using Builder.]

1.  [In the **view**, invoke the **DatePicker** helper with the control ID as the first argument.]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [\<%] [{=Html.MobSyncfusion().DatePicker([\"DatePicker\"])}[%\>]] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [Style Manager:]                                                                                                                                          |
|                                                                                                                                                                                                                   |
| [\<%] [{]                                                                                                             |
|                                                                                                                                                                                                                   |
| [     Html.MobSyncfusion().StyleManager()]                                                                                                                                    |
|                                                                                                                                                                                                                   |
| [          .Register(stylesheets =\>]                                                                                                                                         |
|                                                                                                                                                                                                                   |
| [                  {]                                                                                                                                                         |
|                                                                                                                                                                                                                   |
| [                      stylesheets.Add([MobComponentType].DatePicker)]                                                                                |
|                                                                                                                                                                                                                   |
| [                                 .Theme([MobSkins].DarkNight);]                                                                                      |
|                                                                                                                                                                                                                   |
| [                  }).Render();]                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [}[%\>]]                                                                                                                                          |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[Razor\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [@] [{ Html.MobSyncfusion().DatePicker([\"DatePicker\"]).Render();[}]] |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [Style Manager:]                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [\@{] []                                                                                                                   |
|                                                                                                                                                                                                                        |
| [     Html.MobSyncfusion().StyleManager()]                                                                                                                                         |
|                                                                                                                                                                                                                        |
| [          .Register(stylesheets =\>]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [                  {]                                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [                      stylesheets.Add([MobComponentType].DatePicker)]                                                                                     |
|                                                                                                                                                                                                                        |
| [                                 .Theme([MobSkins].DarkNight);]                                                                                           |
|                                                                                                                                                                                                                        |
| [                  }).Render();]                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [}]                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.  [Build and run the application. The output is shown in the following screenshot.]

[] 

{border="0"} []

Figure 176: DatePicker Input

[] 

[]{#related-topics}

