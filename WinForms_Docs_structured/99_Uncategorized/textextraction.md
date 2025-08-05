---
title: textextraction.md
original_path: WinForms_Docs/99_Uncategorized/textextraction.md
created_at: 2025-08-05
---








  









### Text Extraction {#text-extraction style="tab-stops: 0pt"}

[] 

A PDF file represents an ordered sequence of fixed pages. The planned appearance of everything that each page contains is completely specified down to the smallest detail. All the graphics, images, and text are specified to appear at precise spots on the page, in a particular color, of a given and fixed size, and so on.

 

Essential PDF provides support to extract text from an existing PDF document. By using the **ExtractText** method, you can extract the text, page by page.

 

The following code example illustrates this.

[] 

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
| [// Extract text from first page]                                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [string][ s = page.ExtractText();]                                                                                                         |
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
| [\' Extract text from first page]                                                                                                                          |
|                                                                                                                                                                                                              |
| [Dim][ s [As] [String] = page.ExtractText()]                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: The text will be extracted in the order in which it is written in the document stream. It is not in the order in which it is viewed in the PDF viewer.


 

 

[]{#related-topics}

