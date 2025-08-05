---
title: pagesetup.md
original_path: WinForms_Docs/99_Uncategorized/pagesetup.md
created_at: 2025-08-05
---








  









### Page Setup {#page-setup style="tab-stops: 0pt"}

 

In MS Excel, the way the spreadsheet fits onto paper can be controlled through the **Page Setup** dialog box. You can select the size and orientation of the paper, the width of the margins, what goes into the header and footer of each page, and the order of printing cells for sheets that will take several pieces of paper.

 


Note: Though the sample code uses sheet object, it is possible to read/write page setup options for chart worksheet and embedded chart using IChartPageSetup interface.


 

There may also be a need to change the first page number, which starts with \'1\', by default. This can be done through the page number customization options provided by the Page Setup dialog box.

 

+-----------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                          |
|                                                                                                           |
| []                                                                    |
|                                                                                                           |
| [sheet.PageSetup.AutoFirstPageNumber = [false];] |
|                                                                                                           |
| [sheet.PageSetup.FirstPageNumber = 2;]                                |
+-----------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                      |
|                                                                                                           |
| []                                                                    |
|                                                                                                           |
| [sheet.PageSetup.AutoFirstPageNumber = [false];] |
|                                                                                                           |
| [sheet.PageSetup.FirstPageNumber = 2;]                                |
+-----------------------------------------------------------------------------------------------------------+

[] 

Following topics explain how various other page setup options can be set by using XlsIO.

 

More:













