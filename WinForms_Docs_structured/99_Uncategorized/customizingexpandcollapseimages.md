---
title: customizingexpandcollapseimages.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizingexpandcollapseimages.md
created_at: 2025-07-03
---






##### Customizing Expand / Collapse Images {#customizing-expand-collapse-images style="tab-stops: 0pt"}

[] 

Default Hierarchical Lines

[] 

By default the **ShowLines** property will be set to **True**. This will display the default +/- images.

[] 

{border="0"}

**[]** 

Figure 183: TreeView with default hierarchical line images

[] 

The following are the properties that contain the default line images which can be customized.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                             |
|                                   |                                                                                                             |
|          Property                 | Description                                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| LineImageHeight                   | Specifies height of the line image.                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| LineImageDash                     | Specifies the custom images to replace the default hierarchical line images.                                |
+-----------------------------------+                                                                                                             |
| LineImageDashMinus                |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageDashPlus                 |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageEmpty                    |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageImageI                   |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageImageL                   |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageLMinus                   |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageLPlus                    |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageR                        |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageRMinus                   |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageRPlus                    |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageT                        |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageTMinus                   |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageTPlus                    |                                                                                                             |
+-----------------------------------+                                                                                                             |
| LineImageWidth                    |                                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| UseCustomLineImages               | Gets/sets the boolean value, whether to render the custom hierarchical line images. Default value is False. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+


**[]** 

Custom Hierarchical Line Images

[] 

The default hierarchical line images can be replaced with the custom or user-defined line images for which, set the **UseCustomImages** to **True** and assign the \'Lines\' folder, with the user-defined images placed in it, to **ImageBaseUrl**[ ]property. Also, make sure that **ShowLines** property is set to **True**.

[] 

{border="0"}

**[]** 

Figure 184: Treeview with the large +/- images

[] 

To set the user-defined images, set the following listed properties with the corresponding images. These properties holds default image names. The custom images can either be named accordingly or it can be renamed in which case the images has to be set with the corresponding image names.

[] 


  -------------------- --------------- --------------------------------------------
  Property             Image Name      Model Image
  LineImageDash        dash.gif        {border="0"}
  LineImageDashMinus   dashminus.gif   {border="0"}
  LineImageDashPlus    dashplus.gif    {border="0"}
  LineImageEmpty       empty.gif       {border="0"}
  LineImageI           i.gif           {border="0"}
  LineImageL           l.gif           {border="0"}
  LineImageLMinus      lminus.gif      {border="0"}
  LineImageLPlus       lplus.gif       {border="0"}
  LineImageR           r.gif           {border="0"}
  LineImageRMinus      rminus.gif      {border="0"}
  LineImageRPlus       rplus.gif       {border="0"}
  LineImageT           t.gif           {border="0"}
  LineImageTMinus      tminus.gif      {border="0"}
  LineImageTPlus       tplus.gif       {border="0"}
  -------------------- --------------- --------------------------------------------


[] 

Custom Expand / Collapse images

[] 

To avoid displaying the hierarchical lines, set the **ShowLines** to **False** and add expand and collapse images using **ExpandImageUrl** and **CollapseImageUrl**.

[] 

{border="0"}

**[]** 

Figure 185: Treeview without Showline

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][cc1][:][treeview][ [id][=\"TreeView1\"] [runat][=\"server\"] [width][=\"230px\"] [height][=\"320px\"] [EditNode][=\"False\"] [ExpandSinglePath][=\"True\"] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [CssClass][=\"TreeView \"][ ]**[ShowLines][=\"False\"][ [ExpandImageUrl][=\"exp.gif\" ][CollapseImageUrl][=\"col.gif\"] [LeafNodeImageUrl][=\"noexp.gif\"]]**[ ]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [customcss][=\"css/TreeStyle.css\"\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Additionally you can also set **LeafNodeImageUrl**. This image will get displayed on all the leaf nodes. This picture shows the usage of ExpandImageUrl, CollapseImageUrl and LeafNodeImageUrl.

[] 

{border="0"}

**[]** 

Figure 186: TreeView with leaf node images

[]{#related-topics}

