---
title: enablingtablelayoutwithvariednodesizes1.md
original_path: WinForms_Docs/99_Uncategorized/enablingtablelayoutwithvariednodesizes1.md
created_at: 2025-08-05
---








  









### Enabling Table Layout with Varied Node Sizes {#enabling-table-layout-with-varied-node-sizes style="tab-stops: 0pt"}

 

The **EnableLayoutWithVariedSizes** property , when set to true, center aligns the content of each cell so that all the nodes in that row and column in the table, get aligned with respect to the larger cell size. This property can be set to true, if the nodes are of different sizes (width and height).

 

[] 

[\
\
]

Property:

[] 

  ----------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------
  Property                      Description                                                                                                                                                                                                                                          Type of the property   Value it accepts        Any other dependencies/ sub properties associated
  EnableLayoutWithVariedSizes   Gets or sets a value indicating whether to enable the varied size algorithm. In case the Model consists of the nodes of different sizes, this property can be set to true. This will align the differently sized nodes with respect to the center.   DependencyProperty     Boolean (true/ false)   No
  ----------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------

[] 

The *EnableLayoutWithVariedSizes* can be set in the following way:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [DiagramControl][ dc = ][new][ ][DiagramControl][();]       |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [DiagramModel][ diagramModel = ][new][ ][DiagramModel][();] |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [dc.Model = diagramModel;]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [diagramModel.EnableLayoutWithVariedSizes = [true];]                                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [Dim][ dc [As] [New] [DiagramControl]()]         |
|                                                                                                                                                                                                         |
| [Dim][ diagramModel [As] [New] [DiagramModel]()] |
|                                                                                                                                                                                                         |
| [dc.Model = diagramModel]                                                                                                                                           |
|                                                                                                                                                                                                         |
| [diagramModel.EnableLayoutWithVariedSizes = [True]][]                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                   |
| [\<][syncfusion][:][DiagramModel]                                                       |
|                                                                                                                                                                                                                                                                                                   |
| [    LayoutType][=\"TableLayout\"][ ]                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [    TableExpandMode][=\"Horizontal\"][ ]                                                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| [    HorizontalSpacing][=\"50\"][ ]                                                                                                              |
|                                                                                                                                                                                                                                                                                                   |
| [    VerticalSpacing][=\"50\"][ ]                                                                                                                |
|                                                                                                                                                                                                                                                                                                   |
| [    RowCount][=\"3\"][ ]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| [    ColumnCount][=\"5\"][ [ ]]                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [    EnableLayoutWithVariedSizes][=\"True\"]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                   |
| [    x][:][Name][=\"diagramModel\"\>]                                                           |
|                                                                                                                                                                                                                                                                                                   |
| [\</][syncfusion][:][DiagramModel][\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 103: EnableLayoutWithVariedSize set to false**[]**

**[]** 

{border="0"}

Figure 104: EnableLayoutWithVariedSize set to true[]{#p74}

[]{#related-topics}

