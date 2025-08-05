---
title: primarykeycolumn.md
original_path: WinForms_Docs/99_Uncategorized/primarykeycolumn.md
created_at: 2025-08-05
---








  









### Primary Key Column {#primary-key-column style="tab-stops: 0pt"}

[] 

The primary key is a key used to uniquely identify each record in the table. Essential GridGroupingControl allows us to create such kind of columns. The primary key column doesn\'t allow the user to enter repeated values.

[] 

Creating Primary Key Columns

**[]** 

Through Designer

**[]** 

On clicking the **PrimaryKeyColumns** property of the grid\'s TableDescriptor, the **GridSortColumnDescriptor** Collection Editor is launched, which is used to set a primary key column in the grid.

[] 

{border="0"}

Figure 45

[] 

Through Code

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [this][.GridGroupingControl1.TableDescriptor.PrimaryKeyColumns.AddRange([new] Syncfusion.Grouping.[SortColumnDescriptor]\[\] {]                 |
|                                                                                                                                                                                                                                                                                   |
| [new][ Syncfusion.Grouping.[SortColumnDescriptor]([\"ID\"], System.ComponentModel.[ListSortDirection].Ascending)});] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.gridGroupingControl1.TableDescriptor.PrimaryKeyColumns.AddRange([New] Syncfusion.Grouping.SortColumnDescriptor() { [New] Syncfusion.Grouping.SortColumnDescriptor([\"ID\"], System.ComponentModel.ListSortDirection.Ascending)})] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p35} 

[]{#related-topics}

