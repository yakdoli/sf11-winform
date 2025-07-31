---
title: doctopdf.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\doctopdf.md
created_at: 2025-07-03
---








  









### Doc to PDF {#doc-to-pdf style="tab-stops: 0pt"}

 

Essential DocIO allows you to export the word document into a PDF document. Use the **ConvertToPDF** method of **DocToPDFConverter** class, to convert the doc to pdf, and save the PDF document. Using this, the user can easily convert the word document to PDF document.

 

 


{border="0"}Note: You need to have Essential PDF and Essential DocIO installed in your system. Since \"Syncfusion.DocToPDFConverter.Base.dll\" is conditionally shipped when both DocIO.Base and Pdf.Base is installed.


 

Assembly Dependency for this Conversion

 

[·      ]Syncfusion.DocToPDFConverter.Base.dll

[·      ]Syncfusion.DocIO.Base.dll

[·      ]Syncfusion.Pdf.Base.dll

[·      ]Syncfusion.Core.dll

[·      ]Syncfusion.Compression.Base.dll

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [WordDocument][ wordDoc = [new] [WordDocument]([\"sample.doc\"]);] |
|                                                                                                                                                                                                                                 |
| [DocToPDFConverter converter = [new] DocToPDFConverter();]                                                                                                             |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Convert word document into PDF document]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [PdfDocument pdfDoc = converter.ConvertToPDF(wordDoc);]                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Save the pdf file]                                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [pdfDoc.Save([\"DoctoPDF.pdf\"]);]                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
| []                                                                                                                                                                  |
|                                                                                                                                                                                           |
| [Dim][ wordDoc [As New] WordDocument([\"sample.doc\"])] |
|                                                                                                                                                                                           |
| [Dim][ converter As New DocToPDFConverter()]                                                         |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [\' Convert word document into PDF document]                                                                                            |
|                                                                                                                                                                                           |
| [Dim][ pdfDoc As PdfDocument = converter.ConvertToPDF(wordDoc)]                                      |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [\' Save the pdf file]                                                                                                                  |
|                                                                                                                                                                                           |
| [pdfDoc.Save([\"DoctoPDF.pdf\"])]                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Supported Elements

 

With the initial version of the feature, this feature provides support for the following elements.

 

[·      ]Paragraph and character formatting

[·      ]Multi-Column Texts

[·      ]Headers and Footers

[·      ]Bulleted, numbered and multi-level lists

[·      ]Images

[·      ]Tables (both simple and nested)

[·      ]Table styles for docx formats (Word 2007 and Word 2010 formats)

[·      ]Breaks (page, section, linebreak, etc)

[·      ]OLEObject

[·      ]Textbox

[·      ]Page Settings and background image

[·      ]Document Properties

 

Paragraph and Character formatting

 

This feature supports almost all the paragraph formatting except Full-Justification. The supported paragraph formatting features are,

*[]* 

[·      ]Paragraph and character fonts

[·      ]Font styles (Bold, Italic, Underline, and Strike through)

[·      ]Subscript and Superscript

[·      ]Paragraph and text highlighting

[·      ]Indents, tabs and spaces

[·      ]Line spacing

[·      ]Left, right and center justification

 

+-----------------------------------------------------------------------+
| Known Limitations                                                     |
|                                                                       |
|                                                                       |
|                                                                       |
| [·      ]Borders around paragraphs.      |
|                                                                       |
| [·      ]Full Justification.             |
+-----------------------------------------------------------------------+

 

Multi-Column Texts

 

The word documents containing multi-column text were supported.

 

  ---------------------------------------------------------------------------------------------------------------------------------
  ***Known Limitations* -** But the output may look different in case full-justification formatting is applied on to the columns.
  ---------------------------------------------------------------------------------------------------------------------------------

 

Headers and Footers

 

The page headers and footers are supported and can contain images, texts and page number fields.

 

Bulleted, Numbered and Multi-level lists

 

The bulleted list, numbered and multi-level list were supported with proper indentation and alignments as represented in the word document.

 

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  ***Known Limitations*** - In some case, the image bullets which is set on document may be replaced by the following symbol in the generated document. For eg :
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------

 

{border="0"}

Figure 82: Bulleted, Numbered and Multi-level Lists

 

 

Images

 

The images present in the document are supported along with their corresponding positions and sizes.

 

  --------------------------------------------------------------------------------------------------------------------------
  ***Known Limitations*** - However, the images placed inside a shape will not be preserved in the generated PDF document.
  --------------------------------------------------------------------------------------------------------------------------

 

Tables

 

Both simple and nested tables are supported with proper preservation of text formatting and images present inside the table cell. Text directions are also supported.

 

+---------------------------------------------------------------------------------------------------------------------------------+
| Known Limitations                                                                                                               |
|                                                                                                                                 |
|                                                                                                                                 |
|                                                                                                                                 |
| [·      ]Tables making use of patterns and 3D borders will not be retained in the output document. |
|                                                                                                                                 |
| [·      ]Absolutely positioned tables are not supported.                                           |
+---------------------------------------------------------------------------------------------------------------------------------+

 

Doc to PDF Conversion Support for Table Styles for Word 2007 and Word 2010 Documents

 

Support is now added for table styles in Doc to PDF conversion for Word 2007 and Word 2010 documents. During Doc to PDF conversion, Table-style support provides a unique look and feel to tables in the converted PDF documents, similar to the tables in Word documents.

[] 

{border="0"}[]

[] 

Figure 83: MS Word Document with Table Style

[] 

{border="0"}[]

 

Figure 84: Converted PDF with Table Style -- Light Shading

 

  ----------------------------------------------------------------------------------------
  ***Known Limitations*** - Table styles for Word 97 -- 2003 documents are not supported
  ----------------------------------------------------------------------------------------

 

Breaks

 

The columns, section, line and page breaks are fully-supported.

 

OLEObject

 

The OLEObjects are partially supported, (i.e) image which represents a particular document will be available in the generated PDF document. But the object associated with the object will not be converted into the generated document.

 

Text box

 

The text value present in the text box will be rendered as text at its actual position in the generated PDF document. Text directions are also supported.

 

PageSettings

 

The actual page settings will be preserved in the generated PDF documents, which includes page size, orientation, page borders and its background image if available.

 

Document Properties

 

The document properties present in the word documents will also be preserved in the generated PdfDocument.

 

Un-Supported Elements

 

The following are the list of un-supported elements, which will be supported in the future releases and will not be preserved in the generated PDF document.

 

[·      ]Shapes and auto shapes

[·      ]Comments

[·      ]Hyperlinks

[·      ]Bookmarks

[·      ]Foot note and end note

[·      ]Dynamic Fields

[·      ]Charts

[·      ]Table of Contents

 

  --------------------------------------
  ***Known Limitations -*** Pagination
  --------------------------------------

 

Pagination

 

Essential DocIO makes sensible decision while layouting the text, and its supported elements while generating the PDF documents. But however, we cannot guarantee pagination with all the documents.

 


{border="0"}Note: Currently Doc to Pdf conversion is not supported in Silverlight application.

 

 


[]{#related-topics}

