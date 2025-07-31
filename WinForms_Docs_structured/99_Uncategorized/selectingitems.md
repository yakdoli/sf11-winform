---
title: selectingitems.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\selectingitems.md
created_at: 2025-07-03
---






#### Selecting Items {#selecting-items style="tab-stops: 0pt"}

 

You can select multiple items in a Gallery control by enabling the **AllowMultiSelect** property. If this property is set to false, you will not be able to select multiple items in the control.

 

Use the following lines of code to enable this property.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<!\--][ Adding Gallery ][\--\>]                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion:Gallery][ ][Name][=][\"[gallery]\"[ ][AllowMultiSelect][=]\"[True]\"[\>]]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \<!\--][ Adding GalleryGroup ][\--\>]                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \<][syncfusion:GalleryGroup][ ][Name][=][\"[galleryGroup]\"[ ][Header][=]\"[Photos]\"[\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<!\--][ Adding GalleryItems ][\--\>]                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:GalleryItem][\>]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      \<][Image][ ][Source][=][\"[hr.jpg]\"[/\>]]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \</][syncfusion:GalleryItem][\>]                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:GalleryItem][\>]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      \<][Image][ ][Source][=][\"[emp5.jpg]\"[/\>]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \</][syncfusion:GalleryItem][\>]                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:GalleryItem][\>]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      \<][Image][ ][Source][=][\"[emp2.jpg]\"[/\>]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \</][syncfusion:GalleryItem][\>]                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:GalleryItem][\>]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [      \<][Image][ ][Source][=][\"[emp6.jpg]\"[/\>]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \</][syncfusion:GalleryItem][\>]                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \</][syncfusion:GalleryGroup][\>]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][syncfusion:Gallery][\>]                                                                                                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                  |
|                                                                                                                 |
| []                                             |
|                                                                                                                 |
| [//Allow multiple selection]                  |
|                                                                                                                 |
| [gallery.AllowMultiSelect = [true];  ] |
+-----------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 498: AllowMultiSelect = \"True\"

[] 

Select All

 

You can select all elements of the entire Gallery control using the following lines of code.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                                             |
| [foreach][ (GalleryGroup fgg [in] gallery.Items)] |
|                                                                                                                                                                                             |
| [foreach][ (GalleryItem fgi [in] fgg.Items)]      |
|                                                                                                                                                                                             |
| [fgg.SelectedItems.Add(fgi);]                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 499: Gallery Control with All Items Selected

*[]* 

Select All Items in Group

 

You can also select all the items in a particular group of a Gallery control using the below code snippet.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [foreach][ (GalleryItem fgi [in] gallery.SelectedGroupItem.Items)] |
|                                                                                                                                                                                                              |
| [{]                                                                                                                                                      |
|                                                                                                                                                                                                              |
| [gallery.SelectedGroupItem.SelectedItems.Add(fgi);]                                                                                                      |
|                                                                                                                                                                                                              |
| [}]                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p291} 

[]{#related-topics}

