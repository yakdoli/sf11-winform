---
title: taggedpdf.md
original_path: WinForms_Docs/99_Uncategorized/taggedpdf.md
created_at: 2025-08-05
---






#### Tagged PDF {#tagged-pdf style="tab-stops: 0pt"}

HTML to PDF conversion handled using MSHTML rendering library can now generate tagged PDF documents.

Tagged PDF is a stylized use of PDF that builds on the logical structure framework. It defines a set of standard structure types and attributes that allow page content (text, graphics, and images) to be extracted and reused. The contents are accessible to users with visual impairments.

HTML documents can be converted to tagged PDFs using the **ConvertToTaggedPDF** method. It returns **PdfLayoutResult** which provides the end rectangle bounds and PDF page after the conversion.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                  |
| [public][ [PdfLayoutResult] ConvertToTaggedPDF([PdfDocument] document, [string] url);]                                                                                 |
|                                                                                                                                                                                                                                                                                                                                  |
| [public][ [PdfLayoutResult] ConvertToTaggedPDF([PdfDocument] document, [string] url, [string] userName, [string] password);] |
|                                                                                                                                                                                                                                                                                                                                  |
| [public][ [PdfLayoutResult] ConvertToTaggedPDF([PdfDocument] document, [string] html, [string] baseURL);][]              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]][]**                                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| [public][ PdfLayoutResult ConvertToTaggedPDF(PdfDocument document, [String] url)]                                                                                       |
|                                                                                                                                                                                                                                                                                   |
| [public][ PdfLayoutResult ConvertToTaggedPDF(PdfDocument document, [String] url, [String] userName, [String] password)]       |
|                                                                                                                                                                                                                                                                                   |
| [public][ PdfLayoutResult ConvertToTaggedPDF(PdfDocument document, [String] html, [String] baseURL)][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A tagged PDF can be converted from a Web page or HTML string by using the following code snippet:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][]**                                                       |
|                                                                                                                                                                                                                      |
| [// Create a new PdfDocument.]                                                                                                                                     |
|                                                                                                                                                                                                                      |
| [PdfDocument][ document = [new] [PdfDocument]();]                               |
|                                                                                                                                                                                                                      |
| [PdfLayoutResult][ result = [null];]                                                                    |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [// Create a new instance of HtmlConverter class.]                                                                                                                 |
|                                                                                                                                                                                                                      |
| [using][ ([HtmlConverter] html = [new] [HtmlConverter]())] |
|                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [    [// Turn on or off various options.]]                                                                                                                 |
|                                                                                                                                                                                                                      |
| [    html.EnableJavaScript = [true];]                                                                                                                       |
|                                                                                                                                                                                                                      |
| [    html.EnableActiveXContents = [true];]                                                                                                                  |
|                                                                                                                                                                                                                      |
| [                ]                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [    [// Convert to Tagged PDF.]]                                                                                                                          |
|                                                                                                                                                                                                                      |
| [    result = html.ConvertToTaggedPDF(document, url);]                                                                                                                           |
|                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [// Save and close the document.]                                                                                                                                  |
|                                                                                                                                                                                                                      |
| [document.Save([@\"Sample.pdf\"]);]                                                                                                                      |
|                                                                                                                                                                                                                      |
| [document.Close([true]);][]                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]][]**             |
|                                                                                                                                                                                |
| [\' Create a new PdfDocument.][]                                                         |
|                                                                                                                                                                                |
| [Dim][ document [As] [New] PdfDocument()]       |
|                                                                                                                                                                                |
| [Dim][ result [As] PdfLayoutResult = [Nothing]] |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [\' Create a new instance of HtmlConverter class.][]                                     |
|                                                                                                                                                                                |
| [Using][ html [As] [New] HtmlConverter()]       |
|                                                                                                                                                                                |
| [      \' Turn on or off various options.][]                                             |
|                                                                                                                                                                                |
| [      html.EnableJavaScript = [True]]                                                                                |
|                                                                                                                                                                                |
| [      html.EnableActiveXContents = [True]]                                                                           |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [      \' Convert to Tagged PDF.][]                                                      |
|                                                                                                                                                                                |
| [      result = html.ConvertToTaggedPDF(document, url)]                                                                                    |
|                                                                                                                                                                                |
| [End][ [Using]]                                                      |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [\' Save and close the document.][]                                                      |
|                                                                                                                                                                                |
| [document.Save([\"Sample.pdf\"])]                                                                                  |
|                                                                                                                                                                                |
| [document.Close([True])][]                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}***Note: The HTML to PDF conversion, which creates a metafile during the evolution, would interpret the content as either text or an image. The outcome of this PDF would contain only paragraph and figure tags; hyperlinks are not supported.***

 

[]{#related-topics}

