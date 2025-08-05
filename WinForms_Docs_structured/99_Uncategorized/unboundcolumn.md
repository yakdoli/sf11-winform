---
title: unboundcolumn.md
original_path: WinForms_Docs/99_Uncategorized/unboundcolumn.md
created_at: 2025-08-05
---








  









### Unbound Column {#unbound-column style="tab-stops: 0pt"}

[] 

An unbound column is a column that is not bound to any data. You can add unbound columns to a grid programmatically, and populate the column\'s cells manually. The data for this column can be accessed from a custom data source or by calculating an arithmetic expression against bound columns.

[] 

Creating Unbound Columns

**[]** 

Through Designer

[] 

The **GridUnboundFieldDescriptor** Collection Editor can be used to add Unbound columns to the grid. This collection editor can be viewed by clicking on the **GridUnboundFields** property from the TableDescriptor.

[] 

{border="0"}

Figure 46

[] 

Through Code

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [this][.GridGroupingControl1.TableDescriptor.UnboundFields.Add([\"TotalUnboundField\"]);]                                         |
|                                                                                                                                                                                                                                                |
| [this][.GridGroupingControl1.QueryValue += [new] [FieldValueEventHandler](GridGroupingControl1_QueryValue);] |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [void][ GridGroupingControl1_QueryValue([object] sender, [FieldValueEventArgs] e)]                           |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [if][ (e.Field.MappingName == [\"TotalUnboundField\"])]                                                                           |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [e.Value = ([int])e.Record.GetValue([\"Col1\"]) + ([int])e.Record.GetValue([\"Col2\"]); ]                        |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [Me][.GridGroupingControl1.TableDescriptor.UnboundFields.Add([\"TotalUnboundField\"])]                              |
|                                                                                                                                                                                                                                 |
| [AddHandler][ GridGroupingControl1.QueryValue, [AddressOf] GridGroupingControl1_QueryValue]                           |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [void GridGroupingControl1_QueryValue([Object] sender, FieldValueEventArgs e)]                                                                                         |
|                                                                                                                                                                                                                                 |
| [If][ e.Field.MappingName = [\"TotalUnboundField\"] [Then]]                                    |
|                                                                                                                                                                                                                                 |
| [e.Value = [CInt](Fix(e.Record.GetValue([\"Col1\"]))) + [CInt](Fix(e.Record.GetValue([\"Col2\"])))] |
|                                                                                                                                                                                                                                 |
| [End][ [If]]                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 47

[] 

[]{#related-topics}

