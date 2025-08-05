---
title: howtocreateaborderlesstable.md
original_path: WinForms_Docs/99_Uncategorized/howtocreateaborderlesstable.md
created_at: 2025-08-05
---






#### How To Create a Borderless Table? {#how-to-create-a-borderless-table style="tab-stops: 0pt"}

 

You can create a borderless table by making use of the **Style** property of the **PdfLightTable** class. This is achieved by setting the border color of the table to ***Transparent***. The following code example illustrates this.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [// Creating Border with transparent color.]                                                                                                                  |
|                                                                                                                                                                                                                 |
| [PdfPen][ borderPen = [new] [PdfPen]([Color].Transparent);] |
|                                                                                                                                                                                                                 |
| [borderPen.Width = 1.0f;]                                                                                                                                                   |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [// Assigning the border pen to table cell.]                                                                                                                  |
|                                                                                                                                                                                                                 |
| [PdfCellStyle defStyle = [new] PdfCellStyle();]                                                                                                        |
|                                                                                                                                                                                                                 |
| [defStyle.Font = font;]                                                                                                                                                     |
|                                                                                                                                                                                                                 |
| [defStyle.BorderPen = borderPen;]                                                                                                                                           |
|                                                                                                                                                                                                                 |
| [table.Style.DefaultStyle = defStyle; ]                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [\' Creating Border with transparent color.]                                                                                                 |
|                                                                                                                                                                                                |
| [Dim][ borderPen [As] PdfPen = [New] PdfPen(Color.Transparent)] |
|                                                                                                                                                                                                |
| [borderPen.Width = 1.0F]                                                                                                                                   |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [\' Assigning the border pen to table cell.]                                                                                                 |
|                                                                                                                                                                                                |
| [Dim][ defStyle [As] PdfCellStyle = [New] PdfCellStyle()]       |
|                                                                                                                                                                                                |
| [defStyle.Font = font]                                                                                                                                     |
|                                                                                                                                                                                                |
| [defStyle.BorderPen = borderPen]                                                                                                                           |
|                                                                                                                                                                                                |
| [table.Style.DefaultStyle = defStyle]                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

