---
title: howtomakebackgroundimagescenteredstretchedandfittedwithinthepdfgrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtomakebackgroundimagescenteredstretchedandfittedwithinthepdfgrid.md
created_at: 2025-07-03
---








  









### How to make background images centered, stretched and fitted within the PDF Grid? {#how-to-make-background-images-centered-stretched-and-fitted-within-the-pdf-grid style="LINE-HEIGHT: 115%; TEXT-INDENT: -36pt; MARGIN: 10pt 0pt 0pt 36pt; tab-stops: 36.0pt"}

 

Background image positioning such as stretch, center and fit within the PDF Grid can be done by setting the property "ImagePosition" to PdfGridImagePosition.Stretch, PdfGridImagePosition.Centre and PdfGridImagePosition.Fit respectively.

 

+----------------------------------------------------------------------------------------------------------+
| [grid.Rows(1).Cells(0).ImagePosition = PdfGridImagePosition.Stretch] |
|                                                                                                          |
| [grid.Rows(1).Cells(1).ImagePosition = PdfGridImagePosition.Centre]  |
|                                                                                                          |
| [grid.Rows(1).Cells(2).ImagePosition = PdfGridImagePosition.Fit]     |
+----------------------------------------------------------------------------------------------------------+

**[]** 

For more information on positioning background images, refer to the section Background Image Positioning in .

 

[]{#related-topics}

