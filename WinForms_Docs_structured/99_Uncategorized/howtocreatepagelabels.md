---
title: howtocreatepagelabels.md
original_path: WinForms_Docs/99_Uncategorized/howtocreatepagelabels.md
created_at: 2025-08-05
---






#### How To Create Page Labels? {#how-to-create-page-labels style="tab-stops: 0pt"}

 

You will be able to find a Pages tab in Adobe Reader which contains small page images. Also you will be able to find text underneath each image. You can edit that text by using the **PdfPageLabel** class. This class allows specifying the prefix, numbering style, and starting number for a page group, which is a section. You can create and initialize an instance of this class and assign it to the **Section** property.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [// Create a new document class object.]                                                                                      |
|                                                                                                                                                                                 |
| [PdfDocument][ doc = [new] [PdfDocument]();]     |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [// Create few sections with few pages in each.]                                                                              |
|                                                                                                                                                                                 |
| [for][ ([int] i = 0; i \< 3; ++i)]                                    |
|                                                                                                                                                                                 |
| [{]                                                                                                                                         |
|                                                                                                                                                                                 |
| [PdfSection][ section = doc.Sections.Add();]                                               |
|                                                                                                                                                                                 |
| [PdfPageLabel][ label = [new] [PdfPageLabel]();] |
|                                                                                                                                                                                 |
| [label.Prefix = [\"Sec\"] + i + [\"-\"];]                                                     |
|                                                                                                                                                                                 |
| [section.PageLabel = label;]                                                                                                                |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [PdfPage][ page;]                                                                          |
|                                                                                                                                                                                 |
| [for][ ([int] j = 0; j \< 10; ++j)]                                   |
|                                                                                                                                                                                 |
| [{]                                                                                                                                         |
|                                                                                                                                                                                 |
| [page = section.Pages.Add();]                                                                                                               |
|                                                                                                                                                                                 |
| [}]                                                                                                                                         |
|                                                                                                                                                                                 |
| [}]                                                                                                                                         |
|                                                                                                                                                                                 |
| [doc.Save(filename);]                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]**                                                        |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [\' Create a new document class object.]                                                                                              |
|                                                                                                                                                                                         |
| [Private][ doc [As] PdfDocument = [New] PdfDocument()]   |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [\' Create few sections with few pages in each.]                                                                                      |
|                                                                                                                                                                                         |
| [For][ i [As] [Integer] = 0 [To] 2] |
|                                                                                                                                                                                         |
| [Dim][ section [As] PdfSection = doc.Sections.Add()]                          |
|                                                                                                                                                                                         |
| [Dim][ label [As] PdfPageLabel = [New] PdfPageLabel()]   |
|                                                                                                                                                                                         |
| [      label.Prefix = [\"Sec\"] & i & [\"-\"]]                                                        |
|                                                                                                                                                                                         |
| [      section.PageLabel = label]                                                                                                                   |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [Dim][ page [As] PdfPage]                                                     |
|                                                                                                                                                                                         |
| [      [For] j [As] [Integer] = 0 [To] 9]                       |
|                                                                                                                                                                                         |
| [               page = section.Pages.Add()]                                                                                                         |
|                                                                                                                                                                                         |
| [      [Next] j]                                                                                                               |
|                                                                                                                                                                                         |
| [Next][ i]                                                                                         |
|                                                                                                                                                                                         |
| [doc.Save(filename)]                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p115} 

 

[]{#related-topics}

