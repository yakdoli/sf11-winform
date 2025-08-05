---
title: importpagesastemplates.md
original_path: WinForms_Docs/99_Uncategorized/importpagesastemplates.md
created_at: 2025-08-05
---






#### Import Pages As Templates {#import-pages-as-templates style="tab-stops: 0pt"}

 

You can create a booklet or just place few pages onto a single one by converting the pages into a PdfTemplate object. This template can be scaled, rotated, placed at different coordinates, and so on. It enables you to customize the page representation as per your need.

 

The following code example illustrates how to import a page as a template.

 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                         |
| []                                                                                                  |
|                                                                                                                                         |
| [PdfPage][ page = doc1.Pages.Add();]               |
|                                                                                                                                         |
| [PdfGraphics][ g = page.Graphics;]                 |
|                                                                                                                                         |
| []                                                                                                  |
|                                                                                                                                         |
| [PdfPageBase][ lpage = doc2.Pages\[0\];]           |
|                                                                                                                                         |
| [PdfTemplate][ template = lpage.CreateTemplate();] |
|                                                                                                                                         |
| []                                                                                                  |
|                                                                                                                                         |
| [g.DrawPdfTemplate(template, [PointF].Empty, page.GetClientSize());]           |
+-----------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [Dim][ doc [As] PdfLoadedDocument = [New] PdfLoadedDocument([\"../../Data/sample.pdf\"])] |
|                                                                                                                                                                                                                                                 |
| [Dim][ page [As] PdfPage = doc1.Pages.Add()]                                                                                          |
|                                                                                                                                                                                                                                                 |
| [Dim][ g [As] PdfGraphics = page.Graphics]                                                                                            |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [Dim][ lpage [As] PdfPageBase = doc2.Pages(0)]                                                                                        |
|                                                                                                                                                                                                                                                 |
| [Dim][ template [As] PdfTemplate = lpage.CreateTemplate()]                                                                            |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [g.DrawPdfTemplate(template, PointF.Empty, page.GetClientSize())]                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

