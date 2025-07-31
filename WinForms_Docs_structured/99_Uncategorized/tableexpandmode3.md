---
title: tableexpandmode3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tableexpandmode3.md
created_at: 2025-07-03
---








  









### Table Expand Mode {#table-expand-mode style="tab-stops: 0pt"}

The **TableExpandMode** property is an enumeration that takes two values, **Horizontal** and **Vertical**. The default value is **Horizontal**. It specifies how the table gets expanded when more items are added to the model.**[]**

[·      ]When **TableExpandMode** is set to **Horizontal**, the row count is automatically calculated based on the number of nodes. The **ColumnCount** must be specified and the nodes will be arranged in the specified number of columns. When the maximum column count is reached, it starts placing the nodes in a new row.

[·      ]When **TableExpandMode** is set to **Vertical**, the column count is automatically calculated based on the number of nodes. The row count must be specified and the nodes will be arranged in the specified number of rows. When the maximum row count is reached, the nodes are placed in a new column.

 

The **TableExpandMode** can be set in the following way:

  -- -- --- --- ---
                 
  -- -- --- --- ---

1.   In the **controller**, create an object for the **DiagramPropertiesModel** class and set the **LayoutType** to **Table Layout**.

2.   Set the **TableExpandMode** property to **Horizontal** or **Vertical**.

  ----------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------- ------------------------------------- ------------------------------------
  Property                                                                                  Description                                                                                                   Type                                  Data Type
  [TableExpandMode][]   [Gets or sets the table expand mode.][]   [Server side]   [ExpandMode]
  ----------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------- ------------------------------------- ------------------------------------

**[]** 

**[]** 


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
| [    DiagramMode = ][DiagramMode][.SVG][] |
|                                                                                                                                                                                                                                                                                                           |
| [};]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                           |
| [ViewData\[[\"TableLayout\"]\] = model;][]                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the Diagram is rendered in the SVG mode.

**[]** 

3.   Create a **view**. In the **view**, invoke the **Diagram** helper with the control ID which is the same as the **view data** name.

 


+--------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                       |
|                                                                                                                                      |
| [  [\<%]{]                                                           |
|                                                                                                                                      |
| [              Html.Syncfusion().Diagram([\"TableLayout\"])]             |
|                                                                                                                                      |
| [                  .Render();]                                                                   |
|                                                                                                                                      |
| [    }]                                                                                          |
|                                                                                                                                      |
| [  [%\>]][ ] |
+--------------------------------------------------------------------------------------------------------------------------------------+


[] 

4.   Build and run the application.

{border="0"}

Figure 108: Table Layout with TableExpandMode as Horizontal and ColumnCount as 4

{border="0"}

Figure 109: Table Layout with TableExpandMode as Vertical and RowCount as 4

 

[]{#related-topics}

