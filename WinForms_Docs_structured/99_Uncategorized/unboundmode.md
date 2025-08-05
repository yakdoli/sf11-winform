---
title: unboundmode.md
original_path: WinForms_Docs/99_Uncategorized/unboundmode.md
created_at: 2025-08-05
---






##### Unbound Mode {#unbound-mode style="tab-stops: 0pt"}

[] 

The Grid Grouping control can be operated in **Unbound Mode**. In unbound mode, you can add your own columns to the grouping grid along with the other bound columns.

[] 

**Implementation**

**[]** 

This section demonstrates how to add custom columns to a grouping grid. The **TableDescriptor.UnboundFields.Add()** method will allow you to add unbound fields to the grouping grid. The unbound values can be provided in QueryValue event and any changes in the values can be stored back to the data store by handling SaveValue event. Additionally, you can handle QueryCellStyleInfo event to customize the unbound cells individually.

 

The values must be saved somewhere because the grouping grid does not maintain any data structure to store the cell values. Since the values are unbound, they cannot be stored into the bound data source too. In this example, a HashTable is used to save the values of the unbound column.

 

The example displays an unbound CheckBox column along with other bound columns using a grouping grid.

[] 

1.   Create a Grid Grouping control and bind it to a data store.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [private][ Syncfusion.Windows.Forms.Grid.Grouping.[GridGroupingControl] gridGroupingControl1;]                             |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Define a Grouping Grid.]                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| [this][.gridGroupingControl1 = [new] Syncfusion.Windows.Forms.Grid.Grouping.[GridGroupingControl]();] |
|                                                                                                                                                                                                                                         |
| [this][.gridGroupingControl1.Size = [new] System.Drawing.[Size](160,200 );]                           |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Create a Data Store.]                                                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [DataTable][ dt = [new] [DataTable]([\"MyTable\"]);]                       |
|                                                                                                                                                                                                                                         |
| [int][ nCols = 2;]                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [int][ nRows = 5;]                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [for][([int] i = 0; i \< nCols; i++)]                                                                                         |
|                                                                                                                                                                                                                                         |
| [dt.Columns.Add([new] DataColumn([string].Format([\"Col{0}\"], i)));]                                                             |
|                                                                                                                                                                                                                                         |
| [for][([int] i = 0; i \< nRows; ++i)]                                                                                         |
|                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [DataRow][ dr = dt.NewRow();]                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [for][([int] j = 0; j \< nCols; j++)]                                                                                         |
|                                                                                                                                                                                                                                         |
| [dr\[j\] = [string].Format([\"row{0} col{1}\"], i, j);]                                                                                                |
|                                                                                                                                                                                                                                         |
| [dt.Rows.Add(dr);]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [// Bind the data source to the grouping grid.]                                                                                                                                       |
|                                                                                                                                                                                                                                         |
| [this][.gridGroupingControl1.DataSource = dt;]                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                               |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [\' Define a Grouping Grid.]                                                                                                                                   |
|                                                                                                                                                                                                                  |
| [Private][ gridGroupingControl1 [As] Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl]       |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1 = [New] Syncfusion.Windows.Forms.Grid.Grouping.GridGroupingControl()]       |
|                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.Size = [New] System.Drawing.Size(160,200 )]                                 |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [\' Create a Data Store.]                                                                                                                                      |
|                                                                                                                                                                                                                  |
| [Dim][ dt [As] DataTable = [New] DataTable([\"MyTable\"])] |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ nCols [As] [Integer] = 2]                                                  |
|                                                                                                                                                                                                                  |
| [Dim][ nRows [As] [Integer] = 5]                                                  |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ i [As] [Integer] = 0]                                                      |
|                                                                                                                                                                                                                  |
| [Do][ [While] i \< nCols]                                                                              |
|                                                                                                                                                                                                                  |
| [dt.Columns.Add([New] DataColumn([String].Format([\"Col{0}\"], i)))]                                        |
|                                                                                                                                                                                                                  |
| [i += 1]                                                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [Loop]                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [i = 0]                                                                                                                                                                      |
|                                                                                                                                                                                                                  |
| [Do][ [While] i \< nRows]                                                                              |
|                                                                                                                                                                                                                  |
| [Dim][ dr [As] DataRow = dt.NewRow()]                                                                  |
|                                                                                                                                                                                                                  |
| [Dim][ j [As] [Integer] = 0]                                                      |
|                                                                                                                                                                                                                  |
| [Do][ [While] j \< nCols]                                                                              |
|                                                                                                                                                                                                                  |
| [dr(j) = [String].Format([\"row{0} col{1}\"], i, j)]                                                                             |
|                                                                                                                                                                                                                  |
| [j += 1]                                                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [Loop]                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [dt.Rows.Add(dr)]                                                                                                                                                            |
|                                                                                                                                                                                                                  |
| [i += 1]                                                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [Loop]                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [\' Bind the data source to the grouping grid.]                                                                                                                |
|                                                                                                                                                                                                                  |
| [Me][.GridGroupingControl1.DataSource = dt]                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create a FieldDescriptor that well describes your custom column and add it to the UnboundFieldDescriptor collection of the grouping grid.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                           |
| [FieldDescriptor][ unboundField = [new] [FieldDescriptor]([\"CheckboxCol\"], [\"\"], [false], [\"\"]);] |
|                                                                                                                                                                                                                                                                                                                                           |
| [unboundField.ReadOnly = [false];]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                           |
| [this][.gridGroupingControl1.TableDescriptor.UnboundFields.Add(unboundField);]                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                           |
| [Dim][ unboundField [As] FieldDescriptor = [New] FieldDescriptor([\"CheckboxCol\"], [\"\"], [False], [\"\"])] |
|                                                                                                                                                                                                                                                                                                                                           |
| [unboundField.ReadOnly = [False]]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                           |
| [Me][.gridGroupingControl1.TableDescriptor.UnboundFields.Add(unboundField)]                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Setup check boxes in the unbound column. You can also customize the unbound cells through the Appearance property.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [gridGroupingControl1.TableDescriptor.Columns\[[\"CheckboxCol\"]\].Appearance.AnyRecordFieldCell.CellType = [\"CheckBox\"];]                              |
|                                                                                                                                                                                                                                               |
| [gridGroupingControl1.TableDescriptor.Columns\[[\"CheckboxCol\"]\].Appearance.AnyRecordFieldCell.CheckBoxOptions.CheckedValue = [\"True\"];]              |
|                                                                                                                                                                                                                                               |
| [gridGroupingControl1.TableDescriptor.Columns\[[\"CheckboxCol\"]\].Appearance.AnyRecordFieldCell.CheckBoxOptions.UncheckedValue = [\"False\"];]           |
|                                                                                                                                                                                                                                               |
| [gridGroupingControl1.TableDescriptor.Columns\[[\"CheckboxCol\"]\].Appearance.AnyRecordFieldCell.HorizontalAlignment = [GridHorizontalAlignment].Center;] |
|                                                                                                                                                                                                                                               |
| [gridGroupingControl1.TableDescriptor.Columns\[[\"CheckboxCol\"]\].Appearance.AnyRecordFieldCell.VerticalAlignment = [GridVerticalAlignment].Middle;]     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [gridGroupingControl1.TableDescriptor.Columns([\"CheckboxCol\"]).Appearance.AnyRecordFieldCell.CellType = [\"CheckBox\"]]                     |
|                                                                                                                                                                                                                                   |
| [gridGroupingControl1.TableDescriptor.Columns([\"CheckboxCol\"]\].Appearance.AnyRecordFieldCell.CheckBoxOptions.CheckedValue = [\"True\"]]    |
|                                                                                                                                                                                                                                   |
| [gridGroupingControl1.TableDescriptor.Columns([\"CheckboxCol\"]\].Appearance.AnyRecordFieldCell.CheckBoxOptions.UncheckedValue = [\"False\"]] |
|                                                                                                                                                                                                                                   |
| [gridGroupingControl1.TableDescriptor.Columns([\"CheckboxCol\"]\].Appearance.AnyRecordFieldCell.HorizontalAlignment = GridHorizontalAlignment.Center]                 |
|                                                                                                                                                                                                                                   |
| [gridGroupingControl1.TableDescriptor.Columns([\"CheckboxCol\"]\].Appearance.AnyRecordFieldCell.VerticalAlignment = GridVerticalAlignment.Middle]                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Handle QueryValue and SaveValue events to set and save back the unbound values. Define a HashTable to store the unbound values.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [Hashtable][ unboundValues = [new] [Hashtable]();]                                                             |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [private][ [void] gridGroupingControl1_QueryValue([object] sender, [FieldValueEventArgs] e)] |
|                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [    [if] (e.Field.Name == [\"CheckboxCol\"])]                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [        [string] key = e.Record.GetValue([\"Col1\"]).ToString();]                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [        [if] (key != [null])]                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [            [object] val = unboundValues\[key\];]                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [            e.Value = val;]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [private][ [void] gridGroupingControl1_SaveValue([object] sender, [FieldValueEventArgs] e)]  |
|                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [    [if] (e.Field.Name == [\"CheckboxCol\"])]                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [        [string] key = e.Record.GetValue([\"Col1\"]).ToString();]                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [        [if] (key != [null])]                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [            [object] val = e.Value;]                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| [            unboundValues\[key\] = val;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Hashtable(unboundValues = [New] Hashtable())]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] gridGroupingControl1_QueryValue([ByVal] sender [As] [Object], [ByVal] e [As] FieldValueEventArgs) [Handles] gridGroupingControl1.QueryValue] |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [If][ e.Field.Name = [\"CheckboxCol\"] [Then]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ key [As] [String] = e.Record.GetValue([\"Col1\"]).ToString()]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [If][ [Not] key [Is] [Nothing] [Then]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ val [As] [Object] = unboundValues(key)]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [e.Value = val]                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [If]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [If]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] gridGroupingControl1_SaveValue([ByVal] sender [As] [Object], [ByVal] e [As] FieldValueEventArgs) [Handles] gridGroupingControl1.SaveValue]   |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [If][ e.Field.Name = [\"CheckboxCol\"] [Then]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ key [As] [String] = e.Record.GetValue([\"Col1\"]).ToString()]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [If][ [Not] key [Is] [Nothing] [Then]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ val [As] [Object] = e.Value]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [unboundValues(key) = val]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [If]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [If]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Customize the unbound cells by handling the QueryCellStyleInfo event.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [this][.gridGroupingControl1.QueryCellStyleInfo += [new] Syncfusion.Windows.Forms.Grid.Grouping.[GridTableCellStyleInfoEventHandler]([this].gridGroupingControl1_QueryCellStyleInfo);] |
|                                                                                                                                                                                                                                                                                                                                               |
| [      ]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                               |
| [private][ [void] gridGroupingControl1_QueryCellStyleInfo([object] sender, [GridTableCellStyleInfoEventArgs] e)]                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [if] (e.TableCellIdentity.ColIndex == 3 && e.TableCellIdentity.RowIndex \> 2)]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                               |
| [    {]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                               |
| [        [if] (e.TableCellIdentity.RowIndex % 4 == 0)]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| [        e.Style.CellValue = [false];]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| [        [else]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| [        e.Style.CellValue = [true];]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| [    }]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] gridGroupingControl1_QueryCellStyleInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridTableCellStyleInfoEventArgs) [Handles] gridGroupingControl1.QueryCellStyleInfo] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [If][ e.TableCellIdentity.ColIndex = 3 [AndAlso] e.TableCellIdentity.RowIndex \> 2 [Then]]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [If][ e.TableCellIdentity.RowIndex [Mod] 4 = 0 [Then]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.Style.CellValue = [False]]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Else]                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.Style.CellValue = [True]]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Run the sample. Here is a sample screenshot.

[] 

{border="0"}

[] 

*[Figure ][267][: Adding Unbound Columns to the Grid Grouping Control]*

 

[]{#p414} 

 

[]{#related-topics}

