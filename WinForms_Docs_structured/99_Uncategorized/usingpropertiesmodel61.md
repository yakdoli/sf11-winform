---
title: usingpropertiesmodel61.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel61.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps, explains the appearance of Header Control using the Properties model:

1.   In the **Controller**, create an instance for the **MobHeaderModel** and pass the instance through **ViewData** to **View** as given below.**

*[[ [] ]]{.underline}*  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                          |
|                                                                                                                                                                         |
| **[\[Controller\]]**                                                                                                                |
|                                                                                                                                                                         |
| **[]**                                                                                                                              |
|                                                                                                                                                                         |
| [        [public][ActionResult] CoreFeatures()]                                        |
|                                                                                                                                                                         |
| [        {]                                                                                                                         |
|                                                                                                                                                                         |
| [            [MobHeaderModel] model = [new][MobHeaderModel]()] |
|                                                                                                                                                                         |
| [            {]                                                                                                                     |
|                                                                                                                                                                         |
| [                TargetId = [\"targetHeader\"],]                                                            |
|                                                                                                                                                                         |
| [                Title = [\"Select an action\"],]                                                           |
|                                                                                                                                                                         |
| [                AutoFormat = [MobSkins].MetroBlue,]                                                        |
|                                                                                                                                                                         |
| [                LeftButton = [new][LeftButton]()]                                     |
|                                                                                                                                                                         |
| [                {]                                                                                                                 |
|                                                                                                                                                                         |
| [                    Caption=[\"Back\"],]                                                                   |
|                                                                                                                                                                         |
| [                    ShowButton=[true]]                                                                        |
|                                                                                                                                                                         |
| [                },]                                                                                                                |
|                                                                                                                                                                         |
| [                RightButton = [new][RightButton]()]                                   |
|                                                                                                                                                                         |
| [                {]                                                                                                                 |
|                                                                                                                                                                         |
| [                    Caption = [\"Forward\"],]                                                              |
|                                                                                                                                                                         |
| [                    ShowButton = [true]]                                                                      |
|                                                                                                                                                                         |
| [                }]                                                                                                                 |
|                                                                                                                                                                         |
| [            };]                                                                                                                    |
|                                                                                                                                                                         |
| [            ViewData\[[\"Header\"]\] = model;]                                                             |
|                                                                                                                                                                         |
| [            [return] View();]                                                                                 |
|                                                                                                                                                                         |
| [        }]                                                                                                                         |
|                                                                                                                                                                         |
| []                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, invoke the dialog helper with the ViewData key as the first argument.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [                [\<%][=]Html.MobSyncfusion().Header([\"Header\"])[%\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                   |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                                                            |
|                                                                                                                                                                                                       |
| [    [@]Html.MobSyncfusion().Header([\"Header\"])] [] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

The output is shown in the following screenshot:[]

oB{border="0"}

Figure 52: Header Control with MetroBlue Theme

[]{#related-topics}

