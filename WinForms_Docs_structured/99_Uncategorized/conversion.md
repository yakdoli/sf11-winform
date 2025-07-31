---
title: conversion.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\conversion.md
created_at: 2025-07-03
---








  









## Conversion {#conversion style="tab-stops: 0pt"}

 

[]{#p87}DocIO provides support to convert a Word document into an image of type Bitmap or EMF. It enables to easily convert a single specified page, group of pages or a whole document into image format.

 

The following overloads of the RenderAsImages method that can be used to convert a Word document into an image.

 

[·      ]**WordDocument.RenderAsImages(imageType)**-This is used to convert the whole document into an image.

[·      ]**WordDocument.RenderAsImages(pageIndex, imageFormat)**-This is used to render/convert a particular page of the document into an image; it returns the resultant image of type Stream.

[·      ]**WordDocument.RenderAsImages(pageIndex, imageType)**-This is used to render/convert a particular page of the document into an image; it returns the resultant image of type Image.

[·      ]**WordDocument.RenderAsImages(pageIndex, noOfPages, imageType)**-This is used to render/convert multiple number of pages in the document, starting from the specified page index. It returns the resultant image of type Image\[\] array.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                     |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
| [Image][\[\] images = document.RenderAsImages(ImageType.Metafile);]                        |
|                                                                                                                                                                                    |
| [Stream][ stream = document.RenderAsImages(0, [ImageFormat].Emf);] |
|                                                                                                                                                                                    |
| [Image][ image = document.RenderAsImages(5, ImageType.Metafile);]                          |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [// This converts pages 2,3,4 in the document into images.]                                                                      |
|                                                                                                                                                                                    |
| [Image][\[\] images = document.RenderAsImages(1, 3, ImageType.Metafile);]                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                           |
| [Dim][ images() [As] Image = document.RenderAsImages(ImageType.Metafile)]       |
|                                                                                                                                                                                           |
| [Dim][ stream [As] Stream = document.RenderAsImages(0, ImageFormat.Emf)]        |
|                                                                                                                                                                                           |
| [Dim][ image [As] Image = document.RenderAsImages(5, ImageType.Metafile)]       |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [\' This converts pages 2,3,4 in the document into images.]                                                                             |
|                                                                                                                                                                                           |
| [Dim][ images() [As] Image = document.RenderAsImages(1, 3, ImageType.Metafile)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Note:



***[·    ]***Parameter \"pageIndex\" is a zero based index.

***[·    ]***Layouting of pages in DocIO is not the same as layouting of pages in Word. The total number of pages and layouting of the elements tend to vary.

***[·    ]***Currently Doc to Image conversion is not supported in Silverlight application.


 

For More Information Refer:

 

, , ]{.UGHyperlink}

More:













