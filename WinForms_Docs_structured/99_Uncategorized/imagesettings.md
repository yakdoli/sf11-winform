---
title: imagesettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\imagesettings.md
created_at: 2025-07-03
---






##### Image Settings {#image-settings style="tab-stops: 0pt"}

 

[] 

Images can be easily set for the control, with left and right images for nodes and various states like default and hover, which can also be customized for individual nodes as required.

[] 


{border="0"}Note: Make sure to set the ImageBaseUrl property while setting the images.


[] 

The ImageBaseUrl allows you to specify the path from where the images have to be obtained. By default it is set to \'images\' folder. You can either create a folder called \'images\' in your application, and add all the images to be set through editor dialog or using the item looks. Else use a custom folder and rename the ImageBaseUrl property.

[] 


  ------------------- -------------------------------------------------------------------------------
  TreeView Property   Description
  ImageBaseUrl        Specifies the relative path where the images used for the control are stored.
  ------------------- -------------------------------------------------------------------------------


[] 

Programmatically the images can be set as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                    |
|                                                                                                                     |
| []                                                 |
|                                                                                                                     |
| [TreeView1.ImageBaseURL = [\"images\"];] |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                              |
|                                                                                                                                                                                               |
| []                                                                                                                           |
|                                                                                                                                                                                               |
| [Private][ TreeView1.ImageBaseURL = [\"images\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Expand / Collapse and Leaf node image Settings

[] 

{border="0"}

**[]** 

Figure 179: TreeView with expand, collapse and leaf node images

[] 

Node images of parent nodes can be changed during node expand and collapse actions using the **ExpandImageUrl** and **CollaspeImageUrl** properties. Set these properties to the respective images. This will set the corresponding images to the parent nodes during the expand and collapse actions.

 

A single image can be applied to all the leaf nodes by assigning the image name to the **LeafNodeImageUrl** property.

[] 


  ------------------- --------------------------------------------------
  TreeView Property   Description
  CollapseImageUrl    Specifies the image to be used on node collapse.
  ExpandImageUrl      Specifies the image to be used on node expand.
  LeftNodeImageUrl    Specifies the images used in the leaf nodes.
  ------------------- --------------------------------------------------


[] 

Programmatically the images can be set as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                                 |
| []                                                             |
|                                                                                                                                 |
| [TreeView1.ExpandImageUrl = [\"image name.ext\"];]   |
|                                                                                                                                 |
| [TreeView1.CollapseImageUrl = [\"image name.ext\"];] |
|                                                                                                                                 |
| [TreeView1.LeafNodeImageUrl = [\"image name.ext\"];] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                                           |
| [Private][ TreeView1.ExpandImageUrl = [\"image name.ext\"]]   |
|                                                                                                                                                                                                           |
| [Private][ TreeView1.CollapseImageUrl = [\"image name.ext\"]] |
|                                                                                                                                                                                                           |
| [Private][ TreeView1.LeafNodeImageUrl = [\"image name.ext\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Setting images for items through TreeView Designer dialog

[] 

{border="0"}

[] 

TreeView with right image and hover settings

[] 

The left and right images for a tree item can be set directly by setting the image name to the **ImagePath** property for the left image and **RightImagePath** for the right image. Similarly if you want to change the images or the back color of the image during mouse hover, set those images to the **ImageHoverPath** for the left image and **RightImageHoverPath** for the right image.

[] 


  --------------------- ------------------------------------------------------
  Item Property         Description
  ImageHoverPath        Specifies the left image to be used on hover state.
  ImagePath             Specifies the left image to be used for a node.
  RightImageHoverPath   Specifies the right image to be used on hover state.
  RightImagePath        Specifies the right image to be used for a node.
  --------------------- ------------------------------------------------------


[] 

Programmatically the images can be set as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                            |
|                                                                                                                             |
| []                                                         |
|                                                                                                                             |
| [Node1.ImageHoverPath = [\"folders.gif\"];]      |
|                                                                                                                             |
| [Node1.ImagePath = [\"download.png\"];]          |
|                                                                                                                             |
| [Node1.RightImageHoverPath = [\"folders.gif\"];] |
|                                                                                                                             |
| [Node1.RightImagePath = [\"download.png\"];]     |
+-----------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                                           |
| [Private][ TreeView1.ImageBaseURL = [\"images\"]]             |
|                                                                                                                                                                                                           |
| [Private][ TreeView1.ExpandImageUrl = [\"image name.ext\"]]   |
|                                                                                                                                                                                                           |
| [Private][ TreeView1.CollapseImageUrl = [\"image name.ext\"]] |
|                                                                                                                                                                                                           |
| [Private][ TreeView1.LeafNodeImageUrl = [\"image name.ext\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Setting images for items through item looks

[] 

{border="0"}

Figure 180

 

[] 

The left and right images can be set for an item through ItemLooks, by setting the **LeftImageUrl** and **RightImageUrl** properties to the images respectively.

[] 


  ------------------- ----------------------------------------------------------------
  ItemLook Property   Description
  LeftImageUrl        Specifies the path of the left image to be used for the node.
  RightImageUrl       Specifies the path of the right image to be used for the node.
  ------------------- ----------------------------------------------------------------


 

[]{#related-topics}

