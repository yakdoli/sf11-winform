---
title: settingcolumnstylesandrowstyles.md
original_path: WinForms_Docs/02_Concepts/settingcolumnstylesandrowstyles.md
created_at: 2025-08-05
---






##### Setting Column Styles and Row Styles {#setting-column-styles-and-row-styles style="tab-stops: 0pt"}

[] 

The **GridControl.ColStyles** and **GridControl.RowStyles** collections will allow you to programmatically set the default row or column style. This code will set the **backcolor** and the text color as well as set the font to bold for column two and row three.

[] 


{border="0"}Note:[ ]RowStyles and ColStyles are not supported in a Grid Data Bound Grid. For that grid, you will need to use  the GridBoundColumn.StyleInfo property to set column styles and you will need to use the grid.Model.QueryCellInfo event to set row styles.


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                               |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// Set Back Color, Text Color and Font Style of Column 2.]                                                                |
|                                                                                                                                                                              |
| [this][.gridControl1.ColStyles\[2\].BackColor = [Color].Red;]   |
|                                                                                                                                                                              |
| [this][.gridControl1.ColStyles\[2\].TextColor = [Color].White;] |
|                                                                                                                                                                              |
| [this][.gridControl1.ColStyles\[2\].Font.Bold = [true];]           |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [// Set Back Color, Text Color and Font Style of Row 3.]                                                                   |
|                                                                                                                                                                              |
| [this][.gridControl1.RowStyles\[3\].BackColor = [Color].Red;]   |
|                                                                                                                                                                              |
| [this][.gridControl1.RowStyles\[3\].TextColor = [Color].White;] |
|                                                                                                                                                                              |
| [this][.gridControl1.RowStyles\[3\].Font.Bold = [true];]           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                      |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [\' Set Back Color, Text Color and Font Style of Column 2.]                                                                                           |
|                                                                                                                                                                                                         |
| [Me][.GridControl1.ColStyles(2).BackColor = Color.Red]                                               |
|                                                                                                                                                                                                         |
| [Me][.GridControl1.ColStyles(2).TextColor = Color.White]                                             |
|                                                                                                                                                                                                         |
| [Me][.GridControl1.ColStyles(2).Font.Bold = ][True] |
|                                                                                                                                                                                                         |
| []                                                                                                                                                     |
|                                                                                                                                                                                                         |
| [\' Set Back Color, Text Color and Font Style of Row 3.]                                                                                              |
|                                                                                                                                                                                                         |
| [Me][.GridControl1.RowStyles(3).BackColor = Color.Red]                                               |
|                                                                                                                                                                                                         |
| [Me][.GridControl1.RowStyles(3).TextColor = Color.White]                                             |
|                                                                                                                                                                                                         |
| [Me][.GridControl1.RowStyles(3).Font.Bold = ][True] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[ ][{border="0"}][]**

[] 

*[Figure ][176][: Grid After Setting the Styles For Column 2 and Row 3]*

 

[]{#p331} 

 

[]{#related-topics}

