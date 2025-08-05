---
title: selectionmodes.md
original_path: WinForms_Docs/99_Uncategorized/selectionmodes.md
created_at: 2025-08-05
---






#### Selection Modes {#selection-modes style="tab-stops: 0pt"}

[] 

There are two modes of selection available in the Grid. They are,

[] 

[·      ]Model-Based Selection

**[]** 

1.   In Model-based selection, you will be able to select cell ranges; but the selections will have no knowledge of nested tables, grouping or sorting and hence the functionality is limited like a data bound grid (Grid Data control).

2.   To use the model selection capability, set AllowSelections to any flag except none.

3.   Selection can be made through keyboard and mouse.

[] 

[·      ]Record-Based Selection

**[]** 

4.   It is designed specifically for the data bound grids.

5.   In Record-based selection, the complete grid records (rows) will be selected and these selections function properly with nested tables, sorting, and so on.

6.   To use the record selections, you must set AllowSelections to none and then set ListBoxSelectionMode to any flag except none.

7.   Selection can be made through keyboard and mouse with some restriction. For more details, see Record-based Selection in this topic.

[] 

Let us know more about these selection Modes.

[] 

Model-Based Selection

[] 

Model-based selection is cell-based selection mode that allows you to do a selection across the cell, which is not possible with record-based selection. It can be set by initializing **AllowSelection** property to a Flag value, say, Row.

[] 


{border="0"}Note: Setting the Flag to None will disable selecting of cells.


[] 

The possible values for this type of selection are defined by the enum GridSelectionFlags. To control the selection behavior of the grid, set any of the following flags to the AllowSelection property.

**[]** 

Selection Flags

**[]** 


  -------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Flag           Description
  None           Disables selecting of cells.
  Row            Allows selection of rows.
  Column         Allows selection of columns.
  Table          Allows selection of the whole table.
  Cell           Allows selection of an individual cell.
  Multiple       Allows selection of multiple ranges of cells. The user has to press CTRL Key to select multiple ranges.
  Shift          Allows extending existing selection when user holds SHIFT Key and clicks on a cell.
  Keyboard       Allows extending existing selection when user holds SHIFT Key and presses arrow keys.
  MixRangeType   Allows both rows and columns to be selected at the same time when Multiple is specified. By default, the grid does not allow row and column ranges to be selected at the same time.
  Any            Allows selection of rows, columns, table, cell and multiple ranges of cells; also extends SHIFT Key support and alpha blending.
  -------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

You can combine more than one flag to customize the current selection behavior.

[] 

Example

**[]** 

Here is an example code snippet that sets the selection mode for selecting multiple columns.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                     |
|                                                                                                                                                                                                         |
| [grid.Model.Options.AllowSelection = [GridSelectionFlags].Multiple \| [GridSelectionFlags].Column;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 62: Selecting multiple Columns

[] 

Record-Based Selection

**[]** 

This type of selection mechanism allows selection in terms of record (entire row). It is not cell-based. This selection mode is specifically designed for a data-bound grid in which the grid data can be organized as a collection of record rows.

 

Grid offers the following three types of record-based selections which are together called as List Box Selection Modes.

[] 

[·      ]SelectionMode--One

[·      ]SelectionMode--MultiSimple

[·      ]SelectionMode-MultiExtended

[] 

To enable record-based selection, you need to set the ListBoxSelectionMode property to any of the above values. Once a list box selection is enabled, it automatically turns off the model-based selection by assigning None to the AllowSelection property. Below is a detailed description on each type with example code snippets.

**[]** 

SelectionMode-One

**[]** 

It allows you to select only one item (record). Say, you have selected a record. Now if you select some other record, the previous record selection will be cleared. Hence it is a one record selection mode. The following code is used to set this mode:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                  |
| **[]**                                                                         |
|                                                                                                                                                  |
| [grid.Model.Options.ListBoxSelectionMode = [GridSelectionMode].One;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 63: SelectionMode-one

***[]*** 


{border="0"}Note: Record can be selected using a single mouse click or using UP or DOWN Arrow Keys


[] 

SelectionMode - MultiSimple

**[]** 

In this selection mode, you will be able to select multiple items individually. Say, you have selected a record using mouse and you want to select one more record. Click another record and you will notice that the previous selection is not cleared. You can hence select multiple records without the need of SHIFT or CTRL keys.

 

The following code is used to set this mode:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                           |
|                                                                                                                                                          |
| **[]**                                                                                 |
|                                                                                                                                                          |
| [grid.Model.Options.ListBoxSelectionMode = [GridSelectionMode].MultiSimple;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 64: SelectionMode - MultiSimple

[] 


{border="0"}Note: It does not support the use of SHIFT, CTRL and arrow keys to extend the selection.


[] 

SelectionMode - MultiExtended

[] 

This selection type allows multiple items selection through SHIFT, CTRL and arrow keys.

 

You can do any of the following when this selection mode is enabled:

[] 

[·      ]Select a record, hold down the SHIFT key and select fourth record, for example. You will notice all the records in between 1st and the 4th record are also selected.

[·      ]You can make random selection by holding down the CTRL key.

[·      ]Hold down the Shift key and select the records using the UP or DOWN ARROW keys.

[] 

The following code is used to set this mode:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                                            |
| **[]**                                                                                   |
|                                                                                                                                                            |
| [grid.Model.Options.ListBoxSelectionMode = [GridSelectionMode].MultiExtended;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 65: SelectionMode - MultiExtended

***[]*** 

The Model.Selections Collection

**[]** 

The entire grid selections are managed by the GridModel.Selections collection. It exposes several APIs that let you add, remove and operate on different grid selections. Below is the description of some important properties and APIs:

[] 


  ------------------------------- ----------------------------------------------------------------------------------------------------
  Property/Method                 Description
  Add(), Remove()                 Adds or removes the specified range to/from the collection.
  InsertRows(), InsertColumns()   Inserts new rows or columns into the collection.
  RemoveRows(), RemoveColumns()   Removes the specified rows or columns from the collection.
  Ranges                          A GridRangeInfoList collection that stores all the selected ranges for the grid.
  SelectRange()                   Adds or removes a range to/from the collection.
  GetSelectedRanges()             Retrieves a list of selected ranges and if there are no selected ranges, returns the current cell.
  GetSelectedRows()               Returns the number of selected rows.
  GetSelectedCols()               Returns the number of selected columns.
  ------------------------------- ----------------------------------------------------------------------------------------------------


 

[]{#p191} 

[]{#related-topics}

