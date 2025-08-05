---
title: popupcustomization.md
original_path: WinForms_Docs/99_Uncategorized/popupcustomization.md
created_at: 2025-08-05
---






##### Popup Customization {#popup-customization style="tab-stops: 0pt"}

[] 

Positioning the dropdown

[] 

The dropdown can be aligned with respect to the textbox, horizontally and vertically, by setting the **PopupPositionHorizontal** and **PopupPositionVertical** properties.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| PopupPositionHorizontal           | Specifies the horizontal position of the popup relative to the Text control. The options included are as follows: |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   | [·      ]Near                                                                        |
|                                   |                                                                                                                   |
|                                   | [·      ]Far                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| PopupPositionVertical             | Specifies the vertical position of the popup relative to the Text control. The options included are as follows:   |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   | [·      ]Bottom                                                                      |
|                                   |                                                                                                                   |
|                                   | [·      ]Top                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+


[] 

{border="0"}

[] 

Figure 99: Horizontal set to Far, vertical set to Top and HorizontalAlign set to Right

[] 

Displaying popup and aligning the contents

[] 

The dropdown container can be displayed by default at runtime, by enabling the **InitiallyPopupShown** property.

[] 


  --------------------- -------------------------------------------------
  Property              Description
  InitiallyPopupShown   Specifies whether to show the popup by default.
  --------------------- -------------------------------------------------


[] 

The contents of the dropdown container can aligned to one of the options of the **HorizontalAlign** property.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| HorizontalAlign                   | Specifies the alignment of the text. The default value is NotSet. The options included are as follows: |
|                                   |                                                                                                        |
|                                   | [·      ]NotSet                                                           |
|                                   |                                                                                                        |
|                                   | [·      ]Left                                                             |
|                                   |                                                                                                        |
|                                   | [·      ]Center                                                           |
|                                   |                                                                                                        |
|                                   | [·      ]Right                                                            |
|                                   |                                                                                                        |
|                                   | [·      ]Justify                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+


**[]** 

Setting popup Dimensions

**[]** 

The height and width of the dropdown can be set through the **PopupHeight** and **PopupWidth** properties respectively.

**[]** 


  ------------- -------------------------------------------
  Property      Description
  PopupHeight   Specifies the height of the popup.
  PopupWidth    Specifies the width of the popup control.
  ------------- -------------------------------------------


 

[]{#related-topics}

