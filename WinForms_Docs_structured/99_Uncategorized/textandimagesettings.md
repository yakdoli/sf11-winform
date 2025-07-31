---
title: textandimagesettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textandimagesettings.md
created_at: 2025-07-03
---






##### Text and Image Settings {#text-and-image-settings style="tab-stops: 0pt"}

[] 

Different images can be set for a parent item, enabling to change image during item expand and collapse. These images can be set using the **CollapseImageURL** and **ExpandImageURL** properties in the Designer dialog for the respective parent items.

[] 


+-----------------------------------+----------------------------------------------------------+
|                                   |                                                          |
|                                   |                                                          |
| Property                          | Description                                              |
+-----------------------------------+----------------------------------------------------------+
| CollapseImageURL                  | Specifies path of the image to be used on item collapse. |
+-----------------------------------+----------------------------------------------------------+
| ExpandImageURL                    | Specifies path of the image to be used on item expand.   |
+-----------------------------------+----------------------------------------------------------+


[] 

The **ImageBaseUrl** allows you to specify the path from where the images have to be obtained. By default it is set to \'images\' folder. This property must be set to display the expand / collapse images.

[] 


  -------------- ---------------------------------------------------------------------
  Property       Description
  ImageBaseURL   Specifies the path where the images used in the control are stored.
  -------------- ---------------------------------------------------------------------


[] 

Image and the text position can be aligned relative to each other by specifying the **TextPosition** property which allows to set how the image and the text has to be displayed. This can be set for the entire control which enables all the items to inherit the values, else can be set for individual items by setting it in the Designer dialog.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
| TextPosition                      | Specifies the orientation of the text and image relative to each other. The options included are as follows: |
|                                   |                                                                                                              |
|                                   | [·      ]TextOverImage                                                          |
|                                   |                                                                                                              |
|                                   | [·      ]ImageOverText                                                          |
|                                   |                                                                                                              |
|                                   | [·      ]ImageLeftTextRight                                                     |
|                                   |                                                                                                              |
|                                   | [·      ]TextLeftImageRight                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+


[]{#related-topics}

