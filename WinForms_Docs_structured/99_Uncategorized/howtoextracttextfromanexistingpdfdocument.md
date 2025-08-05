---
title: howtoextracttextfromanexistingpdfdocument.md
original_path: WinForms_Docs/99_Uncategorized/howtoextracttextfromanexistingpdfdocument.md
created_at: 2025-08-05
---








  









### How To Extract Text From an Existing PDF Document? {#how-to-extract-text-from-an-existing-pdf-document style="tab-stops: 0pt"}

 

You can extract text from an existing PDF document page by page by using the **ExtractText** method of the **PdfLoadedPage** class.

The following code example illustrates how to extract text from a document.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [// Load an existing PDF]                                                                                                                         |
|                                                                                                                                                                                                     |
| [PdfLoadedDocument][ ldoc = [new] [PdfLoadedDocument](txtUrl.Text);] |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [// Loading Page collections]                                                                                                                     |
|                                                                                                                                                                                                     |
| [PdfLoadedPageCollection][ loadedPages = ldoc.Pages;]                                                          |
|                                                                                                                                                                                                     |
| [string][ pdftext = [\"\"];]                                                            |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [// Extract text from PDF document pages]                                                                                                         |
|                                                                                                                                                                                                     |
| [foreach][ ([PdfLoadedPage] lpage [in] loadedPages)]                 |
|                                                                                                                                                                                                     |
| [{]                                                                                                                                                             |
|                                                                                                                                                                                                     |
| [  pdftext += lpage.ExtractText();]                                                                                                                             |
|                                                                                                                                                                                                     |
| [}]                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                           |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [\' Load an existing PDF]                                                                                                                                  |
|                                                                                                                                                                                                              |
| [Dim][ ldoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(txtUrl.Text)]    |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [\' Loading Page collections]                                                                                                                              |
|                                                                                                                                                                                                              |
| [Dim][ loadedPages [As] PdfLoadedPageCollection = ldoc.Pages]                                      |
|                                                                                                                                                                                                              |
| [Dim][ pdftext [As] [String] = \"\"]                                          |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [\' Extract text from PDF document pages]                                                                                                                  |
|                                                                                                                                                                                                              |
| [For][ [Each] lpage [As] PdfLoadedPage [In] loadedPages] |
|                                                                                                                                                                                                              |
| [  pdftext &= lpage.ExtractText()]                                                                                                                                       |
|                                                                                                                                                                                                              |
| [Next][ lpage]                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

