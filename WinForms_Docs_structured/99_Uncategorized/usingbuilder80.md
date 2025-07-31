---
title: usingbuilder80.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder80.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The following steps will explain the addition of Footer to an application using Builder:

1.   In **View**, invoke the Footer helper with the Control ID as the first argument followed by the TargetId, Title, AutoFormat, LeftButton and RightButton methods by passing their respective argument.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                               |
|                                                                                                                                                                                  |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                  |
| [                [\<%][=]Html.MobSyncfusion().Footer([\"Footer\"])] |
|                                                                                                                                                                                  |
| [                .TargetId([\"targetFooter\"])]                                                                      |
|                                                                                                                                                                                  |
| [                .Title([\"Select an action\"])]                                                                     |
|                                                                                                                                                                                  |
| [                .AutoFormat([MobSkins].MetroBlue)]                                                                  |
|                                                                                                                                                                                  |
| [                .LeftButton(left =\> left.ShowButton([true]))]                                                         |
|                                                                                                                                                                                  |
| [                .RightButton(right =\> right.ShowButton([true]))[%\>]]                     |
|                                                                                                                                                                                  |
| []                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                  |
|                                                                                                                                                                      |
| **[]**                                                                                                                           |
|                                                                                                                                                                      |
| [                [\@{]Html.MobSyncfusion().Footer([\"Footer\"])]             |
|                                                                                                                                                                      |
| [                .TargetId([\"targetFooter\"])]                                                          |
|                                                                                                                                                                      |
| [                .Title([\"Select an action\"])]                                                         |
|                                                                                                                                                                      |
| [                .AutoFormat([MobSkins].MetroBlue)]                                                      |
|                                                                                                                                                                      |
| [                .LeftButton(left =\> left.ShowButton([true]))]                                             |
|                                                                                                                                                                      |
| [                .RightButton(right =\> right.ShowButton([true])).Render();[}]] |
|                                                                                                                                                                      |
| []                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

**[]**  

[]{#related-topics}

