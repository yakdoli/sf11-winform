---
title: loadpdfwithouttoolstripinviewer1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\loadpdfwithouttoolstripinviewer1.md
created_at: 2025-07-03
---








  









## Load PDF without ToolStrip in viewer? {#load-pdf-without-toolstrip-in-viewer style="tab-stops: 0pt"}

Inorder to view PDF without the toolstrip, make use of PdfDocumentView control instead of PdfViewerControl. Other features and options are similar to PdfViewerControl.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                        |
| [PdfDocumentView][ pdfDocumentView1 = [new] [PdfDocumentView]();] |
|                                                                                                                                                                                                        |
| [pdfDocumentView1.Load([@\"Template.pdf\"]);]                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                 |
|                                                                                                                                                                                      |
| [Dim][ pdfDocumentView1 [As] [New] PdfDocumentView()] |
|                                                                                                                                                                                      |
| [pdfDocumentView1.Load([\"Template.pdf\"])]                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following is the image of PDF document viewed in PdfDocumentView.

{border="0"}

Figure 9:  PDF displayed in PdfDocumentView

[] 

[] 

[] 

[] 

[] 

 

[] 

[]{#related-topics}

