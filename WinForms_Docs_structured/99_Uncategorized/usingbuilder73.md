---
title: usingbuilder73.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder73.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following section explains how to set the **CalStartDay** and **StepMonths** of the date picker using Builder.

1.  [In the **view**, invoke the **DatePicker** helper followed by the **CalStartDay** and **StepMonths** methods with the desired value as arguments.]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                         |
|                                                                                                                                                                                 |
| [\<%] [{=Html.MobSyncfusion().DatePicker([\"DatePicker\"])] |
|                                                                                                                                                                                 |
| [        \-\-\-\-\-\-\-\-\-\-\--]                                                                                                           |
|                                                                                                                                                                                 |
| [        .CalStartDay(0)]                                                                                                                   |
|                                                                                                                                                                                 |
| [        .StepMonths(2)]                                                                                                                    |
|                                                                                                                                                                                 |
| [        \-\-\-\-\-\-\-\-\-\-\--]                                                                                                           |
|                                                                                                                                                                                 |
| [}[%\>]]                                                                                                        |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[Razor\]]**                                                                                                                       |
|                                                                                                                                                                                |
| [\@{] [ Html.MobSyncfusion().DatePicker([\"DatePicker\"])] |
|                                                                                                                                                                                |
| [        \-\-\-\-\-\-\-\-\-\-\--]                                                                                                          |
|                                                                                                                                                                                |
| [        .CalStartDay(0)]                                                                                                                  |
|                                                                                                                                                                                |
| [        .StepMonths(2)]                                                                                                                   |
|                                                                                                                                                                                |
| [        \-\-\-\-\-\-\-\-\-\-\--]                                                                                                          |
|                                                                                                                                                                                |
| [        .Render();]                                                                                                                       |
|                                                                                                                                                                                |
| [}] []                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.  [Build and run the application.]

[]{#related-topics}

