---
title: howtodrawasoftmaskimageintoapdfdocument.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodrawasoftmaskimageintoapdfdocument.md
created_at: 2025-07-03
---






#### How To Draw a SoftMask Image Into a PDF Document? {#how-to-draw-a-softmask-image-into-a-pdf-document style="tab-stops: 0pt"}

 

Essential PDF supports drawing mask images over other images. The **Mask** property of the **PdfBitmap** class is used for drawing masked images.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [// Bitmap with Tiff image mask.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [PdfBitmap][ image = [new] [PdfBitmap](tifImage);]                                                                      |
|                                                                                                                                                                                                                                                        |
| [(image [as] [PdfBitmap]).Mask = [new] [PdfImageMask]([new] [PdfBitmap](bmpImage));] |
|                                                                                                                                                                                                                                                        |
| [page.Graphics.DrawString([\"Image mask\"], font, brush, [new] [PointF](10, 350));]                                                               |
|                                                                                                                                                                                                                                                        |
| [g.DrawImage(image, 10, 450);]                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                      |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [\' Bitmap with Tiff image mask.]                                                                                                     |
|                                                                                                                                                                                         |
| [Dim][ image [As] PdfBitmap = [New] PdfBitmap(tifImage)] |
|                                                                                                                                                                                         |
| [([TryCast](image, PdfBitmap)).Mask = [New] PdfImageMask([New] PdfBitmap(bmpImage))] |
|                                                                                                                                                                                         |
| [page.Graphics.DrawString([\"Image mask\"], font, brush, [New] PointF(10, 350))]                        |
|                                                                                                                                                                                         |
| [g.DrawImage(image, 10, 450)]                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

