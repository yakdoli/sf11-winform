---
title: imagesettingsofgroupview.md
original_path: WinForms_Docs/99_Uncategorized/imagesettingsofgroupview.md
created_at: 2025-08-05
---






##### Image Settings of GroupView {#image-settings-of-groupview style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section describes the image options available for GroupView.

[] 

To add images to the GroupView, **ImageList** **control** must be added to the form with images. ImageList control containing large or small images can be set using the properties given below.

[] 


{border="0"} Note: If the application requirements deem that the GroupView will always display the same-sized image, then it is sufficient to assign just one ImageList. For the VS.NET toolbox interface, the GroupView will use only a single 16\*16-sized small image list.


[] 


  ---------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  GroupView Properties   Description
  LargeImageList         It contains large images (32\*32) to associate with the control.
  SmallImageView         In SmallImageView mode, the GroupView items are displayed using the small 16x16 images and are right-aligned with the text drawn alongside the image. When the SmallImageView property is set to \'False\', items are displayed using the larger 32x32 images and will be center-aligned with the text drawn below the image.
  SmallImageList         It contains small images (16\*16) to associate with the control. SmallImageView must be set to \'True\' to associate small images with the control.
  ---------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [this][.groupView1.LargeImageList = [this].imageList2;] |
|                                                                                                                                                                   |
| [this][.groupView1.SmallImageView = [true];]            |
|                                                                                                                                                                   |
| [this][.groupView1.SmallImageList = [this].imageList1;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [Me][.groupView1.LargeImageList = [Me].imageList2] |
|                                                                                                                                                              |
| [Me][.groupView1.SmallImageView = [True]]          |
|                                                                                                                                                              |
| [Me][.groupView1.SmallImageList = [Me].imageList1] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note : Setting Imagelist component to the above properties will not actually associate the images with the GroupView Item. We need to set the ImageIndex of the images to the GroupView Item through the GroupViewItems Collection editor.


[] 

{border="0"}

[] 

Figure 916: GroupView Items displaying Small Images instead of Icons

[] 

{border="0"}

[] 

Figure 917: GroupView Items displaying Large Images instead of Icons

[] 

Highlighting Images

[] 

We can highlight the image of the GroupView Item when the mouse is moved over it by setting the **HighlightImage** property to \'True\'.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [this][.groupView1.HighLightImage = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [Me][.groupView1.HighLightImage = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 918: Highlighting Images Illustrated

[] 

Image Offset Settings

[] 

The following properties are used to set the image offset for the GroupView Items.

[] 


  ------------------------------ ----------------------------------------------------------------------------------------
  GroupView Property             Description
  SelectedImageOffset            Gets / sets the image offset for the selected GroupView Item.
  SelectingImageOffset           Gets / sets the image offset for the GroupView Item being selected.
  SelectedHighlightImageOffset   Gets / sets the image offset when the mouse is moved over the selected GroupView Item.
  HighlightImageOffset           Gets / sets the image offset for the highlighted GroupView Item.
  ------------------------------ ----------------------------------------------------------------------------------------


**[]** 


{border="0"} Note: HighlightImage property must be set to \'True\' in all the cases.


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                            |
|                                                                                                                                                                                                |
| [this][.groupView1.SelectedImageOffset = [new] System.Drawing.Point(8, 8);]          |
|                                                                                                                                                                                                |
| [this][.groupView1.SelectingImageOffset = [new] System.Drawing.Point(6, 6);]         |
|                                                                                                                                                                                                |
| [this][.groupView1.HighlightImageOffset = [new] System.Drawing.Point(5, 5);]         |
|                                                                                                                                                                                                |
| [this][.groupView1.SelectedHighlightImageOffset = [new] System.Drawing.Point(5, 5);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [Me][.groupView1.SelectedImageOffset = [New] System.Drawing.Point(8, 8)]          |
|                                                                                                                                                                                             |
| [Me][.groupView1.SelectingImageOffset = [New] System.Drawing.Point(6, 6)]         |
|                                                                                                                                                                                             |
| [Me][.groupView1.HighlightImageOffset = [New] System.Drawing.Point(5, 5)]         |
|                                                                                                                                                                                             |
| [Me][.groupView1.SelectedHighlightImageOffset = [New] System.Drawing.Point(5, 5)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following table lists the methods related to the above properties.

[] 


  ----------------------------------- --------------------------------------------------------------------------
  Methods                             Description
  ResetSelectedImageOffset            Resets the SelectedImageOffset property to it\'s default value.
  ResetSelectingImageOffset           Resets the SelectingImageOffset property to it\'s default value.
  ResetSelectedHighlightImageOffset   Resets the SelectedHighlightImageOffset property to it\'s default value.
  ResetHighlightImageOffset           Resets the HighlightImageOffset property to it\'s default value.
  ----------------------------------- --------------------------------------------------------------------------


[] 

Image Spacing

[] 

We can provide spacing between the highlighted edge of a GroupView Item and the image by setting the **ImageSpacing** property to integer values.

 

**HighlightImage** property must be set to \'True\'.

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                             |
|                                                                                                                            |
| []                                                                       |
|                                                                                                                            |
| [this][.groupView1.ImageSpacing = 7;] |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                      |
|                                                                                                                         |
| []                                                                    |
|                                                                                                                         |
| [Me][.groupView1.ImageSpacing = 7] |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 919: GroupView with ImageSpacing = \"7\"

 

 

[]{#p648} 

 

[]{#related-topics}

