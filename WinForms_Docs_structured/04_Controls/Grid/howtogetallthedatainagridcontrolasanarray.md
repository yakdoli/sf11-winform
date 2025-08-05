---
title: howtogetallthedatainagridcontrolasanarray.md
original_path: WinForms_Docs/04_Controls/Grid/howtogetallthedatainagridcontrolasanarray.md
created_at: 2025-08-05
---








  









### How to Get all the Data in a GridControl as an Array {#how-to-get-all-the-data-in-a-gridcontrol-as-an-array style="tab-stops: 0pt"}

[] 

Introduction

[] 

Using an indexer to retrieve the grid\[row, col\].**CellValue** triggers events(like QueryCellInfo). In a **GridControl** where the data is stored in the grid, you can avoid the triggering of these events (which slow things down) by accessing the **GridData** directly.

[] 

Example

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// Accessing data through the GridData object\....\                                                                                                                                                                                              |
| ][GridData gridData = ][this][.gridControl1.Data;\                                           |
| ][int][ numRows = gridData.RowCount;\                                                                                                          |
| ][int][ numCols = gridData.ColCount;\                                                                                                          |
| Console.WriteLine(\"{0} rows by {1} cols\", numRows, numCols);\                                                                                                                                                                                   |
| ][for][(][int][ i = 1; i \<= numRows; ++i)\ |
| {\                                                                                                                                                                                                                                                |
| ][for][(][int][ j = 1; j \<= numCols; ++j)\ |
| {\                                                                                                                                                                                                                                                |
| ][int][ arrayCount=0;\                                                                                                                         |
| ][if][(gridData\[i, j\] != ][null][)\       |
| {\                                                                                                                                                                                                                                                |
| GridStyleInfo style = ][new][ GridStyleInfo(gridData\[i, j\]);\                                                                                |
| strArray\[arrayCount\] = style.Text;\                                                                                                                                                                                                             |
| Console.Write(strArray\[arrayCount\] + \" \");\                                                                                                                                                                                                   |
| arrayCount++;\                                                                                                                                                                                                                                    |
| }\                                                                                                                                                                                                                                                |
| ][else\                                                                                                                                                                                         |
| ][Console.Write(\"empty\");\                                                                                                                                                                     |
| }\                                                                                                                                                                                                                                                |
| Console.WriteLine(\"\");\                                                                                                                                                                                                                         |
| }\                                                                                                                                                                                                                                                |
| }]                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [\' Accessing data through the GridData object\....\                                                                                                                                                                                                                                                                                                                                    |
| ][   Dim][ gridData ][As][ GridData = ][Me][.gridControl1.Data\                |
| ][   Dim][ numRows ][As Integer][ = gridData.RowCount\                                                                                                                            |
| ][   Dim][ numCols ][As Integer][ = gridData.ColCount\                                                                                                                            |
|    Console.WriteLine(\"{0} rows by {1} cols\", numRows, numCols)\                                                                                                                                                                                                                                                                                                                       |
| ][   Dim][ i ][As Integer][ = 1\                                                                                                                                                  |
| ][   Do While][ i \<= numRows\                                                                                                                                                                                                                                                       |
| ][   Dim][ j ][As Integer][ = 1\                                                                                                                                                  |
| ][   Do While][ j \<= numCols\                                                                                                                                                                                                                                                       |
| ][   Dim][ arrayCount ][As Integer][ = 0\                                                                                                                                         |
| ][   If Not][ gridData(i, j) ][Is Nothing Then]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [\                                                                                                                                                                                                                                                                                                                                                                                      |
| ][  \' Storing all the Cell values in an Array using the GridData object.\                                                                                                                                                                                                                                                             |
| ][   Dim][ style ][As][ GridStyleInfo = ][New][ GridStyleInfo(gridData(i, j))\ |
|    strArray(arrayCount) = style.Text\                                                                                                                                                                                                                                                                                                                                                   |
|    Console.Write(strArray(arrayCount) & \"  \")\                                                                                                                                                                                                                                                                                                                                        |
|    arrayCount += 1\                                                                                                                                                                                                                                                                                                                                                                     |
| ][   Else\                                                                                                                                                                                                                                                                                                                            |
| ][   Console.Write(\"empty\")]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [   ][EndIf]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [   j+=1]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [   ][Loop]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [   Console.WriteLine(\"\")]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [   i+=1]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [   ][Loop]                                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p556} 

 

[]{#related-topics}

