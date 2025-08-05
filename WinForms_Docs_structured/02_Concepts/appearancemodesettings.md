---
title: appearancemodesettings.md
original_path: WinForms_Docs/02_Concepts/appearancemodesettings.md
created_at: 2025-08-05
---






##### Appearance Mode Settings {#appearance-mode-settings style="tab-stops: 0pt"}

[] 

Appearance Mode

[] 

The **AppearanceMode** property defines the ability to customize the buttons displayed in the toolbar. Every button on the toolbar can be customized independently to display either text or image or both.

 

This property can be set for the control, enabling all the items to inherit the value, else can be set for individual items using the Toolbar Designer dialog.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| AppearanceMode                    | Specifies to either display text, image or both on toolbar items. The options included are as follows: |
|                                   |                                                                                                        |
|                                   | [·      ]ImageOnly                                                        |
|                                   |                                                                                                        |
|                                   | [·      ]Text                                                             |
|                                   |                                                                                                        |
|                                   | [·      ]ImageandText                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                                 |
| []                                                                          |
|                                                                                                                                 |
| [ToolBar1.AppearanceMode = [AppearanceMode].TextOnly;] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                   |
|                                                                                                                                                                                    |
| []                                                                                                                |
|                                                                                                                                                                                    |
| [Private][ ToolBar1.AppearanceMode = AppearanceMode.TextOnly] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The options to set the appearance mode of the toolbar items are as follows.

[] 

ImageOnly

[] 

This option displays only the image on toolbar items.

[] 

{border="0"}

**[]** 

Figure 258: ImageOnly set for the toolbar items

**[]** 

ImageAndText

[] 

This option displays both the image and the text for a toolbar item. The image and text can be customized to be displayed using the following properties.

[] 

[·      ]ImageOverText

[·      ]TextOverImage

[·      ]TextLeftImageRight

[·      ]ImageLeftTextRight

*[]* 

{border="0"}

**[]** 

Figure 259: ImageAndText set for the toolbar items

[] 

Text

[] 

This option displays only the text on the toolbar items.

[] 

{border="0"}

**[]** 

Figure 260:TextOnly set for the toolbar items

[] 

Text and Image Position Settings

[] 

The image and text can be arranged respective to each other by setting the **TextPosition** property. This property can be set for the control, enabling all the items to inherit the value, else can be set for individual items using the Toolbar Designer dialog.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------+
|                                   |                                                                                     |
|                                   |                                                                                     |
| Property                          | Description                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------+
| TextPosition                      | Specifies the text position for toolbar items. The options included are as follows: |
|                                   |                                                                                     |
|                                   | [·      ]ImageOverText                                 |
|                                   |                                                                                     |
|                                   | [·      ]TextOverImage                                 |
|                                   |                                                                                     |
|                                   | [·      ]TextLeftImageRight                            |
|                                   |                                                                                     |
|                                   | [·      ]ImageLeftTextRight                            |
+-----------------------------------+-------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                  |
| []                                                                           |
|                                                                                                                                  |
| [ToolBar1.TextPosition = [TextPosition].TextOverImage;] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                    |
|                                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                                     |
| [Private][ ToolBar1.TextPosition = TextPosition.TextOverImage] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Appearance Settings

[] 

A toolbar item can be disabled by setting the **Disabled** property. By doing so, the item will be impervious to the user actions.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
| ToolBar Item Property             | Description                                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Disabled                          | Gets/sets the boolean value, whether to disable a toolbar item. When set to true, it does not respond to user actions. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+


[] 

Programmatically when the item is created the disabled property can be set as follows.

[] 

+-----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                    |
|                                                                                                     |
| []                                              |
|                                                                                                     |
| [item.Disabled = [false];] |
+-----------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                              |
|                                                                                                                                                                               |
| []                                                                                                           |
|                                                                                                                                                                               |
| [Private][ item.Disabled = [False]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: The disabled item\'s appearance can be customized using ItemLooks. To know more about the look settings, refer [ItemLook Properties]{.UGHyperlink}[ ]topic.


[] 

See Also

[] 

[CSS applicable segments in ToolBar]{.UGHyperlink}[, ]{.UGHyperlink}[Image Settings]{.UGHyperlink}[, ]{.UGHyperlink}[Behavior Settings]{.UGHyperlink}[, ]{.UGHyperlink}[Button Type Settings]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

