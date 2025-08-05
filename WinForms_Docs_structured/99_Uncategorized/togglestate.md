---
title: togglestate.md
original_path: WinForms_Docs/99_Uncategorized/togglestate.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### ToggleState {#togglestate style="tab-stops: 0pt"}

The toggle state can be customized via the **ToggleState** property while the control is rendered initially.

 

Table 3 ToggleState Properties Table

+----------------+----------------------------------------------------------+------------------+--------------------------------------------------------------------------+-------------+
| Name           | Description                                              | Type of Property | Value it Accepts                                                         | Dependency  |
+----------------+----------------------------------------------------------+------------------+--------------------------------------------------------------------------+-------------+
| Bool Value     | True---Makes the toggle button active in enabled state   | Bool             | True                                                                     | \-          |
|                |                                                          |                  |                                                                          |             |
|                | False---Makes the toggle button active in disabled state |                  | False                                                                    |             |
+----------------+----------------------------------------------------------+------------------+--------------------------------------------------------------------------+-------------+
| MobToggleState | On---Makes the toggle button active in enabled state     | Enum             | [MobToggleState].On  | \-          |
|                |                                                          |                  |                                                                          |             |
|                | Off---Makes the toggle button active in disabled state   |                  | [MobToggleState].Off |             |
+----------------+----------------------------------------------------------+------------------+--------------------------------------------------------------------------+-------------+

 

Using Builder

The following steps explain how to set the state settings in the ToggleButton control using Builder:

 

