---
title: howtoaccesspagesinanexistingdocument.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaccesspagesinanexistingdocument.md
created_at: 2025-07-03
---








  









### How To Access Pages In an Existing Document? {#how-to-access-pages-in-an-existing-document style="tab-stops: 0pt"}

 

Pages in the existing document are different from pages in the newly created document. PdfPageBase class is used to manipulate the existing page in a loaded document. The following code example illustrates how to access the existing page.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [PdfLoadedDocument][ lDoc = [new] [PdfLoadedDocument](txtUrl.Text);]                                                                 |
|                                                                                                                                                                                                                                                                     |
| [PdfPageBase][ lPage = lDoc.Pages\[0\];]                                                                                                                                       |
|                                                                                                                                                                                                                                                                     |
| [PdfGraphics][ g = lPage.Graphics;]                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [g.DrawString([\"Writing text in loaded page\"], font, [PdfPens].Red, [PdfBrushes].Red, [new] [PointF](-150, 450));] |
|                                                                                                                                                                                                                                                                     |
| [lDoc.Save([\"Sample.pdf\"]);]                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                      |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [Dim][ lDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(txtUrl.Text)] |
|                                                                                                                                                                                                           |
| [Dim][ lPage [As] PdfPageBase = lDoc.Pages(0)]                                                  |
|                                                                                                                                                                                                           |
| [Dim][ g [As] PdfGraphics = lPage.Graphics]                                                     |
|                                                                                                                                                                                                           |
| [g.DrawString([\"Writing text in loaded page\"],font,PdfPens.Red,PdfBrushes.Red,[New] PointF(-150,450))]                  |
|                                                                                                                                                                                                           |
| [lDoc.Save([\"Sample.pdf\"])]                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p132} 

 

[]{#related-topics}

