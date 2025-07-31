---
title: settingstyleforthecolumn.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\settingstyleforthecolumn.md
created_at: 2025-07-03
---






#### Setting Style for the Column {#setting-style-for-the-column style="tab-stops: 0pt"}

You can also control the appearance of cells in a particular column by setting the GridStyleInfo values held in the GridTreeColumn.StyleInfo property for a particular column.

 

The following code example illustrates how to set this property for a column in the Grid Tree.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [GridTreeColumn][ tc = [new] [GridTreeColumn]([\"Department\"], [\"Department\"], 100);] |
|                                                                                                                                                                                                                                                                               |
| [tc.StyleInfo.Background = [Brushes].Azure;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [gridTreeControl1.Columns.Add(tc); [ ]]                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screen shot shows the StyleInfo property applied to the "Department" column in the Grid Tree.

 

{border="0"}

Figure 260: Column Styles

 

Grid cell background for the Department column is customized.

 

 

 

[]{#related-topics}

