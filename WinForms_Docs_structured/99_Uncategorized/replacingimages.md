---
title: replacingimages.md
original_path: WinForms_Docs/99_Uncategorized/replacingimages.md
created_at: 2025-08-05
---








  









### Replacing Images {#replacing-images style="tab-stops: 0pt"}

 

Essential PDF supports extracting image locations from an existing document, replace with new images and then save them in the same locations.

 

This feature is implemented using the following APIs.

 

Replacing Images

 

This is done using the ReplaceImage method.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [doc.Pages\[0\].ReplaceImage(1, [new] PdfBitmap([@\"Water lilies.jpg\"]););] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Extracting Image Location**

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [foreach][ (PdfLoadedPage lpage [in] loadedPages)]     |
|                                                                                                                                                                  |
| [{]                                                                                                                          |
|                                                                                                                                                                  |
| [    PdfImageInfo\[\] info = lpage.ImagesInfo;]                                                                              |
|                                                                                                                                                                  |
| [      foreach][ (PdfImageInfo information [in] info)] |
|                                                                                                                                                                  |
| [      {]                                                                                                                    |
|                                                                                                                                                                  |
| [        RectangleF location=information.Bounds.]                                                                            |
|                                                                                                                                                                  |
| [       }]                                                                                                                   |
|                                                                                                                                                                  |
| [}]                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code snippet illustrates the use case for the above APIs.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [PdfLoadedDocument][ doc = [new] [PdfLoadedDocument]([@\"imageDoc.pdf\"]);] |
|                                                                                                                                                                                                                                   |
| [PdfBitmap][ bmp = [new] [PdfBitmap]([@\"Water lilies.jpg\"]);]             |
|                                                                                                                                                                                                                                   |
| [doc.Pages\[0\].ReplaceImage(1, bmp);]                                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| [doc.Save([\"Replace Sample.pdf\"]);]                                                                                                                                  |
|                                                                                                                                                                                                                                   |
| [System.Diagnostics.[Process].Start([\"Replace Sample.pdf\"]);]                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [// Load an existing PDF]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [PdfLoadedDocument ldoc = [new] PdfLoadedDocument(txtUrl.Text);]                                                                                                                           |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [// Loading Page collections]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [PdfLoadedPageCollection loadedPages = ldoc.Pages;]                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [int][ page = 0;]                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [// Extract Image from PDF document pages]                                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [foreach][ (PdfLoadedPage lpage [in] loadedPages)              ]                                                                          |
|                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [    PdfImageInfo\[\] info = lpage.ImagesInfo;]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [    [if] (info != [null])]                                                                                                                                           |
|                                                                                                                                                                                                                                                     |
| [        [foreach] (PdfImageInfo information [in] info)]                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [            information.Image.Save([\"Image\"] + page.ToString() + information.Bounds.ToString() + [\".png\"],    ImageFormat.Png);                            ] |
|                                                                                                                                                                                                                                                     |
| [    page++;]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                     |
| [Image image = info\[0\].Image;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [image.Save([\"test.png\"]);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                     |
| [System.Diagnostics.[Process].Start([\"test.png\"]);    ]                                                                                                           |
|                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p87} 

 

[]{#related-topics}

