---
title: pdfconverter.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\pdfconverter.md
created_at: 2025-07-03
---






##### PDF Converter {#pdf-converter style="tab-stops: 0pt"}

[] 

PDF Export

 

Essential Grid Grouping control supports conversion of grid contents to a PDF file. Users can convert data from the Grid Grouping control into a PDF document using the GridPDFConverter class. PDF libraries are used to support the conversion of grid content to a PDF page.

 

To ensure the convertion of grid data to PDF document, the following dll files should be added, along with the default dll files in the reference folder:

[] 

[·      ]Syncfusion.Pdf.Base 

[·      ]Syncfusion.GridHelperClasses.Windows

[] 

The **ExportToPdf** method should be used to export the grid to a PDF file.

 

The following code example illustrates the conversion of grid data to PDF document.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                      |
| [GridPDFConverter][ pdfConvertor = [new] [GridPDFConverter]();] |
|                                                                                                                                                                                                                                      |
| [pdfConvertor.ExportToPdf([\"Sample.pdf\"], [this].gridGroupingControl1.TableControl);]                                             |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [// Launching the PDF file by using the default Application \[Acrobat Reader\].]                                                                                   |
|                                                                                                                                                                                                                                      |
| [System.Diagnostics.[Process].Start([\"Sample.pdf\"]);]                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                          |
| [Dim][ pdfConvertor [As] [GridPDFConverter] = [New] [GridPDFConverter]()] |
|                                                                                                                                                                                                                                                                                          |
| [pdfConvertor.ExportToPdf(\"Sample.pdf\", [Me].gridGroupingControl1.TableControl)]                                                                                                                              |
|                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                          |
| [\' Launching the PDF file by using the default Application \[Acrobat Reader\].]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                          |
| [System.Diagnostics.Process.Start(\"Sample.pdf\")]                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][379][:  Grid Grouping Data]*

[] 

{border="0"}

[] 

*[Figure ][380][:  Grid Grouping Data converted to PDF]*

 

[]{#p472} 

 

[]{#related-topics}

