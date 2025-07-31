---
title: scrollcellintoview.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scrollcellintoview.md
created_at: 2025-07-03
---






##### Scroll Cell into View {#scroll-cell-into-view style="tab-stops: 0pt"}

[] 

You can use the grid method, **ScrollCellInView**, to scroll the specified cell or range into view. The range that should be scrolled into the visible grid view area is given as the parameter to the method. The following code examples illustrate this:

 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [// Scroll into view cell(2,2).]                                                                                               |
|                                                                                                                                                                                  |
| [this][.gridControl1.ScrollCellInView([GridRangeInfo].Cell(2, 2));] |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [// Scroll into view range Col(2).]                                                                                            |
|                                                                                                                                                                                  |
| [this][.gridControl1.ScrollCellInView([GridRangeInfo].Col(2));]     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [\' Scroll into view cell(2,2).]                                                                  |
|                                                                                                                                                     |
| [Me][.gridControl1.ScrollCellInView(GridRangeInfo.Cell(2, 2))] |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [\' Scroll into view range Col(2).]                                                               |
|                                                                                                                                                     |
| [Me][.gridControl1.ScrollCellInView(GridRangeInfo.Col(2))]     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p79} 

 

[]{#related-topics}

