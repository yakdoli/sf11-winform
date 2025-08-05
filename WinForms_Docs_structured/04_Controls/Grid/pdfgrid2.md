---
title: pdfgrid2.md
original_path: WinForms_Docs/04_Controls/Grid/pdfgrid2.md
created_at: 2025-08-05
---






##### PdfGrid {#pdfgrid style="tab-stops: 0pt"}

 

[]{#p45}PdfGrid class, based on cell model, helps to draw tables of complex structures. Data from DataTables, arrays or other entity classes can be given as input. In Silverlight platform, IEnumerable data objects can be set as data source. Formatting can be done at all levels and it provides direct API for this. It also supports row, column spanning and drawing of nested tables. This section explains how a table can be drawn using PdfGrid. It includes the following sections:

 

###### []{#_Properties,_Methods_and}4.1.2.3.2.1 Properties, Methods and Events {#properties-methods-and-events style="tab-stops: 0pt"}

 

Properties

 


  -------------------------- ------------------------------------------------------------------ -------------------------
  Name                       Description                                                        Data Type
  AllowRowBreakAcrossPages   Gets or sets whether to split or move rows that overflow a page.   Boolean
  Columns                    Gets the columns.                                                  PdfGridColumnCollection
  DataMember                 Gets or sets the data member.                                      String
  DataSource                 Gets or sets the data source.                                      Object
  Headers                    Gets the headers.                                                  PdfGridHeaderCollection
  RepeatHeader               Gets or set a value indicating whether to repeat header            Boolean
  Rows                       Gets the rows.                                                     PdfGridRowCollection
  Style                      Gets or sets the style.                                            PdfGridStyle
  -------------------------- ------------------------------------------------------------------ -------------------------


 

Methods

 


+-----------------+-----------------+---------------------------------------------------------------------------+---------------------+
| Method          | Description     | Parameters                                                                | Return Type         |
+-----------------+-----------------+---------------------------------------------------------------------------+---------------------+
| Draw            | Draws PdfGrid   | Overloads:                                                                | Void                |
|                 |                 |                                                                           |                     |
|                 |                 | (PdfGraphics graphics)                                                    |                     |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfPage page, PointF location)                                           | PdfGridLayoutResult |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfPage page, RectangleF bounds)                                         | PdfGridLayoutResult |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfGraphics graphics, PointF location)                                   | Void                |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfGraphics graphics, RectangleF bounds)                                 | Void                |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfPage page, float x, float y)                                          | PdfGridLayoutResult |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfPage page, PointF location, PdfGridLayoutFormat format)               | PdfGridLayoutResult |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfPage page, PointF location, PdfLayoutFormat format)                   | PdfLayoutResult     |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfPage page, RectangleF bounds, PdfGridLayoutFormat format)             | PdfGridLayoutResult |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfPage page, PointF location, PdfLayoutFormat format)                   | PdfLayoutResult     |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfGraphics graphics, float x, float y)                                  | void                |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfGraphics graphics, PointF location, float width)                      | void                |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfPage page, float x, float y, float width)                             | PdfGridLayoutResult |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | PdfPage page, float x, float y, PdfGridLayoutFormat format)               | PdfGridLayoutResult |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfPage page, float x, float y, PdfLayoutFormat format)                  | PdfLayoutResult     |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfGraphics graphics, float x, float y, float width)                     | void                |
|                 |                 +---------------------------------------------------------------------------+---------------------+
|                 |                 | (PdfPage page, float x, float y, float width, PdfGridLayoutFormat format) | PdfGridLayoutResult |
+=================+=================+===========================================================================+=====================+


 

Events


+-----------------------------------+------------------------------------------------------------------------+
| Name                              | Description                                                            |
+-----------------------------------+------------------------------------------------------------------------+
| BeginPageLayout                   | This event is raised before the element should is printed on the page. |
|                                   |                                                                        |
|                                   | (Inherited from PdfLayoutElement.)                                     |
+-----------------------------------+------------------------------------------------------------------------+
| EndPageLayout                     | This event is raised after the element is printed on the page.         |
|                                   |                                                                        |
|                                   | (Inherited from PdfLayoutElement.)                                     |
+-----------------------------------+------------------------------------------------------------------------+


 

###### []{#_PdfGrid_Creation}4.1.2.3.2.2 PdfGrid Creation {#pdfgrid-creation style="tab-stops: 0pt"}


Note: You must add Syncfusion.Pdf.Grid namespace to work with PdfGrid.


