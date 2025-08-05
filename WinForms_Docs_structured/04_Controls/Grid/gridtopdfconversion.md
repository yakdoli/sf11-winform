---
title: gridtopdfconversion.md
original_path: WinForms_Docs/04_Controls/Grid/gridtopdfconversion.md
created_at: 2025-08-05
---








  









### Grid to PDF Conversion {#grid-to-pdf-conversion style="tab-stops: 0pt"}

[] 

Grid control provides support to convert the grid content to PDF format. You can convert the grid content into a PDF document for offline verification and/or computation. This is achieved by making use of the **GridPDFConverter** class.

 

PDF libraries support the conversion of grid content to a PDF page. The following dependent assemblies need to be referenced for this purpose along with the default assemblies that are present in the **References** folder of your Windows application: **Syncfusion.Pdf.Base** and **Syncfusion.GridHelperClasses.Windows**.

 

Following are the properties, methods and events that are made available to users as part of the GridPDFConverter class.

[] 

Properties

[] 

[·      ]**ShowHeader**-This property gets or sets a value indicating whether the header should be displayed in the PDF document. Default value is set to *false.*

*[]* 

The following code example illustrates how to set this property.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------+
| **[\[C#\]]**                               |
|                                                                                              |
| []                                         |
|                                                                                              |
| [pdfConvertor.ShowHeader = [true];] |
+----------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                          |
|                                                                                             |
| []                                        |
|                                                                                             |
| [pdfConvertor.ShowHeader = [True]] |
+---------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][441][: PDF Document displayed with Header]*

[] 

[·      ]**ShowFooter**-This property gets or sets a value indicating whether the footer should be displayed in the PDF document. Default value is set to *false*.

[] 

The following code example illustrates how to set this property.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------+
| **[\[C#\]]**                               |
|                                                                                              |
| []                                         |
|                                                                                              |
| [pdfConvertor.ShowFooter = [true];] |
+----------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                          |
|                                                                                             |
| []                                        |
|                                                                                             |
| [pdfConvertor.ShowFooter = [True]] |
+---------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][442][: PDF Document displayed with Footer]*

*[]* 

[·      ]**HeaderHeight**-This property gets or sets the height of the header for the PDF document.

[] 

The following code example illustrates how to set this property.

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------+
| **[\[C#\]]**        |
|                                                                       |
| []                  |
|                                                                       |
| [pdfConvertor.HeaderHeight = 15;] |
+-----------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------+
| **[\[VB.NET\]]**    |
|                                                                       |
| []                  |
|                                                                       |
| [pdfConvertor.HeaderHeight = 15]  |
+-----------------------------------------------------------------------+

[] 

[·      ]**FooterHeight**-This property gets or sets the height of the footer for the PDF document.

[] 

The following code example illustrates how to set this property.

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------+
| **[\[C#\]]**        |
|                                                                       |
| []                  |
|                                                                       |
| [pdfConvertor.FooterHeight = 20;] |
+-----------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------+
| **[\[VB.NET\]]**    |
|                                                                       |
| []                  |
|                                                                       |
| [pdfConvertor.FooterHeight = 20]  |
+-----------------------------------------------------------------------+

[] 

[·      ]**Margins**-This property gets or sets margins for the PDF document.

[] 

The following code example illustrates how to set this property.

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------+
| **[\[C#\]]**        |
|                                                                       |
| []                  |
|                                                                       |
| [pdfConvertor.Margins.All = 40;]  |
+-----------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------+
| **[\[VB.NET\]]**    |
|                                                                       |
| []                  |
|                                                                       |
| [pdfConvertor.Margins.All = 40]   |
+-----------------------------------------------------------------------+

[] 

Methods

[] 

[·      ]**ExportToPdf-**This method is used to export the grid to a PDF file.

[] 

The following code example illustrates how to use this method.

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [GridPDFConverter][ pdfConvertor = [new] [GridPDFConverter]();] |
|                                                                                                                                                                                                      |
| [pdfConvertor.ExportToPdf([\"Sample1.pdf\"], [this].gridControl1);]                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                |
|                                                                                                                                                                                   |
| []                                                                                                                              |
|                                                                                                                                                                                   |
| [Dim][ pdfConvertor [As] [New] GridPDFConverter()] |
|                                                                                                                                                                                   |
| [pdfConvertor.ExportToPdf([\"Sample1.pdf\"], [Me].gridControl1)]                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Events

[] 

[·      ]**DrawPDFFooter**-This event lets you draw a footer for the PDF document.

[] 

The following code example illustrates how to handle this event.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [pdfConvertor.DrawPDFFooter += [new] [GridPDFConverter].[DrawPDFHeaderFooterEventHandler](pdfConvertor_DrawPDFFooter);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [AddHandler ][pdfConvertor.DrawPDFFooter, [AddressOf] pdfConvertor_DrawPDFFooter] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**DrawPDFHeader**-This event lets you draw a header for the PDF document.

[] 

The following code example illustrates how to handle this event.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [pdfConvertor.DrawPDFHeader += [new] [GridPDFConverter].[DrawPDFHeaderFooterEventHandler](pdfConvertor_DrawPDFHeader);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [AddHandler][ pdfConvertor.DrawPDFHeader, [AddressOf] pdfConvertor_DrawPDFHeader] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p531} 

 

[]{#related-topics}

