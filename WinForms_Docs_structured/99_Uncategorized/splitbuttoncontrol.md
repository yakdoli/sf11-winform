---
title: splitbuttoncontrol.md
original_path: WinForms_Docs/99_Uncategorized/splitbuttoncontrol.md
created_at: 2025-08-05
---








  









## Split-Button Control {#split-button-control style="tab-stops: 0pt"}

The Split-Button control allows you to click it to perform an action and also act as a drop-down button. The Split-Button control can display both text and images. When the Split-Button is clicked, it looks as if it is being pushed in and released. When you click the right most portion of the Split-Button, it displays the drop-down items.

The text displayed on the Split-Button is contained in the **Text** property. The appearance of the button is controlled by the **Skin** property. The Split-Button control displays images using the **ImageUrl** and the **ImagePosition** properties. The drop-down button position is controlled by the **ArrowPosition** property.

 

Properties

The following table illustrates the properties of the Split-Button control.

 

+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| Name          | Description                                                           | Type of the property | Data Type      | Value it accepts                                                    | Dependency  |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| ContentType   | Specifies the field that provides the content of the button.          | Server side          | ContentTypes   | [ContentTypes].TextOnly                     | NA          |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [ContentTypes].ImageOnly                    |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [ContentTypes].TextAndImage                 |             |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| ImagePosition | Specifies the field that provides the position of the button's image. | Server side          | ImagePositions | [ImagePositions].Left                       | ContentType |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [ImagePositions].Right                      |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [ImagePositions].Top                        |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [ImagePositions].Bottom                     |             |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| Skin          | Specifies the field that provides the appearance of the button.       | Server side          | Enum           | [Skins.Almond]                              | NA          |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Blend]                               |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Blueberry]                           |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Marble]                              |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Midnight]                            |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Monochrome]                          |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Office2007Black]                     |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Office2007Blue]                      |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Office2007Silver]                    |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Olive]                               |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Sandune]                             |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Turquoise]                           |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Vista]                               |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.VS2010]                              |             |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| Height        | Defines the height of the button.                                     | Server side          | Unit           | [Unit.]Pixel(100)[] | NA          |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| Width         | Defines the width of the button.                                      | Server side          | Unit           | [Unit.]Pixel(100)[] | NA          |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+

 

More:









