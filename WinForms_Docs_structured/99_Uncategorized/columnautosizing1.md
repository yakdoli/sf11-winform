---
title: columnautosizing1.md
original_path: WinForms_Docs/99_Uncategorized/columnautosizing1.md
created_at: 2025-08-05
---






#### Column Auto Sizing {#column-auto-sizing style="tab-stops: 0pt"}

This feature allows the grid columns to resize themselves automatically to fit the column content. This resize action is performed based on the size of cells, size of header or size of parent control. According to this criterion, the column resize options are defined below in the GridControlLengthUnitType enumeration.

 

Resize Options

 

1\. GridControlLengthUnitType.Auto

 

In Auto type, column widths of the Grid control/GridData control are adjusted with respect to the cell and header content, i.e., each column\'s header length and cell content length is taken into account.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                     |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [this][.grid.Model.Options.ColumnSizer = GridControlLengthUnitType.Auto;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB.NET\]]                                                                                              |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [Me][.grid.Model.Options.ColumnSizer = GridControlLengthUnitType.Auto] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[Figure ][197][: Auto Resize]

[] 

[] 

2.   GridControlLengthUnitType.AutoWithLastColumnFill

**[]** 

In AutoWithLastColumnFill type, column width of Grid Control/GridData Control is adjusted with respect to cell and header content. The last column\'s width fills the unoccupied space in the parent Framework element.

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                       |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [this][.grid.Model.Options.ColumnSizer = GridControlLengthUnitType.AutoWithLastColumnFill;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB.NET\]]                                                                                                                |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [Me][.grid.Model.Options.ColumnSizer = GridControlLengthUnitType.AutoWithLastColumnFill] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 198: AutoWithLastColumnFill

[] 

3.   GridControlLengthUnitType.SizeToCells

 

In SizeToCells type, column width of Grid Control/GridData Control is adjusted with respect to cell content only.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                            |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [this][.grid.Model.Options.ColumnSizer = GridControlLengthUnitType.SizeToCells;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB.NET\]]                                                                                                     |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [Me][.grid.Model.Options.ColumnSizer = GridControlLengthUnitType.SizeToCells] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 199: SizeToCells

[] 

4.   GridControlLengthUnitType.SizeToHeader

 

In SizeToHeader type, column widths of Grid Control/GridData Control are adjusted with respect to header content only.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                             |
|                                                                                                                                                                        |
| []                                                                                                                   |
|                                                                                                                                                                        |
| [this][.grid.Model.Options.ColumnSizer = GridControlLengthUnitType.SizeToHeader;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB.NET\]]                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [Me][.grid.Model.Options.ColumnSizer = GridControlLengthUnitType.SizeToHeader] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 200: SizeToHeader

[] 

5.   GridControlLengthUnitType.Star

**[]** 

In Star type, column widths are equal and the control and the content occupies total space in the Parent cell. The user need not specify the width for every grid column. They can opt one of these options instead.

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                     |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [this][.grid.Model.Options.ColumnSizer = GridControlLengthUnitType.Star;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB.NET\]]                                                                                              |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [Me][.grid.Model.Options.ColumnSizer = GridControlLengthUnitType.Star] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 201: Star Resize

[] 

6.   MaxLength

 

The user can specify the number of rows that should be considered for calculating column widths using MaxLength property. The following code snippet allows the grid to consider only the data of first 12 rows for calculating column widths.

[] 

+--------------------------------------------------------------------------+
| [\[C#\]]               |
|                                                                          |
| []                     |
|                                                                          |
| [grid.Model.Options.MaxLength = 12;] |
+--------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------+
| [\[VB.NET\]]          |
|                                                                         |
| []                    |
|                                                                         |
| [grid.Model.Options.MaxLength = 12] |
+-------------------------------------------------------------------------+

 

[]{#related-topics}

