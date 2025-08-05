---
title: howtocreatemultiplerowsperrecordinagridgroupingcontrol.md
original_path: WinForms_Docs/04_Controls/Grid/howtocreatemultiplerowsperrecordinagridgroupingcontrol.md
created_at: 2025-08-05
---






#### How to create multiple rows per record in a GridGroupingControl {#how-to-create-multiple-rows-per-record-in-a-gridgroupingcontrol style="tab-stops: 0pt"}

[] 

This can be done by using the **ColumnSets** property of the GridGrouping control.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [//Create a  GridColumnSpanDescriptor and initialize to a column  and mention its location to display ]                                                         |
|                                                                                                                                                                                                                   |
| [GridColumnSpanDescriptor columnSpanDescriptor1 = [new] GridColumnSpanDescriptor([\"Name\"],[\"R0C0\"]); ] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [//Create a GridColumnSetDescriptor ]                                                                                                                           |
|                                                                                                                                                                                                                   |
| [GridColumnSetDescriptor columnSetDescriptor1 = [new] GridColumnSetDescriptor();]                                                                        |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [//Add the  GridColumnSpanDescriptor to the GridColumnSetDescriptor ]                                                                                           |
|                                                                                                                                                                                                                   |
| [columnSetDescriptor1.ColumnSpans.Add(columnSpanDescriptor1);]                                                                                                                |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [//Add the GridColumnSetDescriptor  to the ColumnSet of the GridGroupingControl through the TableDescriptor.]                                                   |
|                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TableDescriptor.ColumnSets.Add(columnSetDescriptor1);]                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [\'Create a  GridColumnSpanDescriptor and initialize to a column  and mention its location to display ]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                   |
| [Dim][ columnSpanDescriptor1 [As] GridColumnSpanDescriptor = [New] GridColumnSpanDescriptor([\"Name\"], [\"R0C0\"])] |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [\'Create a GridColumnSetDescriptor ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                   |
| [Dim][ columnSetDescriptor1 [As] GridColumnSetDescriptor = [New] GridColumnSetDescriptor()]                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [\'Add the  GridColumnSpanDescriptor to the GridColumnSetDescriptor ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                   |
| [columnSetDescriptor1.ColumnSpans.Add(columnSpanDescriptor1)]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [\'Add the GridColumnSetDescriptor  to the ColumnSet of the GridGroupingControl through the TableDescriptor.]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                   |
| [Me][.gridGroupingControl1.TableDescriptor.ColumnSets.Add(columnSetDescriptor1)]                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p679} 

 

[]{#related-topics}

