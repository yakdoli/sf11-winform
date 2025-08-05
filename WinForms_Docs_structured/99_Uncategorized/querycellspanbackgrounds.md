---
title: querycellspanbackgrounds.md
original_path: WinForms_Docs/99_Uncategorized/querycellspanbackgrounds.md
created_at: 2025-08-05
---






#### QueryCellSpanBackgrounds {#querycellspanbackgrounds style="tab-stops: 0pt"}

[] 

This event lets you create cell spans and customize their backgrounds. It receives an argument of type GridQueryCellSpanBackgroundsEventArgs containing the following properties.

[] 


  -------------------- ---------------------------------------------
  Property             Description
  CellRowColumnIndex   Represents the cell row and column indices.
  Range                Defines the covered range for the cell.
  -------------------- ---------------------------------------------


[] 

Example

**[]** 

This event can be triggered using the following code:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [grid.QueryCellSpanBackgrounds += [new] [GridQueryCellSpanBackgroundsEventHandler ](grid_QueryCellSpanBackgrounds);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [void][ grid_QueryCellSpanBackgrounds([object] sender, GridQueryCellSpanBackgroundsEventArgs e)] |
|                                                                                                                                                                                                            |
| [{]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [    [if] (e.CellRowColumnIndex.ColumnIndex == 2 && e.CellRowColumnIndex.RowIndex == 4)]                                                          |
|                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                |
|                                                                                                                                                                                                            |
| [        CellSpanBackgroundInfo item = [new] CellSpanBackgroundInfo(e.CellRowColumnIndex.RowIndex, e.CellRowColumnIndex.ColumnIndex, 9, 4);]      |
|                                                                                                                                                                                                            |
| [        item.Background = [new] ImageBrush(GetImage([@\"common\\Images\\Grid\\BannerCells\\back2.jpg\"]));]              |
|                                                                                                                                                                                                            |
| [        e.Range = [new] List\<CellSpanBackgroundInfo\>();]                                                                                       |
|                                                                                                                                                                                                            |
| [        e.Range.Add(item);]                                                                                                                                           |
|                                                                                                                                                                                                            |
| [        e.Handled = [true];]                                                                                                                     |
|                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                |
|                                                                                                                                                                                                            |
| [}]                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Output

**[]** 

The following output is generated using the code above.

[] 

{border="0"}

[] 

Figure 50: QueryCellSpanBackgrounds

[]{#p201} 

[]{#related-topics}

