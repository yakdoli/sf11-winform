---
title: appearance106.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearance106.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Appearance {#appearance style="tab-stops: 0pt"}

The Form Button control supports built-in themes that provide great visual appeal that are suitable for various layouts. It supports the following four in-built Syncfusion themes to enhance the look and feel:

[·      ] [BlueLight]

[·      ] [DarkNight]

[·      ] [MetroBlue]

[·      ] [Spinach]

Properties

+---------------------------------------------------------------------------+------------------------------------------------------------+----------------------------------+----------------------------------+-----------------------------------+
| Name                                                                      | Description                                                | Type of the Property             | Value it Accepts                 | Dependency                        |
+---------------------------------------------------------------------------+------------------------------------------------------------+----------------------------------+----------------------------------+-----------------------------------+
| []                                           | [To define syncfusion themes] | enum                             | MobSkins.BlueLight,              | [NA] |
|                                                                           |                                                            |                                  |                                  |                                   |
| []                                           |                                                            | []  | MobSkins.DarkNight,              |                                   |
|                                                                           |                                                            |                                  |                                  |                                   |
| []                                           |                                                            |                                  | MobSkins.MetroBlue,              |                                   |
|                                                                           |                                                            |                                  |                                  |                                   |
| [AutoFormat] [] |                                                            |                                  | MobSkins.Spinach                 |                                   |
|                                                                           |                                                            |                                  |                                  |                                   |
| []                                           |                                                            |                                  | []  |                                   |
|                                                                           |                                                            |                                  |                                  |                                   |
| []                                           |                                                            |                                  |                                  |                                   |
|                                                                           |                                                            |                                  |                                  |                                   |
| []                                           |                                                            |                                  |                                  |                                   |
+---------------------------------------------------------------------------+------------------------------------------------------------+----------------------------------+----------------------------------+-----------------------------------+

 

Using Builder

The following steps explain the appearance of the Form Button control using Builder.

1.   In the **view**, invoke the **Button** helper with the control ID as the first argument followed by the **AutoFormat** method with the desired theme as the argument.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    ] [\<] [h3] [\>] [Normal Button [\</][h3][\>]]                   |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<%][=] Html.MobSyncfusion().Button([\"button\"]).ButtonType([MobButtonType].Button).Text([\"Normal\"]).AutoFormat([MobSkins].Spinach)[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<][h3][\>]Reset Button[\</][h3][\>]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<%][=] Html.MobSyncfusion().Button([\"reset\"]).ButtonType([MobButtonType].Reset).Text([\"Reset\"]).AutoFormat([MobSkins].Spinach)[%\>]]    |
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
| [    [\<][h3][\>]Reset Button[\</][h3][\>]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\@{] Html.MobSyncfusion().Button([\"reset\"]).ButtonType([MobButtonType].Reset).Text([\"Reset\"]).AutoFormat([MobSkins].Spinach).Render(); [}]]                   |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\<][h3][\>]Submit Button[\</][h3][\>]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\@{] Html.MobSyncfusion().Button([\"submit\"]).ButtonType([MobButtonType].Submit).Text([\"Submit\"]).AutoFormat([MobSkins].Spinach).Render(); [}]]                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

3.   Build and run the application.

 

Using Properties Model

The following steps explain how to set the appearance of the Form Button control using the properties model:

1.  [In the **controller**, create an instance for the **MobButtonModel** and pass the instance through **ViewData** to the **view** as given below.]**

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [       [public][ActionResult] Button()]                                                                                                    |
|                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                              |
|                                                                                                                                                                                                                              |
| [            [MobButtonModel] model1 = [new][MobButtonModel]()]                                                     |
|                                                                                                                                                                                                                              |
| [                       {]                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| [                ] [Text=[\"Normal\"],]                                                                                      |
|                                                                                                                                                                                                                              |
| [                ButtonType=] [ MobButtonType] [.Button,] [] |
|                                                                                                                                                                                                                              |
| [                AutoFormat=[MobSkins].Spinach]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [             MobButtonModel] [ model2 = [new][MobButtonModel]()]                       |
|                                                                                                                                                                                                                              |
| [                       {]                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| [                ] [Text=[\"Reset\"],]                                                                                       |
|                                                                                                                                                                                                                              |
| [                ButtonType=] [ MobButtonType] [.Reset,] []  |
|                                                                                                                                                                                                                              |
| [                AutoFormat=[MobSkins].Spinach]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [            MobButtonModel] [ model3 = [new][MobButtonModel]()]                        |
|                                                                                                                                                                                                                              |
| [                       {]                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| [                ] [Text=[\"Submit\"],]                                                                                      |
|                                                                                                                                                                                                                              |
| [                ButtonType=] [ MobButtonType] [.Submit,] [] |
|                                                                                                                                                                                                                              |
| [                AutoFormat=[MobSkins].Spinach]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [            ViewData\[[\"button\"]\] = model1;]                                                                                                                 |
|                                                                                                                                                                                                                              |
| [            ViewData\[[\"reset\"]\] = model2;]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [            ViewData\[[\"submit\"]\] = model3;]                                                                                                                 |
|                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                      |
|                                                                                                                                                                                                                              |
| [        }] []                                                                                                                                               |
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
| **[]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                              |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                              |
| [       ] [\@{] [ Html.MobSyncfusion().Button] [([\"button\"]] [).Render(); [}]] |
|                                                                                                                                                                                                                                                                                                                                              |
| [       [\@{] Html.MobSyncfusion().Button] [([\"reset\"]] [).Render(); [}]]                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [       [\@{] Html.MobSyncfusion().Button] [([\"submit\"]] [).Render(); [}]] []                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application.

 

The output is shown in the following screenshot.

{border="0"}

Figure 213: Button---AutoFormat Property

 

{border="0"}

Figure 214: Form Button while Clicking

[]{#related-topics}

