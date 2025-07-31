---
title: usingpropertiesmodel54.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel54.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps, explains about the button settings in Footer control using the Properties model:

1.   In the **Controller**, create an instance of **MobFooterModel**, define the LeftButton propertiesandRightButton properties and pass the instance through **ViewData** to **View** as given below:**

*[[ [] ]]{.underline}*  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                |
|                                                                                                                                                                         |
| [        [public][ActionResult] CoreFeatures()]                                        |
|                                                                                                                                                                         |
| [        {]                                                                                                                         |
|                                                                                                                                                                         |
| [            [MobFooterModel] model = [new][MobFooterModel]()] |
|                                                                                                                                                                         |
| [            {]                                                                                                                     |
|                                                                                                                                                                         |
| [                TargetId = [\"targetFooter\"],]                                                            |
|                                                                                                                                                                         |
| [                Title = [\"Select an action\"],]                                                           |
|                                                                                                                                                                         |
| [                AutoFormat = [MobSkins].MetroBlue,]                                                        |
|                                                                                                                                                                         |
| [                LeftButton = [new][FooterButton]()]                                   |
|                                                                                                                                                                         |
| [                {]                                                                                                                 |
|                                                                                                                                                                         |
| [                    ShowButton = [true],]                                                                     |
|                                                                                                                                                                         |
| [                    NavigateUrl=[\"http://www.google.co.in/\"],]                                           |
|                                                                                                                                                                         |
| [                    ClientSideOnClick=[\"onLeftClick\"]]                                                   |
|                                                                                                                                                                         |
| [                },]                                                                                                                |
|                                                                                                                                                                         |
| [                RightButton = [new][FooterButton]()]                                  |
|                                                                                                                                                                         |
| [                {]                                                                                                                 |
|                                                                                                                                                                         |
| [                    ShowButton = [true],]                                                                     |
|                                                                                                                                                                         |
| [                    NavigateUrl = [\"http://www.google.co.in/\"],]                                         |
|                                                                                                                                                                         |
| [                    ClientSideOnClick = [\"onRightClick\"]]                                                |
|                                                                                                                                                                         |
| [                }]                                                                                                                 |
|                                                                                                                                                                         |
| [            };]                                                                                                                    |
|                                                                                                                                                                         |
| [            ViewData\[[\"Footer\"]\] = model;]                                                             |
|                                                                                                                                                                         |
| [            [return] View();]                                                                                 |
|                                                                                                                                                                         |
| [        }]                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, invoke the Footer helper with the **ViewData** key as the first argument.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [                [\<%][=]Html.MobSyncfusion().Footer([\"Footer\"])[%\>]] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| **[\[Razor\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [\@{] [Html.MobSyncfusion().Footer([\"Footer\"]).Render();[}]]    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

The output is displayed in the following screenshot:

[] 

{border="0"}

Figure 45: Footer Control with Buttons

 

[]{#related-topics}

