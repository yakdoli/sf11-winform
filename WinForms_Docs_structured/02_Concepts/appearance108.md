---
title: appearance108.md
original_path: WinForms_Docs/02_Concepts/appearance108.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Appearance {#appearance style="tab-stops: 0pt"}

The ToggleButton control supports built-in themes that provide stunning visuals that are suitable for various layouts. It supports the following four built-in Syncfusion themes to enhance the look and feel:

[·      ] [BlueLight]

[·      ] [DarkNight]

[·      ] [MetroBlue]

[·      ] [Spinach]

Properties

 

+---------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------+-----------------------------------------------+-----------------------------------+
| Name                                                                      | Description                                              | Type of the Property             | Value it Accepts                              | Dependency                        |
+---------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------+-----------------------------------------------+-----------------------------------+
| []                                           | [Defines syncfusion themes] | enum                             | [MobSkins].BlueLight, | [NA] |
|                                                                           |                                                          |                                  |                                               |                                   |
| []                                           |                                                          | []  | [MobSkins].DarkNight, |                                   |
|                                                                           |                                                          |                                  |                                               |                                   |
| []                                           |                                                          |                                  | [MobSkins].MetroBlue, |                                   |
|                                                                           |                                                          |                                  |                                               |                                   |
| [AutoFormat] [] |                                                          |                                  | [MobSkins].Spinach    |                                   |
|                                                                           |                                                          |                                  |                                               |                                   |
| []                                           |                                                          |                                  | []               |                                   |
|                                                                           |                                                          |                                  |                                               |                                   |
| []                                           |                                                          |                                  |                                               |                                   |
|                                                                           |                                                          |                                  |                                               |                                   |
| []                                           |                                                          |                                  |                                               |                                   |
+---------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------+-----------------------------------------------+-----------------------------------+

 

Using Builder

The following steps explain the appearance of the ToggleButton control using Builder:

4.   In the **view**, invoke the **ToggleButton** helper with the control ID as the first argument followed by the **AutoFormat** method with the desired theme as the argument.

 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                         |
|                                                                                                                                            |
| [        [\<%][=]\                                                                        |
|         Html.MobSyncfusion().ToggleButton([\"Togg\"])\                                                             |
|             .ToggleState([MobToggleState].On)\                                                                     |
|             .OnText([\"Enable\"])\                                                                                 |
|             .OffText([\"Disable\"])\                                                                               |
|             .AutoFormat([MobSkins].Spinach) [%\>]] |
|                                                                                                                                            |
| **[\[Razor\]]**                                                                                        |
|                                                                                                                                            |
| [        ] [\@{] [\               |
| ] [         Html.MobSyncfusion().ToggleButton([\"Togg\"])\                     |
|               .ToggleState([MobToggleState].On)\                                                                   |
|               .OnText([\"Enable\"])\                                                                               |
|               .OffText([\"Disable\"])\                                                                             |
|               .AutoFormat([MobSkins].Spinach)\                                                                     |
|               .Render(); ] [}]                 |
+--------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Build and run the application.

 

Using Properties Model

The following steps explain how to set the appearance of the ToggleButton control using the properties model:

[] 

4.  [In the **controller**, create an instance for the **MobToggleButtonModel** and pass the instance through **ViewData** to **View** as given below:]

*[[]]{.underline}*  

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [        [public][ActionResult] ToggleButton()]                                                                                |
|                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                 |
|                                                                                                                                                                                                                 |
|             [MobToggleButtonModel][ model = [new][MobToggleButtonModel]()] |
|                                                                                                                                                                                                                 |
| [            {]                                                                                                                                                             |
|                                                                                                                                                                                                                 |
| [                ] [OnText=[\"Enable\"],]                                                                       |
|                                                                                                                                                                                                                 |
| [                OffText=[\"Disable\"],]                                                                                                            |
|                                                                                                                                                                                                                 |
| [                AutoFormat=[MobSkins].Spinach]                                                                                                     |
|                                                                                                                                                                                                                 |
| [            };]                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [            ViewData\[[\"Toggle\"]\] = model;]                                                                                                     |
|                                                                                                                                                                                                                 |
| [            [return] View();]                                                                                                                         |
|                                                                                                                                                                                                                 |
| [       }] []                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   In the **view**, invoke the **ToggleButton** helper with the **ViewData** key as the first argument.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                     |
| [       [\<%][=]Html.MobSyncfusion().ToggleButton] [([\"Toggle\"]] [)[%\>]] [] |
|                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                     |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                     |
| **[      ]** [\@{] [Html.MobSyncfusion().ToggleButton([\"Toggle\"]).Render();[}]]                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Build and run the application.

The output is shown in the following screenshot:

 

{border="0"}

Figure 168: ToggleButton---AutoFormat Property

 

[]{#related-topics}

