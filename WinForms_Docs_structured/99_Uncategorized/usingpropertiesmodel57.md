---
title: usingpropertiesmodel57.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel57.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the handling of the client side events of the Footer using the Properties model.

1.   In the **Controller**, create an instance of **MobFooterModel**, define the event handler properties and pass the instance through **ViewData** to **View** as given below.**

**[]**  

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| **[\[Controller\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                     |
|                                                                                                                                                                                                                |
| [public] [ [ActionResult] CoreFeatures()]                                                         |
|                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                |
|                                                                                                                                                                                                                |
| [            [MobFooterModel] model = [new][MobFooterModel]()] [] |
|                                                                                                                                                                                                                |
| [            {]                                                                                                                                                            |
|                                                                                                                                                                                                                |
| [                TargetId = [\"targetFooter\"],]                                                                                                   |
|                                                                                                                                                                                                                |
| [                Title = [\"Select an action\"],]                                                                                                  |
|                                                                                                                                                                                                                |
| [                AutoFormat = [MobSkins].MetroBlue,]                                                                                               |
|                                                                                                                                                                                                                |
| [                ClientSideOnCreate=[\"onCreate\"],]                                                                                               |
|                                                                                                                                                                                                                |
| [                LeftButton = [new][FooterButton]()]                                                                          |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    ShowButton = [true],]                                                                                                            |
|                                                                                                                                                                                                                |
| [                    NavigateUrl=[\"http://www.google.co.in/\"],]                                                                                  |
|                                                                                                                                                                                                                |
| [                    ClientSideOnClick=[\"onLeftClick\"]]                                                                                          |
|                                                                                                                                                                                                                |
| [                },]                                                                                                                                                       |
|                                                                                                                                                                                                                |
| [                RightButton = [new][FooterButton]()]                                                                         |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    ShowButton = [true],]                                                                                                            |
|                                                                                                                                                                                                                |
| [                    NavigateUrl = [\"http://www.google.co.in/\"],]                                                                                |
|                                                                                                                                                                                                                |
| [                    ClientSideOnClick = [\"onRightClick\"]]                                                                                       |
|                                                                                                                                                                                                                |
| [                }]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [            };]                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [            ViewData\[[\"Footer\"]\] = model;]                                                                                                    |
|                                                                                                                                                                                                                |
| [            [return] View();]                                                                                                                        |
|                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]**  

2.   In **View**, invoke the Footer helper with the ViewData key as the first argument.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [                [\<%][=]Html.MobSyncfusion().Footer([\"Footer\"])[%\>]]                                         |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| **[\[Razor\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [    ] [\@{] [Html.MobSyncfusion().Footer([\"Footer\"]).Render();[}]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

**[]**  

4.   Build and run the application.

[]{#related-topics}

