---
title: howtospecifyboundsfortableduringpagination.md
original_path: WinForms_Docs/99_Uncategorized/howtospecifyboundsfortableduringpagination.md
created_at: 2025-08-05
---






#### How to specify bounds for Table during pagination? {#how-to-specify-bounds-for-table-during-pagination style="tab-stops: 0pt"}

 

When PdfLightTable or PdfGrid is paginated, by default it will occupy the entire client area of the PdfPage. But, it is possible to specify bounds for the additional pages using PaginateBounds property of PdfLightTableLayoutFormat or PdfGridLayoutFormat class.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                  |
|                                                                                                                                                  |
|                                                                                                                                                  |
| [format.PaginateBounds = [new] [RectangleF](50, 50, 500, 300);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                    |
|                                                                                                                       |
|                                                                                                                       |
|                                                                                                                       |
| [format.PaginateBounds = [New] RectangleF(50, 50, 500, 300)] |
+-----------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

