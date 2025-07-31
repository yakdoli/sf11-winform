---
title: tables.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tables.md
created_at: 2025-07-03
---






#### Tables {#tables style="tab-stops: 0pt"}

Tables are useful for presenting a large quantity of information clearly and concisely. In PDF, tables are drawn as a series of rectangles with text and image correctly positioned within them. Using Essential PDF, it is drawn with the help of PdfBrush, PdfPen and other PdfGraphics elements. Essential PDF also offers two classes to achieve them without any hassle. They are:

[[·      ]]{.UGHyperlink}[[PdfLightTable ]]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[[PdfGrid]]{.UGHyperlink}

 

PdfLightTable

It allows the creation of table with inputs from DataTable, arrays or any other entity class. It allows you to perform simple formatting using events.  As this class allows minimal customization options, rendering will be faster than PDF Grid and is recommended to draw a simple table. Check the following comparison table for more details.

 

PdfGrid

It is based on cell model that offers rich API for formatting and layout options. It can take input from DataTable, arrays or any other entity class. Formatting can be done to all levels of PdfGrid. More features like Nested Table, Row and Column Spanning are also supported. It offers full control over the appearance and is recommended to draw complex table structures. Check the following comparison table for more details.

 

Comparison between PdfLightTable and PdfGrid

  --------------- --------------- ---------
  Platforms       PdfLightTable   PdfGrid
  Windows Forms   Yes             Yes
  WPF             Yes             Yes
  ASP.NET         Yes             Yes
  ASP.NET MVC     Yes             Yes
  Silverlight     Yes             Yes
  --------------- --------------- ---------

 

+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+
| Features                | PdfLightTable                                                                                | PdfGrid                        |
+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                         |
|                                                                                                                                                         |
| Formatting                                                                                                                                              |
+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+
| Row                     | No direct API, possible through events                                                       | Yes                            |
+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+
| Column                  | Yes (StringFormat)                                                                           | Yes (StringFormat)             |
+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+
| Cell                    | No direct API for single cell formatting, possible through events                            | Yes                            |
+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+
|                                                                                                                                                         |
|                                                                                                                                                         |
| Others                                                                                                                                                  |
+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+
| Row span                | No                                                                                           | Yes                            |
+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+
| Column span             | No direct API, possible through events                                                       | Yes                            |
+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+
| Nested Grid             | Possible through events                                                                      | Yes                            |
+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+
| Layout Events           | BeginCellLayout, BeginPageLayout, BeginRowLayout, EndCellLayout, EndPageLayout, EndRowLayout | BeginPageLayout, EndPageLayout |
+-------------------------+----------------------------------------------------------------------------------------------+--------------------------------+

 

More:







