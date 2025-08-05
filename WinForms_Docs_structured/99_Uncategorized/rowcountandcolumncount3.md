---
title: rowcountandcolumncount3.md
original_path: WinForms_Docs/99_Uncategorized/rowcountandcolumncount3.md
created_at: 2025-08-05
---








  









### Row Count and Column Count {#row-count-and-column-count style="tab-stops: 0pt"}

**RowCount** and **ColumnCount** properties are used to specify the maximum number of rows and columns allowed in the table. Refer to **TableExpandMode** property for more details.**[]**

  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------- ------------------------------------- -----------------------------
  Property                                                                           Description                                                                                                               Type                                  Data Type
  [RowCount][]   [Gets or sets the Row Count for the table layout][]   [Server side]   [Int]
  [ColumnCount]                                                [Gets or sets the Column Count for the table layout]                                                [Server side]   [int]
  ---------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------- ------------------------------------- -----------------------------

 

The **TableExpandMode** can be set in the following way:

1.   In the **controller**, create an object for **DiagramPropertiesModel** class and set the **LayoutType** to **Table Layout**.

2.   Set the **TableExpandMode** property to **Horizontal** or **Vertical**.

 

3.   Set the row count and column count.

 


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
| [    RowCount = 4,]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [    ColumnCount = 4,]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                           |
| [    DiagramMode = ][DiagramMode][.SVG][] |
|                                                                                                                                                                                                                                                                                                           |
| [};]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                           |
| [ViewData\[[\"TableLayout\"]\] = model;][]                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode.

 

4.   Create a **view**. In the **view**, invoke the **Diagram** helper with the control ID which is the same as the **view data** name.

 


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

5.   Build and run the application.

 

{border="0"}

Figure 110: ColumnCount specified as 4

{border="0"}

Figure 111: RowCount specified as 4

[]{#related-topics}

