---
title: usingbuilder88.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder88.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the appearance of Header control using Builder.

1.   In **View**, invoke the Header helper with the Control ID as first argument followed by the AutoFormat method with the desired theme as the argument.

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
| []                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [        [@(]Html.MobSyncfusion().Header([\"Header\"])]                                                                                          |
|                                                                                                                                                                                                                                          |
| [        .TargetId([\"targetHeader\"]) ]                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [        .Title([\"Select an action\"]) ]                                                                                                                                    |
|                                                                                                                                                                                                                                          |
| [        .AutoFormat([MobSkins].MetroBlue)]                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [        .LeftButton(left =\> left.ShowButton([true]).Caption([\"Back\"])) ]                                                                            |
|                                                                                                                                                                                                                                          |
| [        .RightButton(right =\> right.ShowButton([true]).Caption([\"Forward\"]))[)]] [] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

**[]**  

[]{#related-topics}

