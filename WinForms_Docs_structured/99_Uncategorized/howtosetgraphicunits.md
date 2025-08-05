---
title: howtosetgraphicunits.md
original_path: WinForms_Docs/99_Uncategorized/howtosetgraphicunits.md
created_at: 2025-08-05
---






#### How To Set Graphic Units? {#how-to-set-graphic-units style="tab-stops: 0pt"}

 

Essential PDF sets the size of an element in terms of points \[1/72 inch\]. It has a utility class, **PdfUnitConvertor**, which enables to convert different measure units and use them for resizing pages.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| **[]**                                                                                                                                      |
|                                                                                                                                                                                               |
| [// Setting Page size after converting units to points][ ]                                              |
|                                                                                                                                                                                               |
| [PdfUnitConvertor][ con = [new] [PdfUnitConvertor]();]   |
|                                                                                                                                                                                               |
| [doc.PageSettings.Width = con.ConvertUnits(100f, [PdfGraphicsUnit].Millimeter, [PdfGraphicsUnit].Point);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                     |
|                                                                                                                                                          |
| **[]**                                                                                               |
|                                                                                                                                                          |
| [\' Setting Page size after converting units to points ]                               |
|                                                                                                                                                          |
| [Dim con As New [PdfUnitConvertor]()]                                           |
|                                                                                                                                                          |
| [doc.PageSettings.Width = con.ConvertUnits(100F, PdfGraphicsUnit.Millimeter, PdfGraphicsUnit.Point)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: The width or height property of the document is always represented by using Points \[1/72 inch\]. However, the helper method enables you to set page sizes in the desired unit.


 

 

 

[]{#related-topics}

