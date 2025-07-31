---
title: addinganewpage.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addinganewpage.md
created_at: 2025-07-03
---






#### Adding a New Page {#adding-a-new-page style="tab-stops: 0pt"}

[] 

A new page can be created in the existing pdf document or an existing page can be removed from the pdf document. This section discusses the following:

[] 

1.   Creating a page

2.   Removing a page

[] 

Creating a page

 

To add a new page to a PDF document that was created by an anonymous user, do the following:

 

1.   Pass the path of that particular document to the **PdfLoadedDocument** constructor

2.   Call the **doc.Pages.Add** method.

[] 

This will create an empty page with the default parameters.

 

{border="0"} You can also specify the size and margins for the new page.

 

The following code snippet illustrates how to create a new page in the pdf document.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [PdfLoadedDocument][ lDoc = [new] [PdfLoadedDocument](filename);] |
|                                                                                                                                                                                                  |
| [page = lDoc.Pages.Add() [as] [PdfPage];]                                                                          |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [g = page.Graphics;]                                                                                                                                         |
|                                                                                                                                                                                                  |
| [text = [\"Page 2\"];]                                                                                                                |
|                                                                                                                                                                                                  |
| [g.DrawString(text, font, PdfBrushes.Black, [PointF].Empty);]                                                                           |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [filename = OutputPath + [\"AddNewPages.pdf\"];]                                                                                      |
|                                                                                                                                                                                                  |
| [lDoc.Save(filename);]                                                                                                                                       |
|                                                                                                                                                                                                  |
| [lDoc.Close();]                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]**                                                   |
|                                                                                                                                                                                    |
| []                                                                                                                               |
|                                                                                                                                                                                    |
| [Dim][ lDoc [As] [New] PdfLoadedDocument(filename)] |
|                                                                                                                                                                                    |
| [page = [TryCast](lDoc.Pages.Add(), PdfPage) ]                                                                            |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [g = page.Graphics ]                                                                                                                           |
|                                                                                                                                                                                    |
| [text = [\"Page 2\"] ]                                                                                                  |
|                                                                                                                                                                                    |
| [g.DrawString(text, font, PdfBrushes.Black, PointF.Empty) ]                                                                                    |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [filename = OutputPath + [\"AddNewPages.pdf\"] ]                                                                        |
|                                                                                                                                                                                    |
| [lDoc.Save(filename) ]                                                                                                                         |
|                                                                                                                                                                                    |
| [lDoc.Close() ]                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

{border="0"}Note: You can use the page\'s Graphics, but should not use the graphics objects that require the page to layout.


 

A new page is added to the pdf document.

 

Removing a page

[] 

You can also remove pages from the existing PDF document by using the following methods of the **PdfLoadedPageCollection** class.

[] 

[·      ]Remove

[·      ]RemoveAt

 

The following code snippet illustrates how to remove an existing page from the pdf document.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [PdfLoadedDocument][ doc = [new] [PdfLoadedDocument]([\"Sample.pdf\"]);] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [// Removes the page by passing the PDF page]                                                                                                                                |
|                                                                                                                                                                                                                                |
| [doc.Pages.Remove(doc.Pages\[1\]);]                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [// Removes the page by specifying the page index]                                                                                                                           |
|                                                                                                                                                                                                                                |
| [doc.Pages.RemoveAt(2);]                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                        |
|                                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [Dim][ doc [As] PdfLoadedDocument = [New] PdfLoadedDocument(\"Sample.pdf\")] |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [\' Removes the page by passing the PDF page]                                                                                                             |
|                                                                                                                                                                                                             |
| [doc.Pages.Remove(doc.Pages(1))]                                                                                                                                        |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [\' Removes the page by specifying the page index]                                                                                                        |
|                                                                                                                                                                                                             |
| [doc.Pages.RemoveAt(2)]                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

