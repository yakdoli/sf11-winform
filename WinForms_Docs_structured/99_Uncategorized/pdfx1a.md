---
title: pdfx1a.md
original_path: WinForms_Docs/99_Uncategorized/pdfx1a.md
created_at: 2025-08-05
---






#### PDF/X-1a {#pdfx-1a style="tab-stops: 0pt"}

[] 

PDF/X is a subset of the Adobe Portable Document Format (PDF) specification, which exhibits best practices in graphic arts file exchange. PDF/X-1a restricts the content in a PDF document that does not directly serve the purpose of high-quality print production output, such as annotations, Java Actions, and embedded multimedia.

 

PDF/X-1a also eliminates the most common errors in file preparation. Sending the document as a PDF/X-1a file, will guarantee that font errors do not occur. This is because a file declared as complying with the PDF/X-1a standard meets the following requirements:

 

[·      ]All fonts and images must be embedded

[·      ]All elements must be encoded as CMYK

 

In addition,

 

[·      ]MediaBox and TrimBox or ArtBox must be defined; BleedBox is optional

[·      ]The output intent must be specified either by stating a Characterized Printing Condition or identifying an ICC output profile

[] 

Advantages of PDF/X-1a

 

By using a PDF/X-1a workflow,

 

[·      ]Print-ready files will reproduce as you intended.

[·      ]You will save time and money.

[·      ]Reduces additional time and money

 

The following code snippet illustrates how to create a pdf document complying the above standard.

 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [//Create the document.]                                                       |
|                                                                                                                                  |
| [PdfDocument doc = [new] PdfDocument(PdfConformanceLevel.Pdf_X1A2001);] |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [//Set the color space. Should be CMYK.]                                       |
|                                                                                                                                  |
| [doc.ColorSpace = PdfColorSpace.CMYK;]                                                       |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [//Save and close the document.]                                               |
|                                                                                                                                  |
| [doc.Save([\"sample.pdf\"]);]                                         |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                 |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [\'Create the document.]                                                                                                                         |
|                                                                                                                                                                                                    |
| [Dim][ doc [As] [New] PdfDocument(PdfConformanceLevel.Pdf_X1A2001)] |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [\'Set the color space. Should be CMYK.]                                                                                                         |
|                                                                                                                                                                                                    |
| [doc.ColorSpace = PdfColorSpace.CMYK]                                                                                                                          |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [\'Save and close the document.]                                                                                                                 |
|                                                                                                                                                                                                    |
| [doc.Save([\"sample.pdf\"])]                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

