---
title: howtoinsertatableintheheader.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoinsertatableintheheader.md
created_at: 2025-07-03
---






#### How To Insert a Table In The Header? {#how-to-insert-a-table-in-the-header style="tab-stops: 0pt"}

 

**PDFLightTable** model of Essential PDF provides an option to insert tables in headers by using page templates.

 

The following steps illustrate how to insert tables in the header:

 

1.   Create a table with some datasource by using the PdfLightTable class.

2.   Create a Page template where the table has to be placed.

3.   Draw the table in the template.

 

You can also insert images and other graphical objects in the table cell and render it in the header.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [//Create page template  ]                                                                                                                          |
|                                                                                                                                                                                                       |
| [PdfPageTemplateElement][ top = [new] [PdfPageTemplateElement](rect);] |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [//Create a table]                                                                                                                                  |
|                                                                                                                                                                                                       |
| [PdfLightTable table = [new] PdfLightTable();]                                                                                               |
|                                                                                                                                                                                                       |
| [table.DataSource = dataTable;]                                                                                                                                   |
|                                                                                                                                                                                                       |
| [table.Style.CellPadding = 16;]                                                                                                                                   |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [//Draw the table in template]                                                                                                                      |
|                                                                                                                                                                                                       |
| [table.Draw(top.Graphics);]                                                                                                                                       |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [//Place the template at the top.   ]                                                                                                               |
|                                                                                                                                                                                                       |
| [doc.Template.Top = top;]                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                          |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [\'Create page template  ]                                                                                                                                |
|                                                                                                                                                                                                             |
| [Dim][ top [As] PdfPageTemplateElement = [New] PdfPageTemplateElement(rect)] |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\'Create a table]                                                                                                                                        |
|                                                                                                                                                                                                             |
| [Dim][ table [As] PdfLightTable = [New] PdfLightTable()]                     |
|                                                                                                                                                                                                             |
| [table.DataSource = dataTable]                                                                                                                                          |
|                                                                                                                                                                                                             |
| [table.Style.CellPadding = 16]                                                                                                                                          |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\'Draw the table in template]                                                                                                                            |
|                                                                                                                                                                                                             |
| [table.Draw(top.Graphics)]                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\'Place the template at the top.   ]                                                                                                                     |
|                                                                                                                                                                                                             |
| [doc.Template.Top = top]                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p128} 

 

[]{#related-topics}

