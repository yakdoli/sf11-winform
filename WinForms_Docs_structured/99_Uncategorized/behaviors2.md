---
title: behaviors2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\behaviors2.md
created_at: 2025-07-03
---






#### Behaviors {#behaviors style="tab-stops: 0pt"}

The Toggle-Button supports various behaviors such as content type and image positioning.

**ContentType** - The text and the image of a button can be customized using the **ContentType** property (TextOnly, ImageOnly, TextAndImage).

**ImagePosition** - The image of a button can be customized using the **ImagePosition** property (Left, Right, Top, and Bottom).

 

Use Case Scenarios

It allows for easy customization of the content to be displayed on the Toggle-Button.

 

Adding Behavior[ ]to an Application

 

The following steps guides you in defining the behavior of the Toggle-Button control.

Behaviors can be customized through two ways in Toggle-Button.

[·      ]Using Builder

[·      ]Using Properties Model

 

Using Builder

 

1.   In View, invoke the ToggleButton helper with the button id as the first argument followed by the button **Text** and **ImageUrl** and **ContentType** methods.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                         |
|                                                                                                                                                                                |
| [        [\<%][=]Html.Syncfusion().ToggleButton([\"btnToggle\"])] |
|                                                                                                                                                                                |
| [            .Text([\"Save\"])]                                                                                    |
|                                                                                                                                                                                |
| [            .IsChecked([true])]                                                                                      |
|                                                                                                                                                                                |
| [            .ContentType([ContentTypes].TextAndImage)]                                                            |
|                                                                                                                                                                                |
| [            .ImageUrl([\"Content/icon_save.png\"])]                                                               |
|                                                                                                                                                                                |
| [            .ImagePosition([ImagePositions].Right)]                                                               |
|                                                                                                                                                                                |
| [        [%\>]]                                                                                                |
|                                                                                                                                                                                |
| []                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                       |
|                                                                                                                                                                                |
| [        [\@{][ ]Html.Syncfusion().ToggleButton([\"btnToggle\"])] |
|                                                                                                                                                                                |
| [            .Text([\"Save\"])]                                                                                    |
|                                                                                                                                                                                |
| [            .IsChecked([true])]                                                                                      |
|                                                                                                                                                                                |
| [            .ContentType([ContentTypes].TextAndImage)]                                                            |
|                                                                                                                                                                                |
| [            .ImageUrl([\"Content/icon_save.png\"])]                                                               |
|                                                                                                                                                                                |
| [            .ImagePosition([ImagePositions].Right)]                                                               |
|                                                                                                                                                                                |
| [            .Render();]                                                                                                                   |
|                                                                                                                                                                                |
| [        [}]]                                                                                                  |
|                                                                                                                                                                                |
| []                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Run the application.

 

The output is shown in the following screenshot.

 

{border="0"} {border="0"} {border="0"}

Figure 296: Toggle-Button with various ContentType

{border="0"} {border="0"}   {border="0"}   {border="0"}

Figure 297: Toggle-Button with various Image Position

Using Properties Model

 

1.   In Controller, create an object for the **ToggleButtonModel** class and set the **Text, ImageUrl**, **ContentType**, and **ImagePosition** properties. Assign this model class to view data.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                |
|                                                                                                                                                                                                         |
| [        [public] [ActionResult] Index()]                                                                 |
|                                                                                                                                                                                                         |
| [        {]                                                                                                                                            |
|                                                                                                                                                                                                         |
| [            [ToggleButtonModel] toggleButtonModel = [new] [ToggleButtonModel]()] |
|                                                                                                                                                                                                         |
| [            {]                                                                                                                                        |
|                                                                                                                                                                                                         |
| [                Text = [\"Save\"],]                                                                                           |
|                                                                                                                                                                                                         |
| [                IsChecked = [true],]                                                                                             |
|                                                                                                                                                                                                         |
| [                ImageUrl = [\"Content/icon_save.png\"],]                                                                      |
|                                                                                                                                                                                                         |
| [                ContentType = [ContentTypes].TextAndImage,]                                                                   |
|                                                                                                                                                                                                         |
| [                ImagePosition = [ImagePositions].Right]                                                                       |
|                                                                                                                                                                                                         |
| [            };]                                                                                                                                       |
|                                                                                                                                                                                                         |
| [            ViewData\[[\"ToggleButtonModel\"]\] = toggleButtonModel;]                                                         |
|                                                                                                                                                                                                         |
| [        }]                                                                                                                                            |
|                                                                                                                                                                                                         |
| []                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In View, invoke the ToggleButton helper with the button id as the first argument followed by the view data of the **ToggleButtonModel** class.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<%][=][Html][.Syncfusion()][.ToggleButton([\"btnToggle\"],([ToggleButtonModel])ViewData\[[\"ToggleButtonModel\"]\]) [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\@{][ ][Html][.Syncfusion()][.ToggleButton([\"btnToggle\"],([ToggleButtonModel])ViewData\[[\"ToggleButtonModel\"]\]).Render();[}]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   Run the application.

 

The output is shown in the following screenshot.

 

{border="0"} {border="0"} {border="0"}

Figure 298: Toggle-Button with various ContentType

{border="0"} {border="0"}   {border="0"}   {border="0"}

Figure 299: Toggle-Button with various Image Position

Properties

 

The following table illustrates the properties which describes the behaviors of the Toggle-Button.

Table 7: Property Table

+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------+-------------+
| Name          | Description                                                           | Type of the property | Data Type      | Value it accepts          | Dependency  |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------+-------------+
| ContentType   | Specifies the field that provides the content of the button.          | Server side          | ContentTypes   | ContentTypes.TextOnly     | NA          |
|               |                                                                       |                      |                |                           |             |
|               |                                                                       |                      |                | ContentTypes.ImageOnly    |             |
|               |                                                                       |                      |                |                           |             |
|               |                                                                       |                      |                | ContentTypes.TextAndImage |             |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------+-------------+
| ImagePosition | Specifies the field that provides the position of the button's image. | Server side          | ImagePositions | ImagePositions.Left       | ContentType |
|               |                                                                       |                      |                |                           |             |
|               |                                                                       |                      |                | ImagePositions.Right      |             |
|               |                                                                       |                      |                |                           |             |
|               |                                                                       |                      |                | ImagePositions.Top        |             |
|               |                                                                       |                      |                |                           |             |
|               |                                                                       |                      |                | ImagePositions.Bottom     |             |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------+-------------+

[] 

Sample Link

To view the samples, follow the steps below.

1.   Open the **Tools** sample browser from the dashboard. (Refer to the Samples and Location chapter)

2.   Navigate to **Tools.Mvc -\> Button -\> Core Features Demo**.

 

[]{#related-topics}

