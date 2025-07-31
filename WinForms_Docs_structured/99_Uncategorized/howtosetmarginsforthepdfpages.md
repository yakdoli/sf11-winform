---
title: howtosetmarginsforthepdfpages.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetmarginsforthepdfpages.md
created_at: 2025-07-03
---






#### How to set margins for the PDF pages? {#how-to-set-margins-for-the-pdf-pages style="tab-stops: 0pt"}

 

Margins can be set on all sides or on a particular side of the page using the **PageSettings.Margins** property. Following are the options of this property:

 

[·      ]***All***-Sets margins size on all the sides

[·      ]***Bottom***-Sets the bottom margin size

[·      ]***Left***-Sets the left margin size

[·      ]***Top***-Sets the top margin size

[·      ]***Right***-Sets the right margin size

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                     |
|                                                                                                                                                    |
| []                                                                                               |
|                                                                                                                                                    |
| [//Adds a section to the document]                                                               |
|                                                                                                                                                    |
| [PdfSection][ section = doc.Sections.Add();] |
|                                                                                                                                                    |
| []                                                                                               |
|                                                                                                                                                    |
| [//Adds a page to the section]                                                                   |
|                                                                                                                                                    |
| [PdfPage][ page= section.Pages.Add();]       |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [//Sets Margin to the page ]                                                                     |
|                                                                                                                                                    |
| [section.PageSettings.Margins.All = 0;]                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [\'Adds a section to the document ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [Dim][ section ][As][ PdfSection = doc.Sections.Add()] |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [\'Adds a page to the section ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [PdfPage = section.Pages.Add()]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [\'Sets Margin to the page ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [section.PageSettings.Margins.All = 0]                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

