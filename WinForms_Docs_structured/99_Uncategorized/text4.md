---
title: text4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\text4.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Text {#text style="tab-stops: 0pt"}

The user can set the text for On and Off state of the ToggleButton control. The text can be set for those states by the **OnText** and **OffText** properties.

Table 1 Text Properties Table

  --------- ---------------------------------------------------- ------------------ ------------------ ------------
  Name      Description                                          Type of Property   Value it Accepts   Dependency
  OnText    Sets the text for the enable state of the control    String             Any string         \-
  OffText   Sets the text for the disable state of the control   String             Any string         \-
  --------- ---------------------------------------------------- ------------------ ------------------ ------------

 

Using Builder

The following steps, explains about the text settings in ToggleButton control using Builder:

1.   In the **view**, invoke the **ToggleButton** helper with the control ID as the first argument followed by the **AutoFormat**, **OnText**, and **OffText** methods with their respective text.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                        |
|                                                                                                                                                                           |
| [        [\<%][=]\                                                                                                       |
|          Html.MobSyncfusion().ToggleButton([\"Togg\"])\                                                                                           |
|                                           .ToggleState([MobToggleState].On)\                                                                      |
|                                           .OnText([\"Enable\"])\                                                                                  |
|                                            .OffText([\"Disable\"])\                                                                               |
|                                            .AutoFormat([MobSkins].Spinach) [%\>]] |
|                                                                                                                                                                           |
| **[\[Razor\]]**                                                                                                                       |
|                                                                                                                                                                           |
| [        ] [\@{] [\                                              |
|            ] [Html.MobSyncfusion().ToggleButton([\"Togg\"])\                                                  |
|                                             .ToggleState([MobToggleState].On)\                                                                    |
|                                             .OnText([\"Enable\"])\                                                                                |
|                                             .OffText([\"Disable\"])\                                                                              |
|                                             .AutoFormat([MobSkins].Spinach)\                                                                      |
|                                             .Render(); ] [}]                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

 

Using Properties Model

The following steps explain how to manage text settings in the ToggleButton control using the properties model:

 

1.   In the **controller** create an instance of **MobToggleButtonModel**, define the **OnText** and **OffText** properties, and pass the instance through **ViewData** to **View** as given below.**

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

 

2.   In the **view**, invoke the **ToggleButton** helper with the **ViewData** key as the first argument.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                              |
| [       [\<%][=]Html.MobSyncfusion().ToggleButton] [([\"Toggle\"]] [)[%\>]] |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| **[\[Razor\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                              |
| [       [\@{]Html.MobSyncfusion().ToggleButton([\"Toggle\"]).Render();[}]]                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

The output is shown in the following screenshot:

 

 

{border="0"}

Figure 165: ToggleButton---Text Property

[]{#related-topics}

