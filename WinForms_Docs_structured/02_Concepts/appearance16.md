---
title: appearance16.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearance16.md
created_at: 2025-07-03
---






#### Appearance {#appearance style="tab-stops: 0pt"}

The Button control supports fourteen built-in themes that gives a high visual appeal.

Use Case Scenarios

It allows for easy customization of the appearance to be displayed on the button.

Adding Appearance to an Application

Appearance can be customized through two ways in button.

[·      ]Using Builder

[·      ]Using Properties Model

[] 

Using Builder

The following steps guides you in customizing appearance using Builder.

[] 

1.   In **View**, invoke the normal Button helper with the button ID as the first argument followed by the **Skin** methods.

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                   |
|                                                                                                                                                                          |
| [        [\<%][=]Html.Syncfusion().Button([\"btnNormal\"])] |
|                                                                                                                                                                          |
| [        .Text([\"Save\"])]                                                                                  |
|                                                                                                                                                                          |
| [        .Skin([Skins].Almond)]                                                                              |
|                                                                                                                                                                          |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                             |
|                                                                                                                                                                          |
| [        .ContentType([ContentTypes].TextAndImage)]                                                          |
|                                                                                                                                                                          |
| [        [%\>]]                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                       |
|                                                                                                                                                |
| **[]**                                                                                                     |
|                                                                                                                                                |
| [      [\@{]Html.Syncfusion().Button([\"btnNormal\"])] |
|                                                                                                                                                |
| [        .Text([\"Save\"])]                                                        |
|                                                                                                                                                |
| [        .Skin([Skins].Almond)]                                                    |
|                                                                                                                                                |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                   |
|                                                                                                                                                |
| [        .ContentType([ContentTypes].TextAndImage)]                                |
|                                                                                                                                                |
| [        .Render();[}]]                                                        |
|                                                                                                                                                |
| []                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Run the application.

[] 

The output is shown in the following screenshot.

[] 

{border="0"} {border="0"}   {border="0"}   {border="0"}

{border="0"} {border="0"}   {border="0"}   {border="0"}

{border="0"} {border="0"}   {border="0"}   {border="0"}

{border="0"} {border="0"}

Figure 88: Normal Button Themes

Using Properties Model

[] 

The following steps guides you in customizing the appearance using the Properties model.

1.   In Controller, create an object for the **ButtonModel** class and set the **Text**, **ImageUrl**, **ContentType**, **ImagePosition**, and **Skin** properties. Assign this model class to view data.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                 |
|                                                                                                                                                                          |
| **[]**                                                                                                                               |
|                                                                                                                                                                          |
| [        [public] [ActionResult] Index()]                                               |
|                                                                                                                                                                          |
| [        {]                                                                                                                          |
|                                                                                                                                                                          |
| [            [ButtonModel] buttonModel = [new] [ButtonModel]()] |
|                                                                                                                                                                          |
| [            {]                                                                                                                      |
|                                                                                                                                                                          |
| [                Text = [\"Save\"],]                                                                         |
|                                                                                                                                                                          |
| [                **Skin=[Skins].Almond,**]                                                                   |
|                                                                                                                                                                          |
| [                ImageUrl = [\"Content/icon_save.png\"],]                                                    |
|                                                                                                                                                                          |
| [                ContentType = [ContentTypes].TextAndImage,]                                                 |
|                                                                                                                                                                          |
| [                ImagePosition = [ImagePositions].Right]                                                     |
|                                                                                                                                                                          |
| [            };]                                                                                                                     |
|                                                                                                                                                                          |
| [            ViewData\[[\"ButtonModel\"]\] = buttonModel;]                                                   |
|                                                                                                                                                                          |
| [            [return] View();]                                                                                  |
|                                                                                                                                                                          |
| [        }]                                                                                                                          |
|                                                                                                                                                                          |
| []                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

[] 

2.   In View, invoke the normal Button helper with the button id as the first argument followed by the view data of the **ButtonModel** class.

 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().Button([\"btnNormal\"],([ButtonModel])ViewData\[[\"ButtonModel\"]\]) [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                |
| [\@{][ ][Html.Syncfusion().Button([\"btnNormal\"],([ButtonModel])ViewData\[[\"ButtonModel\"]\]).Render();[}]] |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Run the application.

[] 

The output is shown in the following screenshot.

[] 

{border="0"} {border="0"}   {border="0"}   {border="0"}

{border="0"} {border="0"}   {border="0"}   {border="0"}

{border="0"} {border="0"}   {border="0"}   {border="0"}

{border="0"} {border="0"}

Figure 89: Normal Button Themes

 

 

 

Properties

 


+-----------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------+
| **[Name ]**[] | **[Description ]**[] | **[Type of the property]**[] | **[Data Type ]**[] | **[Value it accepts ]**[] | **[Dependency ]**[] |
+-----------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------+
| Skin                                                      | Specifies the field that provides the appearance of the button.  | Server side                                                              | Enum                                                           | [·      ]Skins.Almond                    | NA                                                              |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Blend                     |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Blueberry                 |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Marble                    |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Midnight                  |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Monochrome                |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Office2007Black           |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Office2007Blue            |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Office2007Silver          |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Olive                     |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Sandune                   |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Turquoise                 |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.Vista                     |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                |                                                                       |                                                                 |
|                                                           |                                                                  |                                                                          |                                                                | [·      ]Skins.VS2010                    |                                                                 |
+-----------------------------------------------------------+------------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------+


[] 

Sample Link

To view the samples, follow the steps below.

1.   Open the Tools sample browser from the dashboard. (Refer to the Samples and Location chapter)

2.   Navigate to Tools.Mvc -\> Button -\> Core Features Demo.

 

[]{#related-topics}

