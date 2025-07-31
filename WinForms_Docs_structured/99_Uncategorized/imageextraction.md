---
title: imageextraction.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\imageextraction.md
created_at: 2025-07-03
---








  









### ImageExtraction {#imageextraction style="tab-stops: 0pt"}

 

Essential PDF provides support to extract images from an existing PDF document. You can extract images by using the **ExtractImages** method in the **PdfLoadedPage** class.

 

The following code example illustrates how to extract images from a PDF document.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [// Load an existing PDF]                                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| [PdfLoadedDocument][ ldoc = [new] [PdfLoadedDocument]([\"Sample.pdf\"]);] |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Loading first page]                                                                                                                                                       |
|                                                                                                                                                                                                                                 |
| [PdfLoadedPage][ page = ldoc.Pages\[0\];]                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Extract images from first page]                                                                                                                                           |
|                                                                                                                                                                                                                                 |
| [Image][\[\] img = page.ExtractImages();]                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
| [\' Loading first page]                                                                                                                                    |
|                                                                                                                                                                                                              |
| [Dim][ page [As] PdfLoadedPage = ldoc.Pages(0)]                                                    |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [\' Extract images from first page]                                                                                                                        |
|                                                                                                                                                                                                              |
| [Dim][ img [As] Image() = page.ExtractImages()]                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Limitations**

 

Image extraction does not work with the following constraints:

 

[·      ]If the image has multiple filters in the PDF document.

[·      ]You cannot extract the image which is placed on the Xobject, also known as **PdfTemplate**.

 

 

[]{#related-topics}

