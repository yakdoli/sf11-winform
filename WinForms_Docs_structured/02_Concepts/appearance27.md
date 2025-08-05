---
title: appearance27.md
original_path: WinForms_Docs/02_Concepts/appearance27.md
created_at: 2025-08-05
---






#### Appearance {#appearance style="tab-stops: 0pt"}

The Split-Button supports fourteen built-in themes giving a high visual appeal.

 

Use Case Scenarios

It allows for easy customization of the appearance to be displayed on the Split-Button.

 

Adding Appearance[ ]to an Application

The appearance can be customized by two ways in the Split-Button.

[·      ]Using Builder

[·      ]Using Properties Model

 

Using Builder

The following steps guides you in customizing the appearance using the Builder.

 

1.   In **View**, invoke the SplitButton helper with the button id as the first argument followed by the **Skin** methods.

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [        [\<%][=]Html.Syncfusion().SplitButton([\"btnSplit\"])]                                  |
|                                                                                                                                                                                                               |
| [            .Text([\"Save\"])]                                                                                                                   |
|                                                                                                                                                                                                               |
| [            **.Skin([Skins].Almond)**]                                                                                                           |
|                                                                                                                                                                                                               |
| [            .ContentType([ContentTypes].TextAndImage)]                                                                                           |
|                                                                                                                                                                                                               |
| [            .ImageUrl([\"Content/icon_save.png\"])]                                                                                              |
|                                                                                                                                                                                                               |
| [            .ImagePosition([ImagePositions].Right)]                                                                                              |
|                                                                                                                                                                                                               |
| [            .ArrowPosition([ArrowPositions].Bottom)]                                                                                             |
|                                                                                                                                                                                                               |
| [            .DataSource(([IEnumerable])ViewData\[[\"MenuData\"]\])]                                                      |
|                                                                                                                                                                                                               |
| [            .BindTo(mapping =\> mapping.Id([\"Id\"]).ParentId([\"ParentId\"]).Text([\"Text\"]))] |
|                                                                                                                                                                                                               |
| [        [%\>]]**[]**                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                      |
|                                                                                                                                                                                                               |
| [        [\@{][ ]Html.Syncfusion().SplitButton([\"btnSplit\"])]                                  |
|                                                                                                                                                                                                               |
| [            .Text([\"Save\"])]                                                                                                                   |
|                                                                                                                                                                                                               |
| [            **.Skin([Skins].Almond)**]                                                                                                           |
|                                                                                                                                                                                                               |
| [            .ContentType([ContentTypes].TextAndImage)]                                                                                           |
|                                                                                                                                                                                                               |
| [            .ImageUrl([\"Content/icon_save.png\"])]                                                                                              |
|                                                                                                                                                                                                               |
| [            .ImagePosition([ImagePositions].Right)]                                                                                              |
|                                                                                                                                                                                                               |
| [            .ArrowPosition([ArrowPositions].Bottom)]                                                                                             |
|                                                                                                                                                                                                               |
| [            .DataSource(([IEnumerable])ViewData\[[\"MenuData\"]\])]                                                      |
|                                                                                                                                                                                                               |
| [            .BindTo(mapping =\> mapping.Id([\"Id\"]).ParentId([\"ParentId\"]).Text([\"Text\"]))] |
|                                                                                                                                                                                                               |
| [            .Render();]                                                                                                                                                  |
|                                                                                                                                                                                                               |
| [        [}]]**[]**                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

2.   Run the application.

[] 

The output is shown in the following screenshot.

[] 

[] 

{border="0"}          {border="0"}   {border="0"}   {border="0"}

{border="0"}          {border="0"}   {border="0"}   {border="0"}

{border="0"}          {border="0"}   {border="0"}   {border="0"}

[{border="0"}][     {border="0"}]

Figure 249: Split Button Themes

Using Properties Model

 

The following steps guides you in customizing the appearance using the Properties model.

 

1.   In **Controller**, create an object for the **SplitButtonModel** class and set **Text, ImageUrl, ContentType, ImagePosition,** and **Skin** properties. Assign this model class to view data.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [        [public] [ActionResult] Index()]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                               |
| [            [SplitButtonModel] splitButtonModel = [new] [SplitButtonModel]()]                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [            {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [                Text = [\"Save\"],]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [                ImageUrl = [\"Content/icon_save.png\"],]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| **[                Skin = [Skins].Almond,]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [                ContentType = [ContentTypes].TextAndImage,]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [                ImagePosition = [ImagePositions].Right,]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [                ArrowPosition = [ArrowPositions].Right,]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| [                DataSource = context.MenuData.ToList(),]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [                BindTo = [new] [DropDownFields]() { Id = [\"Id\"], ParentId = [\"ParentId\"], Text = [\"Text\"] },] |
|                                                                                                                                                                                                                                                                               |
| [            };]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [            ViewData\[[\"SplitButtonModel\"]\] = splitButtonModel;]                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [            [return] View();]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, invoke the **SplitButton** helper with the button id as the first argument followed by the view data of the **SplitButtonModel** class.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().SplitButton([\"btnSplit\"],([SplitButtonModel])ViewData\[[\"SplitButtonModel\"]\]) [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\@{][ ][Html.Syncfusion().SplitButton([\"btnSplit\"],([SplitButtonModel])ViewData\[[\"SplitButtonModel\"]\]).Render(); [}]] |
|                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   Run the application.

 

The output is shown in the following screenshot.

[] 

{border="0"}          {border="0"}   {border="0"}   {border="0"}

{border="0"}          {border="0"}   {border="0"}   {border="0"}

{border="0"}          {border="0"}   {border="0"}   {border="0"}

[{border="0"}][     {border="0"}]

Figure 250: Split Button Themes

Properties

The following table illustrates the properties which describes the appearance of the Split-Button.

 

+-----------+-----------------------------------------------------------------+----------------------+-----------+--------------------------------------------------+---------------------------+
| Name      | Description                                                     | Type of the property | Data Type | Value it accepts                                 | Dependency                |
+-----------+-----------------------------------------------------------------+----------------------+-----------+--------------------------------------------------+---------------------------+
| Skin      | Specifies the field that provides the appearance of the button. | Server side          | Enum      | [Skins].Almond           | []  |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Blend            |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Blueberry        |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Marble           |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Midnight         |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Monochrome       |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Office2007Black  |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Office2007Blue   |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Office2007Silver |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Olive            |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Sandune          |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Turquoise        |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].Vista            |                           |
|           |                                                                 |                      |           |                                                  |                           |
|           |                                                                 |                      |           | [Skins].VS2010           |                           |
+-----------+-----------------------------------------------------------------+----------------------+-----------+--------------------------------------------------+---------------------------+

[] 

Sample Link

To view the samples, follow the steps below.

1.   Open the Tools sample browser from the dashboard. (Refer to the Samples and Location chapter).

2.   Navigate to **Tools.Mvc -\> Button -\> Core Features Demo**.

 

[]{#related-topics}

