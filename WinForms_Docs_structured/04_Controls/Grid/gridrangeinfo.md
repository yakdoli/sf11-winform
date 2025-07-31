---
title: gridrangeinfo.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\gridrangeinfo.md
created_at: 2025-07-03
---






##### GridRangeInfo {#gridrangeinfo style="tab-stops: 0pt"}

[] 

This class is used extensively to specify a collection of grid cells that are to be used as parameters for other method calls. **GridRangeInfo** class contains static methods that will allow you to specify a single cell, a rectangular range of cells, a row or rows, a column or columns, or the entire table.

[] 


  --------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------
  GridRangeInfo Method                                            Description
  GridRangeInfo.Cell(int row, int col)                            Returns the GridRangeInfo object with cell row, col.
  GridRangeInfo.Cells(int top, int left, int bottom, int right)   Returns a GridRangeInfo object containing a rectangular collection of cells with top left cell (top, left) and bottom right cell (bot, right).
  GridRangeInfo.Row(int row)                                      Returns GridRangeInfo object with row = row.
  GridRangeInfo.Rows(int fromRow, int toRow)                      Returns a GridRangeInfo object containing rows fromRow through toRow.
  GridRangeInfo.Col(int col)                                      Returns GridRangeInfo object with column col.
  GridRangeInfo.Cols(int fromCol, int toCol)                      Returns a GridRangeInfo object containing columns fromCol through toCol.
  GridRangeInfo.Table()                                           Returns a GridRangeInfo object containing the whole table.
  --------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------


[] 


{border="0"}Note: For a complete description of the GridRangeInfo class, see the Essential Grid Class Reference.


 

[]{#p76} 

 

[]{#related-topics}