You can create a PdfGrid by simply specifying the new operator with a proper constructor. After assigning data source it can be drawn using one of the overloads of Draw method.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
| [// Create a PdfGrid.]                                                                                                      |
|                                                                                                                                                                               |
| [PdfGrid][ pdfGrid = [new] [PdfGrid]();] |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [// Assign data source.]                                                                                                    |
|                                                                                                                                                                               |
| [pdfGrid.DataSource = dataSource;]                                                                                                        |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [// Draw PdfGrid.]                                                                                                          |
|                                                                                                                                                                               |
| [pdfGrid.Draw(graphics);]                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                  |
|                                                                                                                                                                     |
|                                                                                                                                                                     |
|                                                                                                                                                                     |
| [\' Create a PdfGrid.][]                                                      |
|                                                                                                                                                                     |
| [Dim][ pdfGrid [As] [New] PdfGrid()] |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [\' Assign data source.][]                                                    |
|                                                                                                                                                                     |
| [pdfGrid.DataSource = dataSource]                                                                                               |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [\' Draw PdfGrid.][]                                                          |
|                                                                                                                                                                     |
| [pdfGrid.Draw(graphics)]                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Data to PdfGrid can be entered manually or taken from an external data source. Also, the draw method helps to control the layout of the PdfGrid and returns information to user after drawing completes. The following topics discuss them.

[·      ]Data

[·      ]Layout

 

AllowRowBreakAcrossPages

 

This property allows changing the row split behavior across pages. By default, this Boolean property is set to True, which allows splitting the row across pages when the row cannot accommodate within the bounds of the page. If set to false, the entire row will be shifted to the next page.


Note: If the row height is greater than the page height, the row will be split or cut based on the True and False value of this property.


 

[]{#_Data_1}4.1.2.3.2.2.1      Data

 

External Data Source

 

You can bind data to a PdfGrid by associating it with an external data source. You can set the external data source by using the DataSource property. The following code example illustrates this.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
| [DataTable][ dt = [new] [DataTable]();]                 |
|                                                                                                                                                                                              |
| [dt.Columns.Add([\"ID\"]);]                                                                                                      |
|                                                                                                                                                                                              |
| [dt.Columns.Add([\"Name\"]);]                                                                                                    |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
| [dt.Rows.Add([new] [object]\[\] { [\"E01\"], [\"Clay\"] });]   |
|                                                                                                                                                                                              |
| [dt.Rows.Add([new] [object]\[\] { [\"E02\"], [\"Thomas\"] });] |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
| [// Create a PdfGrid.]                                                                                                                     |
|                                                                                                                                                                                              |
| [PdfGrid][ pdfGrid = [new] [PdfGrid]();]                |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
| [// dt is an object that can be an array (two-dimensional, one-dimensional or nested), a DataTable, DataColumn, DataView or DataSet.]      |
|                                                                                                                                                                                              |
| [pdfGrid.DataSource = dt;]                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| [Dim][ dt [As] DataTable = [New] DataTable()]              |
|                                                                                                                                                                                           |
| [dt.Columns.Add([\"ID\"])]                                                                                                    |
|                                                                                                                                                                                           |
| [dt.Columns.Add([\"Name\"])]                                                                                                  |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| [dt.Rows.Add([New] [Object]() { [\"E01\"], [\"Clay\"]})]    |
|                                                                                                                                                                                           |
| [dt.Rows.Add([New] [Object]() { [\"E02\"], [\"Thomas\"] })] |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| [\' Create a PdfGrid.]                                                                                                                  |
|                                                                                                                                                                                           |
| [Dim][ pdfGrid [As] [New] PdfGrid()]                       |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| [\' dt is an object that can be an array (two-dimensional, one-dimensional or nested), a DataTable, DataColumn, DataView or DataSet.]   |
|                                                                                                                                                                                           |
| [pdfGrid.DataSource = dt]                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Direct Rows and Columns

 

Alternatively, you can bind data to a PdfGrid without setting any data source. This is achieved using the PdfGridRow and PdfGridColumn classes. The following code example illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
| [PdfPage][ pdfPage = pdfDocument.Pages.Add();]                                        |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
| [// Create a new PdfGrid.]                                                                                                  |
|                                                                                                                                                                               |
| [PdfGrid][ pdfGrid = [new] [PdfGrid]();] |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
| [// Add three columns.]                                                                                                     |
|                                                                                                                                                                               |
| [pdfGrid.Columns.Add(3);]                                                                                                                 |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
| [// Add header.]                                                                                                            |
|                                                                                                                                                                               |
| [pdfGrid.Headers.Add(1);]                                                                                                                 |
|                                                                                                                                                                               |
| [PdfGridRow][ pdfGridHeader = pdfGrid.Headers\[0\];]                                  |
|                                                                                                                                                                               |
| [pdfGridHeader.Cells\[0\].Value = [\"Employee ID\"];]                                                             |
|                                                                                                                                                                               |
| [pdfGridHeader.Cells\[1\].Value = [\"Employee Name\"];]                                                           |
|                                                                                                                                                                               |
| [pdfGridHeader.Cells\[2\].Value = [\"Salary\"];]                                                                  |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
| [// Add rows.]                                                                                                              |
|                                                                                                                                                                               |
| [PdfGridRow][ pdfGridRow = pdfGrid.Rows.Add();]                                       |
|                                                                                                                                                                               |
| [pdfGridRow.Cells\[0\].Value = [\"E01\"];]                                                                        |
|                                                                                                                                                                               |
| [pdfGridRow.Cells\[1\].Value = [\"Clay\"];]                                                                       |
|                                                                                                                                                                               |
| [pdfGridRow.Cells\[2\].Value = [\"\$10,000\"];]                                                                   |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
|                                                                                                                                                                               |
| [// Draw the PdfGrid.]                                                                                                      |
|                                                                                                                                                                               |
| [pdfGrid.Draw(pdfPage, [PointF].Empty);]                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                   |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
| [Dim][ pdfPage [As] PdfPage = pdfDocument.Pages.Add()]     |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
| [\' Create a new PdfGrid.]                                                                                         |
|                                                                                                                                                                      |
| [Dim][ pdfGrid [As] [New] PdfGrid()]  |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
| [\' Add three columns.]                                                                                            |
|                                                                                                                                                                      |
| [pdfGrid.Columns.Add(3)]                                                                                                         |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
| [\' Add header.]                                                                                                   |
|                                                                                                                                                                      |
| [pdfGrid.Headers.Add(1)]                                                                                                         |
|                                                                                                                                                                      |
| [Dim][ pdfGridHeader [As] PdfGridRow = pdfGrid.Headers(0)] |
|                                                                                                                                                                      |
| [pdfGridHeader.Cells(0).Value = [\"Employee ID\"]]                                                       |
|                                                                                                                                                                      |
| [pdfGridHeader.Cells(1).Value = [\"Employee Name\"]]                                                     |
|                                                                                                                                                                      |
| [pdfGridHeader.Cells(2).Value = [\"Salary\"]]                                                            |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
| [\' Add rows.]                                                                                                     |
|                                                                                                                                                                      |
| [Dim][ pdfGridRow [As] PdfGridRow = pdfGrid.Rows.Add()]    |
|                                                                                                                                                                      |
| [pdfGridRow.Cells(0).Value = [\"E01\"]]                                                                  |
|                                                                                                                                                                      |
| [pdfGridRow.Cells(1).Value = [\"Clay\"]]                                                                 |
|                                                                                                                                                                      |
| [pdfGridRow.Cells(2).Value = [\"\$10,000\"]]                                                             |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
|                                                                                                                                                                      |
| [\' Draw the PdfGrid.]                                                                                             |
|                                                                                                                                                                      |
| [pdfGrid.Draw(pdfPage, PointF.Empty)]                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#_Layout}4.1.2.3.2.2.2      Layout

 

This section speaks about layouting options and the two events associated with PdfGrid.

 

PdfGridLayoutFormat

 

Layouting PdfGrid can be done using the PdfGridLayoutFormat class. Overloads accepting pages can accept standard formats as other layouting elements. However, they treat the PdfLayoutBreakType.FitElement value of Format.Break property as one, for a single row and not for the entire PdfGrid.

 

Properties

 


  ---------------- -------------------------------------------------------- --------------------
  Name             Description                                              Data Type
  Break            Gets or sets the break type                              PdfLayoutBreakType
  Layout           Gets or sets the layout type                             PdfLayoutType
  PaginateBounds   Gets or sets the PdfGrid bounds for the following page   RectangleF
  ---------------- -------------------------------------------------------- --------------------


 

The PdfLayoutType class is used to specify the type of pagination. The Paginate LayoutType draws the PdfGrid to the next following pages, if the element exceeds the page. The OnePage layout draws the element only on one page. The following code example illustrates this.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
|                                                                                                                                                                                                     |
|                                                                                                                                                                                                     |
| [PdfGridTableLayoutFormat][ format = [new] [PdfGridLayoutFormat]();] |
|                                                                                                                                                                                                     |
| [format.Layout = [PdfLayoutType].Paginate;]                                                                                                |
|                                                                                                                                                                                                     |
| [format.Break = [PdfLayoutBreakType].FitElement;]                                                                                          |
|                                                                                                                                                                                                     |
|                                                                                                                                                                                                     |
|                                                                                                                                                                                                     |
| [// Draws the PdfGrid with the layout format]                                                                                                     |
|                                                                                                                                                                                                     |
| [pdfGrid.Draw(pdfPage, [PointF].Empty, format);]                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                   |
|                                                                                                                                                                                                      |
|                                                                                                                                                                                                      |
|                                                                                                                                                                                                      |
| [Dim][ format [As] PdfGridLayoutFormat = [New] PdfGridLayoutFormat()] |
|                                                                                                                                                                                                      |
| [format.Layout = PdfLayoutType.Paginate]                                                                                                                         |
|                                                                                                                                                                                                      |
| [format.Break = PdfLayoutBreakType.FitElement]                                                                                                                   |
|                                                                                                                                                                                                      |
|                                                                                                                                                                                                      |
|                                                                                                                                                                                                      |
| [\' Draws the PdfGrid with the layout format]                                                                                                      |
|                                                                                                                                                                                                      |
| [pdfGrid.Draw(pdfPage, PointF.Empty, format)]                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

PdfGridLayoutResult

 

You can get the layout settings for the drawn PdfGrid with the help of PdfGridLayoutResult class. Also, you can get the bounds and the last page where the PdfGrid was drawn using the Bounds and Page properties. This is mainly used to write some text or any other element below the large table that shows number of pages.

 

Properties

 


  -------- ----------------------------------------------------- ------------
  Name     Description                                           Data Type
  Bounds   Gets the bounds in the last page where it was drawn   RectangleF
  Page     Gets the last page where PdfLightTable was drawn      PdfPage
  -------- ----------------------------------------------------- ------------


 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| [// Draws the PdfGrid]                                                                                                                  |
|                                                                                                                                                                                           |
| [PdfGridLayoutResult][ result = pdfGrid.Draw(pdfPage, [PointF].Empty, format);] |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| [// Returns the rectangle value for the last page.]                                                                                     |
|                                                                                                                                                                                           |
| [Console][.WriteLine(result.Bounds.ToString());]                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [\' Draws the PdfGrid.]                                                                                                                       |
|                                                                                                                                                                                                 |
| [Dim][ result [As] PdfGridLayoutResult = pdfGrid.Draw(pdfPage, PointF.Empty, format)] |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [\' Returns the rectangle value for the last page.]                                                                                           |
|                                                                                                                                                                                                 |
| [Console.WriteLine(result.Bounds.ToString())]                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Events

 

The following events are associated with PdfGrid. The functionalities of these events are common for both PdfGrid and PdfLightTable.

[  ]{.UGHyperlink}

]{.UGHyperlink}

 

###### []{#_PdfGrid_Formatting}[[4.1.2.3.2.3  PdfGrid Formatting]]{.Heading6Char} {#pdfgrid-formatting style="tab-stops: 0pt"}

 

This section explains the most direct options available to format PdfGrid. The PdfGridStyle class, accessible through Style property of PdfGrid provides options to format entire PdfGrid or parts of it. Formatting applicable for entire PdfGrid using PdfGridStyle class is discussed in this section. Header, Row, Column and Cell are discussed in the following links:

[[·      ]]{.UGHyperlink}[[Header ]]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[[Row ]]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[[Column ]]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[[Cell]]{.UGHyperlink}


Note: If the style properties are applied to both PdfGridCell and PdfGridRow, PdfGridCell takes over the precedence. Following is an example for the exact order of precedence.


 

PdfBrush backgroundBrush = Cell.BackgroundBrush ?? Row.Style.BackgroundBrush ?? Row.Grid.Style.BackgroundBrush

 

Properties

 


  ------------------------- ----------------------------------------------------------------------- ---------------------------
  Name                      Description                                                             Data Type
  AllowHorizontalOverflow   Gets or sets a value indicating whether to allow horizontal overflow.   Boolean
  BackgroundBrush           Gets or sets background brush.                                          PdfBrush
  BorderOverlapStyle        Gets or sets border overlap style.                                      PdfBorderOverlapStyle
  CellPadding               Gets or sets cell padding.                                              PdfPaddings
  CellSpacing               Gets or sets cell spacing.                                              Float
  Font                      Gets or sets the font.                                                  PdfFont
  HorizontalOverflowType    Gets or sets the type of horizontal overflow.                           PdfHorizontalOverflowType
  TextBrush                 Gets or sets the text brush.                                            PdfBrush
  TextPen                   Gets or sets the text pen.                                              PdfPen
  ------------------------- ----------------------------------------------------------------------- ---------------------------


 

AllowHorizontalOverflow

 

If set to True, the columns exceeding the current page width would be wrapped and drawn in the next or last page. The default value is false. It should be used along with HorizontalOverflowType property. The default value of HorizontalOverflowType is PdfHorizontalOverflowType.LastPage.

 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                             |
|                                                                                                                                            |
|                                                                                                                                            |
|                                                                                                                                            |
| [pdfGrid.Style.AllowHorizontalOverflow = [true];]                                 |
|                                                                                                                                            |
| [pdfGrid.Style.HorizontalOverflowType = [PdfHorizontalOverflowType].NextPage;] |
+--------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                        |
|                                                                                                                                           |
|                                                                                                                                           |
|                                                                                                                                           |
| [pdfGrid.Style.AllowHorizontalOverflow = T[rue]]                                 |
|                                                                                                                                           |
| [pdfGrid.Style.HorizontalOverflowType = [PdfHorizontalOverflowType].NextPage] |
+-------------------------------------------------------------------------------------------------------------------------------------------+

 

BorderOverlapStyle

 

This property decides if the cell border should overlap with neighboring cells or to draw the interior of cell.


Note: This property applies for all cells in the PdfGrid. Be careful while using overlapping borders, because they may produce bad results if they are not of the same width and color.


 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                                   |
|                                                                                                                                   |
|                                                                                                                                   |
| [pdfGrid.Style.BorderOverlapStyle = [PdfBorderOverlapStyle].Overlap;] |
+-----------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                               |
|                                                                                                                                  |
|                                                                                                                                  |
|                                                                                                                                  |
| [pdfGrid.Style.BorderOverlapStyle = [PdfBorderOverlapStyle].Overlap] |
+----------------------------------------------------------------------------------------------------------------------------------+

 

CellPadding

 

The distance between text and border inside a cell otherwise known as CellPadding, can be set to all cells in the PdfGrid. The PdfPaddings class allows setting padding to individual or all sides.

 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                          |
|                                                                                                                         |
|                                                                                                                         |
|                                                                                                                         |
| [// Padding will be applied for all four sides of cells in PdfGrid.]  |
|                                                                                                                         |
| [pdfGrid.Style.CellPadding.All = 0.3f;]                                             |
|                                                                                                                         |
| []                                                                                  |
|                                                                                                                         |
| [// Padding will be applied only at the top of all cells in PdfGrid.] |
|                                                                                                                         |
| [pdfGrid.Style.CellPadding.Top = 0.3f;]                                             |
+-------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
|                                                                                                                                                                |
|                                                                                                                                                                |
| [\' Padding will be applied for all four sides of cells in PdfGrid.][]   |
|                                                                                                                                                                |
| [pdfGrid.Style.CellPadding.All = 0.3f]                                                                                     |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [\' Padding will be applied only at the top for all cells in PdfGrid.][] |
|                                                                                                                                                                |
| [pdfGrid.Style.CellPadding.Top = 0.3f]                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

CellSpacing

 

The distance between the cells otherwise known as CellSpacing, can be set to all cells in PdfGrid using CellSpacing property.

 

+-------------------------------------------------------------------------+
| **[\[C#\]]**          |
|                                                                         |
|                                                                         |
|                                                                         |
| [pdfGrid.Style.CellSpacing = 0.5f;] |
+-------------------------------------------------------------------------+

 

+------------------------------------------------------------------------+
| **[\[VB.NET\]]**     |
|                                                                        |
|                                                                        |
|                                                                        |
| [pdfGrid.Style.CellSpacing = 0.5f] |
+------------------------------------------------------------------------+

 

[]{#_Header}4.1.2.3.2.3.1      Header

 

Header is a set of rows that can be optionally repeated on each page and has its own style. You can add header as follows:

[·      ]Directly from column captions.

[·      ]By using Add method of the PdfGridHeaderCollection class.


Note: When you bind data source to PdfGrid, column captions will be automatically added to header collection. It can be removed at any time using Clear method of PdfGridHeaderCollection.


 

The following code example illustrates how to add headers to PdfGrid by using the Add method.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                                            |
|                                                                                                                                                            |
|                                                                                                                                                            |
| [// Add a new header to PdfGrid.]                                                                        |
|                                                                                                                                                            |
| [pdfGrid.Headers.Add(1);]                                                                                              |
|                                                                                                                                                            |
|                                                                                                                                                            |
|                                                                                                                                                            |
| [// Get the first header row.]                                                                           |
|                                                                                                                                                            |
| [PdfGridCellCollection][ collection = pdfGrid.Headers\[0\].Cells;] |
|                                                                                                                                                            |
|                                                                                                                                                            |
|                                                                                                                                                            |
| [// Set the header names.]                                                                               |
|                                                                                                                                                            |
| [collection\[0\].Value = [\"Header1\"];]                                                       |
|                                                                                                                                                            |
| [collection\[1\].Value = [\"Header2\"];]                                                       |
|                                                                                                                                                            |
| [collection\[2\].Value = [\"Header3\"];]                                                       |
|                                                                                                                                                            |
| [collection\[3\].Value = [\"Header4\"];]                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                 |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
| [\' Add a new header to PdfGrid.]                                                                                                |
|                                                                                                                                                                                    |
| [pdfGrid.Headers.Add(1)]                                                                                                                       |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
| [\' Get the first header row.]                                                                                                   |
|                                                                                                                                                                                    |
| [Dim][ collection [As] PdfGridCellCollection = pdfGrid.Headers(0).Cells] |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
| [\' Set the header names.]                                                                                                       |
|                                                                                                                                                                                    |
| [collection(0).Value = [\"Header1\"]]                                                                                  |
|                                                                                                                                                                                    |
| [collection(1).Value = [\"Header2\"]]                                                                                  |
|                                                                                                                                                                                    |
| [collection(2).Value = [\"Header3\"]]                                                                                  |
|                                                                                                                                                                                    |
| [collection(3).Value = [\"Header4\"]]                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

RepeatHeader

 

Header can be set to repeat on each page where PdfGrid is paginated.  RepeatHeader property should be set to true to achieve this.

 

+-------------------------------------------------------------------------------------------+
| **[\[C#\]]**                            |
|                                                                                           |
|                                                                                           |
|                                                                                           |
| [pdfGrid.RepeatHeader = [true];] |
+-------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                       |
|                                                                                          |
|                                                                                          |
|                                                                                          |
| [pdfGrid.RepeatHeader = T[rue]] |
+------------------------------------------------------------------------------------------+

 

Style

 

You can specify the header style for the PdfGrid by using the PdfGridRowStyle or PdfGridCellStyle classes. The style applied at the collection will be applied to all rows in the header. Following code example illustrates how to specify the header style.

[] 

+-------------------------------------------------------------------------------+
| **[\[C#\]]**                |
|                                                                               |
|                                                                               |
|                                                                               |
| [// Applying header style.] |
|                                                                               |
| [pdfGrid.Headers.ApplyStyle(style);]      |
+-------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------+
| **[\[VB.NET\]]**            |
|                                                                               |
|                                                                               |
|                                                                               |
| [\' Applying header style.] |
|                                                                               |
| [pdfGrid.Headers.ApplyStyle(style)]       |
+-------------------------------------------------------------------------------+

[] 


Note: Styles for each PdfGridRow in Header can be individually applied using PdfGridRowStyle class.


Refer to the following topics for more details:

[[PdfGridRowStyle]{.UGHyperlink}]()[ ]{.UGHyperlink}

[[PdfGridCellStyle]{.UGHyperlink}]()[ ]{.UGHyperlink}

 

[]{#_Row}4.1.2.3.2.3.2      Row

 

Height

 

The Height property of the PdfGridRow class is used to specify the row height for the PdfGrid rows. The following code example illustrates how to set this property.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                         |
|                                                                                                                                        |
|                                                                                                                                        |
|                                                                                                                                        |
| [// Access the row in PdfGrid.]                                                      |
|                                                                                                                                        |
| [PdfGridRow][ pdfGridRow = pdfGrid.Rows\[0\];] |
|                                                                                                                                        |
|                                                                                                                                        |
|                                                                                                                                        |
| [// Set the height for a row.]                                                       |
|                                                                                                                                        |
| [pdfGridRow.Height = 20;]                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
|                                                                                                                                                                |
|                                                                                                                                                                |
| [\' Access the row in PdfGrid.]                                                                              |
|                                                                                                                                                                |
| [Dim][ pdfGridRow [As] PdfGridRow = pdfGrid.Rows(0)] |
|                                                                                                                                                                |
|                                                                                                                                                                |
|                                                                                                                                                                |
| [\' Set the height for a row.]                                                                               |
|                                                                                                                                                                |
| [pdfGridRow.Height = 20]                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


Note: The unit of the Height property is always points. You can set the PDF units only as points. Also, you can use the  class to convert the other units to points.


 

Row Span

 

PdfGrid enables you to merge cells within a row. You can specify the number of cells to be merged using the RowSpan property of PdfGridCell class. The following code example illustrates this.

 

+-----------------------------------------------------------------------------------------+
| [ ]**[\[C#\]]** |
|                                                                                         |
|                                                                                         |
|                                                                                         |
| [// Merging row cells.]               |
|                                                                                         |
| [pdfGridRow.Cells\[0\].RowSpan = 2;]                |
+-----------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------+
| **[\[VB.NET\]]**        |
|                                                                           |
|                                                                           |
|                                                                           |
| [\' Merging row cells.] |
|                                                                           |
| [pdfGridRow.Cells(0).RowSpan = 2]     |
+---------------------------------------------------------------------------+

[] 

Style

 

The PdfGridRowStyle class, accessed through Style property of PdfGridRow class is used to specify the row style for the PdfGrid rows.


Note: If the style properties are applied to both PdfGridCell and PdfGridRow, PdfGridCell takes over the precedence. Following is an example for the exact order of precedence.


 

PdfBrush backgroundBrush = Cell.BackgroundBrush ?? Row.Style.BackgroundBrush ?? Row.Grid.Style.BackgroundBrush

The following code example illustrates how to specify the row style for the PdfGrid rows:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
| [// Create an instance of PdfGridRowStyle]                                                                                                          |
|                                                                                                                                                                                                       |
| [PdfGridRowStyle][ pdfGridRowStyle = [new] [PdfGridRowStyle]();] |
|                                                                                                                                                                                                       |
| [pdfGridRowStyle.BackgroundBrush = [PdfBrushes].LightYellow;]                                                                             |
|                                                                                                                                                                                                       |
| [pdfGridRowStyle.Font = [new] [PdfStandardFont]([PdfFontFamily].Courier, 10);]               |
|                                                                                                                                                                                                       |
| [pdfGridRowStyle.TextBrush = [PdfBrushes].Blue;]                                                                                          |
|                                                                                                                                                                                                       |
| [pdfGridRowStyle.TextPen = [PdfPens].Pink;]                                                                                               |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [// Set style for the PdfGridRow.]                                                                                                                  |
|                                                                                                                                                                                                       |
| [pdfGrid.Rows\[0\].Style = pdfGridRowStyle;]                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                  |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
| [\' Create an instance of PdfGridRowStyle][]                                                  |
|                                                                                                                                                                                     |
| [Dim][ pdfGridRowStyle [As] [New] PdfGridRowStyle()] |
|                                                                                                                                                                                     |
| [pdfGridRowStyle.BackgroundBrush = PdfBrushes.LightYellow]                                                                                      |
|                                                                                                                                                                                     |
| [pdfGridRowStyle.Font = [New] PdfStandardFont(PdfFontFamily.Courier, 10)]                                                  |
|                                                                                                                                                                                     |
| [pdfGridRowStyle.TextBrush = PdfBrushes.Blue]                                                                                                   |
|                                                                                                                                                                                     |
| [pdfGridRowStyle.TextPen = PdfPens.Pink]                                                                                                        |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [\' Set style for the PdfGridRow.][]                                                          |
|                                                                                                                                                                                     |
| [pdfGrid.Rows(0).Style = pdfGridRowStyle]                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

You may also apply PdfGridCellStyle to a PdfGridRow using the ApplyStyle property. The following code snippet illustrates this:

 

+---------------------------------------------------------------------------------------+
| **[\[C#\]]**                        |
|                                                                                       |
|                                                                                       |
|                                                                                       |
| [// Set style for the PdfGridRow.]  |
|                                                                                       |
| [pdfGrid.Rows\[0\].ApplyStyle(pdfGridCellStyle);] |
+---------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                   |
|                                                                                      |
|                                                                                      |
|                                                                                      |
| [// Set style for the PdfGridRow.] |
|                                                                                      |
| [pdfGrid.Rows(0).ApplyStyle(pdfGridCellStyle)]   |
+--------------------------------------------------------------------------------------+

 

All rows in the PdfGrid can be set with same style using the ApplyStyle method of PdfGridRowCollection. This style can be a PdfGridRowStyle or PdfGridCellStyle. The following is the code snippet:

 

+-------------------------------------------------------------------------------------------+
| **[\[C#\]]**                            |
|                                                                                           |
|                                                                                           |
|                                                                                           |
| [// Set style for all rows in PdfGrid.] |
|                                                                                           |
| [pdfGrid.Rows.ApplyStyle(style);]                     |
+-------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                        |
|                                                                                           |
|                                                                                           |
|                                                                                           |
| [// Set style for all rows in PdfGrid.] |
|                                                                                           |
| [pdfGrid.Rows.ApplyStyle(style)]                      |
+-------------------------------------------------------------------------------------------+

 

Refer to the following topic for more details:

[[PdfGridCellStyle]]()[]

 

[]{#_Column}4.1.2.3.2.3.3      Column

 

Width

 

By default, all the columns in PdfGrid have equal width, and the columns automatically fill the entire width of the PdfGrid. If the width of the PdfGrid is increased or decreased, the column width also changes appropriately.

You can specify the width for a particular column by using the Width property. The following code example illustrates how to set the width.

 

+------------------------------------------------------------------------------------+
| **[\[C#\]]**                     |
|                                                                                    |
|                                                                                    |
|                                                                                    |
| [// Set Width for first column.] |
|                                                                                    |
| [pdfGrid.Columns\[0\].Width = 20f;]            |
+------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                 |
|                                                                                    |
|                                                                                    |
|                                                                                    |
| [\' Set Width for first column.] |
|                                                                                    |
| [pdfGrid.Columns(0).Width = 20f]               |
+------------------------------------------------------------------------------------+

 


Note: The unit of the Width property is always points. You can set the PDF units only as points. Also, you can use the  to convert the other units to points.


 

Column Span

 

PdfGrid enables you to merge cells within a column. You can specify the number of cells to be merged by using the ColumnSpan property PdfGridCell class. The following code example illustrates this.

 

+------------------------------------------------------------------------------------+
| **[\[C#\]]**                     |
|                                                                                    |
|                                                                                    |
|                                                                                    |
| [// Merging column cells.]       |
|                                                                                    |
| [pdfGrid.Rows\[0\].Cells\[0\].ColumnSpan = 2;] |
+------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------+
| **[\[VB.NET\]]**            |
|                                                                               |
|                                                                               |
|                                                                               |
| [\' Merging column cells.]  |
|                                                                               |
| [pdfGrid.Rows(0).Cells(0).ColumnSpan = 2] |
+-------------------------------------------------------------------------------+

[] 

Format

 

You can specify the content format for the PdfGrid columns by using the Format property. Check String Formatting in  for more details.

 

[]{#_Cell}4.1.2.3.2.3.4      Cell

 

Properties

 


  ------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------- ----------------------
  Name                                                                                                                Description                                                      Data Type
  [[ColumnSpan]]()                                                         Gets or set the column span.                                     Integer
  Height                                                                                                              Gets the height.                                                 Float
  ImagePosition                                                                                                       Gets or sets the image alignment type of the background image.   PdfGridImagePosition
  [[RowSpan]]()                                                            Gets or sets the row span                                        Integer
     Gets or sets the string format.                                  PdfStringFormat
  Style                                                                                                               Gets or sets the cell style.                                     PdfGridCellStyle
  Value                                                                                                               Gets or sets the value.                                          Object
  Width                                                                                                               Gets the width.                                                  float
  ------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------- ----------------------


 

Cell Size

 

The width and height cannot be modified for a single cell, but for the entire column or row. Please check [PdfGridColumn]() and [PdfGridRow]() for more details.

 

Value

 

You can specify the value for an individual cell using the Value property. Also, you can specify another PdfGrid as the cell value to make a nested table. The following code snippet illustrates this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                     |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
| [// Set the value to the specific cell.]                                                                                         |
|                                                                                                                                                                                    |
| [parentPdfGrid.Rows\[0\].Cells\[0\].Value = [\"Nested Table\"];]                                                       |
|                                                                                                                                                                                    |
| [parentPdfGrid.Rows\[0\].Cells\[1\].RowSpan = 2;]                                                                                              |
|                                                                                                                                                                                    |
| [parentPdfGrid.Rows\[0\].Cells\[1\].ColumnSpan = 2;]                                                                                           |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
| [PdfGrid][ childPdfGrid = [new] [PdfGrid]();] |
|                                                                                                                                                                                    |
| [childPdfGrid.Columns.Add(5);]                                                                                                                 |
|                                                                                                                                                                                    |
| [for][ ([int] i = 0; i \< 5; i++)]                                       |
|                                                                                                                                                                                    |
| [{]                                                                                                                                            |
|                                                                                                                                                                                    |
| [PdfGridRow][ row = childPdfGrid.Rows.Add();]                                              |
|                                                                                                                                                                                    |
| [for][ ([int] j = 0; j \< 5; j++)]                                       |
|                                                                                                                                                                                    |
| [{]                                                                                                                                            |
|                                                                                                                                                                                    |
| [row.Cells\[j\].Value = [String].Format([\"Cell \[{0} {1}\]\"], j, i);]                        |
|                                                                                                                                                                                    |
| [}]                                                                                                                                            |
|                                                                                                                                                                                    |
| [}]                                                                                                                                            |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
|                                                                                                                                                                                    |
| [// Set the value as another PdfGrid in a cell.]                                                                                 |
|                                                                                                                                                                                    |
| [parentGrid.Rows\[0\].Cells\[1\].Value = childPdfGrid;]                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                      |
|                                                                                                                                                                                         |
|                                                                                                                                                                                         |
|                                                                                                                                                                                         |
| [\' Set the value to the specific cell.][]                                                        |
|                                                                                                                                                                                         |
| [parentPdfGrid.Rows(0).Cells(0).Value = [\"Nested Table\"]]                                                                 |
|                                                                                                                                                                                         |
| [parentPdfGrid.Rows(0).Cells(1).RowSpan = 2]                                                                                                        |
|                                                                                                                                                                                         |
| [parentPdfGrid.Rows(0).Cells(1).ColumnSpan = 2]                                                                                                     |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [Dim][ childPdfGrid [As] [New] PdfGrid()]                |
|                                                                                                                                                                                         |
| [childPdfGrid.Columns.Add(5)]                                                                                                                       |
|                                                                                                                                                                                         |
| [For][ i [As] [Integer] = 0 [To] 4] |
|                                                                                                                                                                                         |
| [Dim][ row [As] PdfGridRow = childPdfGrid.Rows.Add()]                         |
|                                                                                                                                                                                         |
| [For][ j [As] [Integer] = 0 [To] 4] |
|                                                                                                                                                                                         |
| [row.Cells(j).Value = [String].Format([\"Cell \[{0} {1}\]\"], j, i)]                                   |
|                                                                                                                                                                                         |
| [Next][ j]                                                                                         |
|                                                                                                                                                                                         |
| [Next][ i]                                                                                         |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [\' Set the value as another PdfGrid in a cell.][]                                                |
|                                                                                                                                                                                         |
| [parentGrid.Rows(0).Cells(1).Value = childPdfGrid]                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Style

 

PdfGrid provides various options to customize the cell content, text color, background color, and so on. The following properties can be used for this purpose.

 

Properties

 


  ----------------- --------------------------------------------- -----------------
  Name              Description                                   Data Type
  BackgroundBrush   Gets or sets background brush for the cell.   PdfBrush
  BackgroundImage   Gets or sets background image for the cell.   PdfImage
  Borders           Gets or sets the borders                      PdfBorders
  Font              Gets or sets the font.                        PdfFont
  StringFormat      Gets or sets the string format                PdfStringFormat
  TextBrush         Gets or sets the text brush.                  PdfBrush
  TextPen           Gets or sets the text pen.                    PdfPen
  ----------------- --------------------------------------------- -----------------


 

The following code example illustrates how to customize the cell content.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                                          |
|                                                                                                                                                                                                          |
|                                                                                                                                                                                                          |
| [//Specify the style for the PdfGridCell.]                                                                                                             |
|                                                                                                                                                                                                          |
| [PdfGridCellStyle][ pdfGridCellStyle = [new] [PdfGridCellStyle]();] |
|                                                                                                                                                                                                          |
| [pdfGridCellStyle.BackgroundImage = [new] [PdfBitmap]([\"pdf_button.png\"]);]                   |
|                                                                                                                                                                                                          |
| [pdfGridCellStyle.TextPen = [PdfPens].Red;]                                                                                                  |
|                                                                                                                                                                                                          |
| [pdfGridCellStyle.Borders.All = [PdfPens].Red;]                                                                                              |
|                                                                                                                                                                                                          |
| [            ]                                                                                                                                                       |
|                                                                                                                                                                                                          |
| [PdfGridCell][ pdfGridCell = pdfGrid.Rows\[0\].Cells\[0\];]                                                      |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                          |
| [// Apply style]                                                                                                                                       |
|                                                                                                                                                                                                          |
| [pdfGridCell.Style = pdfGridCellStyle;]                                                                                                                              |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                          |
| [// Set image position for the background image in the style.]                                                                                         |
|                                                                                                                                                                                                          |
| [pdfGridCell.ImagePosition = [PdfGridImagePosition].Fit;]                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                    |
|                                                                                                                                                                                       |
|                                                                                                                                                                                       |
|                                                                                                                                                                                       |
| [\'Specify the style for the PdfGridCell.][]                                                    |
|                                                                                                                                                                                       |
| [Dim][ pdfGridCellStyle [As] [New] PdfGridCellStyle()] |
|                                                                                                                                                                                       |
| [pdfGridCellStyle.BackgroundImage = [New] PdfBitmap([\"pdf_button.png\"])]                           |
|                                                                                                                                                                                       |
| [pdfGridCellStyle.TextPen = PdfPens.Red]                                                                                                          |
|                                                                                                                                                                                       |
| [pdfGridCellStyle.Borders.All = PdfPens.Red]                                                                                                      |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [Dim][ pdfGridCell [As] PdfGridCell = pdfGrid.Rows(0).Cells(0)]             |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [\' Apply style][]                                                                              |
|                                                                                                                                                                                       |
| [pdfGridCell.Style = pdfGridCellStyle]                                                                                                            |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [\' Set image position for the background image in the style.][]                                |
|                                                                                                                                                                                       |
| [pdfGridCell.ImagePosition = PdfGridImagePosition.Fit]                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

For more details on PdfGridImagePosition, check the following FAQ:

[ ]{.UGHyperlink}

 

[]{#related-topics}

