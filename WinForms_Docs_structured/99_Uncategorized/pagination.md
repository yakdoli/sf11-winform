---
title: pagination.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\pagination.md
created_at: 2025-07-03
---






##### Pagination {#pagination style="tab-stops: 0pt"}

[] 

**Pagination** is the capability of the elements to span more than one page (to be shared by more than one page). The base class for all such elements is the **PdfLayoutElement** class. All the primitives that are derived from that class support page layouting in their own way. The following events are raised by this class.

[] 


  ----------------- -----------------------------------------------------------------
  Name              Description
  BeginPageLayout   This event is raised before the element is printed on the page.
  EndPageLayout     This event is raised after the element is printed on the page.
  ----------------- -----------------------------------------------------------------


 

The layouting is accomplished by using the following methods.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [public][ [PdfLayoutResult] Draw( PdfPage page, [PointF] location, PdfLayoutFormat format ); ]            |
|                                                                                                                                                                                                                                                                          |
| [public][ [PdfLayoutResult] Draw( PdfPage page, [RectangleF] layoutRectangle, PdfLayoutFormat format ); ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [Public][ PdfLayoutResult Draw(PdfPage page, PointF location, PdfLayoutFormat format) ]           |
|                                                                                                                                                                                                                        |
| [Public][ PdfLayoutResult Draw(PdfPage page, RectangleF layoutRectangle, PdfLayoutFormat format)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The parameters define the page where the layouting should start, a location or bounds on the page, and layouting settings.

 


{border="0"}Note: If, only the location is set, or the width or height is less than or equal to zero, the bounds are calculated, as the remaining space on the page where the location specified is a Left or Top of the bounds.


[] 

**PdfLayoutFormat** class specifies basic layouting settings such as type of page break, the bounds on the next page, and so on. The following are the properties of the PdfgLayoutFormat.

[] 


  ------------------- ---------------------------------------------------------------------------
  Name                Description
  Break               Gets or sets break type of the element.
  Layout              Gets or sets layout type of the element.
  PaginateBounds      Gets or sets the bounds on the next page.
  UsePaginateBounds   Gets a value that indicates whether PaginateBounds should be used or not.
  ------------------- ---------------------------------------------------------------------------


[] 


{border="0"}Note:

 



***[·    ]***PdfLayoutFormat contains the PaginateBounds property that specifies the bounds of the element on the pages that follows. If this property is set, the element will use it for laying out the next pages, otherwise the element will be laid out according to the bounds used on the first page (layoutRectangle parameter or calculated as was mentioned above), but with the Y coordinate set to zero (0).

***[·    ]***Each element may implement its own laying out settings depending on its own structure and specifications.

***[·    ]***The objects supporting page laying out can be drawn on simple graphics or by using the following methods.


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [public][ [void] Draw( PdfGraphics graphics ); ]                                         |
|                                                                                                                                                                                                                                    |
| [public][ [void] Draw( PdfGraphics graphics, [PointF] location ); ] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                               |
|                                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                                  |
| [Public][ void Draw(PdfGraphics graphics) ]                 |
|                                                                                                                                                                                  |
| [Public][ void Draw(PdfGraphics graphics, PointF location)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

After laying out, each element returns a lay out result, depending on the element and the settings. The base result is described by the **PdfLayoutResult** class.

 

The basic information stored in result is the page where the element ends, and the bounds of the element on that page, which might be helpful for further drawing operations on this page.

 

The following are the properties of the PdfLayoutResult class.

 


  -------- ---------------------------------------------------------------------
  Name     Description
  Bounds   Gets the bounds of the element on the last page where it was drawn.
  Page     Gets the last page where the element was drawn.
  -------- ---------------------------------------------------------------------


[] 

For example, **PdfTextLayoutResult** provides a text that was not laid out and a width of the last laid out line. PdfMetafile as well as graphics primitives also supports multipage layout. Additionally, if it is required to eliminate the splitting of text lines between the pages, the **PdfMetafileLayoutFormat** is used as the input parameter of the **Draw** method. This class contains a property, which allows to enable or disable splitting of text lines.

[] 

There are two events provided by the laid out elements: **BeginPageLayout** and **EndPageLayout**. They provide an option to track the current state of the layout, and specify the custom settings for the layout process.[]{#p39}

 

[] 

[]{#related-topics}

