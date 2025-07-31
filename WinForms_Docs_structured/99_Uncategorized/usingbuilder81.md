---
title: usingbuilder81.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder81.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps, explains about the button settings in Footer control using Builder:

1.   In **View**, invoke the Footer helper with the Control ID as the first argument followed by the TargetId, Tilt, AutoFormat, LeftButton, RightButton methods with their respective arguments.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [                [\<%][=]Html.MobSyncfusion().Footer([\"Footer\"])]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                        |
| [                .TargetId([\"targetFooter\"])]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                        |
| [                .Title([\"Select an action\"])]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                        |
| [                .AutoFormat([MobSkins].MetroBlue)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                        |
| [                .LeftButton(left =\> left.ShowButton([true]).NavigateUrl([\"http://www.google.co.in/\"]).ClientSideOnClick([\"onLeftClick\"]))]                                              |
|                                                                                                                                                                                                                                                                                                        |
| [                .RightButton(right =\> right.ShowButton([true]).NavigateUrl([\"http://www.google.co.in/\"]).ClientSideOnClick([\"onRightClick\"]))[%\>]]         |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| **[\[Razor\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [                [\@{]Html.MobSyncfusion().Footer([\"Footer\"])]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                        |
| [                .TargetId([\"targetFooter\"])]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                        |
| [                .Title([\"Select an action\"])]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                        |
| [                .AutoFormat([MobSkins].MetroBlue)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                        |
| [                .LeftButton(left =\> left.ShowButton([true]).NavigateUrl([\"http://www.google.co.in/\"]).ClientSideOnClick([\"onLeftClick\"]))]                                              |
|                                                                                                                                                                                                                                                                                                        |
| [                .RightButton(right =\> right.ShowButton([true]).NavigateUrl([\"http://www.google.co.in/\"]).ClientSideOnClick([\"onRightClick\"])).Render();[}]] |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Build and run the application.

**[]**  

[]{#related-topics}

