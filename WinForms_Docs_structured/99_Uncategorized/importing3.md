---
title: importing3.md
original_path: WinForms_Docs/99_Uncategorized/importing3.md
created_at: 2025-08-05
---






#### Importing {#importing style="tab-stops: 0pt"}

 

The integrated HTML to PDF Converter is implemented by using the **HtmlConverter** class. It basically includes the functionality of the HTML to PDF Converter product, and additionally offers the possibility to specify the position and the size of the PDF content.

 

The following code example illustrates this.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [// Convert web page into image.]                                                                                                                    |
|                                                                                                                                                                                                        |
| [HtmlConverter html = [new] HtmlConverter();]                                                                                                 |
|                                                                                                                                                                                                        |
| [Image][ img= html.ConvertToImage([\"www.syncfusion.com\"], ImageType.Metafile, 1024)]     |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [// Draw the image into the PDF document as metafile]                                                                                                |
|                                                                                                                                                                                                        |
| [// Create metafile image]                                                                                                                           |
|                                                                                                                                                                                                        |
| [PdfMetafile][ metafile = ([PdfMetafile])[PdfImage].FromImage(img);]    |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [// Specify the quality of the metafile]                                                                                                             |
|                                                                                                                                                                                                        |
| [metafile.Quality = 100;]                                                                                                                                          |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [// Set the layout format]                                                                                                                           |
|                                                                                                                                                                                                        |
| [PdfMetafileLayoutFormat][ format = [new] [PdfMetafileLayoutFormat]();] |
|                                                                                                                                                                                                        |
| [format.Break = [PdfLayoutBreakType].FitPage;]                                                                                                |
|                                                                                                                                                                                                        |
| [format.Layout = [PdfLayoutType].Paginate;]                                                                                                   |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [// Prevent text getting break at the page breaks]                                                                                                   |
|                                                                                                                                                                                                        |
| [format.SplitTextLines = [false];]                                                                                                            |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [// Draw the converted image to PDF]                                                                                                                 |
|                                                                                                                                                                                                        |
| [metafile.Draw(page, [new] [RectangleF](0, 0, img.Width, img.Height), format);]                                          |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [// Draw the image into the PDF document as bitmap]                                                                                                  |
|                                                                                                                                                                                                        |
| [PdfImage][ image = [new] [PdfBitmap](img);]                            |
|                                                                                                                                                                                                        |
| [PdfLayoutFormat][ format = [new] [PdfLayoutFormat]();]                 |
|                                                                                                                                                                                                        |
| [format.Break = [PdfLayoutBreakType].FitPage;]                                                                                                |
|                                                                                                                                                                                                        |
| [format.Layout = [PdfLayoutType].Paginate;]                                                                                                   |
|                                                                                                                                                                                                        |
| [image.Draw(page, [new] [RectangleF](0, 0, pageSize.Width, pageSize.Height), format);]                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\' Convert web page into image.]                                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [Dim][ html [As] HtmlConverter = [New] HtmlConverter()]                                            |
|                                                                                                                                                                                                                                   |
| [Dim][ img [As] Image = html.ConvertToImage([\"www.syncfusion.com\"], ImageType.Metafile, 1024)] |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\' Draw the image into the PDF document as metafile]                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [\' Create metafile image]                                                                                                                                                      |
|                                                                                                                                                                                                                                   |
| [Dim][ metafile [As] PdfMetafile = [CType](PdfImage.FromImage(img), PdfMetafile)]                  |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\' Specify the quality of the metafile]                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| [metafile.Quality = 100]                                                                                                                                                                      |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\' Set the layout format]                                                                                                                                                      |
|                                                                                                                                                                                                                                   |
| [Dim][ format [As] PdfMetafileLayoutFormat = [New] PdfMetafileLayoutFormat()]                      |
|                                                                                                                                                                                                                                   |
| [format.Break = PdfLayoutBreakType.FitPage]                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| [format.Layout = PdfLayoutType.Paginate]                                                                                                                                                      |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\' Prevent text getting break at the page breaks]                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [format.SplitTextLines = [False]]                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [\' Draw the converted image to PDF]                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [metafile.Draw(page, [New] RectangleF(0, 0, img.Width, img.Height), format)]                                                                                             |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\' Draw the image into the PDF document as bitmap]                                                                                                                             |
|                                                                                                                                                                                                                                   |
| [Dim][ image [As] PdfImage = [New] PdfBitmap(img)]                                                 |
|                                                                                                                                                                                                                                   |
| [Dim][ format [As] PdfLayoutFormat = [New] PdfLayoutFormat()]                                      |
|                                                                                                                                                                                                                                   |
| [format.Break = PdfLayoutBreakType.FitPage]                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| [format.Layout = PdfLayoutType.Paginate]                                                                                                                                                      |
|                                                                                                                                                                                                                                   |
| [image.Draw(page, [New] RectangleF(0, 0, pageSize.Width, pageSize.Height), format)]                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

