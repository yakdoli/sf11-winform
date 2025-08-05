---
title: coveredranges.md
original_path: WinForms_Docs/99_Uncategorized/coveredranges.md
created_at: 2025-08-05
---






#### Covered Ranges {#covered-ranges style="tab-stops: 0pt"}

[] 

Covered Cells are cells that span over neighboring cells. The combined cells will act as if they are one single cell visually and programmatically. There are different possible options to form a covered range. You can combine the cells in adjacent rows or columns or both.

[] 

Creating Covered Range

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [this][.grid.Model.CoveredCells.Add ([new] [CoveredCellInfo] (6, 4, 7, 4));            ]   |
|                                                                                                                                                                                                                              |
| [this][.grid.Model.CoveredCells.Add ([new] [CoveredCellInfo] (6, 6, 7, 6));]               |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [cell = [this].grid.Model\[6, 4\];]                                                                                                                                 |
|                                                                                                                                                                                                                              |
| [cell.CellValue = [\"Row spanned cell\"];]                                                                                                                       |
|                                                                                                                                                                                                                              |
| [cell.Background = [Brushes].BlanchedAlmond;]                                                                                                                    |
|                                                                                                                                                                                                                              |
| [cell.[HorizontalAlignment] = [HorizontalAlignment].Center;]                                                                             |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [cell = [this].grid.Model\[6, 6\];]                                                                                                                                 |
|                                                                                                                                                                                                                              |
| [cell.CellValue = [\"Row spanned cell\"];]                                                                                                                       |
|                                                                                                                                                                                                                              |
| [cell.[HorizontalAlignment] = [HorizontalAlignment].Center;]                                                                             |
|                                                                                                                                                                                                                              |
| [cell.Background = [Brushes].BlanchedAlmond;            ]                                                                                                        |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [this][.grid.Model.CoveredCells.Add ([new] [CoveredCellInfo] (9, 4, 11, 6));            ]  |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [cell = [this].grid.Model\[9, 4\];]                                                                                                                                 |
|                                                                                                                                                                                                                              |
| [cell.CellValue = [\"Column and row spanned cell\"];            ]                                                                                                |
|                                                                                                                                                                                                                              |
| [cell.[HorizontalAlignment] = [HorizontalAlignment].Center;]                                                                             |
|                                                                                                                                                                                                                              |
| [cell.Background = [Brushes].BlanchedAlmond;            ]                                                                                                        |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [this][.grid.Model.CoveredCells.Add ([new] [CoveredCellInfo] (13, 4, 13, 6));            ] |
|                                                                                                                                                                                                                              |
| [cell = [this].grid.Model\[13, 4\];]                                                                                                                                |
|                                                                                                                                                                                                                              |
| [cell.CellValue = [\"Column spanned cell\"];]                                                                                                                    |
|                                                                                                                                                                                                                              |
| [cell.Background = [Brushes].BlanchedAlmond;]                                                                                                                    |
|                                                                                                                                                                                                                              |
| [cell.[HorizontalAlignment] = [HorizontalAlignment].Center;]                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Output

**[]** 

The following output is generated using the code above.

[] 

{border="0"}

[] 

Figure 45: Covered Ranges

[] 

See Also

[] 

[QueryCoveredRange event][]

[]{#p186} 

 

[]{#related-topics}

