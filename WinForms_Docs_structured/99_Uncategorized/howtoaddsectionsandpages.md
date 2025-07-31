---
title: howtoaddsectionsandpages.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaddsectionsandpages.md
created_at: 2025-07-03
---






#### How To Add Sections And Pages? {#how-to-add-sections-and-pages style="tab-stops: 0pt"}

 

Essential PDF enables to add any number of sections and pages. A PDF document should contain atleast one section. Each section can have any number of pages in it. PdfSection class is used to create sections and PdfPage class is used to add pages.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [PdfDocument][ document = [new] [PdfDocument]();] |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [//Adds a section to the document]                                                                                             |
|                                                                                                                                                                                  |
| [PdfSection section = doc.Sections.Add();]                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [//Adds a page to the section]                                                                                                 |
|                                                                                                                                                                                  |
| [PdfPage = section.Pages.Add();]                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]**                                                       |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [Dim][ document [As] PdfDocument = [New] PdfDocument()] |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [\'Adds a section to the document]                                                                                                   |
|                                                                                                                                                                                        |
| [Dim][ section [As] PdfSection = doc.Sections.Add()]                         |
|                                                                                                                                                                                        |
| []                                                                                                                                                 |
|                                                                                                                                                                                        |
| [\'Adds a page to the section]                                                                                                       |
|                                                                                                                                                                                        |
| [Dim][ page [As] PdfPage = section.Pages.Add()]                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

