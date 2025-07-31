---
title: imagesettings2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\imagesettings2.md
created_at: 2025-07-03
---






##### Image Settings {#image-settings style="tab-stops: 0pt"}

[] 

Settings Images Folder

[] 

While setting images through ItemLooks, the folder name in which the images are stored should be set to **ImageBaseURL** property. The default value is \'images\'. This can be customized with the required folder name.

[] 


  ------------------ ---------------------------------------------------------------------------------------------------------------------
  ToolBar Property   Description
  ImageBaseURL       Specifies the relative path (for example, \'images/\') to the folder containing images used by the toolbar control.
  ------------------ ---------------------------------------------------------------------------------------------------------------------


**[]** 

+------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                      |
| []                                                               |
|                                                                                                      |
| [ToolBar1.ImageBaseURL = [\"pictures\"];] |
+------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                               |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [Private][ ToolBar1.ImageBaseURL = [\"pictures\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Image Settings

[] 

Image can be set for the default and hover states for an item, by setting the images to the **ImagePath** and **ImageHoverPath** properties, in the Designer dialog.

[] 

{border="0"}

[] 

Figure 267: Toolbar with Image and ImageHover settings

[] 


  ----------------------- ----------------------------------------------------------------------
  ToolBar Item Property   Description
  ImagePath               Specifies the url for the image to be displayed on the toolbar item.
  ImageHoverPath          Specifies the url for the image to be displayed on mouse hover.
  ----------------------- ----------------------------------------------------------------------


[] 

The ImagePath and ImageHoverPath properties can be set as follows through code.

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                           |
|                                                                                                                            |
| []                                                                                     |
|                                                                                                                            |
| [ToolBar1.ImagePath = [\"\~/pictures/palette2.png\"];]          |
|                                                                                                                            |
| [ToolBar1.ImageHoverPath = [\"\~/pictures/presentation.png\"];] |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                     |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Private][ ToolBar1.ImagePath = [\"\~/pictures/palette2.png\"]]          |
|                                                                                                                                                                                      |
| [Private][ ToolBar1.ImageHoverPath = [\"\~/pictures/presentation.png\"]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: To set images through ItemLooks and to customize the settings, refer [ItemLook Properties] topic.


[] 

See Also

[] 

[CSS applicable segments in ToolBar]{.UGHyperlink}[, ]{.UGHyperlink}[Appearance Mode Settings]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#related-topics}

