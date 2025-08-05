---
title: orientation11.md
original_path: WinForms_Docs/99_Uncategorized/orientation11.md
created_at: 2025-08-05
---






#### Orientation {#orientation style="tab-stops: 0pt"}

 

While creating small worksheets, it is not necessary to change the direction/orientation of the pages, but some worksheets and charts require the width of the pages to be greater than its length.

 

Similar to the landscape painting, whose width is greater than the length, Landscape page orientation enables you to fit wider items on a page. A page, whose width is greater than the length, is called a Portrait orientation, like portraits of people.

 

Excel allows to change the orientation of the page, through the Page Setup dialog box. It allows to change the orientation to Landscape or Portrait.

 

{border="0"}

Figure 109: Page Setup - Page Orientation[]

 

XlsIO defines the orientation through the **Orientation** property of **IPageSetup**. Following code example illustrates how to set the page orientation.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                           |
| **[]**                                                                                                                                |
|                                                                                                                                                                           |
| [// Setting the Page Orientation as Portrait or Landscape.      ][  ] |
|                                                                                                                                                                           |
| [sheet.PageSetup.Orientation = ExcelPageOrientation.Landscape;]                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                      |
|                                                                                                                                                                           |
| **[]**                                                                                                                                |
|                                                                                                                                                                           |
| [\' Setting the Page Orientation as Portrait or Landscape.    ][    ] |
|                                                                                                                                                                           |
| [sheet.PageSetup.Orientation = ExcelPageOrientation.Landscape]                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 110: XlsIO with Page Orientation Set[]

[] 

 

[]{#related-topics}

