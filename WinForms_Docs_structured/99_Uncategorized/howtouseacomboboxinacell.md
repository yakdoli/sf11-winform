---
title: howtouseacomboboxinacell.md
original_path: WinForms_Docs/99_Uncategorized/howtouseacomboboxinacell.md
created_at: 2025-08-05
---








  









### How to Use a Combo Box in a Cell {#how-to-use-a-combo-box-in-a-cell style="tab-stops: 0pt"}

[] 

Introduction

[] 

The control type of a cell is part of the cell style and is determined by the **GridStyleInfo.CellType** property. The items shown in the dropdown list can be provided in two ways.

[] 

[·      ]Create a StringCollection object holding your choices and then set this StringCollection in the **GridStyleInfo.ChoiceList** property for the cell.

[·      ]Have an IList object that holds object entries that have public properties (such as a **DataTable** object with its columns serving as public properties).

[[]]{.UGHyperlink} 

In the second case, use the GridStyleInfo.DataSource, DisplayMember and ValueMember properties to set the datasource for the drop list. In addition to setting the CellType, ChoiceList, datasource, DisplayMember and ValueMember, the DropDownStyle property of  the [GridStyleInfo]{.UGHyperlink}[ ]controls the editing behavior of the combo box cell. You can also use the GridStyleInfo.ShowButton property to control when the combo box button is visible.[ ]

[] 

Example

[] 

Here is the code that will set cells 4,2 to a combo box by setting the items in the combo box through the styles ChoiceList[ ]property.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                    |
| [// Required to access the StringCollection.]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [using][ System.Collections.Specialized;       ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                    |
| [//\...]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [// Create the list.]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                    |
| [StringCollection items = ][new][ StringCollection();]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                    |
| [items.AddRange(][new][ ][string][\[\]{\"One\", \"Two\", \"Three\", \"Four\", \"Five\"});] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [   ]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                    |
| [// Set the style properties.]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [GridStyleInfo style = gridControl1\[4, 2\];]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [style.CellType = \"ComboBox\";]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                    |
| [style.ChoiceList = items;]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                    |
| [style.CellValue = \"Five\";]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                    |
| [// True droplist - no editing.]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                    |
| [style.DropDownStyle = GridDropDownStyle.Exclusive; ]                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' Required to access the StringCollection.]                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [Imports][ ][System.Collections.Specialized ]                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\'\...]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| [\' Create the list.]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [Dim][ items ][As New][ StringCollection]               |
|                                                                                                                                                                                                                                                               |
| [items.AddRange(][New String][() {\"One\", \"Two\", \"Three\", \"Four\", \"Five\"})]                     |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' Set the style properties.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [Dim][ style ][As][ GridStyleInfo = GridControl1(4, 2)] |
|                                                                                                                                                                                                                                                               |
| [style.CellType = \"ComboBox\"]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [style.ChoiceList = items]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [style.CellValue = \"Five\"]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' True droplist - no editing.]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [style.DropDownStyle = GridDropDownStyle.Exclusive ]                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Here is the code that will set cells 4,2 to a combo box by setting the items in the combo box through a DataTable datasource.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                                   |
| []                                                                                              |
|                                                                                                                                                   |
| [// Assume this.dt is a DataTable object with at least 2 columns named \"id\" and \"display\".] |
|                                                                                                                                                   |
| [   ]                                                                                           |
|                                                                                                                                                   |
| [// Set the style properties.]                                                                  |
|                                                                                                                                                   |
| [GridStyleInfo style = gridControl1\[4, 2\];]                                                   |
|                                                                                                                                                   |
| [style.CellType = \"ComboBox\";]                                                                |
|                                                                                                                                                   |
| [style.DataSource = dt;]                                                                        |
|                                                                                                                                                   |
| [style.DisplayMember = \"display\"; ]                                                           |
|                                                                                                                                                   |
| []                                                                                              |
|                                                                                                                                                   |
| [// Displayed in the grid cell.]                                                                |
|                                                                                                                                                   |
| [style.ValueMember = \"id\"; ]                                                                  |
|                                                                                                                                                   |
| []                                                                                              |
|                                                                                                                                                   |
| [// Value in the grid cell.]                                                                    |
|                                                                                                                                                   |
| [style.DropDownStyle = GridDropDownStyle.AutoComplete;]                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' Assume this.dt is a DataTable object with at least 2 columns named \"id\" and \"display\".]                                                                                                             |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' Set the style properties.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                               |
| [Dim][ style ][As][ GridStyleInfo = GridControl1(4, 2)] |
|                                                                                                                                                                                                                                                               |
| [style.CellType = \"ComboBox\"]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [style.DataSource = dt]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                               |
| [style.DisplayMember = \"display\" ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' Displayed in the grid cell.]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [style.ValueMember = \"id\" ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' Value in the grid cell.]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [style.DropDownStyle = GridDropDownStyle.AutoComplete]                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p576} 

 

[]{#related-topics}

