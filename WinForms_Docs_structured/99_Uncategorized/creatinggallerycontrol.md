---
title: creatinggallerycontrol.md
original_path: WinForms_Docs/99_Uncategorized/creatinggallerycontrol.md
created_at: 2025-08-05
---








  









### Creating Gallery Control {#creating-gallery-control style="tab-stops: 0pt"}

There are two different methods to create a simple Gallery control. They are listed below.

 

Through Designer

 

To create the Gallery control through designer, do the following steps.

 

1.   Drag a Gallery control from the toolbox onto the design area.

[] 

{border="0"}

Figure 495: Dragging Gallery Control from the Toolbox

***[]*** 

2.   Set the properties for Gallery control in design mode, using SmartTag feature.

[] 

Programmatically

 

To create the Gallery control through code, use the following XAML or C# code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<!\-- Adding Gallery \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [              ][\<][syncfusion][:][Gallery][ Name][=\"gallery\"\>][      ]                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                     ][\<!\-- Adding GalleryGroup \--\>][      ]                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                     ][\<][syncfusion][:][GalleryGroup][ Name][=\"galleryGroup\"][ Header][=\"GalleryGroup\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                           ][\<][syncfusion][:][GalleryItem][\>]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                                  ][\<][Image][ Source][=\"hr.jpg\"/\>]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                           ][\</][syncfusion][:][GalleryItem][\>]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                     ][\</][syncfusion][:][GalleryGroup][\>]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [              ][\</][syncfusion][:][Gallery][\>][      ]                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [//Creating an instance of Gallery control]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [Gallery gallery = [new] Gallery();]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [//Creating an instance of GalleryGroup]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [GalleryGroup galleryGroup = [new] GalleryGroup();]                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [//Adding gallery group to gallery]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                    |
| [gallery.Items.Add(galleryGroup);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [//Adding header to gallery group]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [galleryGroup.Header = [\"Gallery Group\"];]                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [//Creating an gallery item instance ]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [GalleryItem galleryItem = [new] GalleryItem();]                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [//Adding image]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                    |
| [Image image = [new] Image();]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [image.Source = [new] BitmapImage([new] [Uri]([\"hr.jpg\"], [UriKind].RelativeOrAbsolute));] |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [//Add image to gallery item]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [galleryItem.Content = image;]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [//Adding gallery item to gallery group]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [galleryGroup.Items.Add(galleryItem);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [//Adding control to the window]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                    |
| [this][.Content = gallery;]                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 496: Gallery Control with Gallery Item

 

[]{#p288} 

[]{#related-topics}

