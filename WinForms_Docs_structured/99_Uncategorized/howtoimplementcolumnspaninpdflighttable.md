---
title: howtoimplementcolumnspaninpdflighttable.md
original_path: WinForms_Docs/99_Uncategorized/howtoimplementcolumnspaninpdflighttable.md
created_at: 2025-08-05
---






#### How To Implement Column Span In PdfLightTable? {#how-to-implement-column-span-in-pdflighttable style="tab-stops: 0pt"}

 

You can span any number of columns with the help of the **BeginRowLayout** event handler and **ColumnSpan** property. ColumnSpanMap property of this event enables column spanning, which merges cells within a row. To specify the span, you should create an array of integers with size equal to the number of cells in a row, and assign it to the **ColumnSpanMap** property.

 

The description of the map values are as follows

 

[·      ]0 or 1: denotes an ordinary cell; 0 allows you to omit explicit specification of 1

[·      ]Negatives: denotes that the cell is covered by a merged cell; you should not specify those values

[·      ]2 and more: denotes how many cells should be merged

 

The following code example illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [void][ table_BeginRowLayout([object] sender, [BeginRowLayoutEventArgs] args)] |
|                                                                                                                                                                                                               |
| [{]                                                                                                                                                                       |
|                                                                                                                                                                                                               |
| [   [if] (args.RowIndex == 1)]                                                                                                                       |
|                                                                                                                                                                                                               |
| [   {]                                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [     [PdfLightTable] table = ([PdfLightTable])sender;]                                                                         |
|                                                                                                                                                                                                               |
| [     [int] count = table.Columns.Count;]                                                                                                            |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [     [int]\[\] spanMap = [new] [int]\[count\];]                                                           |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [     [// Set just spanned cells. Other values are not important]]                                                                                  |
|                                                                                                                                                                                                               |
| [     [// Except negatives that are not allowed.]]                                                                                                  |
|                                                                                                                                                                                                               |
| [     spanMap\[0\] = 2;]                                                                                                                                                  |
|                                                                                                                                                                                                               |
| [     spanMap\[2\] = 3;]                                                                                                                                                  |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [     args.ColumnSpanMap = spanMap;]                                                                                                                                      |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [     [//Sets row height.]]                                                                                                                         |
|                                                                                                                                                                                                               |
| [     args.MinimalHeight = 30f;]                                                                                                                                          |
|                                                                                                                                                                                                               |
| [   }]                                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [}]                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] table_BeginRowLayout([ByVal] sender [As] [Object], [ByVal] args [As] BeginRowLayoutEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                    |
| [   [If] args.RowIndex = 1 [Then]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                    |
| [       [Dim] table [As] PdfLightTable = [CType](sender, PdfLightTable)]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                    |
| [       [Dim] count [As] [Integer] = table.Columns.Count]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [       [Dim] spanMap [As] [Integer]() = [New] [Integer](count - 1){}]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [       [\' Set just spanned cells. Other values are not important]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                    |
| [       [\' Except negatives that are not allowed.]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                    |
| [       spanMap(0) = 2]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                    |
| [       spanMap(2) = 3]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [       args.ColumnSpanMap = spanMap]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                    |
| [       [\'Sets row height.]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                    |
| [       args.MinimalHeight = 30f]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                    |
| [   [End] [If]]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

