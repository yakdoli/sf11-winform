---
title: doctopdf1.md
original_path: WinForms_Docs/99_Uncategorized/doctopdf1.md
created_at: 2025-08-05
---








  









### Doc To PDF {#doc-to-pdf style="tab-stops: 0pt"}

 

Essential DocIO enables to export the Word document into a PDF document. By using the **ConvertToPDF** method of the **DocToPDFConverter** class, you can convert the Word document to PDF, and save the PDF document.

 


{border="0"}Note:[ ]You need to have Essential PDF and Essential DocIO installed in your system. This is because \"Syncfusion.DocToPDFConverter.Base.dll\" is conditionally shipped when both DocIO.Base and Pdf.Base is installed.


 

This section covers the following:

 

[·      ]Assemblies Dependent for this Conversion

[·      ]Supported Elements and Limitations

[·      ]UnSupported Elements and Limitation

[] 

Assembly Dependency for this Conversion

**[]** 

[·      ]Syncfusion.DocToPDFConverter.Base.dll

[·      ]Syncfusion.DocIO.Base.dll

[·      ]Syncfusion.Pdf.Base.dll

[·      ]Syncfusion.Core.dll

[·      ]Syncfusion.Compression.Base.dll

 

The following code illustrates how to convert a word document, say, \"sample.doc\" to a PDF document.

 

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
| [//Convert word document into PDF document]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [PdfDocument pdfDoc = converter.ConvertToPDF(wordDoc);]                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [//Save the pdf file]                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [pdfDoc.Save([\"DoctoPDF.pdf\"]);]                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

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
| [\'Convert word document into PDF document]                                                                                             |
|                                                                                                                                                                                           |
| [Dim][ pdfDoc As PdfDocument = converter.ConvertToPDF(wordDoc)]                                      |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [\'Save the pdf file]                                                                                                                   |
|                                                                                                                                                                                           |
| [pdfDoc.Save([\"DoctoPDF.pdf\"])]                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Supported Elements

 

This feature provides support for the following elements.

 

[·      ]Paragraph and Character Formatting

[·      ]MultiColumn Text

[·      ]Headers and Footers

[·      ]Bulleted, Numbered and MultiLevel Lists

[·      ]Images

[·      ]Tables (both simple and nested)

[·      ]Breaks (page, section, linebreak, etc.)

[·      ]OLEObject

[·      ]Text Box

[·      ]Page Settings and Background Image

[·      ]Document Properties

[] 

[·      ]Paragraph and Character Formatting

[] 

This feature supports almost all the paragraph formatting options except Full-Justification. The supported paragraph formatting options are as follows.

[] 

[·      ]Paragraph and Character Fonts

[·      ]Font styles (Bold, Italic, Underline and Strike through)

[·      ]Subscript and Superscript

[·      ]Paragraph and Text Highlighting

[·      ]Indents, tabs and spaces

[·      ]Line Spacing

[·      ]Left, Right and Center Justification

**[]** 

+-------------------------------------------------------------------------------------------+
| Known Limitations                                                                         |
|                                                                                           |
| **[]**  |
|                                                                                           |
| [·      ]Borders around paragraphs.                          |
|                                                                                           |
| [·      ]Full Justification.                                 |
+-------------------------------------------------------------------------------------------+

[] 

[·      ]MultiColumn Text

 

Word document containing multicolumn text is supported.

 

  --------------------------------------------------------------------------------------------------------------------------------
  ***Known Limitations* -** But the output may look different in case full-justification formatting is applied onto the columns.
  --------------------------------------------------------------------------------------------------------------------------------

[] 

[·      ]Headers and Footers

 

Page headers and footers are supported and can contain images, text and page number fields.

 

[·      ]Bulleted, Numbered and MultiLevel Lists

 

Bulleted, numbered and multilevel lists are supported with proper indentation and alignments as represented in the Word document.

 

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  ***Known Limitations*** - In some case, the image bullets which is set on document may be replaced by the following symbol in the generated document. For eg :
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------

[] 

[{border="0"}]

Figure 64: Image replacement

[·      ]Images

 

The images present in the document are supported along with their corresponding positions and sizes.

 

  --------------------------------------------------------------------------------------------------------------------------
  ***Known Limitations*** - However, the images placed inside a shape will not be preserved in the generated PDF document.
  --------------------------------------------------------------------------------------------------------------------------

 

[·      ]Tables

 

Both simple and nested tables are supported with proper preservation of text formatting and images present inside the table cell.

 

+---------------------------------------------------------------------------------------------------------------------------------+
| Known Limitations                                                                                                               |
|                                                                                                                                 |
| **[]**                                        |
|                                                                                                                                 |
| [·      ]Tables making use of patterns and 3D borders will not be retained in the output document. |
|                                                                                                                                 |
| [·      ]Absolutely positioned tables are not supported.                                           |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Breaks

 

Columns, section, line and page breaks are fully supported.

 

[·      ]OLEObject

 

OLEObjects are partially supported, i.e., the image, which represents a particular document that will be available in the generated PDF document. But the object associated with the object will not be converted into the generated document.

 

[·      ]Text Box []

 

The text value present in the text box will be rendered as text in its actual position in the generated PDF document.

 

[·      ]Page Settings []

 

The actual page settings will be preserved in the generated PDF document which includes page size, orientation, page borders and its background image, if available.

 

[·      ]Document Properties

 

The document properties present in the Word document will also be preserved in the generated PDF Document.

 

Unsupported Elements

 

The following are the list of unsupported elements, which will not be preserved in the generated PDF document.

 

[·      ]Shapes and AutoShapes

[·      ]Comments

[·      ]Hyperlinks

[·      ]Bookmarks

[·      ]Footnotes and Endnotes

[·      ]Dynamic Fields

[·      ]Charts

[·      ]Table of Contents

[] 

[] 

  ------------------------------------
  **Known Limitations** - Pagination
  ------------------------------------

[] 

Pagination

Essential DocIO, when generating the PDF document, makes sensible decisions while laying out the text and its supported elements. However, pagination is not guaranteed with all the documents.

 

 

[]{#related-topics}

