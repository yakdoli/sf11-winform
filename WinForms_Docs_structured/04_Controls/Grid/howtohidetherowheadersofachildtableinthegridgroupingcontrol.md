---
title: howtohidetherowheadersofachildtableinthegridgroupingcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtohidetherowheadersofachildtableinthegridgroupingcontrol.md
created_at: 2025-07-03
---






#### How to hide the row headers of a child table in the GridGroupingControl {#how-to-hide-the-row-headers-of-a-child-table-in-the-gridgroupingcontrol style="tab-stops: 0pt"}

[] 

You can do this by accessing the Child Table of the GridGroupingControl using the **GridTableModel**. Then handle the **QueryColWidth** event handler of the Child Table, and hide the Row Header (which is column zero) by setting the **Size** property to *Zero*.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [GridTableModel][ tbl = [this].gridGroupingControl1.GetTableModel([\"ChildTable\"]); ] |
|                                                                                                                                                                                                                             |
| [tbl.QueryColWidth += [new] GridRowColSizeEventHandler(tbl_QueryColWidth); ]                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [void][ tbl_QueryColWidth([object] sender, GridRowColSizeEventArgs e) ]                                           |
|                                                                                                                                                                                                                             |
| [{ ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [if][ (e.Index == 0) ]                                                                                                                 |
|                                                                                                                                                                                                                             |
| [{ ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [e.Size = 0; ]                                                                                                                                                                          |
|                                                                                                                                                                                                                             |
| [e.Handled = [true]; ]                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [} ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [} ]                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [Dim][ tbl [As] GridTableModel = [Me].GridGroupingControl1.GetTableModel([\"ChildTable\"])]                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| [AddHandler][ tbl.QueryColWidth, [AddressOf] tbl_QueryColWidth ]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] tbl_QueryColWidth([ByVal] sender [As] [Object], [ByVal] e [As] GridRowColSizeEventArgs)] |
|                                                                                                                                                                                                                                                                                                                              |
| [If][ e.Index = 0 [Then]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                              |
| [e.Size = 0]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                              |
| [e.Handled = [True]]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                              |
| [End][ [If]]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub] [\'tbl_QueryColWidth ]]                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p661} 

 

[]{#related-topics}

