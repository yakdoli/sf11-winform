---
title: usingbuilder107.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder107.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

1.   In **View**, invoke the ProgressBar helper with the control ID as an argument, followed by the **AutoFormat** method, with the desired theme as an argument.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                              |
|                                                                                                                                                                                 |
| []                                                                                                                      |
|                                                                                                                                                                                 |
| [\<%] [Html.MobSyncfusion().ProgressBar([\"progressBar\"])] |
|                                                                                                                                                                                 |
| [       .Value(30)]                                                                                                                         |
|                                                                                                                                                                                 |
| [      ** .AutoFormat([MobSkins].Spinach)**]                                                                        |
|                                                                                                                                                                                 |
| [      .Render();]                                                                                                                          |
|                                                                                                                                                                                 |
| [    [%\>]]                                                                                                     |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                        |
|                                                                                                                                                                            |
| ```                                                                                                                                           |
|                                                                                                                                                                            |
|                                                                                                                                                                            |
| ```                                                                                                                                                                        |
|                                                                                                                                                                            |
| [\@{] []                                           |
|                                                                                                                                                                            |
| [    ] [Html.MobSyncfusion().ProgressBar([\"progressBar\"])] |
|                                                                                                                                                                            |
| [       .Value(30)]                                                                                                                    |
|                                                                                                                                                                            |
| [      ** .AutoFormat([MobSkins].Spinach)**]                                                                   |
|                                                                                                                                                                            |
| [      .Render();]                                                                                                                     |
|                                                                                                                                                                            |
| [}] []                                             |
|                                                                                                                                                                            |
| []                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

 

 

{border="0"}

Figure 90: Progressbar with Spinach Theme

 

 

[]{#related-topics}

