---
title: columns.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\columns.md
created_at: 2025-07-03
---








  









### Columns {#columns style="tab-stops: 0pt"}

[] 

[]{#header1}Essential GridGroupingControl is mainly used for data display. This control provides an easy way to bind the data from the database to the user in a user-friendly manner. The GridGroupingControl renders a tabular, data-bound grid. The GridGroupingControl displays the fields of a datasource as columns in a table.

 

The following are the collections in TableDescriptor which are used to control the columns that are shown on the grid.

[] 

[·      ]**Fields**: the entries in this collection have a one-to-one correspondence with the bound datasource table.

[·      ]**ExpressionFields**: the entries in this collection are populated manually and these columns contain values based on values in the other databound columns.

[·      ]**UnboundFields**: the entries in this collection are populated manually and represent columns whose values are manually populated during runtime.

[] 

Creating Columns

**[]** 

Through Designer

[] 

Using the **GridColumnDescriptor** Collection Editor, you can add columns to the grid. To view this Collection Editor, you have to click on the \'Build Columns\' option from the smart tag.

[] 

{border="0"}

Figure 43

[] 

You can add or remove columns to the VisibleColumns collection of the GridGroupingControl by using the GridColumnDescriptor Collection Editor.

[] 

{border="0"}

Figure 44

[] 

Once the columns get added to the grid, it will automatically generate the code in the aspx page as given below.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [\<][tabledescriptor][\>]                                                                            |
|                                                                                                                                                                                                                                                            |
| [\<][Columns][\>]                                                                                    |
|                                                                                                                                                                                                                                                            |
| [       [\<][syncfusion][:][GridColumnDescriptor] [MappingName][=\"ID\"\>]]         |
|                                                                                                                                                                                                                                                            |
| [       [\</][syncfusion][:][GridColumnDescriptor][\>]]                                                 |
|                                                                                                                                                                                                                                                            |
| [       [\<][syncfusion][:][GridColumnDescriptor] [MappingName][=\"First Name\"\>]] |
|                                                                                                                                                                                                                                                            |
| [       [\</][syncfusion][:][GridColumnDescriptor][\>]]                                                 |
|                                                                                                                                                                                                                                                            |
| [       [\<][syncfusion][:][GridColumnDescriptor] [MappingName][=\"Last Name\"\>]]  |
|                                                                                                                                                                                                                                                            |
| [       [\</][syncfusion][:][GridColumnDescriptor][\>]]                                                 |
|                                                                                                                                                                                                                                                            |
| [\</][Columns][\>]                                                                                   |
|                                                                                                                                                                                                                                                            |
| [\</][tabledescriptor][\>]                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p34} 

[]{#related-topics}

