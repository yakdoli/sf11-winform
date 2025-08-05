---
title: pdfa1b.md
original_path: WinForms_Docs/99_Uncategorized/pdfa1b.md
created_at: 2025-08-05
---






#### PDF/A-1b {#pdfa-1b style="tab-stops: 0pt"}

 

PDF/A

 

The PDF/A formats specified in the ISO 19005 standards, strive to provide a mechanism for representing electronic documents. These documents are represented in a manner that preserves their visual appearance over time, independent of the tools and systems used for creating, storing or rendering the files. A key element to this reproducibility is the requirement for PDF/A documents to be 100 percent self-contained.

 

All of the information necessary for displaying the document in the same manner every time is embedded in the file. This includes all visible content like text, raster images, vector graphics, fonts, color information and much more. The standard is based on PDF 1.4, and imposes some restrictions regarding the use of color, fonts, annotations, and other elements.

[] 

There are two flavors of PDF/A-1:

[] 

[·      ]**ISO 19005-1 Level B conformance (PDF/A-1b)** ensures that the visual appearance of a document is preservable over the long term. PDF/A-1b ensures that the document will look the same, when it is processed sometime in the future.

[·      ]**ISO 19005-1 Level A conformance (PDF/A-1a)**: It is based on level B, but adds crucial properties from »Tagged PDF« It requires structure information and reliable text semantics in order to preserve the document\'s logical structure and natural reading order. PDF/A-1a not only ensures that the document will look the same when it is used in the future, but also ensures that its contents can be reliably interpreted and accessed by physically impaired users.


 

{border="0"}Note: PDF/A-1a and PDF/A-1b differ primarily with respect to text extraction.


[] 

PDF/A-1b

[] 

Creating PDF/A-1b document is very simple. You must set PdfConformanceLevel to ***PdfA1B*** while creating an instance to the PDF document. PDF/A standard imposes some restrictions regarding the usage of color, fonts, annotations, and other elements. These restrictions are listed as follows.

[] 

[·      ]The use of JavaScript is forbidden

[·      ]Attaching any file to PDF document is forbidden

[·      ]Hyperlink to a Non-PDF file is forbidden

[·      ]Security features are forbidden

[·      ]The use of Form Fields are forbidden

[·      ]Text Containing HTML Tags is forbidden

[·      ]Supports the use of TrueType fonts only; Does not support Type1 font

[·      ]Supports the use of RGB color; Does not support CMYK color

[] 

Validating PDF/A1-b

[] 

Adobe Acrobat Preflight tool is used to verify the compliance of a PDF document with the PDF/A standard.

 

You can verify the compliance of a PDF file by using the Preflight tool. Using the menu options select Advanced -\> Preflight -\> PDF/A compliance -\> Verify compliance with PDF/A-1b.

 

The following code example illustrates how to create PDF/A-1b compliant output.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [//Create a new document with PDF/A standard.]                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [PdfDocument][ doc = [new] [PdfDocument]([PdfConformanceLevel].Pdf_A1B);]                         |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [//Add a page]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [PdfPage][ page = doc.Pages.Add();]                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [//Create Pdf graphics for the page]                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [PdfGraphics][ g = page.Graphics;]                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [//Create a solid brush]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [PdfBrush][ brush = [new] [PdfSolidBrush]([Color].Black);]                                        |
|                                                                                                                                                                                                                                                       |
| [float][ fontSize = 20f;]                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| [Font][ f = [new] [Font]([\"Helvetica\"], fontSize, [FontStyle].Regular);] |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [//Set the font]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [PdfFont][ font = [new] [PdfTrueTypeFont](f, [true]);]                                            |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [//Draw the text]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [g.DrawString([\"Hello world!\"], font, brush, [new] [PointF](20, 20));]                                                                         |
|                                                                                                                                                                                                                                                       |
| [doc.Save([\"Sample.pdf\");]]                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [\'Create a new document with PDF/A standard.]                                                                                                                 |
|                                                                                                                                                                                                                  |
| [Dim][ doc [As] PdfDocument = [New] PdfDocument(PdfConformanceLevel.Pdf_A1B)]     |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [\'Add a page]                                                                                                                                                 |
|                                                                                                                                                                                                                  |
| [Dim][ page [As] PdfPage = doc.Pages.Add()]                                                            |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [\'Create Pdf graphics for the page]                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ g [As] PdfGraphics = page.Graphics]                                                             |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [\'Create a solid brush]                                                                                                                                       |
|                                                                                                                                                                                                                  |
| [Dim][ brush [As] PdfBrush = [New] PdfSolidBrush(Color.Black)]                    |
|                                                                                                                                                                                                                  |
| [Dim][ fontSize [As] [Single] = 20f]                                              |
|                                                                                                                                                                                                                  |
| [Dim][ f [As] Font = [New] Font(\"Helvetica\", fontSize, FontStyle.Regular)]      |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [\'Set the font]                                                                                                                                               |
|                                                                                                                                                                                                                  |
| [Dim][ font [As] PdfFont = [New] PdfTrueTypeFont(f, [True])] |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [\'Draw the text]                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [g.DrawString(\"Hello world!\", font, brush, [New] PointF(20, 20))]                                                                                     |
|                                                                                                                                                                                                                  |
| [doc.Save(\"Sample.pdf\")]                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

