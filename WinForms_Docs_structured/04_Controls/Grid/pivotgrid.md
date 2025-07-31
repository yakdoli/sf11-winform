---
title: pivotgrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\pivotgrid.md
created_at: 2025-07-03
---






#### Pivot Grid {#pivot-grid style="tab-stops: 0pt"}

[] 

Essential Pivot Grid simulates the Pivot Table feature of MS Excel. The Pivot Grid pivots the data via drag-and-drop to organize the data in a cross-tabulated form. The major advantage of pivot grid is that you can extract any desired information within a limited span of time. Apart from being able to present the data in a proper manner, you can also summarize and group the data. Pivot Grid has its main application in the financial domain. It is used to organize and analyze the business data.

[] 

The Pivot Grid control is built on the foundation of the Grid control. It comprises of the following components.

[] 

[·      ]**Display Grid** - Displays the data extracted from the underlying database.

[·      ]**Pivot Table Field List** - Lists the available fields from the database. Provides a way to add / remove the fields from the grid.

[·      ]**Drag-Drop Panel** - Serves as a view state of the pivot grid, where you can rearrange the fields by performing a drag-and-drop operation between the row and column label areas.

[·      ]**Filter Area** - Lets you filter the results according to certain criteria in a desired manner.

 

Pivot Grid provides a UI that allows you to specify the rows and columns in the pivot table through drag-and-drop operations. The visual aspects of the control are saved in an Appearance object. The control supports Office 2003 and Office 2007 styles.

 

The calculations are done through the Grouping Engine, which is a part of Essential Grouping. The default calculation is *Summation*, but there exists an option to change the calculation type to *Average*, *Median*, *Percentiles*, *Variances*, *Standard Deviations*, and so on. You can also provide \"custom\" calculations through the grouping engine.

[] 

Features

**[]** 

[·      ]Data-binding support

[·      ]Auto-calculation of Total Summary

[·      ]Filters

[·      ]Grouping support

[·      ]Customizable Appearance

[·      ]Support for XML and Binary Serialization

[] 

APIs

 

Here is a brief explanation on some important methods implemented in the Pivot Grid.

[] 

[·      ]**CollapseAll()** - This will collapse all the expanded tables in the Pivot Grid.

[] 

+------------------------------------------------------------------------+
| **[\[C#\]]**         |
|                                                                        |
| []                   |
|                                                                        |
| [pivotGridControl1.CollapseAll();] |
+------------------------------------------------------------------------+

[] 

[·      ]**ExpandAll()** - Expands all the collapsed nodes in the Pivot Grid.

[] 

+-----------------------------------------------------------------------+
| **[\[C#\]]**        |
|                                                                       |
| []                  |
|                                                                       |
| [pivotGridControl1.ExpandAll();]  |
+-----------------------------------------------------------------------+

[] 

[·      ]**InitSchema()** - A new Pivot schema will be created, and it will be associated with the Pivot Grid.

[] 

+-----------------------------------------------------------------------+
| **[\[C#\]]**        |
|                                                                       |
| []                  |
|                                                                       |
| [pivotGridControl1.InitSchema();] |
+-----------------------------------------------------------------------+

[] 

[·      ]**ResetSchema()** - Resets the Pivot Grid control into an initial schema which will be empty.

[] 

+------------------------------------------------------------------------+
| **[\[C#\]]**         |
|                                                                        |
| []                   |
|                                                                        |
| [pivotGridControl1.ResetSchema();] |
+------------------------------------------------------------------------+

[] 

[·      ]**SetAppearance()** - This method sets the appearance of the Pivot Grid.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [pivotGridControl1.SetAppearance([new] PivotGridLibrary.[PivotAppearance](pivotGridControl2));] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Here is a brief explanation on some important properties implemented in the Pivot Grid.

[] 

[·      ]**AllString** - This will get the string values that appear in the dropdown filter, when all the filter values get selected.

[] 

+--------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                         |
|                                                                                                        |
| []                                                   |
|                                                                                                        |
| [pivotGridControl1.AllString = [\"All\"];] |
+--------------------------------------------------------------------------------------------------------+

[] 

[·      ]**AutoSizeColumns** - Sizes the column according to the calculated value of the display width.

[] 

+--------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                         |
|                                                                                                        |
| []                                                   |
|                                                                                                        |
| [pivotGridControl1.AutoSizeColumns = [true];] |
+--------------------------------------------------------------------------------------------------------+

[] 

[·      ]**ColumnCount** - This specifies the number of columns in the main display grid.

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                                 |
| []                                                                            |
|                                                                                                                                 |
| [int][ i = pivotGridControl1.ColumnCount;] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**ColumnsCount** - This specifies the number of distinct fields in the pivot grid.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [int][ i = pivotGridControl1.ColumnsCount;] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**DataRowCount** - This specifies the number of rows in the underlying IList datasource.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [int][ i = pivotGridControl1.DataRowCount;] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**DefaultComputationName** - This specifies the name of the default calculation. The default value is *Sum*.

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                      |
|                                                                                                                     |
| []                                                                |
|                                                                                                                     |
| [pivotGridControl1.DefaultComputationName = [\"Sum\"];] |
+---------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**DefaultDescriptionFormat** - This specifies the format of the calculated description. By default it will be, *{0} of {1}*, where {0} is the value of computation name and {1} is the value of the field name.

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                              |
| []                                                                         |
|                                                                                                                              |
| [pivotGridControl1.DefaultDescriptionFormat = [\"{0} of {1}\"];] |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**FilterCount** - This specifies the number of distinct fields added to the filter.

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                                 |
| []                                                                            |
|                                                                                                                                 |
| [int][ i = pivotGridControl1.FilterCount;] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**FreezeHeaders** - This determines whether the row and column headers should be frozen.

[] 

+------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                       |
|                                                                                                      |
| []                                                 |
|                                                                                                      |
| [pivotGridControl1.FreezeHeaders = [true];] |
+------------------------------------------------------------------------------------------------------+

[] 

[·      ]**GrandTotalString** - This provides the text for the summary cells of the Pivot Grid.

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                        |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [pivotGridControl1.GrandTotalString = [\"Grand Total\"];] |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**LeftPanelWidth** - This specifies the width of the left-most Panel.

[] 

+------------------------------------------------------------------------------+
| **[\[C#\]]**               |
|                                                                              |
| []                         |
|                                                                              |
| [pivotGridControl1.LeftPanelWidth = 20;] |
+------------------------------------------------------------------------------+

[] 

[·      ]**LeftPanelHeight** - This specifies the height of the top-most Panel.

[] 

+-------------------------------------------------------------------------------+
| **[\[C#\]]**                |
|                                                                               |
| []                          |
|                                                                               |
| [pivotGridControl1.LeftPanelHeight = 20;] |
+-------------------------------------------------------------------------------+

[] 

[·      ]**MainDisplayGrid** - This is a basic grid which stores the pivot results.

[] 

[·      ]**MultipleString** - This specifies the text that should appear when the Multiple Filter selected in the Filter Combo Box is changed. By default it will be set to **Multiple**.

[] 

+------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                   |
|                                                                                                                  |
| []                                                             |
|                                                                                                                  |
| [pivotGridControl1.MultipleString = [\"Multiple\"];] |
+------------------------------------------------------------------------------------------------------------------+

 

[]{#p314} 

 

[]{#related-topics}

