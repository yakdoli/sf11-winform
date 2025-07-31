---
title: usingbuilder70.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder70.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following section explains how to set the navigation range of the date picker using Builder.

1.  [In **View**, invoke the **DatePicker** helper followed by the **MinDate** and **MaxDate** methods with the desired dates as arguments.]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                         |
|                                                                                                                                                                                 |
| [\<%] [{=Html.MobSyncfusion().DatePicker([\"DatePicker\"])] |
|                                                                                                                                                                                 |
| [        \-\-\-\-\-\-\-\-\-\-\--]                                                                                                           |
|                                                                                                                                                                                 |
| [        .MinDate([DateTime].Now.AddMonths(-5))]                                                                    |
|                                                                                                                                                                                 |
| [        .MaxDate([DateTime].Now.AddMonths(5))]                                                                     |
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
| [        .MinDate([DateTime].Now.AddMonths(-5))]                                                                   |
|                                                                                                                                                                                |
| [        .MaxDate([DateTime].Now.AddMonths(5))]                                                                    |
|                                                                                                                                                                                |
| [        \-\-\-\-\-\-\-\-\-\-\--]                                                                                                          |
|                                                                                                                                                                                |
| [        .Render();]                                                                                                                       |
|                                                                                                                                                                                |
| [}] []                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.  [Build and run the application.]

[]{#related-topics}

