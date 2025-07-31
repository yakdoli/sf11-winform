---
title: backgroundimagesettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\backgroundimagesettings.md
created_at: 2025-07-03
---






##### BackgroundImage Settings {#backgroundimage-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Essential Tabs provide a set of options to customize the TabControlAdv with images.

 

The TabControlAdv can have,

[] 

[·      ]Images inside the TabItems.

[·      ]Images outside the TabBounds.

[·      ]Image as Background for the TabPage.

[] 

Images in TabItems

 

To set images to the TabItems, add an ImageListControl and populate it with the required images. Then set the ImageIndex property of the TabPage to one of the indices, to display the corresponding image to the left of the text by default.

[] 

{border="0"}

[] 

Figure 1060: TabControl with Background Image Set for the TabPage and Image Set for the TabItem

[] 

**ImageAlignmentR** of the TabControlAdv allows you to set the tab\'s text and image. By default the image appears to the left and the text appears to the right. This setting can be changed using one of the below given options.

[] 


+-----------------------------------+---------------------------------------------------------------------------------+
| TabControlAdv Property            | Description                                                                     |
+-----------------------------------+---------------------------------------------------------------------------------+
| ImageAlignmentR                   | Specifies the alignment of the image relative to the text. The options include, |
|                                   |                                                                                 |
|                                   |                                                                                 |
|                                   |                                                                                 |
|                                   | [·      ]LeftOfText,                               |
|                                   |                                                                                 |
|                                   | [·      ]RightOfText,                              |
|                                   |                                                                                 |
|                                   | [·      ]AboveText,                                |
|                                   |                                                                                 |
|                                   | [·      ]BelowText and                             |
|                                   |                                                                                 |
|                                   | [·      ]Overlap.                                  |
+-----------------------------------+---------------------------------------------------------------------------------+
| ImageIndex                        | Gets / sets the image for the tabitem.                                          |
+-----------------------------------+---------------------------------------------------------------------------------+


[] 

Code snippets showing the Image Settings

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [this][.tabControlAdv1.ImageAlignmentR = Syncfusion.Windows.Forms.Tools.[RelativeImageAlignment].RightOfText;] |
|                                                                                                                                                                                                                          |
| [this][.tabPageAdv1.ImageIndex = 0;]                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                              |
|                                                                                                                                                                                                                       |
| [Me][.tabControlAdv1.ImageAlignmentR = Syncfusion.Windows.Forms.Tools.[RelativeImageAlignment].RightOfText] |
|                                                                                                                                                                                                                       |
| [Me][.tabPageAdv1.ImageIndex = 0]                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Images outside the TabBounds

**[]** 

TabControlAdv can have images set outside the TabBounds.

[] 

[{border="0"}][]

***[]*** 

Figure 1061: TabControlAdv with Images set outside the Tab Bounds

**[]** 

To move the image outside the TabBounds, set the below given properties.

[] 


  ------------------------ -------------------------------------------------------------------
  TabControlAdv Property   Description
  ImageOffset              Adjusts Y-axis position of the image.
  AdjustTopGap             Adjusts the gap between the tabcontroladv\'s top and tabs.
  LevelTextAndImage        Indicates whether the text and image should be in the same level.
  ItemSize                 Sets the size of the tabs.
  ------------------------ -------------------------------------------------------------------


[] 

Background Image for TabPages

**[]** 

The below properties sets the background image for the pages.

[] 


+-----------------------------------+------------------------------------------------------------------------------+
| TabPageAdv Property               | Description                                                                  |
+-----------------------------------+------------------------------------------------------------------------------+
| BackgroundImage                   | Specifies the background image for the tabpage.                              |
+-----------------------------------+------------------------------------------------------------------------------+
| BackgroundImageLayout             | Specifies the layout for the background image when set. The options include: |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   | [·      ]None,                                  |
|                                   |                                                                              |
|                                   | [·      ]Tile,                                  |
|                                   |                                                                              |
|                                   | [·      ]Center,                                |
|                                   |                                                                              |
|                                   | [·      ]Stretch and                            |
|                                   |                                                                              |
|                                   | [·      ]Zoom.                                  |
+-----------------------------------+------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| **[]**                                                                                                                                         |
|                                                                                                                                                                                                  |
| [this][.tabPageAdv1.BackgroundImage = imageList1.Images\[0\];]                                              |
|                                                                                                                                                                                                  |
| [this][.tabPageAdv1.BackgroundImageLayout = System.Windows.Forms.[ImageLayout].Right;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                                              |
|                                                                                                                                                                                                       |
| [Private][ [Me].tabPageAdv1.BackgroundImage = imageList1.Images(0)]                         |
|                                                                                                                                                                                                       |
| [Private][ [Me].tabPageAdv1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Right] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

DisableInactivePageImage

**[]** 

The DisableInactivePageImage property specifies the value which determines whether the image should be disabled when the TabPage is not selected. The default value is set to True.

[] 


  -------------------------- ---------------------------------------------------------------------------------------------------------------
  TabControlAdv Property     Description
  DisableInactivePageImage   Gets / sets the value which determines whether the image should be disabled when the TabPage is not selected.
  -------------------------- ---------------------------------------------------------------------------------------------------------------


[      ]

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| **[]**                                                                                                     |
|                                                                                                                                                              |
| [this][.tabPageAdv1.DisableInactivePageImage = imageList1.Images\[0\];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| **[]**                                                                                                                               |
|                                                                                                                                                                                        |
| [Private][ [Me].tabPageAdv1.DisableInactivePageImage = imageList1.Images(0)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

