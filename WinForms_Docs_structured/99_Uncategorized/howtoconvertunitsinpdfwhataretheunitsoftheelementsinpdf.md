---
title: howtoconvertunitsinpdfwhataretheunitsoftheelementsinpdf.md
original_path: WinForms_Docs/99_Uncategorized/howtoconvertunitsinpdfwhataretheunitsoftheelementsinpdf.md
created_at: 2025-08-05
---








  









### How To Convert Units In PDF / What Are the Units Of the Elements In PDF? {#how-to-convert-units-in-pdf-what-are-the-units-of-the-elements-in-pdf style="tab-stops: 0pt"}

 

Essential PDF measure unit of the elements are \"points\". A point is equal to 1/72 of an \"inch\". Points are represented in terms of float values. **PdfUnitConvertor** enables to convert different measure units.

The following code example illustrates how to convert pixels to points.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [//Converts inches to points]                                                                                                                                           |
|                                                                                                                                                                                                                           |
| [float][ height = con.ConvertUnits(800, [PdfGraphicsUnit].Inch, [PdfGraphicsUnit].Point);] |
|                                                                                                                                                                                                                           |
| [float][ width = con.ConvertUnits(500, [PdfGraphicsUnit].Inch, [PdfGraphicsUnit].Point);]  |
|                                                                                                                                                                                                                           |
| [SizeF][ pageSize = [new] [SizeF](width, height);]                                         |
|                                                                                                                                                                                                                           |
| [doc.PageSettings.Size = pageSize;]                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [\'Converts inches to points]                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [Dim][ height [As] [Single] = con.ConvertUnits(800, PdfGraphicsUnit.Inch, PdfGraphicsUnit.Point)] |
|                                                                                                                                                                                                                                  |
| [Dim][ width [As] [Single] = con.ConvertUnits(500, PdfGraphicsUnit.Inch, PdfGraphicsUnit.Point)]  |
|                                                                                                                                                                                                                                  |
| [Dim][ pageSize [As] SizeF = [New] SizeF(width, height)]                                          |
|                                                                                                                                                                                                                                  |
| [doc.PageSettings.Size = pageSize]                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

