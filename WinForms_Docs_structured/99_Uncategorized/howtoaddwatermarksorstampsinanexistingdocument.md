---
title: howtoaddwatermarksorstampsinanexistingdocument.md
original_path: WinForms_Docs/99_Uncategorized/howtoaddwatermarksorstampsinanexistingdocument.md
created_at: 2025-08-05
---








  









### How To Add Watermarks Or Stamps In an Existing Document? {#how-to-add-watermarks-or-stamps-in-an-existing-document style="tab-stops: 0pt"}

 

You can add watermarks or stamps in an existing document by adding transparent images or text on the pages. The following code example illustrates this.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [PdfLoadedDocument][ lDoc = [new] [PdfLoadedDocument](txtUrl.Text);]                                                   |
|                                                                                                                                                                                                                                                       |
| [PdfFont][ font = [new] [PdfStandardFont]([PdfFontFamily].Helvetica, 36f);]                       |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [foreach][ ([PdfPageBase] lPage [in] lDoc.Pages)]                                                                      |
|                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [PdfGraphics][ g = lPage.Graphics;]                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [PdfGraphicsState][ state = g.Save();]                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [g.SetTransparency(0.25f);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [g.RotateTransform(-40);]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [g.DrawString([\"Stamping text\"], font, [PdfPens].Red, [PdfBrushes].Red, [new] [PointF](-150, 450));] |
|                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [lDoc.Save([\"Sample.pdf\"]);]                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ lDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(txtUrl.Text)]        |
|                                                                                                                                                                                                                  |
| [Dim][ font [As] PdfFont = [New] PdfStandardFont(PdfFontFamily.Helvetica, 36.0F)] |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ lPage [As] PdfPageBase]                                                                         |
|                                                                                                                                                                                                                  |
| [For][ [Each] lPage [In] lDoc.Pages]                                              |
|                                                                                                                                                                                                                  |
| [Dim][ g [As] PdfGraphics = lPage.Graphics]                                                            |
|                                                                                                                                                                                                                  |
| [Dim][ state [As] PdfGraphicsState = g.Save()]                                                         |
|                                                                                                                                                                                                                  |
| [      g.SetTransparency(0.25f)]                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [      g.RotateTransform(-40)]                                                                                                                                               |
|                                                                                                                                                                                                                  |
| [      g.DrawString([\"Stamping text\"],font,PdfPens.Red,PdfBrushes.Red,[New] PointF(-150,450))]                                 |
|                                                                                                                                                                                                                  |
| [Next]                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [lDoc.Save([\"Sample.pdf\"])]                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

