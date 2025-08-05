---
title: usingpropertiesmodel62.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel62.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the handling of the client side events of the Header using the Properties model.

1.   In the **Controller**, create an instance of MobHeader**Model**, define the event handler properties and pass the instance through **ViewData** to **View** as given below.**

**[]**  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                          |
|                                                                                                                                                                         |
| **[\[Controller\]]**                                                                                                                |
|                                                                                                                                                                         |
| **[]**                                                                                                                              |
|                                                                                                                                                                         |
| [public] [ [ActionResult] CoreFeatures()]                  |
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
| [                ClientSideOnCreate=[\"onCreate\"],]                                                        |
|                                                                                                                                                                         |
| [                LeftButton = [new][LeftButton]()]                                     |
|                                                                                                                                                                         |
| [                {]                                                                                                                 |
|                                                                                                                                                                         |
| [                    Caption = [\"Back\"],]                                                                 |
|                                                                                                                                                                         |
| [                    ShowButton = [true],]                                                                     |
|                                                                                                                                                                         |
| [                    ClientSideOnClick=[\"onLeftClick\"]]                                                   |
|                                                                                                                                                                         |
| [                },]                                                                                                                |
|                                                                                                                                                                         |
| [                RightButton = [new][RightButton]()]                                   |
|                                                                                                                                                                         |
| [                {]                                                                                                                 |
|                                                                                                                                                                         |
| [                    Caption = [\"Forward\"],]                                                              |
|                                                                                                                                                                         |
| [                    ShowButton = [true],]                                                                     |
|                                                                                                                                                                         |
| [                    ClientSideOnClick=[\"onRightClick\"]]                                                  |
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
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

2.   In **View**, invoke the Header helper with the ViewData key as the first argument.

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

3.   In Javascript, define the handlers as given below:

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
| [            [\</][script][\>][]]                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

**[]**  

[]{#related-topics}

