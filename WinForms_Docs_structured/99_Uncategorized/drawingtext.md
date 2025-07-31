---
title: drawingtext.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drawingtext.md
created_at: 2025-07-03
---






##### Drawing Text {#drawing-text style="tab-stops: 0pt"}

 

This section elaborates on various procedures for drawing the text in a PDF document.

 

The following are the procedures used:

 

[·      ]Using DrawString

[·      ]Paginating the text area

[·      ]String Formatting and

[·      ]RTF Support

[] 

Using DrawString

[] 

**PdfGraphics** class contains plenty of **DrawString** methods. It draws the specified text string at the specified location with the specified size, brush and font. The format of the methods is similar to the **System.Drawing.Graphics.DrawString** methods.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                    |
| [public ][DrawString( [string] s, [PdfFont] font, [PdfBrush] brush, [PointF] point );]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| [public ][DrawString( [string] s, [PdfFont] font, [PdfBrush] brush, [PointF] point, [PdfStringFormat] format );]                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [public ][DrawString( [string] s, [PdfFont] font, [PdfBrush] brush, [float] x, [float] y );]                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [public ][DrawString( [string] s, [PdfFont] font, [PdfBrush] brush, [float] x, [float] y, [PdfStringFormat] format );] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [public ][DrawString( [string] s, [PdfFont] font, [PdfPen] pen, [PointF] point );]                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following code example illustrates this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [PdfLoadedDocument][ lDoc = [new] [PdfLoadedDocument](filename);]                                                                         |
|                                                                                                                                                                                                                                                                          |
| [page = lDoc.Pages.Add() [as] [PdfPage];]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [PdfGraphics][ g = page.Graphics;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                          |
| [PdfFont][ font = [new] [PdfStandardFont]([PdfFontFamily].Helvetica, 14, [PdfFontStyle].Bold);] |
|                                                                                                                                                                                                                                                                          |
| [g.DrawString([\"Polygon\"], font, [PdfBrushes].DarkBlue, [new] [PointF](50, 0));]                                                             |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [lDoc.Save(filename);]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| [lDoc.Close();]                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                  |
| [Dim][ lDoc [As] Syncfusion.Pdf.Parsing.PdfLoadedDocument = [New] Syncfusion.Pdf.Parsing.PdfLoadedDocument(filename)]                             |
|                                                                                                                                                                                                                                                                                  |
| [page = [TryCast](lDoc.Pages.Add(), PdfPage)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [Dim][ g [As] Syncfusion.Pdf.Graphics.PdfGraphics = page.Graphics]                                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [Dim][ font [As] Syncfusion.Pdf.Graphics.PdfFont = [New] Syncfusion.Pdf.Graphics.PdfStandardFont(PdfFontFamily.Helvetica, 14, PdfFontStyle.Bold)] |
|                                                                                                                                                                                                                                                                                  |
| [g.DrawString([\"Polygon\"], font, PdfBrushes.DarkBlue, [New] PointF(50, 0))]                                                                                                                    |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [lDoc.Save(filename)]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                  |
| [lDoc.Close()]                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2\. Paginating the text Area

[] 

**PdfTextElement** class represents the text area with the ability to span several pages. The **Layout** property of the **PDFLayoutFormat** class enables to break the text into multiple pages. Unicode text is also supported by this method.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Create a text element with large amount of text.]                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [PdfTextElement][ element = [new] [PdfTextElement](text, font);]                                           |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Set the properties for the text element.]                                                                                                                                           |
|                                                                                                                                                                                                                                           |
| [element.Brush = [new] [PdfSolidBrush]([Color].Black);]                                                                                |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Set the string format. This can be used for setting unicode text.]                                                                                                                  |
|                                                                                                                                                                                                                                           |
| [element.StringFormat = format;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Set the layout format properties to make the text flow through multiple pages.]                                                                                                     |
|                                                                                                                                                                                                                                           |
| [PdfLayoutFormat][ layoutFormat = [new] [PdfLayoutFormat]();]                                              |
|                                                                                                                                                                                                                                           |
| [layoutFormat.Break = [PdfLayoutBreakType].FitPage;]                                                                                                                             |
|                                                                                                                                                                                                                                           |
| [layoutFormat.Layout = [PdfLayoutType].Paginate;]                                                                                                                                |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Set the bounds.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [RectangleF][ bounds = [new] [RectangleF]([PointF].Empty, page.Graphics.ClientSize);] |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Draw the text element.]                                                                                                                                                             |
|                                                                                                                                                                                                                                           |
| [element.Draw(page, bounds, layoutFormat);]                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [\' Create a text element with large amount of text.]                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [Dim][ element [As] Syncfusion.Pdf.Graphics.PdfTextElement = [New] Syncfusion.Pdf.Graphics.PdfTextElement(Text, Font)] |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [\' Set the properties for the text element.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [element.Brush = [New] PdfSolidBrush(Color.Black)]                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [\' Set the string format. This can be used for setting unicode text.]                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [element.StringFormat = format]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [\' Set the layout format properties to make the text flow through multiple pages.]                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [Dim][ layoutFormat [As] Syncfusion.Pdf.Graphics.PdfLayoutFormat = [New] Syncfusion.Pdf.Graphics.PdfLayoutFormat()]    |
|                                                                                                                                                                                                                                                       |
| [layoutFormat.Break = PdfLayoutBreakType.FitPage]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [layoutFormat.Layout = PdfLayoutType.Paginate]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [\' Set the bounds.]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [Dim][ bounds [As] RectangleF = [New] RectangleF(PointF.Empty, page.Graphics.ClientSize)]                              |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [\' Draw the text element.]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [element.Draw(page, bounds, layoutFormat)]                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3\. String Formatting

[] 

For dedicated presentation of text in a PDF document, use a PdfStringFormat object. **PdfStringFormat** class provides support for the following features:

[] 

[·      ]CharacterSpacing, WordSpacing and LineSpacing

[·      ]Right-To-Left languages such as Arabic, Hebrew, Urdu, and so on

[·      ]Center, Left, Right and Justify text alignments

[·      ]Subscript and superscript modes

[·      ]ParagraphIndent customization

[·      ]WordWrapType style

[·      ]MeasureTrailingSpaces

[] 

4\. RTF Support

[] 

The **Rich Text Format (RTF)** specification is a method of encoding formatted text and graphics such as bold characters and typefaces, document formatting and structures, for easy transfer between applications. Essential PDF supports drawing RTF text into a PDF document by using the **FromRtf** method in the **PdfImage** class.

[] 

You can draw RTF text by converting it into a bitmap or metafile image. Converting RTF text into a bitmap file, provides improved performance, while converting RTF text into a metafile image, provides high resolution and searchable text.

 

The following code example illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                       |
| [public][ [PdfImage] FromRtf( [string] rtf, [float] width, [PdfImageType] type )]                                      |
|                                                                                                                                                                                                                                                                                                       |
| [public][ [PdfImage] FromRtf( [string] rtf, [float] width, [float] height, [PdfImageType] type )] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [Public][ PdfImage FromRtf([String] rtf, [single] width, PdfImageType type)]                                       |
|                                                                                                                                                                                                                                                   |
| [Public][ PdfImage FromRtf([String] rtf, [single] width, [single] height, PdfImageType type)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

For More Information Refer:

[] 

[]{.UGHyperlink}

[[]]{.UGHyperlink} 

 

 

[]{#related-topics}

