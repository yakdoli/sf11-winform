---
title: howtogettherowpositionoftheaddnewrecordinthegridgroupingcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtogettherowpositionoftheaddnewrecordinthegridgroupingcontrol.md
created_at: 2025-07-03
---






#### How to get the row position of the AddNewRecord in the GridGroupingControl {#how-to-get-the-row-position-of-the-addnewrecord-in-the-gridgroupingcontrol style="tab-stops: 0pt"}

[] 

You can get the row index of the AddNewRecord using the **SourceListRecordChanged** event handler. In the event handler, you can check the **e.Action** property and get the row position from the **FilteredRecordsCollection**.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [void][ gridGroupingControl1_SourceListRecordChanged([object] sender, RecordChangedEventArgs e)] |
|                                                                                                                                                                                                            |
| [{]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [if][ (e.Action == RecordChangedType.Added)]                                                                          |
|                                                                                                                                                                                                            |
| [{]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [int][ offset = gridGroupingControl1.TableControl.GetMinimumTopRowIndex();]                                           |
|                                                                                                                                                                                                            |
| [int][ newRowIndex = e.TableListChangedEventArgs.Table.FilteredRecords.IndexOf(e.Record) + offset;]                   |
|                                                                                                                                                                                                            |
| [Console][.WriteLine(newRowIndex);]                                                                                |
|                                                                                                                                                                                                            |
| [}]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [} ]                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] gridGroupingControl1_SourceListRecordChanged([ByVal] sender [As] [Object], [ByVal] e [As] RecordChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                        |
| [If][ e.Action = RecordChangedType.Added [Then]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Dim][ offset [As] [Integer] = gridGroupingControl1.TableControl.GetMinimumTopRowIndex()]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Dim][ newRowIndex [As] [Integer] = e.TableListChangedEventArgs.Table.FilteredRecords.IndexOf(e.Record) + offset]                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Console.WriteLine(newRowIndex)]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [If]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p701} 

 

[]{#related-topics}

