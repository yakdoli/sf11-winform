---
title: popupsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\popupsettings.md
created_at: 2025-07-03
---






##### Pop-up Settings {#pop-up-settings style="tab-stops: 0pt"}

 

This section provides information on the Pop-up Settings of the MultiSelectionDropDown control. It includes the following topics.

 

###### 5.1.8.2.5.1 Pop-up Settings {#pop-up-settings-1 style="tab-stops: 0pt"}

[] 

Positioning the DropDown

**[]** 

The dropdown can be aligned with respect to the textbox, horizontally and vertically, by setting the **PopupPositionHorizontal** and **PopupPositionVertical** properties.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| PopupPositionHorizontal           | Specifies the horizontal position of the popup relative to the Text control. The options included are as follows: |
|                                   |                                                                                                                   |
|                                   | [·      ]Near                                                                        |
|                                   |                                                                                                                   |
|                                   | [·      ]Far                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| PopupPositionVertical             | Specifies the vertical position of the popup relative to the Text control. The options included are as follows:   |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   | *Bottom*                                                                                                          |
|                                   |                                                                                                                   |
|                                   | *Top*                                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+


[] 

[{border="0"}][]

[] 

Figure 130: Horizontal set to Far, Vertical set to Top and HorizontalAlign set to Left

[] 

Displaying Popup and Aligning the Contents

[] 

The dropdown container can be displayed by default at runtime, by enabling the **InitiallyPopupShown** property.

[] 


  --------------------- -------------------------------------------------
  Property              Description
  InitiallyPopupShown   Specifies whether to show the popup by default.
  --------------------- -------------------------------------------------


[] 

The contents of the dropdown container can be aligned using the options provided by the **HorizontalAlign** property.

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


 

###### 5.1.8.2.5.2 Setting Popup Dimensions {#setting-popup-dimensions style="tab-stops: 0pt"}

[] 

The height and width of the dropdown can be set through the **PopupHeight** and **PopupWidth** properties respectively.

[] 


  -------------------------- --------------------------------------------
           Property          Description
  PopupHeight                Specifies the height of the popup control.
  PopupWidth                 Specifies the width of the popup control.
  -------------------------- --------------------------------------------


[]{#p214} 

[]{#related-topics}

