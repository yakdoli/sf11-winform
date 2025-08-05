---
title: howtoeditheaderinpdfgrid.md
original_path: WinForms_Docs/04_Controls/Grid/howtoeditheaderinpdfgrid.md
created_at: 2025-08-05
---






#### How to edit header in PdfGrid? {#how-to-edit-header-in-pdfgrid style="tab-stops: 0pt"}

 

When data source is set to PdfGrid, captions from source will automatically add as header. This header can be edited to display any custom text.


Note: Editing text will affect only the PdfGrid and will not reflect in data source.


The following is the code snippet:

 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                          |
|                                                                                                                          |
|                                                                                                                          |
| [// Edit cell value in header.]                                        |
|                                                                                                                          |
| [pdfGrid.Headers\[0\].Cells\[0\].Value = [\"Employee ID\"];] |
+--------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                  |
|                                                                                                                     |
|                                                                                                                     |
|                                                                                                                     |
| [\' Edit cell value in header.]                                   |
|                                                                                                                     |
| [pdfGrid.Headers(0).Cells(0).Value = [\"Employee ID\"]] |
+---------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

