---
title: usingbuilder105.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder105.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

1.   In **View**, invoke the ProgressBar helper with the control ID as an argument, followed by the **Maximum, Minimum, StepValue and Value** method, with the desired value as an argument.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                              |
|                                                                                                                                                                                 |
| [\<%] [Html.MobSyncfusion().ProgressBar([\"progressBar\"])] |
|                                                                                                                                                                                 |
| [       .Value(30)]                                                                                                                         |
|                                                                                                                                                                                 |
| [       .Width(500)]                                                                                                                        |
|                                                                                                                                                                                 |
| [       .**Maximum(100)**]                                                                                                                  |
|                                                                                                                                                                                 |
| **[       .Minimum(10)]**                                                                                                                   |
|                                                                                                                                                                                 |
| **[       .Value(20)]**                                                                                                                     |
|                                                                                                                                                                                 |
| **[       .StepValue(10)]**                                                                                                                 |
|                                                                                                                                                                                 |
| [       ]                                                                                                                                   |
|                                                                                                                                                                                 |
| [      .Render();]                                                                                                                          |
|                                                                                                                                                                                 |
| [    [%\>]]                                                                                                     |
|                                                                                                                                                                                 |
| **[]**                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ```                                                                                                                               |
|                 [Razor]                                                                                                                                        |
|                                                                                                                                                                |
| ```                                                                                                                                                            |
|                                                                                                                                                                |
| ```                                                                                                                               |
|                                                                                                                                                                |
|                                                                                                                                                                |
| ```                                                                                                                                                            |
|                                                                                                                                                                |
| [\@{] []                               |
|                                                                                                                                                                |
| [       ] [Html.MobSyncfusion().ProgressBar([\"progressBar\"])] |
|                                                                                                                                                                |
| [       .Value(30)]                                                                                           |
|                                                                                                                                                                |
| [       .Width(500)]                                                                                          |
|                                                                                                                                                                |
| [       .**Maximum(100)**]                                                                                    |
|                                                                                                                                                                |
| **[       .Minimum(10)]**                                                                                     |
|                                                                                                                                                                |
| **[       .Value(20)]**                                                                                       |
|                                                                                                                                                                |
| **[       .StepValue(10)]**                                                                                   |
|                                                                                                                                                                |
| [       ]                                                                                                     |
|                                                                                                                                                                |
| [      .Render();]                                                                                            |
|                                                                                                                                                                |
| [}] []                                 |
|                                                                                                                                                                |
| []                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Build and run the application.

 

 

{border="0"}

Figure 85: Progressbar with range set

 

 

[]{#related-topics}

