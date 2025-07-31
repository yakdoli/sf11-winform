---
title: howtohidetheplusminussymboloftheparenttablewhenthereisnorecordinthechildtable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtohidetheplusminussymboloftheparenttablewhenthereisnorecordinthechildtable.md
created_at: 2025-07-03
---








  









## How to hide the Plus / Minus symbol of the parent table when there is no record in the child table {#how-to-hide-the-plus-minus-symbol-of-the-parent-table-when-there-is-no-record-in-the-child-table style="tab-stops: 0pt"}

[] 

In order to hide the Plus / Minus symbol of the parent table when there is no record in the child table, you have to set the Plus / Minus **CellType** property of the parent table to *Static*. The following code example illustrates this.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [protected][ [void] GridGroupingControl1_QueryCellStyleInfo([object] sender, [GridTableCellStyleInfoEventArgs] e)] |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [if][ (e.TableCellIdentity.TableCellType == [GridTableCellType].RecordPlusMinusCell)]                                                                        |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [Record r = e.TableCellIdentity.DisplayElement.ParentRecord [as] Record;]                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [if][ (r != [null] && r.NestedTables.Count \> 0 && r.NestedTables\[0\].ChildTable.FilteredChildNodeCount == 0)]                                                 |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [e.Style.CellType = [\"Static\"];]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [} ]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Protected][ [Sub] GridGroupingControl1_QueryCellStyleInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridTableCellStyleInfoEventArgs)]                 |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [If][ e.TableCellIdentity.TableCellType = GridTableCellType.RecordPlusMinusCell [Then]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ r [As] Record = [CType](IIf([TypeOf] e.TableCellIdentity.DisplayElement.ParentRecord [Is] Record, e.TableCellIdentity.DisplayElement.ParentRecord, [Nothing]), Record)] |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [If][ [Not] r [Is] [Nothing] [AndAlso] r.NestedTables.Count \> 0 [AndAlso] r.NestedTables(0).ChildTable.FilteredChildNodeCount = 0 [Then]]                |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [e.Style.CellType = [\"Static\"]]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [If]]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [If]]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p121} 

[]{#related-topics}

