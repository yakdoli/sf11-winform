---
title: creatingandembeddingpdflayersinthepdfdocument.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingandembeddingpdflayersinthepdfdocument.md
created_at: 2025-07-03
---






##### Creating and Embedding PDF Layers in the PDF Document {#creating-and-embedding-pdf-layers-in-the-pdf-document style="tab-stops: 0pt"}

To create PDF Layers, optional content should be implemented. The following code snippets explain the creation of optional content and the embedding of layers in a PDF document.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [C#]                                                                                                                                                         |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [//Add the layer]                                                                                                                                            |
|                                                                                                                                                                                                                |
| [PdfPageLayer][ layer = page.Layers.Add([\"Layer1\"]);]                                        |
|                                                                                                                                                                                                                |
| [PdfGraphics][ graphics = layer.Graphics;]                                                                             |
|                                                                                                                                                                                                                |
| [graphics.TranslateTransform(100, 60);]                                                                                                                                    |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [//Draw Arc ]                                                                                                                                                |
|                                                                                                                                                                                                                |
| [PdfPen][ pen = [new] [PdfPen]([Color].Red, 50);] |
|                                                                                                                                                                                                                |
| [RectangleF][ rect = [new] [RectangleF](0, 0, 50, 50);]                   |
|                                                                                                                                                                                                                |
| [graphics.DrawArc(pen, rect, 360, 360);]                                                                                                                                   |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [pen = [new] [PdfPen]([Color].Blue, 30);]                                                             |
|                                                                                                                                                                                                                |
| [graphics.DrawArc(pen, 0, 0, 50, 50, 360, 360);]                                                                                                                           |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [pen = [new] [PdfPen]([Color].Yellow, 20);]                                                           |
|                                                                                                                                                                                                                |
| [graphics.DrawArc(pen, rect, 360, 360);]                                                                                                                                   |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [pen = [new] [PdfPen]([Color].Green, 10);]                                                            |
|                                                                                                                                                                                                                |
| [graphics.DrawArc(pen, 0, 0, 50, 50, 360, 360);]                                                                                                                           |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [            ]                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [VB  ]                                                                                                                                          |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [\'Add the layer][]                                                                                         |
|                                                                                                                                                                                                   |
| [Dim][ layer [As] PdfPageLayer = page.Layers.Add([\"Layer1\"])] |
|                                                                                                                                                                                                   |
| [Dim][ graphics [As] PdfGraphics = layer.Graphics]                                      |
|                                                                                                                                                                                                   |
| [graphics.TranslateTransform(100, 60)]                                                                                                                        |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [\'Draw Arc ][]                                                                                             |
|                                                                                                                                                                                                   |
| [Dim][ pen [As] [New] PdfPen(Color.Red, 50)]                       |
|                                                                                                                                                                                                   |
| [Dim][ rect [As] [New] RectangleF(0, 0, 50, 50)]                   |
|                                                                                                                                                                                                   |
| [graphics.DrawArc(pen, rect, 360, 360)]                                                                                                                       |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [pen = [New] PdfPen(Color.Blue, 30)]                                                                                                     |
|                                                                                                                                                                                                   |
| [graphics.DrawArc(pen, 0, 0, 50, 50, 360, 360)]                                                                                                               |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [pen = [New] PdfPen(Color.Yellow, 20)]                                                                                                   |
|                                                                                                                                                                                                   |
| [graphics.DrawArc(pen, rect, 360, 360)]                                                                                                                       |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [pen = [New] PdfPen(Color.Green, 10)]                                                                                                    |
|                                                                                                                                                                                                   |
| [graphics.DrawArc(pen, 0, 0, 50, 50, 360, 360)[  ]]                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

