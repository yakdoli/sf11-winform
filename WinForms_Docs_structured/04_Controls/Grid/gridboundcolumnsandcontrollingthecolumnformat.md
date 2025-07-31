---
title: gridboundcolumnsandcontrollingthecolumnformat.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\gridboundcolumnsandcontrollingthecolumnformat.md
created_at: 2025-07-03
---






#### GridBoundColumns and Controlling the Column Format {#gridboundcolumns-and-controlling-the-column-format style="tab-stops: 0pt"}

[] 

To control the properties of a column in your Grid Data Bound Grid, you must use a **GridBoundColumn** class object. You can also explicitly add a GridBoundColumn object to the **GridDataBoundGrid.GridBoundColumns** collection for each column that you want to see in the grid or you can let the **GridDataBoundGrid.Binder** class generate these columns for you.

 

Here are the code samples that will explicitly add GridBoundColumns. Note that you can add these GridBoundColumns at design-time provided that you properly set the **MappingName** property for each column.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [private][ [void] Form1_Load([object] sender, System.[EventArgs] e)]          |
|                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                      |
| [    [this].gridDataBoundGrid1.DataSource = ReturnATable();]                                                                                                                |
|                                                                                                                                                                                                                                      |
| [    [this].gridDataBoundGrid1.EnableAddNew = [false];]                                                                                                |
|                                                                                                                                                                                                                                      |
| [    [this].gridDataBoundGrid1.BackColor = [Color].FromArgb(0xcc, 0xd4, 0xe6);]                                                                     |
|                                                                                                                                                                                                                                      |
| [        ]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| [    [// Create a GridBoundColumn for each displayed column.]]                                                                                                             |
|                                                                                                                                                                                                                                      |
| [    [GridBoundColumn] gbc = [new] [GridBoundColumn]();]                                                                    |
|                                                                                                                                                                                                                                      |
| [    gbc.MappingName = [\"FirstName\"];  ]                                                                                                                               |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [    [// Must set to column mapping name.]]                                                                                                                                |
|                                                                                                                                                                                                                                      |
| [    gbc.HeaderText = [\"Name\"];]                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [    [// Set some style properties.]]                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [    gbc.StyleInfo.BackColor = [Color].FromArgb(0xC0, 0xC9, 0xdb);]                                                                                                      |
|                                                                                                                                                                                                                                      |
| [    gbc.StyleInfo.TextColor = [Color].Blue;]                                                                                                                            |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [    [// Add the column to the GridBoundColumns collection.]]                                                                                                              |
|                                                                                                                                                                                                                                      |
| [    [this].gridDataBoundGrid1.GridBoundColumns.Add(gbc);]                                                                                                                  |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [    [// Repeat for each column.]]                                                                                                                                         |
|                                                                                                                                                                                                                                      |
| [    gbc = [new] [GridBoundColumn]();]                                                                                                              |
|                                                                                                                                                                                                                                      |
| [    gbc.MappingName = [\"LastName\"];]                                                                                                                                  |
|                                                                                                                                                                                                                                      |
| [    gbc.HeaderText = [\"FamilyName\"];]                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [    gbc.StyleInfo.Font.Bold = [true];]                                                                                                                                     |
|                                                                                                                                                                                                                                      |
| [    [this].gridDataBoundGrid1.GridBoundColumns.Add(gbc);]                                                                                                                  |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [    gbc = [new] [GridBoundColumn]();]                                                                                                              |
|                                                                                                                                                                                                                                      |
| [    gbc.MappingName = [\"City\"];]                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [    gbc.HeaderText = [\"City\"];]                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| [    [this].gridDataBoundGrid1.GridBoundColumns.Add(gbc);]                                                                                                                  |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [    [// Need to initialize the GridBoundColumns so that their settings will replace the currently set values.]]                                                           |
|                                                                                                                                                                                                                                      |
| [    [this].gridDataBoundGrid1.Binder.InitializeColumns();]                                                                                                                 |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [    [// Resize the column headers.]]                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [    [this].gridDataBoundGrid1.Model.ColWidths.ResizeToFit([GridRangeInfo].Row(0), [GridResizeToFitOptions].NoShrinkSize);] |
|                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.DataSource = ReturnATable()]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.EnableAddNew = [False]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.BackColor = Color.FromArgb(&HCC, &HD4, &HE6)]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [\' Create a GridBoundColumn for each displayed column.]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [Dim][ gbc [As] [New] GridBoundColumn()]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [gbc.MappingName = [\"FirstName\"]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [\' Must set to column mapping name.]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [gbc.HeaderText = [\"Name\"]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [\' Set some style properties.]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                |
| [gbc.StyleInfo.BackColor = Color.FromArgb(&HC0, &HC9, &HDB)]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                |
| [gbc.StyleInfo.TextColor = Color.Blue]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [\' Add the column to the GridBoundColumns collection.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.GridBoundColumns.Add(gbc)]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [\' Repeat for each column.]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| [gbc = [New] GridBoundColumn()]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| [gbc.MappingName = [\"LastName\"]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| [gbc.HeaderText = [\"FamilyName\"]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                |
| [gbc.StyleInfo.Font.Bold = [True]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.GridBoundColumns.Add(gbc)]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [gbc = [New] GridBoundColumn()]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| [gbc.MappingName = [\"City\"]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [gbc.HeaderText = [\"City\"]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.GridBoundColumns.Add(gbc)]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [\' Need to initialize the GridBoundColumns so their settings will replace the currently set values.]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.Binder.InitializeColumns()]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [\' Resize the column headers.]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.gridDataBoundGrid1.Model.ColWidths.ResizeToFit(GridRangeInfo.Row(0), GridResizeToFitOptions.NoShrinkSize)]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| [\' Form1_Load]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p371} 

 

More:





