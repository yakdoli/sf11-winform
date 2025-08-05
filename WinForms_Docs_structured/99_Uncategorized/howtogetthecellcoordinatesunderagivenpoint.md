---
title: howtogetthecellcoordinatesunderagivenpoint.md
original_path: WinForms_Docs/99_Uncategorized/howtogetthecellcoordinatesunderagivenpoint.md
created_at: 2025-08-05
---








  









### How to Get the Cell Coordinates Under a Given Point {#how-to-get-the-cell-coordinates-under-a-given-point style="tab-stops: 0pt"}

[] 

Introduction

[] 

If the point is given as part of one of the grids mouse event arguments, the e.X and e.Y members of the event args should give the point in the grids coordinates. If the point is obtained in some other manner, you will have to first change it to the grid\'s coordinates. Once you have the point in grid coordinates, you can call the **Grid.PointToRowCol** method to get the row and column under the point.

[] 

Example

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [// In a mouse event you might have code such as this to get the point.       ]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Point pt = ][new][ Point(e.X, e.Y);        ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [// In other situations, you could use the static Cursor.Position method to get the current mouse point in screen coordinates.        ]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Point pt = ][this][.gridControl1.PointToClient(Cursor.Position);        ]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [// Then get the row and col.]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [int][ row, col; ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [this][.grid.PointToRowCol(pt, ][out][ row, ][out][ col);        ] |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [// From the row, col, you can get the cell rectangle.      ][  ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Rectangle cellRect = ][this][.grid.RangeInfoToRectangle(GridRangeInfo.Cell(row, col));]                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\' In a mouse event you might have code such as this to get the point.        ]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ pt ][As New][ Point(e.X, e.Y)]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\' In other situations, you could use the static Cursor.Position method to get the current mouse point in screen coordinates.        ]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ pt ][As][ Point = ][Me][.GridControl1.PointToClient(Cursor.Position)]                       |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Then get the row and col.      ][  ]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ row, col ][As Integer]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.grid.PointToRowCol(pt, row, col)]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\' From the row, col, you can get the cell rectangle.    ][    ]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ cellRect ][As][ Rectangle = ][Me][.grid.RangeInfoToRectangle(GridRangeInfo.Cell(row, col))] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p621} 

 

[]{#related-topics}

