---
title: 321appearance.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\321appearance.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### 3.2.1 Appearance {#appearance style="tab-stops: 0pt"}

The RouteLink Button control supports built-in themes that provide great visual appeal that are suitable for various layouts. It supports the following four built-in Syncfusion themes to enhance the look and feel:

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

The following steps explain the appearance customization of the RouteLink Button control using Builder.

 

1.   In the **view**, invoke the RouteLink Button helper with the text of the button as first argument followed by the **AutoFormat** method with the desired theme as its argument.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<%] [=] [ Html.MobSyncfusion().RouteLink([\"RouteLink\"], [\"Button\"]).AutoFormat([MobSkins].Spinach)[%\>]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\@{] [] [Html.MobSyncfusion().RouteLink([\"RouteLink\"], [\"Button\"]).AutoFormat([MobSkins].Spinach)] [.] [Render();] [] [}] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

The output is shown in the following screenshot.[]

{border="0"}

Figure 218:  RouteLink Button---AutoFormat Property

 

If users click the route link button, the theme will be applied to the control. The following screenshot shows how the theme is applied to the control.

 

{border="0"}

Figure 219: RouteLinkButton while Clicking

 

[]{#related-topics}

