---
title: usingpropertiesmodel58.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel58.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

 

The following steps will explain the addition of a Header to an application using the Properties model:

1.   Create an instance for the **MobHeaderModel** in the Controller, define the properties and pass the created instance through the **ViewData** to **View** as given below:**

*[[ [] ]]{.underline}*  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
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
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, invoke the Header helper with the **ViewData** key as first argument.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [                [\<%][=]Html.MobSyncfusion().Header([\"Header\"])[%\>]] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                       |
|                                                                                                                                                                           |
| **[]**                                                                                                                                |
|                                                                                                                                                                           |
| [    [@]Html.MobSyncfusion().Header([\"Header\"])] [] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

The output is shown in the following screenshot:

 

{border="0"}

Figure 49: Header using Properties Model

[] 

[]{#related-topics}

