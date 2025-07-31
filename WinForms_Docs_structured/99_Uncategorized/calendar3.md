---
title: calendar3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\calendar3.md
created_at: 2025-07-03
---






##### Calendar {#calendar style="tab-stops: 0pt"}

[] 

The Calendar cell type by can be added by registering the cell model by using the **RegisterCellModel** class.

 

The following code examples illustrate how to set the cell type to Calendar.

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                              |
|                                                                                                                             |
| []                                                                        |
|                                                                                                                             |
| [GridStyleInfo][ style;]            |
|                                                                                                                             |
| [style = gridControl1\[row, 2\];]                                                       |
|                                                                                                                             |
| [style.CellType = [CustomCellTypes].Calendar.ToString();]       |
|                                                                                                                             |
| [style.Control = [new] [MonthCalendar]();] |
+-----------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                         |
|                                                                                                                                            |
| []                                                                                       |
|                                                                                                                                            |
| [Dim][ style [As] GridStyleInfo] |
|                                                                                                                                            |
| [style = gridControl1(row, 2)]                                                                         |
|                                                                                                                                            |
| [style.CellType = CustomCellTypes.Calendar.ToString()]                                                 |
|                                                                                                                                            |
| [style.Control = [New] MonthCalendar()]                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][107][: Calendar Cell]*

 

[]{#p96} 

 

[]{#related-topics}

