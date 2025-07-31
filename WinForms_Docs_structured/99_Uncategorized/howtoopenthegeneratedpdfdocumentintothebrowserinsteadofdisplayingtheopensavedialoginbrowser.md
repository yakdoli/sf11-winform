---
title: howtoopenthegeneratedpdfdocumentintothebrowserinsteadofdisplayingtheopensavedialoginbrowser.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoopenthegeneratedpdfdocumentintothebrowserinsteadofdisplayingtheopensavedialoginbrowser.md
created_at: 2025-07-03
---






#### How to open the generated PDF document into the browser instead of displaying the Open/Save dialog in browser? {#how-to-open-the-generated-pdf-document-into-the-browser-instead-of-displaying-the-opensave-dialog-in-browser style="tab-stops: 0pt"}

[] 

You can open the PDF document directly in the browser with the help of the Response object.

Follow the below steps to generate the PDF document inline:

1.   Save the PDF document as Stream object.

2.   Write the stream in the Response object.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [        ]                                                                                                                                 |
|                                                                                                                                                                                |
| [\[C#\]]                                                                                                                                   |
|                                                                                                                                                                                |
| [ //Save the PDFDocument as a Stream.]                                                                                       |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [        [MemoryStream] stream = [new] [MemoryStream]();]             |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [        doc.Save(stream);]                                                                                                                |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [        [//Stream the output to the browser.]]                                                                      |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [        Response.ContentType = [\"application/pdf\"];]                                                            |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [        Response.AddHeader([\"content-disposition\"], [\"inline; filename=MyPDF.PDF\"]);] |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [        Response.AddHeader([\"content-length\"], stream.Length.ToString());]                                      |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [        Response.BinaryWrite(stream.ToArray());]                                                                                          |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [        Response.End();]                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                     |
|                                                                                                                                                                               |
| [  ][      [Save the PDFDocument as a Stream.]]                   |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [        [Dim] stream [As] [New] MemoryStream()]                           |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [        doc.Save(stream)]                                                                                                                |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [        [\'Stream the output to the browser.]]                                                                     |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [        Response.ContentType = [\"application/pdf\"]]                                                            |
|                                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                                               |
| [        Response.AddHeader([\"content-disposition\"], [\"inline; filename=MyPDF.PDF\"])] |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [        Response.AddHeader([\"content-length\"], stream.Length.ToString())]                                      |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [        Response.BinaryWrite(stream.ToArray())]                                                                                          |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [  Response.End()][]                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

