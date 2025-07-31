---
title: howtoinsertsectionbreaks.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoinsertsectionbreaks.md
created_at: 2025-07-03
---








  









## How to insert section breaks? {#how-to-insert-section-breaks style="LINE-HEIGHT: 115%; TEXT-INDENT: -28.8pt; MARGIN: 10pt 0pt 0pt 28.8pt; tab-stops: 28.8pt"}

Essential DocIO provides direct support to insert section breaks to Word documents. You can insert a section break to a Word document by using the InsertSectionBreak method of WParagraph class.

The following code snippets illustrate how to insert a section break:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                      |
| [//Inserting a section break and it returns a newly created section.]                                                                                                              |
|                                                                                                                                                                                                                                      |
| [WSection][ section = paragraph.][InsertSectionBreak();]                                                    |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [//Inserting a section break of the specified type and it returns a newly created section.]                                                                                        |
|                                                                                                                                                                                                                                      |
| [WSection][ section = paragraph.][InsertSectionBreak([SectionBreakCode].EvenPage);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\'][Inserting a section break and it returns a newly created section.]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ ][section ][As ][WSection][ = paragraph.][InsertSectionBreak()]                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\'][Inserting a section break of the specified type and it returns a newly created section.]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ ][section ][As ][WSection][ = paragraph.][InsertSectionBreak([SectionBreakCode].EvenPage)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

