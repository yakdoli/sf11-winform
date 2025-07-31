---
title: tablelayout2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tablelayout2.md
created_at: 2025-07-03
---








  









### Table Layout {#table-layout style="MARGIN-BOTTOM: 12pt; tab-stops: 0pt"}

Table layout arranges the nodes in a tabular structure based on specified intervals between them. The number of nodes in each row and column can be specified and the layout will take place accordingly. The nodes are assigned rows and columns based on the order in which they are added to the model and based on the maximum nodes allowed in that row and column.

 

  Property                                                                                  Description                                                                                                                                                                                                                                                              Type                                  Data Type                                       Reference Links
  ----------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------- ----------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [VerticalSpacing][]   [Gets or sets the vertical spacing between nodes.][]                                                                                                                                                 [Server side]   [Double]                  [[http://help.syncfusion.com/ug_92/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2F4313layoutspacing.htm]{.UGHyperlink}](http://help.syncfusion.com/ug_92/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2F4313layoutspacing.htm)[]{.UGHyperlink}
  [HorizontalSpacing]                                                 [Gets or sets the horizontal spacing between nodes.]                                                                                                                                                                                               [Server side]   [Double]                  [[http://help.syncfusion.com/ug_92/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2F4313layoutspacing.htm]{.UGHyperlink}](http://help.syncfusion.com/ug_92/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2F4313layoutspacing.htm)[]{.UGHyperlink}
  [TableExpandMode]                                                   [Gets or sets the table expand mode.]                                                                                                                                                                                                              [Server side]   [ExpandMode]              [Table Expand Mode][]
  [RowCount]                                                          [Gets or sets the row count for the table layout.]                                                                                                                                                                                                 [Server side]   [Int]                     [Row Count and Column Count][]
  [ColumnCount]                                                       [Gets or sets the column count for the table layout.]                                                                                                                                                                                              [Server side]   [int]                     [Row Count and Column Count][]
  [EnableLayoutWithVariedSizes]                                       [Gets or sets a value indicating whether to enable the varied size algorithm. In case the model consists of nodes of different sizes, this property can be set to true. This will align the differently sized nodes with respect to the center.]   [Server side]   [Binary, true or false]   [Enabling Table Layout with Varies Node Sizes][]

 

The layout manager lets you orient the table in two directions, horizontal and vertical. The **TableExpandMode** property of the **Diagram** model is used to specify the orientation.

**Horizontal**: When set to horizontal, the row count is automatically calculated based on the number of nodes. The column count must be specified and the nodes will be arranged in the specified number of columns.

**Vertical**: When set to vertical, the column count is automatically calculated based on the number of nodes. The row count must be specified and the nodes will be arranged in the specified number of rows.

 

The following code shows how the automatic layout can be generated. 

1.   In the **controller**, create an object for the **DiagramPropertiesModel** class and set the **LayoutType** to **TableLayout**.

2.   Set the **TableExpandMode** property to **Horizontal** or **Vertical**.

3.   Set the row count and column count.

4.   Pass this model class to the **view data**.


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| [DiagramPropertiesModel][ model = [new] [DiagramPropertiesModel]()]                                                                |
|                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [    LayoutType = [LayoutType].TableLayout,]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                           |
| [    TableExpandMode = [ExpandMode].Horizontal,]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [    HorizontalSpacing = 60,]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| [    VerticalSpacing = 60,]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [    RowCount = 5,]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [    ColumnCount = 4,]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                           |
| [    RootOffsetX = 100,]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [    RootOffsetY = 50,]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| [    DiagramMode = ][DiagramMode][.SVG][] |
|                                                                                                                                                                                                                                                                                                           |
| [};]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                           |
| [ViewData\[[\"TableLayout\"]\] = model;][]                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.**[]**

 

5.   Create a **view**. In the **view**, invoke the **Diagram** helper with the control which is the same as the **view data** name.

 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View][]**                                                                  |
|                                                                                                                                                                        |
| [  [\<%]{]                                                                            |
|                                                                                                                                                                        |
| [              Html.Syncfusion().Diagram([\"TableLayout\"])]                              |
|                                                                                                                                                                        |
| [                  .Render();]                                                                                    |
|                                                                                                                                                                        |
| [    }]                                                                                                           |
|                                                                                                                                                                        |
| [  [%\>]][ ] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

6.   Build and run the application.

 

{border="0"}

Figure 120: Table Layout

 

See Also

 

[·      ]**Layout Spacing**---Refer to Concepts and Features \> Diagram Model \> Layout Spacing.

 

[·      ]**TableExpandMode**---Refer to Concepts and Features \> Diagram Model \> Table Expand Mode.

 

[·      ]**RowCount and ColumnCount**---Refer to Concepts and Features \> Diagram Model \> RowCount and ColumnCount.

 

[·      ]**Enable TableLayout with varied Node sizes**---Refer to Concepts and Features \> Diagram Model \> Enable TableLayout with Varied Node Size.

 

[]{#related-topics}

