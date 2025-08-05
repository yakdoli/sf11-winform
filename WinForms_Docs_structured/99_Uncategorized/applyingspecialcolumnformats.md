---
title: applyingspecialcolumnformats.md
original_path: WinForms_Docs/99_Uncategorized/applyingspecialcolumnformats.md
created_at: 2025-08-05
---






#### Applying Special Column Formats {#applying-special-column-formats style="tab-stops: 0pt"}

[] 

The **GridBoundColumn** collection property of the Grid Data Bound Grid is used to set column properties. This collection will let you control the columns that are displayed as well as their order. For each column that you want displayed, add a Grid Bound Column. In this Grid Bound Column, you must set the **MappingName** property; the other properties such as **HeaderText** and the **Style** are optional. Under the Style property, you will have access to the normal **GridStyleInfo** properties that you can apply to this column such as **BackColor**, **CellType** and **Font**.

[] 

{border="0"}

[] 

Figure 56: GridBoundColumns Collection in the Grid Data Bound Grid\'s PropertyGrid

[] 

1.   Open the **GridBoundColumns** collection editor by using the property grid.

 

2.   Click the **Add** button to add a grid bound column, and then set **MappingName** property of that grid bound column to *ProductName*.

[] 

{border="0"}

[] 

Figure 57: Adding a GridBoundColumn to hold the ProductName Column

[] 

[] 

3.   Select **StyleInfo** property and set the back color for the column as shown in the following screen shot.

[] 

{border="0"}

[] 

Figure 58: Setting StyleInfo.BackColor for the Column

[] 

[] 

4.   Repeat the above steps to add Grid Bound Columns for \'UnitPrice\' and \'UnitsInStock\'. For the \'UnitPrice\' Grid Bound Column, set **StyleInfo.Format** to *C*.

[] 

{border="0"}

[] 

Figure 59: Setting the StyleInfo.Format Property on Column 2

[] 

[] 

5.   Compile and run the project to see the formatted Grid Data Bound Grid. In the following screen shot, you will be able to see the grid with the columns that you specified and in the order that you specified them. Notice that the \'UnitPrice\' column shows the price in the specified currency format.

[] 

{border="0"}

[] 

Figure 60: Formatted Grid Data Bound Grid

 

[]{#p19} 

 

[]{#related-topics}

