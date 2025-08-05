---
title: querycellinfoandcommitcellinfo.md
original_path: WinForms_Docs/99_Uncategorized/querycellinfoandcommitcellinfo.md
created_at: 2025-08-05
---






#### QueryCellInfo and CommitCellInfo {#querycellinfo-and-commitcellinfo style="tab-stops: 0pt"}

[] 

These events are widely used to allow customization of each and every cell in the required format. **QueryCellInfo** accepts an argument of type GridQueryCellInfoEventArgs and **CommitCellInfo** accepts an argument of type GridCommitCellInfoEventArgs. The table below  lists the customization properties exposed by these two event arguments.

[] 


  ---------- --------------------------------------------------------------------------
  Property   Description
  Cell       Gives the cell co-ordinates.
  Style      Specifies the style for the cell represented by the above Cell property.
  ---------- --------------------------------------------------------------------------


[] 

These events are essential to operate the grid in virtual mode, where:

[] 

[·      ]QueryCellInfo is used to provide the cell values on demand and,

[·      ]Changes made in the grid will be saved back by the CommitCellInfo event.

[] 

The QueryCellInfo is used to completely customize the grid cells. The code below sets up a Virtual Grid by applying these events and also paints alternate rows using QueryCellInfo event. The QueryCellInfo event is raised for each cell that requires redrawing.

[] 

Example

[] 

These events can be triggered using the following code:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [this][.grid.QueryCellInfo += [new] [GridQueryCellInfoEventHandler](grid_QueryCellInfo);]    |
|                                                                                                                                                                                                                                |
| [this][.grid.CommitCellInfo += [new] [GridCommitCellInfoEventHandler](grid_CommitCellInfo);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handlers

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Dictionary][\<[RowColumnIndex], [object]\> committedValues = [new] [Dictionary]\<[RowColumnIndex], [object]\>();] |
|                                                                                                                                                                                                                                                                                                                                                   |
| [void][ grid_QueryCellInfo([object] sender, GridQueryCellInfoEventArgs e)]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    [if] (e.Cell.ColumnIndex \> 0 && e.Cell.RowIndex \> 0)]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        [if] (e.Cell.RowIndex % 2 == 0)]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                   |
| [            e.Style.Background = Brushes.LightGreen;]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    [if] (e.Cell.RowIndex == 0)]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    {]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        [if] (e.Cell.ColumnIndex \> 0)]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                   |
| [            e.Style.CellValue = e.Cell.ColumnIndex;]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    }]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    [else] [if] (e.Cell.RowIndex \> 0)]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    {]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        [if] (e.Cell.ColumnIndex == 0)]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                   |
| [            e.Style.CellValue = e.Cell.RowIndex;]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        [else] [if] (e.Cell.ColumnIndex \> 0)]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                   |
| [            [if] (committedValues.ContainsKey(e.Cell))]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                   |
| [                e.Style.CellValue = committedValues\[e.Cell\];]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                   |
| [            [else]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                   |
| [                e.Style.CellValue = String.Format([\"{0}/{1}\"], e.Cell.RowIndex, e.Cell.ColumnIndex);]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    }]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [void][ grid_CommitCellInfo([object] sender, GridCommitCellInfoEventArgs e)]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    [if] (e.Style.HasCellValue)]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    {]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        committedValues\[e.Cell\] = e.Style.CellValue;]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        e.Handled = [true];]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    }]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Output

**[]** 

The following output is generated using the code above.

[] 

{border="0"}

[] 

Figure 82: QueryCellInfo and CommitCellInfo

 

[]{#p198} 

[]{#related-topics}

