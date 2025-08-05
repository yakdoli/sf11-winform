---
title: marginandshadowsettings1.md
original_path: WinForms_Docs/99_Uncategorized/marginandshadowsettings1.md
created_at: 2025-08-05
---






##### Margin and Shadow Settings {#margin-and-shadow-settings style="tab-stops: 0pt"}

[] 

Shadow Settings

[] 

Shadow for the context menu drop down is controlled using the below property.

[] 


  ------------------- ---------------------------------------------------------------
  Property            Description
  DropShadowEnabled   Shows or hides three dimensional shadow for the context menu.
  ------------------- ---------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                                          |
| []                                                                                                                                                     |
|                                                                                                                                                                                                          |
| [this][.contextMenuStripEx1.DropShadowEnabled = [true];][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1186}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [Me][.contextMenuStripEx1.DropShadowEnabled = [True]][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The below image displays a shadow for the context menu strip.

[] 

{border="0"}

[] 

Figure 1428: DropShadowEnabled = \"True\"

[] 

Margin Settings

**[]** 

We can set margins for the context menu using the below properties.

[] 


  ----------------- -----------------------------------------------------------------------
  Property          Description
  ShowCheckMargin   Shows or hides check margin on the left side of the context menu.
  ShowImageMargin   Shows or hides the image margin on the left side of the context menu.
  ImageScaling      Sets the size of images on items.
  ----------------- -----------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [this][.][contextMenuStripEx1.ShowCheckMargin = [true];]                                       |
|                                                                                                                                                                                                                                              |
| [this][.][contextMenuStripEx1.ShowImageMargin = [true];][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [Me][.][contextMenuStripEx1.ShowCheckMargin =[ True]]                                                    |
|                                                                                                                                                                                                                                                        |
| [Me][.][contextMenuStripEx1.ShowImageMargin =[ True]][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1429: ShowCheckMargin = \"True\"; ShowImageMargin = \"False\"

[] 

{border="0"}

[] 

Figure 1430: ShowCheckMargin = \"True\"; ShowImageMargin = \"True\"

**[]** 


{border="0"} Note: The check functionality can be enabled using the Checked property and check state can be provided using CheckedState property available for individual menu item, through Items Collection Editor.


 

 

 

 

[]{#related-topics}

