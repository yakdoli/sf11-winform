---
title: appearance105.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearance105.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Appearance {#appearance style="tab-stops: 0pt"}

The AjaxActionLink Button control supports built-in themes that provide high visual appeal that are suitable for various layouts. It supports the following four built-in Syncfusion themes to enhance the look and feel:

[·      ] [BlueLight]

[·      ] [DarkNight]

[·      ] [MetroBlue]

[·      ] [Spinach]

 

Properties

+---------------------------------------------------------------------------+------------------------------------------------------------+----------------------------------+-----------------------------------------------+-----------------------------------+
| Name                                                                      | Description                                                | Type of the Property             | Value it Accepts                              | Dependency                        |
+---------------------------------------------------------------------------+------------------------------------------------------------+----------------------------------+-----------------------------------------------+-----------------------------------+
| []                                           | [To define syncfusion themes] | enum                             | [MobSkins].BlueLight, | [NA] |
|                                                                           |                                                            |                                  |                                               |                                   |
| []                                           |                                                            | []  | [MobSkins].DarkNight, |                                   |
|                                                                           |                                                            |                                  |                                               |                                   |
| []                                           |                                                            |                                  | [MobSkins].MetroBlue, |                                   |
|                                                                           |                                                            |                                  |                                               |                                   |
| [AutoFormat] [] |                                                            |                                  | [MobSkins].Spinach    |                                   |
|                                                                           |                                                            |                                  |                                               |                                   |
| []                                           |                                                            |                                  | []               |                                   |
|                                                                           |                                                            |                                  |                                               |                                   |
| []                                           |                                                            |                                  |                                               |                                   |
|                                                                           |                                                            |                                  |                                               |                                   |
| []                                           |                                                            |                                  |                                               |                                   |
+---------------------------------------------------------------------------+------------------------------------------------------------+----------------------------------+-----------------------------------------------+-----------------------------------+

 

Using Builder

The following steps explain the appearance of the AjaxActionLink Button control using Builder.

 

1.   In the **view**, invoke the **AjaxActionLinkButton** helper with the text of the button as the first argument, followed by the **AutoFormat** method with the desired theme as the argument.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<%] [=] [ Ajax.MobSyncfusion().ActionLink([\"Link Button\"], [\"ShowTime\"], [new] { }, [new][AjaxOptions] { UpdateTargetId = [\"ShowTime\"], InsertionMode = [InsertionMode].Replace }, [new] { }).AutoFormat([MobSkins].DarkNight)[%\>]]                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [        ] [\@{] [] [Ajax.MobSyncfusion().ActionLink([\"Link Button\"], [\"ShowTime\"], [new] { }, [new][AjaxOptions] { UpdateTargetId = [\"ShowTime\"], InsertionMode = [InsertionMode].Replace }, [new] { }).AutoFormat([MobSkins].DarkNight).Render();] [] [\ |
|         [}]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

 

The output is shown in the following screenshot.[]

[] 

[ ] {border="0"}

Figure 228: Ajax ActionLink Button---AutoFormat Property

While clicking the AJAX action link the theme is applied.

{border="0"}

Figure 229: AJAX ActionLink after Theme is Applied

 

The updated view can be shown as follows:

{border="0"}

Figure 230: Updated Time after AJAX Action Link is Clicked

 

[]{#related-topics}

