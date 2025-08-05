---
title: howtosetwidthfortable.md
original_path: WinForms_Docs/99_Uncategorized/howtosetwidthfortable.md
created_at: 2025-08-05
---






#### How to set width for Table? {#how-to-set-width-for-table style="tab-stops: 0pt"}

 

By default, both PdfLightTable and PdfGrid classes automatically calculate width if one is not specified during Draw. However, it is possible to specify width using one of the overloads in Draw method. The following is the code snippet.

 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                       |
|                                                                                                                       |
|                                                                                                                       |
| [// Draw PdfLightTable specified width.]                            |
|                                                                                                                       |
| [pdfLightTable.Draw(pdfGraphics, [PointF].Empty, width);] |
|                                                                                                                       |
| [pdfLightTable.Draw(pdfGraphics, xPos, yPos, width);]                             |
|                                                                                                                       |
| [pdfLightTable.Draw(pdfPage, xPos, yPos, width);]                                 |
|                                                                                                                       |
| [pdfLightTable.Draw(pdfPage, xPos, yPos, width, pdfLightTableLayoutFormat);]      |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [// Draw PdfGrid with specified width.]                             |
|                                                                                                                       |
| [pdfGrid.Draw(pdfGraphics, [PointF].Empty, width);]       |
|                                                                                                                       |
| [pdfGrid.Draw(pdfGraphics, xPos, yPos, width);]                                   |
|                                                                                                                       |
| [pdfGrid.Draw(pdfPage, xPos, yPos, width);]                                       |
|                                                                                                                       |
| [pdfGrid.Draw(pdfPage, xPos, yPos, width, pdfGridLayoutFormat);]                  |
+-----------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                               |
|                                                                                                                                  |
|                                                                                                                                  |
|                                                                                                                                  |
| [\' Draw PdfLightTable specified width.][] |
|                                                                                                                                  |
| [pdfLightTable.Draw(pdfGraphics, PointF.Empty, width)]                                       |
|                                                                                                                                  |
| [pdfLightTable.Draw(pdfGraphics, xPos, yPos, width)]                                         |
|                                                                                                                                  |
| [pdfLightTable.Draw(pdfPage, xPos, yPos, width)]                                             |
|                                                                                                                                  |
| [pdfLightTable.Draw(pdfPage, xPos, yPos, width, pdfLightTableLayoutFormat)]                  |
|                                                                                                                                  |
|                                                                                                                                  |
|                                                                                                                                  |
|  [\' Draw PdfGrid with specified width.][] |
|                                                                                                                                  |
| [pdfGrid.Draw(pdfGraphics, PointF.Empty, width)]                                             |
|                                                                                                                                  |
| [pdfGrid.Draw(pdfGraphics, xPos, yPos, width)]                                               |
|                                                                                                                                  |
| [pdfGrid.Draw(pdfPage, xPos, yPos, width)]                                                   |
|                                                                                                                                  |
| [pdfGrid.Draw(pdfPage, xPos, yPos, width, pdfGridLayoutFormat)]                              |
+----------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

