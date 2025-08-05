---
title: howtounfreezetherowsandcolumnsinxlsio.md
original_path: WinForms_Docs/99_Uncategorized/howtounfreezetherowsandcolumnsinxlsio.md
created_at: 2025-08-05
---








  









### How to unfreeze the rows and columns in XlsIO? {#how-to-unfreeze-the-rows-and-columns-in-xlsio style="tab-stops: 0pt"}

 

You can unfreeze rows and columns in XlsIO by using the RemovePanes method. The following code example illustrates this.

 

+--------------------------------------------------------------------------+
| **[\[C#\]]**                         |
|                                                                          |
| []                     |
|                                                                          |
| [sheet.Range\[8, 1\].FreezePanes();] |
|                                                                          |
| [sheet.RemovePanes();]               |
+--------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------+
| **[\[VB.NET\]]**                  |
|                                                                       |
| []                                |
|                                                                       |
| [sheet.Range(8, 1).FreezePanes()] |
|                                                                       |
| [sheet.RemovePanes()]             |
+-----------------------------------------------------------------------+

 

[]{#related-topics}

