---
title: margins1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\margins1.md
created_at: 2025-07-03
---






#### Margins {#margins style="tab-stops: 0pt"}

 

Page margins are the blank spaces between the worksheet data and the edges of the printed page, and hence provide better readability. Page margins can be used for items such as headers, footers and page numbers.

 

Excel allows to set the page margin through the Page Setup dialog box. Note that the page margins that you define in a given worksheet, are stored with that particular worksheet, when you save the workbook. You cannot change the default page margins for new workbooks.

 

{border="0"}

Figure 107: Page Setup - Margins[]

[] 

XlsIO has APIs to define the margins in a sheet through the properties of IPageSetup. It sets the value in terms of inches.

 

Following code example illustrates how to set the margin.

 

+---------------------------------------------------------------------------------------+
| **[\[C#\]]**                                      |
|                                                                                       |
| **[]**                                            |
|                                                                                       |
| [// Page Setup Using Margins.]      |
|                                                                                       |
| [sheet.PageSetup.LeftMargin = 2;]   |
|                                                                                       |
| [sheet.PageSetup.RightMargin = 2;]  |
|                                                                                       |
| [sheet.PageSetup.TopMargin = 2;]    |
|                                                                                       |
| [sheet.PageSetup.BottomMargin = 2;] |
+---------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                 |
|                                                                                      |
| **[]**                                           |
|                                                                                      |
| [\' Page Setup Using Margins.]     |
|                                                                                      |
| [sheet.PageSetup.LeftMargin = 2]   |
|                                                                                      |
| [sheet.PageSetup.RightMargin = 2]  |
|                                                                                      |
| [sheet.PageSetup.TopMargin = 2]    |
|                                                                                      |
| [sheet.PageSetup.BottomMargin = 2] |
+--------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 108: XlsIO with Margins[]

[] 

 

[]{#related-topics}

