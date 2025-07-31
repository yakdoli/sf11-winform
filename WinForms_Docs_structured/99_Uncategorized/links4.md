---
title: links4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\links4.md
created_at: 2025-07-03
---






##### Links {#links style="tab-stops: 0pt"}

[] 

A hyperlink, which is more commonly called a link, is an electronic connection between one web page and other web pages on the same web site, or web pages located on another web site. More specifically, a hyperlink is a connection between one page of a hypertext document to another.

[] 

You can create hyperlinks in a PDF document by using the **PdfTextWebLink** class. The **DrawTextWebLink** method is used to draw hyperlinks in PDF pages.

 

The following code example illustrates how to draw hyperlinks.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [// Create the Text Web Link]                                                                                                        |
|                                                                                                                                                                                        |
| [PdfTextWebLink][ textLink = [new] [PdfTextWebLink]();] |
|                                                                                                                                                                                        |
| [textLink.Url = [\"http://www.google.com\"];]                                                                               |
|                                                                                                                                                                                        |
| [textLink.Text = [\"Google Search\"];]                                                                                      |
|                                                                                                                                                                                        |
| [textLink.Brush = brush;]                                                                                                                          |
|                                                                                                                                                                                        |
| [textLink.Font = font;]                                                                                                                            |
|                                                                                                                                                                                        |
| [textLink.Pen = [PdfPens].Brown;]                                                                                             |
|                                                                                                                                                                                        |
| [textLink.DrawTextWebLink(page, [new] [PointF](10, 40));]                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\' Create the Text Web Link]                                                                                                              |
|                                                                                                                                                                                              |
| [Dim][ textLink [As] PdfTextWebLink = [New] PdfTextWebLink()] |
|                                                                                                                                                                                              |
| [textLink.Url = \"http://www.google.com\"]                                                                                                               |
|                                                                                                                                                                                              |
| [textLink.Text = \"Google Search\"]                                                                                                                      |
|                                                                                                                                                                                              |
| [textLink.Brush = brush]                                                                                                                                 |
|                                                                                                                                                                                              |
| [textLink.Font = font]                                                                                                                                   |
|                                                                                                                                                                                              |
| [textLink.Pen = PdfPens.Brown]                                                                                                                           |
|                                                                                                                                                                                              |
| [textLink.DrawTextWebLink(page, [New] PointF(10, 40))]                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

