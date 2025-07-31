---
title: usingpropertiesmodel59.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel59.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps, explains about the Button settings in Header control using the *Properties* model:

1.   In the **Controller**, create an instance of **MobHeaderModel**, define the LeftButton propertiesandRightButton properties and pass the instance through **ViewData** to **View** as given below:**

*[[ [] ]]{.underline}*  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                |
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
| [                ClientSideOnCreate = [\"onCreate\"],]                                                      |
|                                                                                                                                                                         |
| [                LeftButton = [new][LeftButton]()]                                     |
|                                                                                                                                                                         |
| [                {]                                                                                                                 |
|                                                                                                                                                                         |
| [                    Caption = [\"Back\"],]                                                                 |
|                                                                                                                                                                         |
| [                    ShowButton = [true],]                                                                     |
|                                                                                                                                                                         |
| [                    ClientSideOnClick = [\"onLeftClick\"]]                                                 |
|                                                                                                                                                                         |
| [                },]                                                                                                                |
|                                                                                                                                                                         |
| [                RightButton = [new][RightButton]()]                                   |
|                                                                                                                                                                         |
| [                {]                                                                                                                 |
|                                                                                                                                                                         |
| [                    Caption = [\"Forward\"],]                                                              |
|                                                                                                                                                                         |
| [                    ShowButton = [true],]                                                                     |
|                                                                                                                                                                         |
| [                    ClientSideOnClick = [\"onRightClick\"]]                                                |
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
| **[]**                                                                                                                              |
|                                                                                                                                                                         |
| [            ]                                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, invoke the Header helper with the **ViewData** key as the first argument.

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

 

The output is displayed in the following screenshot:

[] 

{border="0"}

Figure 50: Header Control with Buttons

 

[]{#related-topics}

