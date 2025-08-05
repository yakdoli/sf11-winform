---
title: usingbuilder128.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder128.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how to display the tooltip for the slider through the builder:

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **ShowToolTip** method with the desired value as an argument.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [        .Value(20)]                                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [        **.ShowToolTip([true])**]                                                                                                                                |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Razor\]]**                                                                                                                   |
|                                                                                                                                                                        |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                        |
| [    .Value(20)]                                                                                                                   |
|                                                                                                                                                                        |
| [    **.ShowToolTip([true])**]                                                                                |
|                                                                                                                                                                        |
| [    .Render();]                                                                                                                   |
|                                                                                                                                                                        |
| [    [}]]                                                                                              |
|                                                                                                                                                                        |
| []                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in emulator.

**[]**  

[ {border="0"} ] []

Figure 134: Slider with tooltip[]

**[]**  

[]{#related-topics}

