---
title: icons.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\icons.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Icons {#icons style="tab-stops: 0pt"}

The user can give images for On and Off state along with the **Text** property of the ToggleButton control. The image can be set for the states with the **ImageURL** property.

 

Table 2 Icons Properties Table

  ------------------ ------------------------------------------------------ ------------------ ------------------ ------------
  Name               Description                                            Type of Property   Value it Accepts   Dependency
  OnStateImageUrl    Sets the image for the enable state of the control.    String             Any string         \-
  OffStateImageUrl   Sets the image for the disable state of the control.   String             Any string         \-
  ------------------ ------------------------------------------------------ ------------------ ------------------ ------------

 

Using Builder

The following steps explain how to set the image settings in the ToggleButton control using Builder:

3.   In the **view**, invoke the **ToggleButton** helper with the control ID as the first argument followed by the **AutoFormat**, **OnText**, **OffText**, **OnStateImageUrl**, and **OffStateImageUrl** methods with its respective text and images.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                         |
|                                                                                                                                                            |
| [        [\<%][=]\                                                                                        |
|         Html.MobSyncfusion().ToggleButton([\"Togg\"])\                                                                             |
|                             .OnText([\"Enable\"])\                                                                                 |
|                             .OffText([\"Disable])\                                                                                 |
|                             .OnStateImageUrl([\"Wifi.png\"])\                                                                      |
|                             .OffStateImageUrl([\"Bluetooth.png\"])\                                                                |
|                             .AutoFormat([MobSkins].Spinach) [%\>]] |
|                                                                                                                                                            |
| **[\[Razor\]]**                                                                                                        |
|                                                                                                                                                            |
| [        ] [\@{] [\                               |
| ] [        Html.MobSyncfusion().ToggleButton([\"Togg\"])\                                      |
|                             .OnText([\"Enable\"])\                                                                                 |
|                             .OffText([\"Disable])\                                                                                 |
|                             .OnStateImageUrl([\"Wifi.png\"])\                                                                      |
|                             .OffStateImageUrl([\"Bluetooth.png\"])\                                                                |
|                             .AutoFormat([MobSkins].Spinach)\                                                                       |
|                             .Render(); ] [}]                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

 

Using Properties Model

The following steps explain how to set the image settings in the ToggleButton control using the properties model:

 

4.   In the **Controller**, create an instance of **MobToggleButtonModel**, define the **OnStateImageUrl** and **OffStateImageUrl** properties and pass the instance through **ViewData** to **View** as given below.**

*[[]]{.underline}*  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                |
|                                                                                                                                                                                     |
| [        [public][ActionResult] ToggleButton()]                                                    |
|                                                                                                                                                                                     |
| [        {]                                                                                                                                     |
|                                                                                                                                                                                     |
| [            [MobToggleButtonModel] model = [new][MobToggleButtonModel]()] |
|                                                                                                                                                                                     |
| [            {]                                                                                                                                 |
|                                                                                                                                                                                     |
| [                ] [OnText=[\"Enable\"],]                                           |
|                                                                                                                                                                                     |
| [                OffText=[\"Disable\"],]                                                                                |
|                                                                                                                                                                                     |
| [                OnStateImageUrl=[\"Wifi.png\"],[]]                                             |
|                                                                                                                                                                                     |
| [                OffStateImageUrl=[\"Bluetooth.png\"],]                                                                 |
|                                                                                                                                                                                     |
| [                AutoFormat=[MobSkins].Spinach]                                                                         |
|                                                                                                                                                                                     |
| [            };]                                                                                                                                |
|                                                                                                                                                                                     |
| [            ViewData\[[\"Toggle\"]\] = model;]                                                                         |
|                                                                                                                                                                                     |
| [            [return] View();]                                                                                             |
|                                                                                                                                                                                     |
| [        }]                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   In the **view**, invoke the **ToggleButton** helper with the **ViewData** key as the first argument.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                     |
| [       [\<%][=]Html.MobSyncfusion().ToggleButton] [([\"Toggle\"]] [)[%\>]] [] |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                     |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                     |
| [       [\@{]Html.MobSyncfusion().ToggleButton([\"Toggle\"]).Render();[}]]                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Build and run the application.

 

The output is shown in the following screenshot.

{border="0"} 

Figure 166: ToggleButton---ImageUrl Property

[]{#related-topics}

