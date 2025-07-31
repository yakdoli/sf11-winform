---
title: dataselection.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\dataselection.md
created_at: 2025-07-03
---








  









## Data Selection {#data-selection style="tab-stops: 0pt"}

[] 

GridGroupingControl provides support for different types of selection modes. Depending upon the selection mode, the selection style can be varied. The following code example illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [GridGroupingControl1.TableOptions.ListBoxSelectionMode = Syncfusion.Web.UI.WebControls.Tools.SelectionMode.One;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                   |
|                                                                                                                                                      |
| []                                                                                                  |
|                                                                                                                                                      |
| [GridGroupingControl1.TableOptions.ListBoxSelectionMode = Syncfusion.Web.UI.WebControls.Tools.SelectionMode.One] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To access the Selected record, events have been provided both on the server-side and client-side.

[] 

Server-Side Event

[] 

The **SelectedRecordsChanged** event will be triggered on a record click on the server-side.

[] 

Note:

[] 

The following properties have to be set to **True**, to trigger the event.

[] 

[·      ]PostBackOnFocusedChanged

[·      ]PostBackOnRowDblClick

[] 

Refer the below code snippet which illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [protected][ [void] GridGroupingControl1_RecordsChanged([object] sender, Syncfusion.Grouping.[SelectedRecordsChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [Record][ r = [this].GridGroupingControl1.Table.CurrentRecord;]                                                                                                              |
|                                                                                                                                                                                                                                                                                           |
| [if][(r != [null])]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| [this][.TextBox1.Text = r.GetValue([\"id\"]).ToString();]                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [if][ (ViewState\[[\"currentrecord\"]\] == [null])]                                                                                                     |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [ViewState\[[\"currentrecord\"]\] = r.GetValue([\"id\"]).ToString();]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [else][ [if] (r != [null] && r.IsCurrent)]                                                                                                                 |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [if][ (ViewState\[[\"currentrecord\"]\].ToString() != r.GetValue([\"id\"]).ToString())]                                                              |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [Record][ currentrec = r;]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [this][.TextBox1.Text = currentrec.GetValue([\"id\"]).ToString();]                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                      |
| [    [Protected] [Sub] GridGroupingControl1_RecordsChanged([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Grouping.SelectedRecordsChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                      |
| [        [Dim] r [As] Syncfusion.Grouping.Record = [Me].GridGroupingControl1.Table.CurrentRecord]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                      |
| [        [If] r [IsNot] [Nothing] [Then]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                      |
| [            [Me].TextBox1.Text = r.GetValue([\"id\"]).ToString()]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                      |
| [        [End] [If]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                      |
| [        [If] ViewState([\"currentrecord\"]) [Is] [Nothing] [Then]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                      |
| [            ViewState([\"currentrecord\"]) = r.GetValue([\"id\"]).ToString()]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                      |
| [        [ElseIf] r [IsNot] [Nothing] [AndAlso] r.IsCurrent [Then]]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                      |
| [            [If] ViewState([\"currentrecord\"]).ToString() \<\> r.GetValue([\"id\"]).ToString() [Then]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                      |
| [                [Dim] currentrec [As] Syncfusion.Grouping.Record = r]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                      |
| [                [Me].TextBox1.Text = currentrec.GetValue([\"id\"]).ToString()]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                      |
| [            [End] [If]]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                      |
| [        [End] [If]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                      |
| [    [End] [Sub]]                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Client-Side Event

[] 

The **ClientSideOnRecordClick** event will be triggered on a record click on the client-side.\
\
Refer the below code snippet which illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][sfwg][:][GridGroupingControl][ [ID][=\"GridGroupingControl1\"] [runat][=\"server\" ][ClientSideOnRecordClick][=\"][select][(][this][)\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][sfwg][:][GridGroupingControl][\>]                                                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[JScript\]]**                                                   |
|                                                                                                                       |
| []                                                                   |
|                                                                                                                       |
| [function select(gridObj)]                                                        |
|                                                                                                                       |
| [{]                                                                               |
|                                                                                                                       |
| [document.getElementById(\'TextBox1\').innerText = gridObj.Row.GetValue(\'id\');] |
|                                                                                                                       |
| [}]                                                                               |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

[]{#p46}[] 

More:







