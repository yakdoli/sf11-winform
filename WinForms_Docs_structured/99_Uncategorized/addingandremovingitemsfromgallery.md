---
title: addingandremovingitemsfromgallery.md
original_path: WinForms_Docs/99_Uncategorized/addingandremovingitemsfromgallery.md
created_at: 2025-08-05
---








  









### Adding and Removing Items from Gallery {#adding-and-removing-items-from-gallery style="tab-stops: 0pt"}

 

This topic discusses how to add different items to the Gallery and remove the items from it.

 

Adding Gallery Group to Gallery

 

You can easily add any number of groups to a Gallery control using the Add method of the control. Here is the code snippet.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [GalleryGroup][ galleryGroup = [new] [GalleryGroup]();] |
|                                                                                                                                                                                                                              |
| [gallery.Items.Add(galleryGroup);]                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Adding Gallery Item to Gallery Group

 

You can add any number of items to a GalleryGroup, by calling Add method. Here is the code snippet.

 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                            |
|                                                                                                                           |
| []                                                      |
|                                                                                                                           |
| [GalleryItem galleryItem = [new] GalleryItem();] |
|                                                                                                                           |
| [galleryGroup.Items.Add(galleryItem);]                                |
+---------------------------------------------------------------------------------------------------------------------------+

[] 

Removing Selected Gallery Item from Gallery

 

You can remove a selected Gallery Item from a Gallery control, by calling the Remove method as follows.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [GalleryItem][ galleryItem = [new] [GalleryItem]();] |
|                                                                                                                                                                                                                           |
| [galleryGroup.Items.Remove(galleryItem);]                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Removing Selected Gallery Group from Gallery

 

You can remove a selected Gallery Group from a Gallery control, by calling the Remove method as follows.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                    |
|                                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                                   |
| [if][ (gallery.SelectedItem != [null])] |
|                                                                                                                                                                                   |
| [gallery.Items.Remove(galleryGroup);]                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Removing Selected Gallery Item from Gallery Group

 

You can also remove the selected Gallery Item from a Gallery Group. Here is the code snippet for selecting the Gallery Item.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                                           |
| [if][ (galleryGroup != [null])] |
|                                                                                                                                                                           |
| [galleryGroup.SelectedItems.Remove(galleryItem);]                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p296} 

[]{#related-topics}

