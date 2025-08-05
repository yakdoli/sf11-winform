---
title: howtosetavalueintoacell.md
original_path: WinForms_Docs/99_Uncategorized/howtosetavalueintoacell.md
created_at: 2025-08-05
---








  









### How to Set a Value into a Cell {#how-to-set-a-value-into-a-cell style="tab-stops: 0pt"}

[] 

Introduction

[] 

A style object holds all the information that affects the cells appearance. One property contained in the style object is its

CellValue. It is this property that you have to set in order to place a value in a cell. Another property called GridStyleInfo.Text, will allow you to set the value of a cell using a string. Text and [CellValue]{.UGHyperlink} are related properties and setting one of these properties will also set the other.\
\

Example

[] 

Use a two-parameter indexer (rowIndex, colIndex) on your **GridControl** object to get a reference to that particular cells style, a **GridStyleInfo** object.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [// Setting the CellValues of the cell.]                                       |
|                                                                                                                                  |
| [int][ rowIndex = 1;]         |
|                                                                                                                                  |
| [int][ colIndex = 2;        ] |
|                                                                                                                                  |
| [gridControl1\[rowIndex, colIndex\].CellValue = \"PI\";]                       |
|                                                                                                                                  |
| [rowIndex++;]                                                                  |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [// Sets a different value in the next row.]                                   |
|                                                                                                                                  |
| [gridControl1\[rowIndex, colIndex\].CellValue = 3.14159;]                      |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [\' Setting the CellValues of the cell.]                                                                                                                                                |
|                                                                                                                                                                                                                                           |
| [Dim][ rowIndex ][As Integer][ = 1] |
|                                                                                                                                                                                                                                           |
| [Dim][ colIndex ][As Integer][ = 2] |
|                                                                                                                                                                                                                                           |
| [GridControl1(rowIndex, colIndex).CellValue = \"PI\"]                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [rowIndex = rowIndex + 1]                                                                                                                                                               |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [\' Sets a different value in the next row.]                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| [GridControl1(rowIndex, colIndex).CellValue = 3.14159]                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note:

 

Using an indexer on the GridControl to set values will trigger of several notification events that listeners (and the GridControl itself) can use to monitor the state of the GridControl. These events may slow things down if you have a lot of data to move into the GridControl. In this case, you can want to employ a technique that will avoid these events.


[] 

There are several ways to do this; if your data is in some form supported by the **GridControl.PopulateValues** method, you can use that method to move such data into the GridControl. Another option is to use the **GridControl.SetCellInfo** method, by passing it appropriate parameters to avoid the notification events. But, if you are only setting a few values or you need the notification events to be raised, then using an indexer is a straight-forward way to accomplish this task.

 

[]{#p567} 

 

[]{#related-topics}

