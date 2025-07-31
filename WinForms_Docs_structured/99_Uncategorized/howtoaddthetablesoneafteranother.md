---
title: howtoaddthetablesoneafteranother.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaddthetablesoneafteranother.md
created_at: 2025-07-03
---






#### How To Add the Tables One After Another? {#how-to-add-the-tables-one-after-another style="tab-stops: 0pt"}

 

You can draw the table relative to the position of the previous table by using the **PdfLayoutResult** class. This class stores the boundary values of the table that is drawn. By using the boundary values, you can set the starting position of the table relative to the height of the previous table. The following code example illustrates this.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [// Drawing first table.]                                                                                                                           |
|                                                                                                                                                                                                       |
| [PdfLightTable][ table = [new] [PdfLightTable]();]                     |
|                                                                                                                                                                                                       |
| [table.DataSource = dt;]                                                                                                                                          |
|                                                                                                                                                                                                       |
| [table.Style.ShowHeader = [true];]                                                                                                           |
|                                                                                                                                                                                                       |
| [PdfLayoutResult][ result = table.Draw(page, [new] [PointF](0, 20));]  |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [// Calculating Second table position. ]                                                                                                            |
|                                                                                                                                                                                                       |
| [RectangleF][ bounds = result.Bounds;]                                                                           |
|                                                                                                                                                                                                       |
| [PointF][ location = [new] [PointF](bounds.Left, bounds.Bottom + 30);] |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [// Drawing the second table.]                                                                                                                      |
|                                                                                                                                                                                                       |
| [table.Draw(page, location);]                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                          |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [ [\' Drawing first table.]]                                                                                                                      |
|                                                                                                                                                                                                             |
| [Dim][ table [As] PdfLightTable = [New] PdfLightTable()]                     |
|                                                                                                                                                                                                             |
| [table.DataSource = dt]                                                                                                                                                 |
|                                                                                                                                                                                                             |
| [table.Style.ShowHeader = [True]]                                                                                                                  |
|                                                                                                                                                                                                             |
| [Dim][ result [As] PdfLayoutResult = table.Draw(page, [New] PointF(0, 20))]  |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\' Calculating Second table position.]                                                                                                                   |
|                                                                                                                                                                                                             |
| [Dim][ bounds [As] RectangleF = result.Bounds]                                                    |
|                                                                                                                                                                                                             |
| [Dim][ location [As] PointF = [New] PointF(bounds.Left, bounds.Bottom + 30)] |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [ [\' Drawing the second table.]]                                                                                                                 |
|                                                                                                                                                                                                             |
| [table.Draw(page, location)]                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

