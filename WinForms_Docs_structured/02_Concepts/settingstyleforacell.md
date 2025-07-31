---
title: settingstyleforacell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\settingstyleforacell.md
created_at: 2025-07-03
---






#### Setting Style for a Cell {#setting-style-for-a-cell style="tab-stops: 0pt"}

To specify the style for a particular cell, you need to handle the QueryCellInfo event on the embedded GridTreeControlImpl. The following code example illustrates this.

 

Here is the code for coloring a particular cell.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                      |
|                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                        |
|                                                                                                                                                                                                                 |
| [// Subscribe to the event.]                                                                                                                                  |
|                                                                                                                                                                                                                 |
| [gridTreeControl1.Model.QueryCellInfo += [new] [GridQueryCellInfoEventHandler](Model_QueryCellInfo);]                          |
|                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                      |
|                                                                                                                                                                                                                 |
| [// Event handler]                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [void][ Model_QueryCellInfo([object] sender, [GridQueryCellInfoEventArgs] e)] |
|                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                         |
|                                                                                                                                                                                                                 |
| [    [if] (e.Cell.RowIndex \> 0) [//skip header]]                                                                                |
|                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                     |
|                                                                                                                                                                                                                 |
| [        [// Get the node.]]                                                                                                                          |
|                                                                                                                                                                                                                 |
| [        [GridTreeNode] node = gridTreeControl1.InternalGrid.GetNodeAtRowIndex(e.Cell.RowIndex);]                                                   |
|                                                                                                                                                                                                                 |
| [        [if] (node != [null] && node.Item != [null])]                                                       |
|                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                 |
|                                                                                                                                                                                                                 |
| [            [// Cast it to the appropriate type.]]                                                                                                   |
|                                                                                                                                                                                                                 |
| [            [Employee] emp = node.Item [as] [Employee];]                                              |
|                                                                                                                                                                                                                 |
| [            [if] (emp != [null])]                                                                                                |
|                                                                                                                                                                                                                 |
| [            {]                                                                                                                                                             |
|                                                                                                                                                                                                                 |
| [                [// Pick out the cell by employee and column that you want to style.]]                                                               |
|                                                                                                                                                                                                                 |
| [                [// For example, here we color the Department of the employee whose ID is 159.]]                                                     |
|                                                                                                                                                                                                                 |
| [                [if] (emp.ID == 159)]                                                                                                                 |
|                                                                                                                                                                                                                 |
| [                {]                                                                                                                                                         |
|                                                                                                                                                                                                                 |
| [                    [string] name = gridTreeControl1.InternalGrid.ColumnIndexToName(e.Cell.ColumnIndex);]                                             |
|                                                                                                                                                                                                                 |
| [                    [if] (name == [\"Department\"])]                                                                          |
|                                                                                                                                                                                                                 |
| [                    {]                                                                                                                                                     |
|                                                                                                                                                                                                                 |
| [                        e.Style.Background = [Brushes].Red;]                                                                                       |
|                                                                                                                                                                                                                 |
| [                        e.Handled = [true];]                                                                                                          |
|                                                                                                                                                                                                                 |
| [                    }]                                                                                                                                                     |
|                                                                                                                                                                                                                 |
| [                }]                                                                                                                                                         |
|                                                                                                                                                                                                                 |
| [            }]                                                                                                                                                             |
|                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                 |
|                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                     |
|                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 261: Cell Style

 

Thus, the background of a grid cell can be customized.

 


{border="0"}Note: Level styles are the lowest in precedence, followed by column styles, and then followed by cell -specific styles set in QueryCellInfo.


 

[]{#p319} 

 

[]{#related-topics}

