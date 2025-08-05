---
title: loadpdfwithouttoolstripinviewer.md
original_path: WinForms_Docs/99_Uncategorized/loadpdfwithouttoolstripinviewer.md
created_at: 2025-08-05
---








  









## Load PDF without ToolStrip in Viewer? {#load-pdf-without-toolstrip-in-viewer style="tab-stops: 0pt"}

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

 

The following is the image of a PDF document viewed in PdfDocumentView.

{border="0"}

Figure 10:  PDF displayed in PdfDocumentView

 

[]{#related-topics}

