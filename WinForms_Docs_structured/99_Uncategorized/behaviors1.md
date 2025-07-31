---
title: behaviors1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\behaviors1.md
created_at: 2025-07-03
---






#### Behaviors {#behaviors style="tab-stops: 0pt"}

The Split-Button supports various behaviors such as content type and image positioning.

**ContentType**: - The text and image of a button can be customized using the **ContentType** property(TextOnly, ImageOnly, TextAndImage).

**ImagePosition**: - the image of a button can be customized using the **ImagePosition** property (Left, Right, Top, and Bottom).

**ArrowPosition**: - The arrow of a split button can be customized using the **ArrowPosition** property (Right and Bottom).

 

Use Case Scenarios

The Split-Button control allows for easy customization of the content to be displayed on the Split-Button.

 

Adding Behavior[ ]to an Application

The following steps guides you in defining the behavior of the Split-Button control.

The behaviors can be customized by two ways in the Split-Button.

[·      ]Using Builder

[·      ]Using Properties Model

 

Using Builder

 

1.   In View, invoke the SplitButton helper with the button id as the first argument followed by the button **Text**, **ImageUrl** and **ContentType** methods. Set the **DataSource** and **BindTo** properties.

 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [        [\<%][=]Html.Syncfusion().SplitButton([\"btnSplit\"])]                                  |
|                                                                                                                                                                                                               |
| [            .Text([\"Save\"])]                                                                                                                   |
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
| [        [%\>]]                                                                                                                               |
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
| [        [}]]                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

2.   Run the application.

 

The output is shown in the following screenshot.

 

{border="0"}          {border="0"} {border="0"}

Figure 243: Split Button with various ContentType

{border="0"}          {border="0"}   {border="0"}   {border="0"}

Figure 244: Split Button with various Image Position

{border="0"}          {border="0"}

Figure 245: Split Button with various Arrow Position

Using Properties Model

1.   In Controller, create an object for the SplitButtonModel class and set the **Text**, **ImageUrl**, **ContentType**, **ArrowPosition**, and **ImagePosition** properties. Assign this model class to view data.

 

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
| [                Skin = [Skins].Almond,]                                                                                                                                                                          |
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
| [        }]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In View, invoke the normal SplitButton helper with the button id as the first argument followed by the view data of the **SplitButtonModel** class.

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

[] 

The output is shown in the following screenshot.

 

{border="0"}          {border="0"} {border="0"}

Figure 246: Split Button with various ContentType

{border="0"}          {border="0"}   {border="0"}   {border="0"}

Figure 247: Split Button with various Image Position

{border="0"}          {border="0"}

Figure 248: Split Button with various Arrow Position

Properties

The following table illustrates the properties which describes the behaviors of the split button.

 

+---------------+-------------------------------------------------------------------------+----------------------+-----------+-----------------------------------------------------+-------------+
| Name          | Description                                                             | Type of the property | Data Type | Value it accepts                                    | Dependency  |
+---------------+-------------------------------------------------------------------------+----------------------+-----------+-----------------------------------------------------+-------------+
| ContentType   | Specifies the field that provides the content of the button.            | Server side          | Enum      | [ContentTypes].TextOnly     | NA          |
|               |                                                                         |                      |           |                                                     |             |
|               |                                                                         |                      |           | [ContentTypes].ImageOnly    |             |
|               |                                                                         |                      |           |                                                     |             |
|               |                                                                         |                      |           | [ContentTypes].TextAndImage |             |
+---------------+-------------------------------------------------------------------------+----------------------+-----------+-----------------------------------------------------+-------------+
| ImagePosition | Specifies the field that provides the position of the button's image.   | Server side          | Enum      | [ImagePositions].Left       | ContentType |
|               |                                                                         |                      |           |                                                     |             |
|               |                                                                         |                      |           | [ImagePositions].Right      |             |
|               |                                                                         |                      |           |                                                     |             |
|               |                                                                         |                      |           | [ImagePositions].Top        |             |
|               |                                                                         |                      |           |                                                     |             |
|               |                                                                         |                      |           | [ImagePositions].Bottom     |             |
+---------------+-------------------------------------------------------------------------+----------------------+-----------+-----------------------------------------------------+-------------+
| ArrowPosition | Specifies the field that provides the position of the drop-down button. | Server side          | Enum      | [ArrowPositions].Right      | NA          |
|               |                                                                         |                      |           |                                                     |             |
|               |                                                                         |                      |           | [ArrowPositions].Bottom     |             |
+---------------+-------------------------------------------------------------------------+----------------------+-----------+-----------------------------------------------------+-------------+

[] 

Sample Link

To view the samples, follow the steps below:

1.   Open the Tools Sample Browser from the Dashboard. (Refer to the Samples and Location chapter)

2.   Navigate to **Tools.Mvc -\> Button -\> Core Features Demo**.

 

[]{#related-topics}

