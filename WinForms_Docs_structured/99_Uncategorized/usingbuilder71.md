---
title: usingbuilder71.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder71.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following section explains how to set a default date and enable or disable manual input of the date picker using Builder.

1.  [In the **view**, invoke the date picker helper followed by the **DefaultDate** and **DisableManualInput** methods with the desired value as arguments.]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                         |
|                                                                                                                                                                                 |
| [\<%] [{=Html.MobSyncfusion().DatePicker([\"DatePicker\"])] |
|                                                                                                                                                                                 |
| [         \-\-\-\-\-\-\-\-\-\-\--]                                                                                                          |
|                                                                                                                                                                                 |
| [         .DisplayDefaultDate([true])]                                                                                 |
|                                                                                                                                                                                 |
| [         .DefaultDate([DateTime].Now)]                                                                             |
|                                                                                                                                                                                 |
| [         .DisableManualInput([true])]                                                                                 |
|                                                                                                                                                                                 |
| [         \-\-\-\-\-\-\-\-\-\-\--]                                                                                                          |
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
| [         .DisplayDefaultDate([true])]                                                                                |
|                                                                                                                                                                                |
| [         .DefaultDate([DateTime].Now)]                                                                            |
|                                                                                                                                                                                |
| [         .DisableManualInput([true])]                                                                                |
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

3.  [Build and run the application.]

[]{#related-topics}

