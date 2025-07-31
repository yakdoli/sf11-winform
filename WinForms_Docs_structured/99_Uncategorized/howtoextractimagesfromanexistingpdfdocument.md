---
title: howtoextractimagesfromanexistingpdfdocument.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoextractimagesfromanexistingpdfdocument.md
created_at: 2025-07-03
---








  









### How To Extract Images From an Existing PDF Document? {#how-to-extract-images-from-an-existing-pdf-document style="tab-stops: 0pt"}

 

You can extract images from an existing PDF document page by page, using the **ExtractImages** method of the **PdfLoadedPage** class.

The following code example illustrates how to extract images from a document.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [// Load an existing PDF]                                                                                                                                                                   |
|                                                                                                                                                                                                                                               |
| [PdfLoadedDocument][ ldoc = [new] [PdfLoadedDocument]([\"Sample.pdf\"]);]              |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [// Loading Page collections]                                                                                                                                                               |
|                                                                                                                                                                                                                                               |
| [PdfLoadedPageCollection][ loadedPages = ldoc.Pages;]                                                                                                    |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [// Extract Image from PDF document pages]                                                                                                                                                  |
|                                                                                                                                                                                                                                               |
| [foreach][ ([PdfLoadedPage] lpage [in] loadedPages)]                                                           |
|                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                               |
| [  [Image]\[\] img = lpage.ExtractImages();                   ]                                                                                                                      |
|                                                                                                                                                                                                                                               |
| [  [foreach] ([Image] img1 [in] img)]                                                                                                      |
|                                                                                                                                                                                                                                               |
| [  {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                               |
| [     img1.Save([\"Image\"] + [Guid].NewGuid().ToString() + [\".png\"], [ImageFormat].Png);                     ] |
|                                                                                                                                                                                                                                               |
| [  }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                           |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [\' Load an existing PDF]                                                                                                                                  |
|                                                                                                                                                                                                              |
| [Dim][ ldoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(\"Sample.pdf\")] |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [\' Loading Page collections]                                                                                                                              |
|                                                                                                                                                                                                              |
| [Dim][ loadedPages [As] PdfLoadedPageCollection = ldoc.Pages]                                      |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [\' Extract Image from PDF document pages]                                                                                                                 |
|                                                                                                                                                                                                              |
| [For][ [Each] lpage [As] PdfLoadedPage [In] loadedPages] |
|                                                                                                                                                                                                              |
| [  [Dim] img [As] Image() = lpage.ExtractImages()]                                                                             |
|                                                                                                                                                                                                              |
| [  [For] [Each] img1 [As] Image [In] img]                                            |
|                                                                                                                                                                                                              |
| [       img1.Save(\"Image\" & Guid.NewGuid().ToString() & \".png\", ImageFormat.Png)]                                                                                    |
|                                                                                                                                                                                                              |
| [  [Next] img1]                                                                                                                                     |
|                                                                                                                                                                                                              |
| [Next][ lpage]                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p140} 

[]{#related-topics}

