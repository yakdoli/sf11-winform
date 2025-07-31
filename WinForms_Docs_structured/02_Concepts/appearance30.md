---
title: appearance30.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearance30.md
created_at: 2025-07-03
---






#### Appearance {#appearance style="tab-stops: 0pt"}

 

The Toggle-Button supports fourteen built-in themes giving a high visual appeal.

 

Use Case Scenarios

It allows for easy customization of the appearance to be displayed on the Toggle-Button.

 

Adding Appearance[ ]to an Application

The appearance can be customized through two ways in Toggle-Button.

[·      ]Using Builder

[·      ]Using Properties Model

 

Using Builder

 

The following steps guides you in customizing the appearance using Builder.

 

1.   In View, invoke the Toggle-Button helper with the button id as the first argument followed by the **Skin** methods.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                         |
|                                                                                                                                                                                |
| [        [\<%][=]Html.Syncfusion().ToggleButton([\"btnToggle\"])] |
|                                                                                                                                                                                |
| [        .Text([\"Save\"])]                                                                                        |
|                                                                                                                                                                                |
| [        **.Skin([Skins].Almond)**]                                                                                |
|                                                                                                                                                                                |
| [        .IsChecked([true])]                                                                                          |
|                                                                                                                                                                                |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                   |
|                                                                                                                                                                                |
| [        .ContentType([ContentTypes].TextAndImage)]                                                                |
|                                                                                                                                                                                |
| [        [%\>]]                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                       |
|                                                                                                                                                                                |
| [        [\@{][ ]Html.Syncfusion().ToggleButton([\"btnToggle\"])] |
|                                                                                                                                                                                |
| [        .Text([\"Save\"])]                                                                                        |
|                                                                                                                                                                                |
| [        **.Skin([Skins].Almond)**]                                                                                |
|                                                                                                                                                                                |
| [        .IsChecked([true])]                                                                                          |
|                                                                                                                                                                                |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                   |
|                                                                                                                                                                                |
| [        .ContentType([ContentTypes].TextAndImage)]                                                                |
|                                                                                                                                                                                |
| [        .Render();]                                                                                                                       |
|                                                                                                                                                                                |
| [        [}]]                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   Run the application.

 

The output is shown in the following screenshot.

[] 

{border="0"} {border="0"}   {border="0"}   {border="0"}

{border="0"} {border="0"}   {border="0"}   {border="0"}

{border="0"} {border="0"}   {border="0"}   {border="0"}

Figure 300: Toggle-Button Themes

[] 

**Using Properties Model**

 

The following steps guides in customizing the appearance using the Properties model.

1.   In Controller, create an object for the **ToggleButtonModel** class and set the **Text, ImageUrl, ContentType, ImagePosition,** and **Skin** properties.

2.   Assign this model class to **View** data.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                   |
|                                                                                                                                                                                            |
| [        [public] [ActionResult] Index()]                                                                 |
|                                                                                                                                                                                            |
| [        {]                                                                                                                                            |
|                                                                                                                                                                                            |
| [            [ToggleButtonModel] toggleButtonModel = [new] [ToggleButtonModel]()] |
|                                                                                                                                                                                            |
| [            {]                                                                                                                                        |
|                                                                                                                                                                                            |
| [                Text = [\"Save\"],]                                                                                           |
|                                                                                                                                                                                            |
| [                **Skin = [Skins].Almond,**]                                                                                   |
|                                                                                                                                                                                            |
| [                IsChecked = [true],]                                                                                             |
|                                                                                                                                                                                            |
| [                ImageUrl = [\"Content/icon_save.png\"],]                                                                      |
|                                                                                                                                                                                            |
| [                ContentType = [ContentTypes].TextAndImage,]                                                                   |
|                                                                                                                                                                                            |
| [                ImagePosition = [ImagePositions].Right]                                                                       |
|                                                                                                                                                                                            |
| [            };]                                                                                                                                       |
|                                                                                                                                                                                            |
| [            ViewData\[[\"ToggleButtonModel\"]\] = toggleButtonModel;]                                                         |
|                                                                                                                                                                                            |
| [            [return] View();]                                                                                                    |
|                                                                                                                                                                                            |
| [        }]                                                                                                                                            |
|                                                                                                                                                                                            |
| []                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In View, invoke the ToggleButton helper with the button id as the first argument followed by the view data of the **ToggleButtonModel** class.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().ToggleButton([\"btnToggle\"],([ToggleButtonModel])ViewData\[[\"ToggleButtonModel\"]\]) [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\@{][ ][Html.Syncfusion().ToggleButton([\"btnToggle\"],([ToggleButtonModel])ViewData\[[\"ToggleButtonModel\"]\]).Render();][}][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Run the application.

 

The output is shown in the following screenshot.

[] 

{border="0"} {border="0"}   {border="0"}   {border="0"}

{border="0"} {border="0"}   {border="0"}   {border="0"}

{border="0"} {border="0"}   {border="0"}   {border="0"}

Figure 301: Toggle-Button Themes

Properties

[] 

The following table illustrates the properties which describes the appearance of the Toggle-Button.

[] 

+-----------+-----------------------------------------------------------------+----------------------+-----------+------------------------+---------------------------+
| Name      | Description                                                     | Type of the property | Data Type | Value it accepts       | Dependency                |
+-----------+-----------------------------------------------------------------+----------------------+-----------+------------------------+---------------------------+
| Skin      | Specifies the field that provides the appearance of the button. | Server side          | Enum      | Skins.Almond           | []  |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Blend            |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Blueberry        |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Marble           |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Midnight         |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Monochrome       |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Office2007Black  |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Office2007Blue   |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Office2007Silver |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Olive            |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Sandune          |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Turquoise        |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.Vista            |                           |
|           |                                                                 |                      |           |                        |                           |
|           |                                                                 |                      |           | Skins.VS2010           |                           |
+-----------+-----------------------------------------------------------------+----------------------+-----------+------------------------+---------------------------+

[] 

Sample Link

To view the samples, follow the steps below.

1.   Open the Tools sample browser from the dashboard. (Refer to the Samples and Location chapter)

2.   Navigate to **Tools.Mvc -\> Button -\> Core Features Demo**.

**[]** 

[]{#related-topics}

