---
title: enablingtablelayoutwithvariednodesizes2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\enablingtablelayoutwithvariednodesizes2.md
created_at: 2025-07-03
---








  









### Enabling Table Layout with Varied Node Sizes {#enabling-table-layout-with-varied-node-sizes style="tab-stops: 0pt"}

[Setting the **EnableLayoutWithVariedSizes** property to **true** center aligns the content of each cell so that all the nodes in a specific row and column of the table get aligned with respect to the larger cell size. This property can be set to **true** if the nodes are of different sizes (width and height).]

**[Property][]**

  ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------- -----------------------
  Property                      Description                                                                                                                                                                                                                                      Type          Data Type
  EnableLayoutWithVariedSizes   Gets or sets a value indicating whether to enable the varied size algorithm. In case the Model consists of nodes of different sizes, this property can be set to true. This will align the differently sized nodes with respect to the center.   Server side   Binary, true or false
  ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------- -----------------------

 

The **EnableLayoutWithVariedSizes** can be set in the following way:

1.   In the **controller**, create an object for the **DiagramPropertiesModel** class and set **LayoutType** to **TableLayout**.

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
| [    EnableLayoutWithVariedSizes = [true,]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                           |
| [    DiagramMode = ][DiagramMode][.SVG][] |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                   |
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

Figure 112: EnableLayoutWithVariedSize set to False

{border="0"}

Figure 113: EnableLayoutWithVariedSize set to True

[]{#related-topics}

