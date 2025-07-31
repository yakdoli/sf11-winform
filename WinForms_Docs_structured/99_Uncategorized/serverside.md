---
title: serverside.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\serverside.md
created_at: 2025-07-03
---








  









### Server-Side {#server-side style="tab-stops: 0pt"}

[] 

GridGroupingControl has support different types of selection mode. Depending upon this our selection style can be varied.

 

The selection mode for the Grid control can be set via the **ListBoxSelectionMode** property in the TableOptions. The Grid can emulate list boxes and this property indicates the list box selection mode setting. The options are None, One, MultiSimple and MultiExtended. The grid\'s Table.SelectedRecords can be used to retrieve the selected records programmatically.

 

By default, selection is turned off (None), there will be no selected records, which means no rows will be highlighted when the user clicks on different rows (the current record indicator will still move along with the user\'s click).

[] 

[·      ]**One**: only a single row stays selected as the user clicks on different rows.

[·      ]**MultiSimple**: clicking on an unselected row selects it and clicking on an already selected row unselects it, without affecting the selection state of other rows. When the current row is moved by using ARROW keys, the selection state of the new current row will be toggled.

[·      ]**MultiExtended**: adjacent rows can be selected by pressing the SHIFT key and pressing the Up / Down buttons on the keyboard. To select the rows that are not adjacent, the user can hold down the CTRL key and click on the row he or she desires to select. To remove selection, the user should hold down the CTRL key and click the selected row.

[] 

The following code example illustrates this.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| [\                                                                                                                                                                                                      |
| ][GridGroupingControl1.TableOptions.ListBoxSelectionMode = Syncfusion.Web.UI.WebControls.Tools.SelectionMode.One;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                     |
|                                                                                                                                                                                                        |
| [\                                                                                                                                                                                                     |
| ][GridGroupingControl1.TableOptions.ListBoxSelectionMode = Syncfusion.Web.UI.WebControls.Tools.SelectionMode.One] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To access the selected record, events have been provided both on the server-side and client-side.

[] 

Server-Side Event

[] 

The event which will trigger for a record click on server side is **SelectedRecordsChanged** event.

[] 

Note:

[] 

The following properties has to be set to **True**, to handle this event.

[] 

[·      ]PostBackOnFocusedChanged

[·      ]PostBackOnRowDblClick

[] 

The following code example illustrates this.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [\                                                                                                                                                                                                                                                             |
| protected][ [void] GridGroupingControl1_RecordsChanged([object] sender, Syncfusion.Grouping.SelectedRecordsChangedEventArgs e)] |
|                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [Record r = [this].GridGroupingControl1.Table.CurrentRecord;]                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [if][(r != [null])]                                                                                                                                  |
|                                                                                                                                                                                                                                                                |
| [this][.TextBox1.Text = r.GetValue([\"id\"]).ToString();]                                                                                         |
|                                                                                                                                                                                                                                                                |
| [if][ (ViewState\[[\"currentrecord\"]\] == [null])]                                                                          |
|                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [ViewState\[[\"currentrecord\"]\] = r.GetValue([\"id\"]).ToString();]                                                                                                      |
|                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [else][ [if] (r != [null] && r.IsCurrent)]                                                                                      |
|                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [if][ (ViewState\[[\"currentrecord\"]\].ToString() != r.GetValue([\"id\"]).ToString())]                                   |
|                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [Record currentrec = r;]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                |
| [this][.TextBox1.Text = currentrec.GetValue([\"id\"]).ToString();]                                                                                |
|                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\                                                                                                                                                                                                                                                                                                                                                                          |
| Protected][ [Sub] GridGroupingControl1_RecordsChanged([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Grouping.SelectedRecordsChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [    [Dim] r [As] Record = [Me].GridGroupingControl1.Table.CurrentRecord]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [    [If] r [IsNot] [Nothing] [Then]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [        [Me].TextBox1.Text = r.GetValue([\"id\"]).ToString()]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [    [End] [If]]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [    [If] ViewState([\"currentrecord\"]) [Is] [Nothing] [Then]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [        ViewState([\"currentrecord\"]) = r.GetValue([\"id\"]).ToString()]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [    [ElseIf] r [IsNot] [Nothing] [AndAlso] r.IsCurrent [Then]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [        [If] ViewState([\"currentrecord\"]).ToString() \<\> r.GetValue([\"id\"]).ToString() [Then]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [            [Dim] currentrec [As] Record = r]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [            [Me].TextBox1.Text = currentrec.GetValue([\"id\"]).ToString()]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [        [End] [If]]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [    [End] [If]]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

