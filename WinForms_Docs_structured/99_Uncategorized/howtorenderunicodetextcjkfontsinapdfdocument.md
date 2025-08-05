---
title: howtorenderunicodetextcjkfontsinapdfdocument.md
original_path: WinForms_Docs/99_Uncategorized/howtorenderunicodetextcjkfontsinapdfdocument.md
created_at: 2025-08-05
---






#### How To Render Unicode Text \[CJK Fonts\] In a PDF Document? {#how-to-render-unicode-text-cjk-fonts-in-a-pdf-document style="tab-stops: 0pt"}

 

 Essential PDF provides support for Unicode languages. You can render unicode text with the help of the **PdfCjkStandardFont** class. Languages like Japanese, Korean, Simplified Chinese, Traditional Chinese, and so on, are classified under CJK Fonts.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [// Apply Cjk font for the chinese text.]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                        |
| [PdfCjkStandardFont][ font = [new] [PdfCjkStandardFont]([PdfCjkFontFamily].HeiseiKakuGothicW5, 12F, [PdfFontStyle].Regular);] |
|                                                                                                                                                                                                                                                                                                        |
| [page.Graphics.DrawString(unicode_text, font, [PdfBrushes].Black, [new] [RectangleF](0F, 0F, ([float])(page.Size.Width), ([float])(page.Size.Height)));]  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                  |
| [\' Apply Cjk font for the chinese text.]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                  |
| [Dim][ font [As] PdfCjkStandardFont = [New] PdfCjkStandardFont(PdfCjkFontFamily.HeiseiKakuGothicW5, 12.0F, PdfFontStyle.Regular)] |
|                                                                                                                                                                                                                                                                  |
| [page.Graphics.DrawString(unicode_text, font, PdfBrushes.Black, [New] RectangleF(0.0F, 0.0F, [CSng](page.Size.Width), [CSng](page.Size.Height)))]             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

You can also apply cjk fonts from disk and embed them. The following code example illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                                           |
| []                                                                                                                      |
|                                                                                                                                                                           |
| [//Add CJK font to the font collection]                                                                                 |
|                                                                                                                                                                           |
| [string font = \"gulim.ttf\";]                                                                                                        |
|                                                                                                                                                                           |
| [PrivateFontCollection][ fcol = new [PrivateFontCollection()];] |
|                                                                                                                                                                           |
| [fcol.AddFontFile(font);]                                                                                                             |
|                                                                                                                                                                           |
| [Font][ f = new [Font](fcol.Families\[0\], 14);]                |
|                                                                                                                                                                           |
| [PdfFont font = new PdfTrueTypeFont(f, true);]                                                                                        |
|                                                                                                                                                                           |
| [string koreanText = \"korean.txt\";]                                                                                                 |
|                                                                                                                                                                           |
| []                                                                                                                      |
|                                                                                                                                                                           |
| [//Read the text from text file]                                                                                        |
|                                                                                                                                                                           |
| [StreamReader reader = new StreamReader(koreanText, Encoding.Unicode);]                                                               |
|                                                                                                                                                                           |
| [string text = reader.ReadToEnd();]                                                                                                   |
|                                                                                                                                                                           |
| [reader.Close();]                                                                                                                     |
|                                                                                                                                                                           |
| [          ]                                                                                                                          |
|                                                                                                                                                                           |
| [page.Graphics.DrawString(text, font, brush,PointF.Empty);]                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                        |
|                                                                                                                                                                           |
| []                                                                                                                      |
|                                                                                                                                                                           |
| [//Add CJK font to the font collection]                                                                                 |
|                                                                                                                                                                           |
| [string font = \"gulim.ttf\";]                                                                                                        |
|                                                                                                                                                                           |
| [PrivateFontCollection][ fcol = new [PrivateFontCollection()];] |
|                                                                                                                                                                           |
| [fcol.AddFontFile(font);]                                                                                                             |
|                                                                                                                                                                           |
| [Font][ f = new [Font](fcol.Families\[0\], 14);]                |
|                                                                                                                                                                           |
| [PdfFont font = new PdfTrueTypeFont(f, true);]                                                                                        |
|                                                                                                                                                                           |
| [string koreanText = \"korean.txt\";]                                                                                                 |
|                                                                                                                                                                           |
| []                                                                                                                      |
|                                                                                                                                                                           |
| [//Read the text from text file]                                                                                        |
|                                                                                                                                                                           |
| [StreamReader reader = new StreamReader(koreanText, Encoding.Unicode);]                                                               |
|                                                                                                                                                                           |
| [string text = reader.ReadToEnd();]                                                                                                   |
|                                                                                                                                                                           |
| [reader.Close();]                                                                                                                     |
|                                                                                                                                                                           |
| [          ]                                                                                                                          |
|                                                                                                                                                                           |
| [page.Graphics.DrawString(text, font, brush,PointF.Empty);]                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

