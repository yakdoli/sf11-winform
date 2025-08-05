---
title: htmlstyledtext.md
original_path: WinForms_Docs/02_Concepts/htmlstyledtext.md
created_at: 2025-08-05
---






##### Html Styled Text {#html-styled-text style="tab-stops: 0pt"}

[] 

Essential PDF provides support to render the HTML string in a PDF document, which can flow to multiple pages by using the **PdfHTMLTextElement** class. The PdfHTMLTextElement class contains methods, which are used to render the specified HTML string in the PDF document. It draws the specified text string at the specified location with the specified size, brush and font. You can also align the text by using the **TextAlign** property.

[] 

The **PdfMetafileLayoutFormat** class enables to break the HTML text into multiple pages.

[] 

Supported Tags (Should be XHTML-compliant)

[] 

[·      ]Font

[·      ]B

[·      ]I

[·      ]U

[·      ]St

[·      ]sub

[·      ]sup

[·      ]BR

 

The following code example illustrates how to render the HTML string in a PDF document.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [// HtmlString]                                                                                                                                                           |
|                                                                                                                                                                                                                             |
| [string][ longText = [\"\<font color=\'#0000F8\'\>Essential PDF\</font\> is a \<u\>\<i\>.NET\</i\>\</u\> \"] +] |
|                                                                                                                                                                                                                             |
| [\"library with the capability to produce Adobe PDF files \"][;]                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [// Rendering HtmlText]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [PdfHTMLTextElement][ richTextElement = [new] [PdfHTMLTextElement](longText, font, brush);]  |
|                                                                                                                                                                                                                             |
| [richTextElement.TextAlign = [TextAlign].Justify;            ]                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [// Formatting Layout]                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [PdfMetafileLayoutFormat][ format = [new] [PdfMetafileLayoutFormat]();]                      |
|                                                                                                                                                                                                                             |
| [format.Layout = [PdfLayoutType].OnePage;]                                                                                                                         |
|                                                                                                                                                                                                                             |
| [format.Break = [PdfLayoutBreakType].FitPage;]                                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [// Drawing htmlString]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [richTextElement.Draw(page, [new] [RectangleF](30, 30, 600, page.GetClientSize().Height), format);]                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [\' HtmlString]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                  |
| [Dim][ longText [As] [String] = [\"\<font color=\'#0000F8\'\>Essential PDF\</font\> is a \<u\>\<i\>.NET\</i\>\</u\> \"] +] |
|                                                                                                                                                                                                                                                                                  |
| [\"library with the capability to produce Adobe PDF files \"]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                  |
| [\' Rendering HtmlText]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                  |
| [Dim][ richTextElement [As] PdfHTMLTextElement = [New] PdfHTMLTextElement(longText, font, brush)]                                                 |
|                                                                                                                                                                                                                                                                                  |
| [richTextElement.TextAlign = TextAlign.Justify]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                  |
| [\' Formatting Layout]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [Dim][ format [As] PdfMetafileLayoutFormat = [New] PdfMetafileLayoutFormat()]                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [format.Layout = PdfLayoutType.OnePage]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                  |
| [format.Break = PdfLayoutBreakType.FitPage]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                  |
| [\' Drawing htmlString]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                  |
| [richTextElement.Draw(page, [New] RectangleF(30, 30, 600, page.GetClientSize().Height), format)]                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

