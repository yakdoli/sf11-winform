---
title: usingpropertiesmodel56.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel56.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps, explains the appearance of Footer Control using the Properties model:

1.   In the **Controller**, create an instance for the **MobFooterModel** and pass the instance through **ViewData** to **View** as given below.**

*[[ [] ]]{.underline}*  

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| **[\[Controller\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                     |
|                                                                                                                                                                                                                |
| [        [public][ActionResult] CoreFeatures()]                                                                               |
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
| [                LeftButton = [new][FooterButton]()]                                                                          |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    ShowButton = [true]]                                                                                                             |
|                                                                                                                                                                                                                |
| [                },]                                                                                                                                                       |
|                                                                                                                                                                                                                |
| [                RightButton = [new][FooterButton]()]                                                                         |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    ShowButton = [true]]                                                                                                             |
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
| []                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, invoke the dialog helper with the ViewData key as the first argument.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [                 [\<%][=]Html.MobSyncfusion().Footer([\"Footer\"])[%\>]]                                        |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| **[\[Razor\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [    ] [\@{] [Html.MobSyncfusion().Footer([\"Footer\"]).Render();[}]] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

The output is shown in the following screenshot:

[] 

{border="0"}

Figure 47: Footer Control with MetroBlue Theme

[]{#related-topics}

