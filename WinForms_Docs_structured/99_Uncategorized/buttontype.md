---
title: buttontype.md
original_path: WinForms_Docs/99_Uncategorized/buttontype.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Button Type {#button-type style="tab-stops: 0pt"}

The user can decide the button type of the button control while rendering the control via the **ButtonType** property.[]

 

+-------------+------------------------------------------------------+------------------+-----------------------------+-------------+
| Name        | Description                                          | Type of Property | Value it Accepts            | Dependency  |
+-------------+------------------------------------------------------+------------------+-----------------------------+-------------+
| ButtonType  | Button---Create an input-type button of type Button. | Enum             | []  | \-          |
|             |                                                      |                  |                             |             |
|             | Reset---Create an input-type button of type Reset.   |                  | []  |             |
|             |                                                      |                  |                             |             |
|             | Submit---Create an input-type button of type Submit. |                  | MobButtonType.Button        |             |
|             |                                                      |                  |                             |             |
|             |                                                      |                  |                             |             |
|             |                                                      |                  |                             |             |
|             |                                                      |                  | MobButtonType.Reset         |             |
|             |                                                      |                  |                             |             |
|             |                                                      |                  |                             |             |
|             |                                                      |                  |                             |             |
|             |                                                      |                  | MobButtonType.Submit        |             |
|             |                                                      |                  |                             |             |
|             |                                                      |                  |                             |             |
|             |                                                      |                  |                             |             |
|             |                                                      |                  |                             |             |
+-------------+------------------------------------------------------+------------------+-----------------------------+-------------+

 

Using Builder

The following steps explain how to set the button type settings in the Form Button control using Builder.

 

1.   In the **view**, invoke the **Button** helper with the control ID as the first argument followed by the **ButtonType** methods with their respective text as desired by the user.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    ] [\<] [h3] [\>] [Normal Button [\</][h3][\>]]                   |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<%][=] Html.MobSyncfusion().Button([\"button\"]).ButtonType([MobButtonType].Button).Text([\"Normal\"]).AutoFormat([MobSkins].Spinach)[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<][h3][\>]Reset Button[\</][h3][\>]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<%][=] Html.MobSyncfusion().Button([\"reset\"]).ButtonType([MobButtonType].Reset).Text([\"Reset\"]).AutoFormat([MobSkins].Spinach)[%\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<][h3][\>]Submit Button[\</][h3][\>]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<%][=] Html.MobSyncfusion().Button([\"submit\"]).ButtonType([MobButtonType].Submit).Text([\"Submit\"]).AutoFormat([MobSkins].Spinach)[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                     |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    ] [\<] [h3] [\>] [Normal Button [\</][h3][\>]]      |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\@{] Html.MobSyncfusion().Button([\"button\"]).ButtonType([MobButtonType].Button).Text([\"Normal\"]).AutoFormat([MobSkins].Spinach).Render(); [}]]                |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<][h3][\>]Reset Button[\</][h3][\>]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\@{] Html.MobSyncfusion().Button([\"reset\"]).ButtonType([MobButtonType].Reset).Text([\"Reset\"]).AutoFormat([MobSkins].Spinach).Render(); [}]]                   |
|                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<][h3][\>]Submit Button[\</][h3][\>]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\@{] Html.MobSyncfusion().Button([\"submit\"]).ButtonType([MobButtonType].Submit).Text([\"Submit\"]).AutoFormat([MobSkins].Spinach).Render(); [}]]                |
|                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

 

Using Properties Model

The following steps explain how to set the button type settings in the Form Button control using the properties model:

 

1.   In the **Controller**, create an instance of **MobButtonModel**, define the **ButtonType** property, and pass the instance through **ViewData** to the **view** as given below:**

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [       [public][ActionResult] Button()]                                                                                                    |
|                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                              |
|                                                                                                                                                                                                                              |
| [            [MobButtonModel] model1 = [new][MobButtonModel]()]                                                     |
|                                                                                                                                                                                                                              |
|                        [{]                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| [                ] [Text=[\"Normal\"],]                                                                                      |
|                                                                                                                                                                                                                              |
| [                ButtonType=] [ MobButtonType] [.Button,] [] |
|                                                                                                                                                                                                                              |
| [                AutoFormat=[MobSkins].Spinach]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [             MobButtonModel] [ model2 = [new][MobButtonModel]()]                       |
|                                                                                                                                                                                                                              |
|                        [{]                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| [                ] [Text=[\"Reset\"],]                                                                                       |
|                                                                                                                                                                                                                              |
| [                ButtonType=] [ MobButtonType] [.Reset],[]   |
|                                                                                                                                                                                                                              |
| [                AutoFormat=[MobSkins].Spinach]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [            MobButtonModel] [ model3 = [new][MobButtonModel]()]                        |
|                                                                                                                                                                                                                              |
|                        [{]                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| [                ] [Text=[\"Submit\"],]                                                                                      |
|                                                                                                                                                                                                                              |
| [                ButtonType=] [ MobButtonType] [.Submit],[]  |
|                                                                                                                                                                                                                              |
| [                AutoFormat=[MobSkins].Spinach]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [            ViewData\[[\"button\"]\] = model1;]                                                                                                                 |
|                                                                                                                                                                                                                              |
| [            ViewData\[[\"reset\"]\] = model2;]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [            ViewData\[[\"submit\"]\] = model3;]                                                                                                                 |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                      |
|                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In the **view**, invoke the **Button** helper with the **ViewData** key as the first argument.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                              |
| [       [\<%][=]Html.MobSyncfusion().Button] [([\"button\"]] [)[%\>]]                                                       |
|                                                                                                                                                                                                                                                                                                                                              |
| [       [\<%][=]Html.MobSyncfusion().Button] [([\"reset\"]] [)[%\>]]                                                        |
|                                                                                                                                                                                                                                                                                                                                              |
| **[ ]** [      [\<%][=]Html.MobSyncfusion().Button] [([\"submit\"]] [)[%\>]]            |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                              |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                              |
| [       ] [\@{] [ Html.MobSyncfusion().Button] [([\"button\"]] [).Render(); [}]] |
|                                                                                                                                                                                                                                                                                                                                              |
| [       [\@{] Html.MobSyncfusion().Button] [([\"reset\"]] [).Render(); [}]]                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [       [\@{] Html.MobSyncfusion().Button] [([\"submit\"]] [).Render(); [}]]                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

The output is shown in the following screenshot.

{border="0"}

Figure 212: Button---ButtonType Properties

[]{#related-topics}

