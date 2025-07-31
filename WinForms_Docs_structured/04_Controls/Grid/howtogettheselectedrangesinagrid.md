---
title: howtogettheselectedrangesinagrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtogettheselectedrangesinagrid.md
created_at: 2025-07-03
---








  









### How to Get the Selected Ranges in a Grid {#how-to-get-the-selected-ranges-in-a-grid style="tab-stops: 0pt"}

[] 

Introduction

[] 

The grid.Selections.Ranges is a **GridRangeInfoList** object which, holds the currently selected ranges.

[] 

Example

[] 

You can iterate through this list retrieving GridRangeInfo objects with code such as.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [// Iterate through the SelectionRanges, to display every range in the list.]                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [foreach][(GridRangeInfo range ][in this][.grid.Selections.Ranges)] |
|                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [         MessageBox.Show(range.ToString());]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [ Dim][ range ][As][ GridRangeInfo]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\' Iterate through the SelectionRanges, to display every range in the list.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [For][ ][Each][ range ][In Me][.grid.Selections.Ranges] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [        MessageBox.Show(range.ToString())]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Next]                                                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In the previous code, note that the GridRangeInfo object is not really being used for anything. When you actually try to use it, you will need to take into account the fact that you cannot make any assumptions regarding whether this range object is a row range or a cell range or a column range or something else. For example, you may want to make use of Range.Top and Range.Bottom to get the top and bottom rows that have been selected. But, if the range happens to be a column range, then these properties will not be valid as column ranges.

[] 

So, before using such range properties, you must check whether these properties have been properly set. The GridRangeInfo class has a method that can manage this task: **GridRangeInfo.ExpandRange**. If you need to access properties like left, right, top and bottom in a GridRangeInfo where it is unknown whether or not the range is a cell range, then you should first call **ExpandRange** to make sure that this is the case.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                   |
| [int][ rowLimit = grid.Model.RowCount;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                   |
| [    ][int][ colLimit = grid.Model.ColCount;]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                   |
| [    // Call ExpandRange method and display the top and bottom rows in each range.]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                   |
| [    ][foreach][(GridRangeInfo range ][in this][.grid.Selections.Ranges)] |
|                                                                                                                                                                                                                                                                                                                                   |
| [    {]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                   |
| [        GridRangeInfo range1 = range.ExpandRange(1, 1, rowLimit, colLimit);]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                   |
| [        MessageBox.Show(\"top={0} bot={1}\", range1.Top, range1.Bottom);]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                   |
| [    }]                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ rowLimit ][As Integer][ = grid.Model.RowCount]                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    ][Dim][ colLimit ][As Integer][ = grid.Model.ColCount]                             |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    ][Dim][ range ][As][ GridRangeInfo]                                                |
|                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                 |
| [        \' Call ExpandRange method and display the top and bottom rows in each range.]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                 |
| [        ][For Each][ range ][In Me][.grid.Selections.Ranges]                           |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    ][Dim][ range1 ][As][ GridRangeInfo = range.ExpandRange(1, 1, rowLimit, colLimit)] |
|                                                                                                                                                                                                                                                                                                                                                 |
| [              MessageBox.Show(\"top={0} bot={1}\", range1.Top, range1.Bottom)]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                 |
| [        ][Next][ range]                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[   ]

To retrieve the active range, use the below given code snippet.

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                      |
|                                                                                                                     |
| []                                                                                            |
|                                                                                                                     |
| [// Retrieve the active range.]                                   |
|                                                                                                                     |
| [GridRangeInfo activeRange = grid.Selections.Ranges.ActiveRange;] |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [\' Retrieve the active range.]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [Dim][ activeRange ][As][ GridRangeInfo = grid.Selections.Ranges.ActiveRange] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p620} 

 

[]{#related-topics}

