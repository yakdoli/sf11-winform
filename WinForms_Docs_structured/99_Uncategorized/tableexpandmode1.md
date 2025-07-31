---
title: tableexpandmode1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tableexpandmode1.md
created_at: 2025-07-03
---








  









### Table Expand Mode   {#table-expand-mode style="tab-stops: 0pt"}

The **TableExpandMode** property is an enumeration which takes two values, Horizontal and Vertical. Default value is Horizontal. It specifies how the table gets expanded when more items are added to the model.\
\

Property:

 

+-----------------+-------------------------------------+----------------------+-----------------------+---------------------------------------------------+
| Property        | Description                         | Type of the property | Value it accepts      | Any other dependencies/ sub properties associated |
+-----------------+-------------------------------------+----------------------+-----------------------+---------------------------------------------------+
| TableExpandMode | Gets or sets the table expand mode. | DependencyProperty   | ExpandMode.Horizontal | No                                                |
|                 |                                     |                      |                       |                                                   |
|                 |                                     |                      | ExpandMode.Vertical   |                                                   |
+-----------------+-------------------------------------+----------------------+-----------------------+---------------------------------------------------+

[·      ]When TableExpandMode is set to **Horizontal**, the row count is automatically calculated based on the number of nodes. The ColumnCount must be specified and the nodes will be arranged in the specified number of columns. When the maximum column count is reached, it starts placing the nodes in a new row.

[·      ]When TableExpandMode is set to **Vertical**, the column count is automatically calculated based on the number of nodes. The row count must be specified and the nodes will be arranged in the specified number of rows. When the maximum row count is reached, the nodes are placed in a new column.

[] 

The *TableExpandMode* can be set in the following way:

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
| [diagramModel.TableExpandMode=TableExpandMode.Horizontal;]                                                                                                                                                                                                                                                                             |
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
| [diagramModel.TableExpandMode=TableExpandMode.Horizontal][]                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                          |
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
| [    RowCount][=\"4\"][ ]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| [    ColumnCount][=\"4\"][ [ ]]                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [    x][:][Name][=\"diagramModel\"\>]                                                           |
|                                                                                                                                                                                                                                                                                                   |
| [\</][syncfusion][:][DiagramModel][\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 99: Table layout with TableExpandMode as Horizontal and ColumnCount as 4**[]**

[] 

{border="0"}

Figure 100: Table layout with TableExpandMode as Vertical and RowCount as 4[]

[]{#related-topics}

