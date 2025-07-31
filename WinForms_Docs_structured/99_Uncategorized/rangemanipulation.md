---
title: rangemanipulation.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\rangemanipulation.md
created_at: 2025-07-03
---






#### Range Manipulation {#range-manipulation style="tab-stops: 0pt"}

 

The **IRange** interface represents a single cell or a group of cells in a worksheet. XlsIO has several useful methods for manipulating the data and formatting it in the ranges. This section discusses the topics listed below.

 

[·      ]Accessing a Range

[·      ]IMigrant Range

[·      ]Copying/Moving a Range

[·      ]Clearing a Range

[·      ]Getting Used Range

 

Accessing a Range

 

Range of cells can be accessed through the IRange interface. Following code example illustrates this.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [// Get cell range.]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [IRange][ [this]\[[string] name\] { [get]; }]                                                                                                           |
|                                                                                                                                                                                                                                                                                                             |
| [        ]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                             |
| [// Gets/sets cell by row and index.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                             |
| [IRange][ [this]\[[int] row, [int] column\] { [get]; }]                                                                            |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [// Get cell range.]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [IRange][ [this]\[[string] name, [bool] IsR1C1Notation\] { [get]; }]                                                               |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [// Get cells range.]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                             |
| [IRange][ [this]\[[int] row, [int] column, [int] lastRow, [int] lastColumn\] { [get]; }] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Here row and column indexes in the range are \"one based\". Following code example explains various ways of accessing cells.


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                        |
| **[]**                                                                                                                             |
|                                                                                                                                                                        |
| [// Method 1 to Access a Range.]                                                                                     |
|                                                                                                                                                                        |
| [sheet.Range\[[\"A7\"]\].Text = [\"Accessing a Range (Method 1)\"];]               |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [// Method 2 to Access a Range.]                                                                                     |
|                                                                                                                                                                        |
| [sheet.Range\[9, 1\].Text = [\"Accessing a Range (Method 2)\"];]                                           |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [// Method 3 to Access a Range(using defined names).]                                                                |
|                                                                                                                                                                        |
| [sheet.Range\[[\"Name\"]\].Text = [\"Accessing a Range (Method 3)\"];]             |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [// Accessing a Range of cells (Method 1).]                                                                          |
|                                                                                                                                                                        |
| [sheet.Range\[[\"A13:C13\"]\].Text = [\"Accessing a Range of Cells (Method 1)\"];] |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [// Accessing a Range of cells (Method 2).]                                                                          |
|                                                                                                                                                                        |
| [sheet.Range\[15, 1, 15, 3\].Text = [\"Accessing a Range of Cells (Method 2)\"];]                          |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [// Accessing a Range of cells (Method 3 using defined names).]                                                      |
|                                                                                                                                                                        |
| [sheet.Range\[[\"Name1\"]\].Text = [\"Accessing a Range of Cells (Method 3)\"];]   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                              |
|                                                                                                                                                                   |
| **[]**                                                                                                                        |
|                                                                                                                                                                   |
| [\' Method 1 to Access a Range.]                                                                                |
|                                                                                                                                                                   |
| [sheet.Range([\"A7\"]).Text = [\"Accessing a Range (Method 1)\"]]               |
|                                                                                                                                                                   |
| []                                                                                                             |
|                                                                                                                                                                   |
| [\' Method 2 to Access a Range.]                                                                                |
|                                                                                                                                                                   |
| [sheet.Range(9, 1).Text = [\"Accessing a Range (Method 2)\"]]                                          |
|                                                                                                                                                                   |
| []                                                                                                             |
|                                                                                                                                                                   |
| [\' Method 3 to Access a Range(using defined names).]                                                           |
|                                                                                                                                                                   |
| [sheet.Range([\"Name\"]).Text = [\"Accessing a Range (Method 3)\"]]             |
|                                                                                                                                                                   |
| []                                                                                                             |
|                                                                                                                                                                   |
| [\' Accessing a Range of cells (Method 1).]                                                                     |
|                                                                                                                                                                   |
| [sheet.Range([\"A13:C13\"]).Text = [\"Accessing a Range of Cells (Method 1)\"]] |
|                                                                                                                                                                   |
| []                                                                                                             |
|                                                                                                                                                                   |
| [\' Accessing a Range of cells (Method 2).]                                                                     |
|                                                                                                                                                                   |
| [sheet.Range(15, 1, 15, 3).Text = [\"Accessing a Range of Cells (Method 2)\"]]                         |
|                                                                                                                                                                   |
| []                                                                                                             |
|                                                                                                                                                                   |
| [\' Accessing a Range of cells (Method 3 using defined names).]                                                 |
|                                                                                                                                                                   |
| [sheet.Range([\"Name1\"]).Text = [\"Accessing a Range of Cells (Method 3)\"]]   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Accessing Discontinuous Ranges

 

You can also access different discontinuous ranges and add them to the **RangesCollection**, so that the same format is applied to different ranges. Following code example explains the same.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [IRange][ range1 = sheet.Range\[ [\"A1:A2\"] \];] |
|                                                                                                                                                                   |
| [IRange][ range2 = sheet.Range\[[\"C1:C2\"] \];]  |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [RangesCollection ranges = [new] RangesCollection( engine.Excel, sheet );]                               |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [ranges.Add( range1 );]                                                                                                       |
|                                                                                                                                                                   |
| [ranges.Add( range2 );]                                                                                                       |
|                                                                                                                                                                   |
| [ranges.Text = [\"Test\"];]                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [Dim][ range1 [As] IRange = sheet.Range([\"A1:A2\"])]                            |
|                                                                                                                                                                                                                   |
| [Dim][ range2 [As] IRange = sheet.Range([\"C1:C2\"])]                            |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [Dim][ ranges [As] RangesCollection = [New] RangesCollection(engine.Excel, sheet)] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [ranges.Add(range1)]                                                                                                                                                          |
|                                                                                                                                                                                                                   |
| [ranges.Add(range2)]                                                                                                                                                          |
|                                                                                                                                                                                                                   |
| [ranges.Text = [\"Test\"]]                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

IMigrantRange

[] 

The **IMigrantRange** interface can be used to access the worksheet range and manipulate it. This is an optimal method of writing strings with better memory performance. Following code example illustrates this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                           |
|                                                                                                                                                            |
| []                                                                                                                     |
|                                                                                                                                                            |
| [// Writing Data.]                                                                                       |
|                                                                                                                                                            |
| [for][ ([int] row = 1; row \<= rowCount; row++)] |
|                                                                                                                                                            |
| [{]                                                                                                                    |
|                                                                                                                                                            |
| [    [for] ([int] column = 1; column \<= colCount; column++)]                |
|                                                                                                                                                            |
| [    {]                                                                                                                |
|                                                                                                                                                            |
| [        [// Writing values.]]                                                                   |
|                                                                                                                                                            |
| [        migrantRange.ResetRowColumn(row, column);]                                                                    |
|                                                                                                                                                            |
| [        migrantRange.Text = [\"Test\"];]                                                      |
|                                                                                                                                                            |
| [    }]                                                                                                                |
|                                                                                                                                                            |
| [}]                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                |
| **[]**                                                                                                                                     |
|                                                                                                                                                                                |
| [\' Writing Data.]                                                                                                           |
|                                                                                                                                                                                |
| [Dim][ row [As] [Integer]]                      |
|                                                                                                                                                                                |
| []                                                                                                                            |
|                                                                                                                                                                                |
| [For][  row = 1 [To]  rowCount [Step]  row + 1] |
|                                                                                                                                                                                |
| [Dim][ column [As] [Integer]]                   |
|                                                                                                                                                                                |
| [      [For]  column = 1 [To]  colCount [Step]  column + 1]                 |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [\' Writing values.]                                                                                                         |
|                                                                                                                                                                                |
| [            migrantRange.ResetRowColumn(row, column)]                                                                                     |
|                                                                                                                                                                                |
| [            migrantRange.Text = [\"Test\"]]                                                                        |
|                                                                                                                                                                                |
| [      [Next]]                                                                                                        |
|                                                                                                                                                                                |
| [Next]                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Copying/Moving Range

 

Moving and copying cells is a very common procedure when you are creating or editing your worksheets. XlsIO provides support to copy a range of cells from one end to another. **CopyTo** method enables copying range of cells from the source to destination. It has an option to copy all the formats or only specific formats to the destination range by using the **ExcelCopyRangeOptions** enumerator. Following values can be set for the ExcelCopyRangeOptions.

[] 


  ------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------
  Member Name              Description
  None                     No flags.
  UpdateFormulas           Indicates whether update formula during copy. WARNING: you should always specify this flag if your operations could change the position of Array formula.
  UpdateMerges             Indicates whether update merges during copy.
  CopyStyles               Indicates that we have to copy styles during range copy.
  CopyShapes               Indicates that we have to copy shapes during range copy.
  CopyErrorIndicators      Indicates that we have to copy error indicators during range copy.
  CopyConditionalFormats   Indicates that we have to copy conditional formats during range copy.
  All                      All flags.
  ------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------


 

Following code example illustrates how to copy a range of cells from the source to destination preserving only cell styles.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                     |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                     |
| [// Copying a Range.]                                                                                                             |
|                                                                                                                                                                                     |
| [Dim][ source [As] IRange = sheet.Range([\"A1\"])] |
|                                                                                                                                                                                     |
| [Dim][ des [As] IRange = sheet.Range([\"A5\"])]    |
|                                                                                                                                                                                     |
| [source.CopyTo(des)]                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                     |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                     |
| [\' Copying a Range.]                                                                                                             |
|                                                                                                                                                                                     |
| [Dim][ source [As] IRange = sheet.Range([\"A1\"])] |
|                                                                                                                                                                                     |
| [Dim][ des [As] IRange = sheet.Range([\"A5\"])]    |
|                                                                                                                                                                                     |
| [source.CopyTo(des)]                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**MoveTo** method is used for moving a range of cells to the destination. The only difference between copy and move operation is that Move will not create a copy in the source. This is similar to the **Cut** and **Paste** option in Excel.

[] 


{border="0"}Note: Move does not update formulas.


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                     |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                     |
| [// Moving a Range.]                                                                                                              |
|                                                                                                                                                                                     |
| [Dim][ source [As] IRange = sheet.Range([\"A1\"])] |
|                                                                                                                                                                                     |
| [Dim][ des [As] IRange = sheet.Range([\"A5\"])]    |
|                                                                                                                                                                                     |
| [source.MoveTo(des)]                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                     |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                     |
| [\' Moving a Range.]                                                                                                              |
|                                                                                                                                                                                     |
| [Dim][ source [As] IRange = sheet.Range([\"A1\"])] |
|                                                                                                                                                                                     |
| [Dim][ des [As] IRange = sheet.Range([\"A5\"])]    |
|                                                                                                                                                                                     |
| [source.MoveTo(des)]                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Clearing a Range

 

While editing Excel workbooks, one of the most common action that users perform is clearing or deleting cells. Clearing cells mean erasing everything within them, whereas deleting actually deletes the entire cell. You can clear the cell content by using the **Clear** method. XlsIO also provides options to clear styles or data alone.

 

Following code example illustrates how to clear a range along with its formatting.

 

+---------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                            |
|                                                                                             |
| []                                                      |
|                                                                                             |
| [// Clearing a Range and its formatting.] |
|                                                                                             |
| [sheet.Range\[\"A4\"\].Clear(true);]      |
+---------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                        |
|                                                                                             |
| []                                                      |
|                                                                                             |
| [\' Clearing a Range and its formatting.] |
|                                                                                             |
| [sheet.Range(\"A4\").Clear(True)]                       |
+---------------------------------------------------------------------------------------------+

[] 

Getting Used Range

[] 

XlsIO enables to get the range of cells used in a given sheet. This will help the user to apply the same format to all the cells used in the worksheet. You can also get the first row/column, last row/column, and number of rows/columns used in the sheet, by using the various methods of IRange.

 


{border="0"}Note: By default, XlsIO considers a cell as used, even if there exists some formatting. You can disable this behavior, and make XlsIO consider a cell as used, only when there exists data, by using the UsedRangeIncludesFormatting property.


 

Following code example is used to format the Used Range.

 

+----------------------------------------------------------------------------------------+
| **[\[C#\]]**                                       |
|                                                                                        |
| []                                                 |
|                                                                                        |
| [// Modifying only the Used Ranges.] |
|                                                                                        |
| [sheet.UsedRange.ColumnWidth = 20;]  |
|                                                                                        |
| [sheet.UsedRange.RowHeight = 20;]    |
+----------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                   |
|                                                                                        |
| []                                                 |
|                                                                                        |
| [\' Modifying only the Used Ranges.] |
|                                                                                        |
| [sheet.UsedRange.ColumnWidth = 20]   |
|                                                                                        |
| [sheet.UsedRange.RowHeight = 20]     |
+----------------------------------------------------------------------------------------+

 

[]{#p51}**[]** 

[]{#related-topics}

