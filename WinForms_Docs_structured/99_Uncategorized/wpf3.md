---
title: wpf3.md
original_path: WinForms_Docs/99_Uncategorized/wpf3.md
created_at: 2025-08-05
---








  









### WPF {#wpf style="tab-stops: 0pt"}

 

Now, you have created a WPF application (refer to ). This section covers the following:

 

[·      ]Deploying Essential PDF in a WPF Application

[·      ]Create and add a PDF document with pages to the application

[] 

Deploying Essential PDF in a WPF Application

 

To deploy Essential PDF:

1.   Go to **Solution Explorer** of the application you have created. Right-click the **Reference** folder and then click **Add References**.

2.   Add the following assemblies as references in the application:

[·      ]Syncfusion.Core.dll

[·      ]Syncfusion.Compression.Base.dll

[·      ]Syncfusion.Pdf.Base.dll

[] 

{border="0"} For detailed documentation on Windows Application deployment, see: [[http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf.]{.UGHyperlink}](http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf.)

Essential PDF is deployed in the Windows application:

 

Create and add a PDF document with pages to the application

 

The following steps will guide you to create and add a PDF document to this application:

 

3.   Create a PDF document using the following code.

[] 

{border="0"} The PDF document represents the document that is created in the memory. It is only the memory representation of the PDF document that is written to the disk.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [// Create a new PDF document. This object represents the PDF document.]                                                     |
|                                                                                                                                                                                |
| [// This document has one page, by default. Additional pages have to be added.]                                              |
|                                                                                                                                                                                |
| [PdfDocument][ pdfDoc = [new] [PdfDocument]();] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [\' Create a new PDF document. This object represents the PDF document.]                                                                                         |
|                                                                                                                                                                                                                    |
| [\' This document has one page, by default. Additional pages have to be added.]                                                                                  |
|                                                                                                                                                                                                                    |
| [Dim][ pdfDoc [As] Syncfusion.Pdf.PdfDocument = [New] Syncfusion.Pdf.PdfDocument()] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A new PDF document is created.

[] 

Add a new page to the created document.

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                          |
| []                                                                     |
|                                                                                                                          |
| [// Add a page to the document ]                                       |
|                                                                                                                          |
| [PdfPage][ page = doc.Pages.Add();] |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                        |
|                                                                                                                                                                           |
| []                                                                                                                      |
|                                                                                                                                                                           |
| [\'Add a page to the document ]                                                                                         |
|                                                                                                                                                                           |
| [Dim][ firstPage [As] Syncfusion.Pdf.PdfPage = doc.Pages.Add()] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A PDF page is added to the document (doc).

 

4.   Write the string \"Hello World\" on the first page in the PDF document. This task is further subdivided into the following tasks.

[] 

[·      ]Create the font object to be used for writing the \"Hello World\" string. You can set the font size and style in the same statement.

[·      ]Write the text using the **DrawString** method of the Graphics object.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [// Use the predefined fonts to draw the text. ]                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [PdfFont][ font = [new] [PdfStandardFont]([PdfFontFamily].Helvetica, fontSize, fontStyle);] |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [// Draw the string at the specified coordinates.]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [firstPage.Graphics.DrawString([\"Hello World\"], pdfFont, [PdfBrushes].Black, 0, 0);  ]                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [\' Use the predefined fonts to draw the text. ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| [Dim][ font [As] Syncfusion.Pdf.Graphics.PdfFont = [New] Syncfusion.Pdf.Graphics.PdfStandardFont(PdfFontFamily.Helvetica, fontSize, FontStyle)] |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [\' Draw the string at the specified coordinates.]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [firstPage.Graphics.DrawString([\"Hello World\"], pdfFont, PdfBrushes.Black, 0,0)]                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The string \"Hello World\" is written to the document.

 

5.   Then write the PDF document we have created to the disk. This can be done by using the **Save** method of the PDF document.

[] 

+----------------------------------------------------------------------------------------------+
| **[\[C#\]]**                               |
|                                                                                              |
| []                                         |
|                                                                                              |
| [// Save the PDF document to disk.]        |
|                                                                                              |
| [pdfDoc.Save([\"Sample.pdf\"]); ] |
+----------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                         |
|                                                                                            |
| []                                       |
|                                                                                            |
| [\' Save the PDF document to disk.]      |
|                                                                                            |
| [pdfDoc.Save([\"Sample.pdf\"])] |
+--------------------------------------------------------------------------------------------+

[] 

You can also save the changes to the loaded document as follows.

[] 

+------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                 |
|                                                                                                |
| []                                           |
|                                                                                                |
| [// Save the document with same name       ] |
|                                                                                                |
| [pdfDoc.Save([)];]                  |
+------------------------------------------------------------------------------------------------+

[     ]

+-----------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                            |
|                                                                                               |
| []                                          |
|                                                                                               |
| [\' Save the document with same name      ] |
|                                                                                               |
| [pdfDoc.Save()]                                           |
+-----------------------------------------------------------------------------------------------+

**[]** 

The created pdf document is saved to the disk using the above code.

[] 

6.   Finally close the PDF Document using the following code, so that the objects are released.

[] 

+---------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                |
|                                                                                                               |
| []                                                          |
|                                                                                                               |
| [// Release the common resources.        ]                  |
|                                                                                                               |
| [pdfDoc.Close();]                                                         |
|                                                                                                               |
| []                                                                        |
|                                                                                                               |
| [//(or)]                                                    |
|                                                                                                               |
| []                                                          |
|                                                                                                               |
| [//Releases document stream. This releases entire document] |
|                                                                                                               |
| [PdfDoc.Close(true);]                                                     |
+---------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                               |
|                                                                                                                                                  |
| **[]**                                                                                         |
|                                                                                                                                                  |
| [\' Release the common resources.  ][      ] |
|                                                                                                                                                  |
| [pdfDoc.Close()]                                                                               |
|                                                                                                                                                  |
| []                                                                                             |
|                                                                                                                                                  |
| [\'(or)]                                                                                       |
|                                                                                                                                                  |
| []                                                                                             |
|                                                                                                                                                  |
| [\'Releases document stream. This releases entire document]                                    |
|                                                                                                                                                  |
| [PdfDoc.Close(True)]                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

PDF document will be closed after saving.

 

The sample pdf document created through the above procedure is shown below.

[] 

{border="0"}

Figure 22: PDF Document with pages

***[]*** 

A PDF document is created in the WPF application.

 

[]{#related-topics}

