---
title: usingbuilder89.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder89.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps, explains the handling of client side events of the Header using Builder.

1.   In the **View,** invoke the Header helper with the Control ID as the first argument followed by the event handler methods with the desired hanlders as argument.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [                 [\<%][=]Html.MobSyncfusion().Header([\"Header\"])]                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [                .TargetId([\"targetHeader\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [                .Title([\"Select an action\"])]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [                .AutoFormat([MobSkins].MetroBlue)]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [                .ClientSideOnCreate([\"onCreate\"])]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [                .LeftButton(left =\> left.ShowButton([true]).Caption([\"Back\"]).ClientSideOnClick([\"onLeftClick\"]))]                                          |
|                                                                                                                                                                                                                                                                            |
| [                .RightButton(right =\> right.ShowButton([true]).Caption([\"Forward\"]).ClientSideOnClick([\"onRightClick\"])) [%\>]] |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [        [@(]Html.MobSyncfusion().Header([\"Header\"])]                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [        .TargetId([\"targetHeader\"]) ]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [        .Title([\"Select an action\"]) ]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                 |
| [        .AutoFormat([MobSkins].MetroBlue)]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [        .ClientSideOnCreate([\"onCreate\"])]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [        .LeftButton(left =\> left.ShowButton([true]).Caption([\"Back\"]).ClientSideOnClick([\"onLeftClick\"])) ]                                      |
|                                                                                                                                                                                                                                                                 |
| [        .RightButton(right =\> right.ShowButton([true]).Caption([\"Forward\"]).ClientSideOnClick([\"onRightClick\"]))[)]] |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Using **Javascript**, define the handlers as given below:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [        [function] onCreate(event) {]                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [//event             - object send by jQuery event trigger.]]                                                                                           |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] onLeftClick(event, ui) {]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            [//event             - object send by jQuery event trigger.]]                                                                                           |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] onRightClick(event, ui) {]                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            [//event             - object send by jQuery event trigger.]]                                                                                           |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [\</][script][\>]]                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.

**[]**  

[]{#related-topics}

