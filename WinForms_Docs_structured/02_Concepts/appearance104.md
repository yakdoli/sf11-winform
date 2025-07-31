---
title: appearance104.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearance104.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Appearance {#appearance style="tab-stops: 0pt"}

The ActionLink Button control supports built-in themes that give high visual appeal that are suitable for various layouts. It supports the following four built-in Syncfusion themes to enhance the look and feel:

[·      ] [BlueLight]

[·      ] [DarkNight]

[·      ] [MetroBlue]

[·      ] [Spinach]

Properties

+---------------------------------------------------------------------------+------------------------------------------------------------------+----------------------------------+----------------------------------+-----------------------------------+
| Name                                                                      | Description                                                      | Type of the Property             | Value it Accepts                 | Dependency                        |
+---------------------------------------------------------------------------+------------------------------------------------------------------+----------------------------------+----------------------------------+-----------------------------------+
| []                                           | [Used to define Syncfusion themes.] | enum                             | MobSkins.BlueLight,              | [NA] |
|                                                                           |                                                                  |                                  |                                  |                                   |
| []                                           |                                                                  | []  | MobSkins.DarkNight,              |                                   |
|                                                                           |                                                                  |                                  |                                  |                                   |
| []                                           |                                                                  |                                  | MobSkins.MetroBlue,              |                                   |
|                                                                           |                                                                  |                                  |                                  |                                   |
| [AutoFormat] [] |                                                                  |                                  | MobSkins.Spinach                 |                                   |
|                                                                           |                                                                  |                                  |                                  |                                   |
| []                                           |                                                                  |                                  | []  |                                   |
|                                                                           |                                                                  |                                  |                                  |                                   |
| []                                           |                                                                  |                                  |                                  |                                   |
|                                                                           |                                                                  |                                  |                                  |                                   |
| []                                           |                                                                  |                                  |                                  |                                   |
+---------------------------------------------------------------------------+------------------------------------------------------------------+----------------------------------+----------------------------------+-----------------------------------+

 

Using Builder

The following steps explain how to customize the appearance of the ActionLink Button control using Builder.

1.   In the **view**, invoke the **ActionLink Button** helper with the text of the button as the first argument followed by the **AutoFormat** method with the desired theme as the argument.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [        [\<%][=] Html.MobSyncfusion()] [.ActionLink([\"Link Button\"], [\"ActionLink\"], [\"Button\"]).AutoFormat([MobSkins].Spinach)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [ ] [       ] [%\>]                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [        ] [\@{] [] [Html.MobSyncfusion()] [.ActionLink([\"Link Button\"], [\"ActionLink\"], [\"Button\"]).AutoFormat([MobSkins].Spinach).] [Render(); ] [\ |
|         [}]]                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

 

The output is shown in the following screenshot.[]

{border="0"}

Figure 206: ActionLink Button---AutoFormat Property

 

{border="0"}

Figure 207: ActionLink Button while Clicking

 

 

[]{#related-topics}

