---
title: howtouseacomboboxinacolumn.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtouseacomboboxinacolumn.md
created_at: 2025-07-03
---








  









### How to Use a Combo Box in a Column {#how-to-use-a-combo-box-in-a-column style="tab-stops: 0pt"}

[] 

Introduction

[] 

The control type of a cell is part of the cell style and is determined by the[ ]**GridStyleInfo.CellType** property. The items shown in the dropdown list can be provided in two ways.

[] 

[·      ]Create a StringCollection object that will hold your choices and then set this StringCollection in the **GridStyleInfo.ChoiceList** property for the cell.

[·      ]Have an IList object that will hold object entries that have public properties (such as a DataTable object with its columns serving as public properties).

[] 

In the second case, use the **GridStyleInfo.DataSource**, **DisplayMember**[ ]and **ValueMember** properties to set the datasource for the drop list. In addition to setting the cell type, ChoiceList, **datasource**, DisplayMember and ValueMember, the **DropDownStyle** property of **GridStyleInfo** controls the editing behavior of the combobox cell. You can also use the **GridStyleInfo.ShowButton** property to control when the combo box button is visible.

[] 

Example

[] 

Here is the code that sets column 2 to be a combo box with the droplist being set through the styles **ChoiceList** property. To access a column\'s style, you must use either the GridDataBoundGrid.GridBoundColumns or GridDataBoundGrid.Binder.InternalColumn depending upon whether you have explicitly added the **GridBoundColumns** or not.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [// Required to access StringCollection.]                                                                                                                                               |
|                                                                                                                                                                                                                                           |
| [using][ System.Collections.Specialized;       ]                                                                                       |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [//\...]                                                                                                                                                                                |
|                                                                                                                                                                                                                                           |
| [// Create the list.]                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [StringCollection items = ][new][ StringCollection();]                               |
|                                                                                                                                                                                                                                           |
| [items.AddRange(new string\[\]{\"One\", \"Two\", \"Three\", \"Four\", \"Five\"});]                                                                                                      |
|                                                                                                                                                                                                                                           |
| [   ]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [// Set the style properties.]                                                                                                                                                          |
|                                                                                                                                                                                                                                           |
| [GridStyleInfo style = ][this][.gridDataBoundGrid1.GridBoundColumns\[1\].StyleInfo;] |
|                                                                                                                                                                                                                                           |
| [style.CellType = \"ComboBox\";]                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| [style.ChoiceList = items;]                                                                                                                                                             |
|                                                                                                                                                                                                                                           |
| [style.CellValue = \"Five\";]                                                                                                                                                           |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [// True droplist - no editing.]                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| [style.DropDownStyle = GridDropDownStyle.Exclusive;]                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [ \' Required to access StringCollection.]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Imports][ System.Collections.Specialized ]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\'\...]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Create the list.]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ items][ As New][ StringCollection]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [items.AddRange(][New String][() {\"One\", \"Two\", \"Three\", \"Four\", \"Five\"})]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Set the style properties.]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ style ][As][ GridStyleInfo = ][Me][.gridDataBoundGrid1.GridBoundColumns(1).StyleInfo] |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.CellType = \"ComboBox\"]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.ChoiceList = items]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.CellValue = \"Five\"]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\' True droplist - no editing.]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.DropDownStyle = GridDropDownStyle.Exclusive ]                                                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Here is the code that will set column 2 to a combobox setting the items in the combobox through a **DataTable** datasource.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [// Assume this.dt is a DataTable object with at least 2 columns named \"id\" and \"display\".]                                                                                         |
|                                                                                                                                                                                                                                           |
| [   ]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [// Set the style properties.]                                                                                                                                                          |
|                                                                                                                                                                                                                                           |
| [GridStyleInfo style = ][this][.gridDataBoundGrid1.GridBoundColumns\[1\].StyleInfo;] |
|                                                                                                                                                                                                                                           |
| [style.CellType = \"ComboBox\";]                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| [style.DataSource = dt;]                                                                                                                                                                |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [// Displayed in the grid cell.]                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| [style.DisplayMember = \"display\"; ]                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [// Value in the grid cell.]                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| [style.ValueMember = \"id\"; ]                                                                                                                                                          |
|                                                                                                                                                                                                                                           |
| [style.DropDownStyle = GridDropDownStyle.AutoComplete;]                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Assume this.dt is a DataTable object with at least 2 columns named \"id\" and \"display\".]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Set the style properties.]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ style ][As][ GridStyleInfo = ][Me][.gridDataBoundGrid1.GridBoundColumns(1).StyleInfo] |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.CellType = \"ComboBox\"]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.DataSource = dt]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Displayed in the grid cell.]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [   style.DisplayMember = \"display\" ]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Value in the grid cell.]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.ValueMember = \"id\" ]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [style.DropDownStyle = GridDropDownStyle.AutoComplete]                                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p603} 

 

[]{#related-topics}

