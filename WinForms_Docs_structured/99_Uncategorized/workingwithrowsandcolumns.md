---
title: workingwithrowsandcolumns.md
original_path: WinForms_Docs/99_Uncategorized/workingwithrowsandcolumns.md
created_at: 2025-08-05
---






#### Working with Rows and Columns {#working-with-rows-and-columns style="tab-stops: 0pt"}

[] 

Grid control has properties that allow users to manipulate rows and columns programmatically. The following properties will be discussed in this section.

[] 

[·      ]**GridControl.Cols, GridControl.Rows** - Allows you to hide rows and columns, to freeze them to prevent scrolling and  to control the number of headers.

[·      ]**GridControl.ColWidths, GridControl.RowHeights** - Allows you to set the row heights and column widths programmatically.

[·      ]**GridListControl.ColStyles, GridListControl.RowStyles** - Allows you to set the row or column styles.

[] 

For a Grid Data Bound Grid, you can access the first two items through the **GridDataBoundGrid.Model** property. The Grid Data Bound Grid does not use **RowStyles** or **ColStyles**. It uses the **GridBoundColumn.StyleInfo** object to set column styles with row styles not being directly supported. See the section on Grid Data Bound Grid for more information on how to set its styles.

 

This section comprises the following topics:

 

[]{#p325} 

 

More:





















