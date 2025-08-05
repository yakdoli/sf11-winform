---
title: papersize.md
original_path: WinForms_Docs/99_Uncategorized/papersize.md
created_at: 2025-08-05
---






#### Paper Size {#paper-size style="tab-stops: 0pt"}

**[]** 

In order to fit information on a page or change the appearance of the page, you may want to customize your page layout. One better option is to change the paper size of the worksheet, as per the need.

[] 

The default paper size in Excel is 8 1/2\" x 11\" sheets, but it can be changed through the **Page Setup** dialog box. XlsIO allows to change the paper size through the **PaperSize** property.

[] 

{border="0"}

Figure 111: Page Setup - Page \[Paper Size\][]

[] 

Following code example illustrates how to set the paper size in XlsIO.

[] 

+---------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                         |
| []                                                                  |
|                                                                                                         |
| [// Setting the Paper Type.]                          |
|                                                                                                         |
| [sheet.PageSetup.PaperSize = ExcelPaperSize.PaperA3;] |
+---------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                   |
|                                                                                                        |
| []                                                                 |
|                                                                                                        |
| [\' Setting the Paper Type.]                         |
|                                                                                                        |
| [sheet.PageSetup.PaperSize = ExcelPaperSize.PaperA3] |
+--------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

