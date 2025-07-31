---
title: howtofindtheendpositionofatable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtofindtheendpositionofatable.md
created_at: 2025-07-03
---






#### How To Find the End Position Of a Table? {#how-to-find-the-end-position-of-a-table style="tab-stops: 0pt"}

[] 

There is often a need to determine the end position of a published table since the next table needs to be positioned after the first one. This position is determined by using the **PdfLightTableLayoutResult** object of the table returned by the **PdfLightTable.Draw** method. This finds the exact position of the table, even if it spans for multiple pages. PdfLightTableLayoutResult has several methods to work with the bounds and page where the table ends.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [// Draw a large table that can span for multiple pages and get the result.]                                                                   |
|                                                                                                                                                                                                  |
| [PdfLightTableLayoutResult result = table.Draw(page, [PointF].Empty);]                                                                  |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [// Get the location where the table ends]                                                                                                     |
|                                                                                                                                                                                                  |
| [PointF][ location = [new] [PointF](bounds.Left, bounds.Bottom);] |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [// Draw another table just below the previous table ]                                                                                         |
|                                                                                                                                                                                                  |
| [table.Draw(result.Page, location);]                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                   |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [\' Draw a large table that can span for multiple pages and get the result.]                                                                         |
|                                                                                                                                                                                                        |
| [Dim][ result [As] PdfLightTableLayoutResult = table.Draw(page, PointF.Empty)]               |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [\' Get the location where the table ends]                                                                                                           |
|                                                                                                                                                                                                        |
| [Dim][ location [As] PointF = [New] PointF(bounds.Left, bounds.Bottom)] |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [\' Draw another table just below the previous table ]                                                                                               |
|                                                                                                                                                                                                        |
| [table.Draw(result.Page, location)]                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

