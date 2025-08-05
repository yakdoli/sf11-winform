---
title: howtodeterminethatnocellisselected.md
original_path: WinForms_Docs/99_Uncategorized/howtodeterminethatnocellisselected.md
created_at: 2025-08-05
---








  









### How to Determine that No Cell is Selected {#how-to-determine-that-no-cell-is-selected style="tab-stops: 0pt"}

[      ]

To determine whether the cell is selected or not, use the **GetSelectedRange** method. It returns the list with selected range. If it returns the range as zero, then no cell is selected.

[                  ]

[·      ]**ranges** - It sets the range of cells to be selected.

[·      ]**ConsiderCurrentCell**

 

**True** - If the current cell should be treated as selected range.

 

Example

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                                |
|                                                                                                                                                                                           |
| **[   ]**[GridRangeInfoList rangeList = [null];]                                             |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                                |
|                                                                                                                                                                                           |
| [   [this].gridDataBoundGrid1.Selections.GetSelectedRanges([out ]rangeList, [false]);] |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [   [if] (rangeList.Count == 0)]                                                                                                 |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [          {]                                                                                                                                         |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [     Console.WriteLine([\"no selection\"]);]                                                                                 |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [           }]                                                                                                                                        |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                            |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                                  |
|                                                                                                                                                                                             |
|         [Dim][ rangeList [As] GridRangeInfoList = [Nothing]] |
|                                                                                                                                                                                             |
| [   [Me].gridDataBoundGrid1.Selections.GetSelectedRanges(rangeList,[False])]                                  |
|                                                                                                                                                                                             |
| [   [If] rangeList.Count = 0 [Then]]                                                                          |
|                                                                                                                                                                                             |
| [             Console.WriteLine([\"no Selection\"])]                                                                            |
|                                                                                                                                                                                             |
| [   [End] [If]]                                                                                               |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

[]{#related-topics}

