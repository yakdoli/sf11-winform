---
title: typesoforientation.md
original_path: WinForms_Docs/99_Uncategorized/typesoforientation.md
created_at: 2025-08-05
---






##### Types of Orientation {#types-of-orientation style="tab-stops: 0pt"}

[] 

The TabStrip enables you to render tab elements and text in different orientations.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ImageAndTextPosition              | Specifies the orientation of text and the image in an item. Default value is ImageOverText. The options included are as follows: |
|                                   |                                                                                                                                  |
|                                   | [·      ]ImageOverText                                                                              |
|                                   |                                                                                                                                  |
|                                   | [·      ]TextOverImage                                                                              |
|                                   |                                                                                                                                  |
|                                   | [·      ]ImageLeftTextRight                                                                         |
|                                   |                                                                                                                                  |
|                                   | [·      ]TextLeftImageRight                                                                         |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| TextAlign                         | Specifies the alignment of text. The options included are as follows:                                                            |
|                                   |                                                                                                                                  |
|                                   | [·      ]Left                                                                                       |
|                                   |                                                                                                                                  |
|                                   | [·      ]Right                                                                                      |
|                                   |                                                                                                                                  |
|                                   | [·      ]Center                                                                                     |
|                                   |                                                                                                                                  |
|                                   | [·      ]Justify                                                                                    |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+


[] 

ChildItemsPosition

[] 

The **ChildItemsPosition** specifies the relative positioning of the child elements to the parent. There are four types of orientation which are as follows.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ChildItemsPosition                | Specifies the position of child item relative to the parent. Default value is Bottom. The options included are as follows: |
|                                   |                                                                                                                            |
|                                   | [·      ]Bottom                                                                               |
|                                   |                                                                                                                            |
|                                   | [·      ]Top                                                                                  |
|                                   |                                                                                                                            |
|                                   | [·      ]Left                                                                                 |
|                                   |                                                                                                                            |
|                                   | [·      ]Right                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+


[] 


  ------------------------- ------------------------------------------------------------------------
  ChildItemsPosition Type   Description
  Bottom                    The child elements will be displayed at the bottom of the parent node.
  Top                       The child elements will be displayed on top of the parent node.
  Left                      The child elements will be displayed to the left of the parent node.
  Right                     The child elements will be displayed to the right of the parent node.
  ------------------------- ------------------------------------------------------------------------


[] 

ChidLayout

[] 

The **ChildLayout** specifies the orientation of child elements. There are two types of tab orientation which are as follows.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| ChildLayout                       | Specifies the layout of child items. Default value is Horizontal. The options included are as follows: |
|                                   |                                                                                                        |
|                                   | [·      ]Horizontal                                                       |
|                                   |                                                                                                        |
|                                   | [·      ]Vertical                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+


[] 


  ------------------ ----------------------------------------------------
  ChildLayout Type   Description
  Horizontal         The child elements will be displayed horizontally.
  Vertical           The child elements will be displayed vertically.
  ------------------ ----------------------------------------------------


[] 

TabLayout

[] 

This property setting specifies the relative positioning of the different rows in a multi-level tab. There are four types of orientation which are as follows.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| TabLayout                         | Specifies the layout of the tab elements. Default value is Horizontal. The options included are as follows: |
|                                   |                                                                                                             |
|                                   | [·      ]Horizontal                                                            |
|                                   |                                                                                                             |
|                                   | [·      ]Vertical                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+


[] 


  ---------------- -------------------------------------------------------
  TabLayout Type   Description
  Horizontal       The root tab elements will be displayed horizontally.
  Vertical         The root tab elements will be displayed vertically.
  ---------------- -------------------------------------------------------


[] 

TextLayout

[] 

The **TextLayout** specifies the alignment of content within tab elements. There are four types of text orientation which are as follows.

[] 


+-----------------------------------+--------------------------------------------------------------------+
| Property                          | Description                                                        |
+-----------------------------------+--------------------------------------------------------------------+
| TextLayout                        | Specifies the layout of text. The options included are as follows: |
|                                   |                                                                    |
|                                   | [·      ]Horizontal                   |
|                                   |                                                                    |
|                                   | [·      ]Vertical                     |
|                                   |                                                                    |
|                                   | [·      ]LeftToRight                  |
|                                   |                                                                    |
|                                   | [·      ]RightToLeft                  |
+-----------------------------------+--------------------------------------------------------------------+


[] 


+-----------------------------------+------------------------------------------------+
| TextLayout Type                   | Description                                    |
+-----------------------------------+------------------------------------------------+
| Horizontal                        | The text will be displayed horizontally.       |
+-----------------------------------+------------------------------------------------+
| Vertical                          | The                                            |
|                                   |                                                |
|                                   | text will be displayed vertically.             |
+-----------------------------------+------------------------------------------------+
| LeftToRight                       | The text will be displayed from left to right. |
+-----------------------------------+------------------------------------------------+
| RightToLeft                       | The text will be displayed from right to left. |
+-----------------------------------+------------------------------------------------+


[] 

Here are some example settings with screen shots on how they affect the tab rendering.

[] 


  ------------ ------------- ------------------- ------------- --------------------------------------------
  TabLayout    TextLayout    ChildItemPosition   ChildLayout   Example
  Horizontal   Horizontal    Bottom              Horizontal    {border="0"}
  Horizontal   RightToLeft   Bottom              Horizontal    {border="0"}
  Horizontal   Vertical      Bottom              Horizontal    {border="0"}
  Vertical     Horizontal    Right               Vertical      {border="0"}
  Vertical     Vertical      Right               Vertical      {border="0"}
  Vertical     LeftToRight   Right               Vertical      {border="0"}
  ------------ ------------- ------------------- ------------- --------------------------------------------


 

[]{#related-topics}

