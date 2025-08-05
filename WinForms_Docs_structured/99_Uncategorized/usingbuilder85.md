---
title: usingbuilder85.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder85.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

 

The following steps will explain the addition of a Header to an application using Builder:

1.   In **View**, invoke the Header helper with the Control ID as the first argument followed by the TargetId, Title, AutoFormat, LeftButton and RightButton methods by passing their respective argument.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                          |
|                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                  |
|                                                                                                                                                                                                             |
| [                [\<%][=]Html.MobSyncfusion().Header([\"Header\"])]                            |
|                                                                                                                                                                                                             |
| [                .TargetId([\"targetHeader\"])]                                                                                                 |
|                                                                                                                                                                                                             |
| [                .Title([\"Select an action\"])]                                                                                                |
|                                                                                                                                                                                                             |
| [                .AutoFormat([MobSkins].MetroBlue)]                                                                                             |
|                                                                                                                                                                                                             |
| [                .LeftButton(left =\> left.ShowButton([true]).Caption([\"Back\"]))]                                        |
|                                                                                                                                                                                                             |
| [                .RightButton(right =\> right.ShowButton([true]).Caption([\"Forward\"]))[%\>]] |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| []                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                               |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                                        |
|                                                                                                                                                                                                   |
| [        [@(]Html.MobSyncfusion().Header([\"Header\"])]                                                   |
|                                                                                                                                                                                                   |
| [        .TargetId([\"targetHeader\"]) ]                                                                                              |
|                                                                                                                                                                                                   |
| [        .Title([\"Select an action\"]) ]                                                                                             |
|                                                                                                                                                                                                   |
| [        .AutoFormat([MobSkins].MetroBlue)]                                                                                           |
|                                                                                                                                                                                                   |
| [        .LeftButton(left =\> left.ShowButton([true]).Caption([\"Back\"])) ]                                     |
|                                                                                                                                                                                                   |
| [        .RightButton(right =\> right.ShowButton([true]).Caption([\"Forward\"]))[)]] |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

2.   Build and run the application.

**[]**  

[]{#related-topics}

