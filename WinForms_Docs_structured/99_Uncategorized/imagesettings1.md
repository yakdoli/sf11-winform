---
title: imagesettings1.md
original_path: WinForms_Docs/99_Uncategorized/imagesettings1.md
created_at: 2025-08-05
---






##### Image Settings {#image-settings style="tab-stops: 0pt"}

[] 

Check image

[] 

The **Checked** property when set displays a check mark to the left of the text. This property can be individually set for the items in the designer dialog.

 

The check image can be customized by assigning the image to the **ImageCheck** property. This replaces the default image with the custom image.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                              |
|                                   |                                                                                                              |
| Property                          | Description                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
| Checked                           | Gets / sets the boolean value, whether a checkmark image should be shown by default. Default value is False. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
| ImageCheck                        | Path of the check image to be used.                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+


[] 

Arrow image

[] 

The arrows which appears to the right of the text will be displayed for parent menu items by default. This arrow image can be customized by assigning the image to be used to the **ImageArrow** property.

[] 


+-----------------------------------+---------------------------------------+
|                                   |                                       |
|                                   |                                       |
| Menu Property                     | Description                           |
+-----------------------------------+---------------------------------------+
| ImageArrow                        | Specifies the arrow image to be used. |
+-----------------------------------+---------------------------------------+


[] 

{border="0"}

**[]** 

Figure 217: Menu with custom Check and Arrow images

[] 

Image Settings

[] 

The **ImageBaseUrl** allows you to specify the path from where the images have to be obtained. By default it is set to \'images\' folder.

 

**ImagePath** can be used to set the left image for an item. **ImageHoverPath** can be used to set the image during mouse over action for an item. Both these properties should be set for individual items in the Designer dialog. 

 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                |
|                                   |                                                                                                                |
|          Item Property            | Description                                                                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| ImageBaseURL                      | Specifies the relative path of the folder containing images used by the menu control. Default value is Images. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| ImageHoverPath                    | Specifies the path of the image to be used for an item, in hover state.                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+
| ImagePath                         | Specifies the path of the image to be used for an item.                                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------+


[] 

Setting Left and Right images through ItemLooks

[] 

The left and right images can be set for an item through ItemLooks, by setting the **LeftImageUrl** and **RightImageUrl** properties to the images respectively.

[] 


+-----------------------------------+----------------------------------------------------------------+
|                                   |                                                                |
|                                   |                                                                |
| ItemLook Property                 | Description                                                    |
+-----------------------------------+----------------------------------------------------------------+
| LeftImageUrl                      | Specifies the path of the left image to be used for the node.  |
+-----------------------------------+----------------------------------------------------------------+
| RightImageUrl                     | Specifies the path of the right image to be used for the node. |
+-----------------------------------+----------------------------------------------------------------+


 

[]{#related-topics}

