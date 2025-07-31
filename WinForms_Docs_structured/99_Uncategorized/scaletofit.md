---
title: scaletofit.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scaletofit.md
created_at: 2025-07-03
---








  









### Scale To Fit {#scale-to-fit style="tab-stops: 0pt"}

 

Scaling lets you specify a certain percentage to reduce or enlarge your worksheet. The \"Fit to\" Page feature allows you to force the worksheet to print on a specific number of pages, without having to calculate the percentage yourself.

 

When you need to print a worksheet that is too large to fit on the page, without making the font very small, you can use the Orientation and Scaling features.

 

Excel enables this feature through the Page Setup dialog box.

 

{border="0"}

Figure 115: Page Setup - Page Scaling[]

 

XlsIO allows to scale the pages length and width wise, while printing. The following code example illustrates this.

 

+---------------------------------------------------------------------------+
| **[\[C#\]]**                          |
|                                                                           |
| **[]**                                |
|                                                                           |
| [sheet.PageSetup.FitToPagesTall = 2;] |
|                                                                           |
| [sheet.PageSetup.FitToPagesWide = 3;] |
+---------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------+
| **[\[VB.NET\]]**                      |
|                                                                           |
| **[]**                                |
|                                                                           |
| [sheet.PageSetup.FitToPagesTall = 2;] |
|                                                                           |
| [sheet.PageSetup.FitToPagesWide = 3;] |
+---------------------------------------------------------------------------+

 

 

[]{#related-topics}

