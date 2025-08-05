---
title: usingbuilder72.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder72.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following section explains how to set the **DateFormat** and **ShowOtherMonths** properties of the DatePicker control using Builder.

1.  [In the **view**, invoke the date picker helper followed by the **DateFormat()** and **ShowOtherMonths()** methods with the desired arguments.]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                         |
|                                                                                                                                                                                 |
| [\<%] [{=Html.MobSyncfusion().DatePicker([\"DatePicker\"])] |
|                                                                                                                                                                                 |
| [        \-\-\-\-\-\-\-\-\-\-\--]                                                                                                           |
|                                                                                                                                                                                 |
| [        .DateFormat([\"d MM,y\"])]                                                                                 |
|                                                                                                                                                                                 |
| [        .ShowOtherMonths([true])]                                                                                     |
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
| [        .DateFormat([\"d MM,y\"])]                                                                                |
|                                                                                                                                                                                |
| [        .ShowOtherMonths([true])]                                                                                    |
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

