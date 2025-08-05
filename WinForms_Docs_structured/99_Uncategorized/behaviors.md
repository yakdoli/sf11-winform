---
title: behaviors.md
original_path: WinForms_Docs/99_Uncategorized/behaviors.md
created_at: 2025-08-05
---






#### Behaviors {#behaviors style="tab-stops: 0pt"}

The Button supports various behaviors such as content type and image positioning.

**ContentType** - The text and the image of a button can be customized using the **ContentType** property (TextOnly, ImageOnly, TextAndImage).

**ImagePosition** - The image of a button can be customized using the **ImagePosition** property (Left, Right, Top, and Bottom).

 

Use Case Scenarios

The Button control allows for easy customization of the content to be displayed on the button.

 

Adding Behavior[ ]to an Application

The following steps guide you in defining the behavior of the Button control.

Behaviors can be customized through two ways in button.

1.   Using Builder

2.   Using Properties Model

 

Using Builder

 

1.   In View, invoke the normal Button helper with the button id as the first argument followed by the button **Text** and **ImageUrl** and **ContentType** methods.

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                   |
|                                                                                                                                                                          |
| [        [\<%][=]Html.Syncfusion().Button([\"btnNormal\"])] |
|                                                                                                                                                                          |
| [        .Text([\"Save\"])]                                                                                  |
|                                                                                                                                                                          |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                             |
|                                                                                                                                                                          |
| [        .ContentType([ContentTypes].TextAndImage)]                                                          |
|                                                                                                                                                                          |
| [        .ImagePosition([ImagePositions].Right)    ]                                                         |
|                                                                                                                                                                          |
| [        [%\>]]                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                 |
|                                                                                                                                                                          |
| [        [\@{][ ]Html.Syncfusion().Button([\"btnNormal\"])] |
|                                                                                                                                                                          |
| [        .Text([\"Save\"])]                                                                                  |
|                                                                                                                                                                          |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                             |
|                                                                                                                                                                          |
| [        .ContentType([ContentTypes].TextAndImage)]                                                          |
|                                                                                                                                                                          |
| [        .ImagePosition([ImagePositions].Right)    ]                                                         |
|                                                                                                                                                                          |
| [        [%}]]                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   Run the application.

[] 

The output is shown in the following screenshot.

[] 

 

{border="0"} {border="0"} {border="0"}

Figure 84: Normal Button with various Content Type

{border="0"} {border="0"}   {border="0"}   {border="0"}

Figure 85: Normal Button with various Image Position

 

Using Properties Model

[] 

1.   In Controller, create an object for the **ButtonModel** class and set the **Text**, **ImageUrl,** **ContentType**, and **ImagePosition** properties. Assign this model class to view data.

 

 

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
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[] 

 

2.   In View, invoke the normal Button helper with the button id as the first argument followed by the view data of the **ButtonModel** class.

 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().Button([\"btnNormal\"],([ButtonModel])ViewData\[[\"ButtonModel\"]\]) [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| [\@{][Html.Syncfusion().Button([\"btnNormal\"], ([ButtonModel])ViewData\[[\"ButtonModel\"]\]).Render();[}]] |
|                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

[] 

3.   Run the application.

[] 

The output is shown in the following screenshot.

[] 

{border="0"} {border="0"} {border="0"}

Figure 86: Normal Button with various Content Type

{border="0"} {border="0"}   {border="0"}   {border="0"}

Figure 87: Normal Button with various Image Position

 

Properties

 

+---------------+-----------------------------------------------------------------------+----------------------+----------------+-----------------------------------------------------+-------------+
| Name          | Description                                                           | Type of the property | Data Type      | Value it accepts                                    | Dependency  |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+-----------------------------------------------------+-------------+
| ContentType   | Specifies the field that provides the content of the button.          | Server side          | ContentTypes   | [ContentTypes].TextOnly     | NA          |
|               |                                                                       |                      |                |                                                     |             |
|               |                                                                       |                      |                | [ContentTypes].ImageOnly    |             |
|               |                                                                       |                      |                |                                                     |             |
|               |                                                                       |                      |                | [ContentTypes].TextAndImage |             |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+-----------------------------------------------------+-------------+
| ImagePosition | Specifies the field that provides the position of the button's image. | Server side          | ImagePositions | [ImagePositions].Left       | ContentType |
|               |                                                                       |                      |                |                                                     |             |
|               |                                                                       |                      |                | [ImagePositions].Right      |             |
|               |                                                                       |                      |                |                                                     |             |
|               |                                                                       |                      |                | [ImagePositions].Top        |             |
|               |                                                                       |                      |                |                                                     |             |
|               |                                                                       |                      |                | [ImagePositions].Bottom     |             |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+-----------------------------------------------------+-------------+

[] 

Sample Link

To view the samples, follow the steps below.

1.   Open the Tools Sample Browser from the dashboard. (Refer to the [Samples and Location]{.UGHyperlink} chapter)

2.   Navigate to **Tools.Mvc -\> Button -\> Core Features Demo**.

 

[]{#related-topics}