3.   In the **view**, invoke the **ToggleButton** helper with the control ID as the first argument followed by the **AutoFormat**, **ToggleState**, **OnText**, **OffText**, **OnStateImageUrl**, and **OffStateImageUrl** methods with their respective text and images.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                              |
|                                                                                                                                                                 |
| [        [\<%][=]\                                                                                             |
|           Html.MobSyncfusion().ToggleButton([\"Togg\"])\                                                                                |
|              .ToggleState([MobToggleState].On)\                                                                                         |
|              .OnText([\"Enable\"])\                                                                                                     |
|              .OffText([\"Disable])\                                                                                                     |
|              .OnStateImageUrl([\"../Content/Button/Images/Wifi.png\"])\                                                                 |
|              .OffStateImageUrl([\"../Content/Button/Images/Wifi.png\"])\                                                                |
|              .AutoFormat([MobSkins].Spinach)[%\>\                                                                                       |
| \                                                                                                                                                               |
| ]]                                                                                              |
|                                                                                                                                                                 |
| [        [\<%][=]\                                                                                             |
|            Html.MobSyncfusion().ToggleButton([\"Togg1\"])\                                                                              |
|                .ToggleState(false)\                                                                                                                             |
|                .OnText([\"Enable\"])\                                                                                                   |
|                .OffText([\"Disable])\                                                                                                   |
|                .OnStateImageUrl([\"../Content/Button/Images/Wifi.png\"])\                                                               |
|                .OffStateImageUrl([\"../Content/Button/Images/Wifi.png\"])\                                                              |
|                .AutoFormat([MobSkins].Spinach) [%\>]]                   |
|                                                                                                                                                                 |
| **[\[Razor\]]**                                                                                                             |
|                                                                                                                                                                 |
| [        ] [\@{] [\                                    |
|         ] [Html.MobSyncfusion().ToggleButton([\"Togg\"])\                                           |
|             .ToggleState([MobToggleState].On)\                                                                                          |
|             .OnText([\"Enable\"])\                                                                                                      |
|             .OffText([\"Disable])\                                                                                                      |
|             .OnStateImageUrl([\"../Content/Button/Images/Wifi.png\"])\                                                                  |
|             .OffStateImageUrl([\"../Content/Button/Images/Wifi.png\"])\                                                                 |
|             .AutoFormat([MobSkins].Spinach)\                                                                                            |
|             .Render(); ] [}] [] |
|                                                                                                                                                                 |
| [         ] [\@{] [\                                  |
| ] [         Html.MobSyncfusion().ToggleButton([\"Togg1\"])[\                                        |
| ]            .ToggleState(false)\                                                                                                       |
|             .OnText([\"Enable\"])\                                                                                                      |
|             .OffText([\"Disable])\                                                                                                      |
|             .OnStateImageUrl([\"../Content/Button/Images/Wifi.png\"])\                                                                  |
|             .OffStateImageUrl([\"../Content/Button/Images/Wifi.png\"])\                                                                 |
|            .AutoFormat([MobSkins].Spinach)\                                                                                             |
|            .Render(); ] [}]                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

 

Using Properties Model

The following steps explain how to set the state settings in the ToggleButton control using the properties model:

 

4.   In the **controller**, create an instance of **MobToggleButtonModel**, define the **ToggleState** property and pass the instance through **ViewData** to **View** as given below:**

*[[]]{.underline}*  

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [       [public][ActionResult] ToggleButton()]                                                                                    |
|                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                    |
|                                                                                                                                                                                                                    |
| [            [MobToggleButtonModel] model = [new][MobToggleButtonModel]()]                                |
|                                                                                                                                                                                                                    |
|             [{]                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [                ] [OnText=[\"Enable\"],]                                                                          |
|                                                                                                                                                                                                                    |
| [                OffText=[\"Disable\"],]                                                                                                               |
|                                                                                                                                                                                                                    |
| [                OnStateImageUrl=[\"../Content/Button/Images/Wifi.png\"],[]]                                                   |
|                                                                                                                                                                                                                    |
| [                OffStateImageUrl=[\"../Content/Button/Images/ Bluetooth.png\"],]                                                                      |
|                                                                                                                                                                                                                    |
| [                AutoFormat=[MobSkins].Spinach]                                                                                                        |
|                                                                                                                                                                                                                    |
| [            };]                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [             MobToggleButtonModel] [ model1 = [new][MobToggleButtonModel]()] |
|                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [                ] [OnText=[\"Enable\"],]                                                                          |
|                                                                                                                                                                                                                    |
| [                OffText=[\"Disable\"],]                                                                                                               |
|                                                                                                                                                                                                                    |
| [                OnStateImageUrl=[\"../Content/Button/Images/Wifi.png\"],[]]                                                   |
|                                                                                                                                                                                                                    |
| [                OffStateImageUrl=[\"../Content/Button/Images/Bluetooth.png\"],]                                                                       |
|                                                                                                                                                                                                                    |
| [                AutoFormat=[MobSkins].Spinach,]                                                                                                       |
|                                                                                                                                                                                                                    |
| [                ToggleState = [MobToggleState].Off]                                                                                                   |
|                                                                                                                                                                                                                    |
| [            };]                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [            ViewData\[[\"Toggle\"]\] = model;]                                                                                                        |
|                                                                                                                                                                                                                    |
| [            ViewData\[[\"Toggle1\"]\] = model1;]                                                                                                      |
|                                                                                                                                                                                                                    |
| [            [return] View();]                                                                                                                            |
|                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   In the **view**, invoke the **ToggleButton** helper with the **ViewData** key as the first argument.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                      |
| [       [\<%][=]Html.MobSyncfusion().ToggleButton] [([\"Toggle\"]] [)[%\>]]                                         |
|                                                                                                                                                                                                                                                                                                                                      |
| [       [\<%][=]Html.MobSyncfusion().ToggleButton] [([\"Toggle1\"]] [)[%\>]] [] |
|                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                      |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                      |
| [       [\@{]Html.MobSyncfusion().ToggleButton([\"Toggle\"]).Render();[}]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| [       [\@{]Html.MobSyncfusion().ToggleButton([\"Toggle1\"]).Render();[}]]                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Build and run the application.

 

The output is shown in the following screenshot:

{border="0"}

Figure 167: ToggleButton---ToggleState Property

[]{#related-topics}

