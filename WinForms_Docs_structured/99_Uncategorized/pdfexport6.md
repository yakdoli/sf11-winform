---
title: pdfexport6.md
original_path: WinForms_Docs/99_Uncategorized/pdfexport6.md
created_at: 2025-08-05
---








  





### PDF Export {#pdf-export style="tab-stops: 0pt"}

The OlapGrid can be exported to a PDF file using the following code:

 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                         |
| [// Export OLAP Grid data to PDF.][] |
|                                                                                                                                         |
| [this][.OlapGrid1.ExportToPDF();]                  |
+-----------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                       |
|                                                                                                                                        |
| [\'Export OLAP Grid data to PDF][.] |
|                                                                                                                                        |
| [Me][.OlapGrid1.ExportToPDF()]                    |
+----------------------------------------------------------------------------------------------------------------------------------------+

 

The OlapGrid control supports PDF file customization using the **QueryPdfExportCellInfo** event while exporting.

 

Refer to the code snippet below to add an event handler to customize the PDF file.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                              |
| [this][.OlapGridControl1.QueryPdfExportCellInfo += [new] [EventHandler]\<[PdfExportCellInfoEventArgs]\>(OlapGridControl1_QueryPdfExportCellInfo);] |
|                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                              |
| [void][ OlapGridControl1_QueryPdfExportCellInfo([object] sender, [PdfExportCellInfoEventArgs] e)]                                                                          |
|                                                                                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                              |
| [        e.Cell.Style.TextBrush = Syncfusion.Pdf.Graphics.[PdfBrushes].Chocolate;]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                       |
| [AddHandler][ OlapGridControl1.QueryPdfExportCellInfo, [AddressOf] OlapGridControl1_QueryPdfExportCellInfo]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] OlapGridControl1_QueryPdfExportCellInfo([ByVal] sender [As] [Object], [ByVal] e [As] PdfExportCellInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                       |
| [            e.Cell.Style.TextBrush = Syncfusion.Pdf.Graphics.PdfBrushes.Chocolate]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

