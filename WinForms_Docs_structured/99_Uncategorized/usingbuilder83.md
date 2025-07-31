---
title: usingbuilder83.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder83.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps will explain the appearance of Footer control using Builder.

1.   In **View**, invoke the Footer helper with the Control ID as first argument followed by the AutoFormat method with the desired theme as the argument.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                               |
|                                                                                                                                                                                                                          |
| [                [\<%][=]Html.MobSyncfusion().Footer([\"Footer\"])]                                         |
|                                                                                                                                                                                                                          |
| [                .TargetId([\"targetFooter\"])]                                                                                                              |
|                                                                                                                                                                                                                          |
| [                .Title([\"Select an action\"])]                                                                                                             |
|                                                                                                                                                                                                                          |
| [                .AutoFormat([MobSkins].MetroBlue)]                                                                                                          |
|                                                                                                                                                                                                                          |
| [                .LeftButton(left =\> left.ShowButton([true]))]                                                                                                 |
|                                                                                                                                                                                                                          |
| [                .RightButton(right =\> right.ShowButton([true]))[%\>]]                                                             |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| **[\[Razor\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                               |
|                                                                                                                                                                                                                          |
| [                [\@{]Html.MobSyncfusion().Footer([\"Footer\"])]                                                                 |
|                                                                                                                                                                                                                          |
| [                .TargetId([\"targetFooter\"])]                                                                                                              |
|                                                                                                                                                                                                                          |
| [                .Title([\"Select an action\"])]                                                                                                             |
|                                                                                                                                                                                                                          |
| [                .AutoFormat([MobSkins].MetroBlue)]                                                                                                          |
|                                                                                                                                                                                                                          |
| [                .LeftButton(left =\> left.ShowButton([true]))]                                                                                                 |
|                                                                                                                                                                                                                          |
| [         .RightButton(right =\> right.ShowButton([true])).Render();[}]] [] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

2.   Build and run the application.

**[]**  

[]{#related-topics}

