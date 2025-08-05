---
title: howtomeasurethestringwhoseendpositionisnotknown.md
original_path: WinForms_Docs/99_Uncategorized/howtomeasurethestringwhoseendpositionisnotknown.md
created_at: 2025-08-05
---






#### How To Measure the String Whose End Position Is Not Known? {#how-to-measure-the-string-whose-end-position-is-not-known style="tab-stops: 0pt"}

 

PdfFont provides the **MeasureString** method which determines the rectangle that a string should occupy on a PDF page. This information is used for relative positioning of several paragraphs of text.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| []                                                                                                                   |
|                                                                                                                                                                        |
| [// Create a font.]                                                                                                  |
|                                                                                                                                                                        |
| [PdfStandardFont font = [new] PdfStandardFont(PdfFontFamily.Symbol, 12, PdfFontStyle.Bold);]                  |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [// Measure the size of the text based on string format and font.]                                                   |
|                                                                                                                                                                        |
| [SizeF][ textSize = pdfFont.MeasureString(text, rect.Size, format);]              |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [// Draw the rectangle for the size of the text.]                                                                    |
|                                                                                                                                                                        |
| [page.Graphics.DrawRectangle(PdfPens.Red, [new] [RectangleF](rect.Location, textSize));] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [\' Create a font.]                                                                                                                                                                 |
|                                                                                                                                                                                                                                       |
| [Dim][ font [As] PdfStandardFont = [New] PdfStandardFont(PdfFontFamily.Symbol, 12, PdfFontStyle.Bold)] |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [\' Measure the size of the text based on string format and font. ]                                                                                                                 |
|                                                                                                                                                                                                                                       |
| [Dim][ textSize [As] SizeF = pdfFont.MeasureString(text, rect.Size, format)]                                                |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [\' Draw the rectangle for the size of the text.]                                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [page.Graphics.DrawRectangle(PdfPens.Red, [New] RectangleF(rect.Location, textSize))]                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p129} 

 

[]{#related-topics}

