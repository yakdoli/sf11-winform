---
title: cyclicpathinhierarchicaltreelayout1.md
original_path: WinForms_Docs/99_Uncategorized/cyclicpathinhierarchicaltreelayout1.md
created_at: 2025-08-05
---








  









### Cyclic path in Hierarchical-Tree Layout {#cyclic-path-in-hierarchical-tree-layout style="tab-stops: 0pt"}

The Hierarchical-Tree layout provides support for creating cyclic paths. A cycle is said to exist if nodes are connected in a chain such that the last node in the chain is connected back to the first node. For example, if there are four nodes namely n1, n2, n3 and n4, such that n1 is connected to n2, n2 is connected to n3, n3 is connected to n4, and n4 is again connected to n1 (n1\--\>n2\--\>n3\--\>n4), then these nodes are said to form a cycle.

[] 

Table 56: Property Table[]

  ---------------------- ---------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------
  Property               Description                                                                  Type of the property   Value it accepts        Any other dependencies/ sub properties associated
  EnableCycleDetection   Gets or sets a value indicating whether Cycle detection is enabled or not.   DependencyProperty     Boolean (true/ false)   No
  ---------------------- ---------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------

[] 

To specify a cyclic path is as giving input to the Hierarchical-Tree layout. **EnableCycleDetection** property must be set to True. Enabling this property checks for cycles and makes connections accordingly.

***[]*** 


{border="0"}Note: The EnableCycleDetection property takes effect only for the Hierarchical-Tree layout type of the Diagram Model.


[] 

The following code example illustrates how to set the EnableCycleDetection property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][\<!\--Diagram Control\--\>][]                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][\<][syncfusion][:][DiagramControl][ [ Name][=\"diagramControl\"\>]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [        ][\<!\-- Model to add nodes and connections\--\>][]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [ \<][syncfusion][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][syncfusion][:][DiagramModel][ [x][:][Name][=\"diagramModel\"][ LayoutType][=\"HierarchicalTreeLayout\" ][EnableCycleDetection][=\"True\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Orientation][=\"TopBottom\"][ [\>]]                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\</][syncfusion][:][DiagramModel][\>]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [ \</][syncfusion][:][DiagramControl.Model][\>][]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [        ][\<!\--View to display nodes and connections added through model.\--\>][]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [        ][\<][syncfusion][:][DiagramControl.View][\>][]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            ][\<][syncfusion][:][DiagramView][ Name][=\"diagramView\"\>][]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            ][\</][syncfusion][:][DiagramView][\>][]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [        ][\</][syncfusion][:][DiagramControl.View][\>][]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][\</][syncfusion][:][DiagramControl][\>][]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [DiagramModel][ diagramModel = [new] [DiagramModel]();] |
|                                                                                                                                                                                              |
| [diagramModel.Orientation = [TreeOrientation].TopBottom;]                                                                        |
|                                                                                                                                                                                              |
| [diagramModel.LayoutType = [LayoutType].HierarchicalTreeLayout;]                                                                 |
|                                                                                                                                                                                              |
| [diagramModel.EnableCycleDetection = [true];]                                                                                       |
|                                                                                                                                                                                              |
| [diagramControl.Model = diagramModel;]                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [Dim][ diagramModel [As] [New] [DiagramModel]()] |
|                                                                                                                                                                                                         |
| [diagramModel.Orientation = TreeOrientation.TopBottom]                                                                                                              |
|                                                                                                                                                                                                         |
| [diagramModel.LayoutType = LayoutType.HierarchicalTreeLayout]                                                                                                       |
|                                                                                                                                                                                                         |
| [diagramModel.EnableCycleDetection = [True]]                                                                                                   |
|                                                                                                                                                                                                         |
| [diagramControl.Model = diagramModel][]                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates Cyclic Paths in the Hierarchical-Tree layout.

[] 

{border="0"}

Figure 126: Cyclic Paths In Hierarchical-Tree Layout[]

[] 


{border="0"}Note: If a cyclic path is specified as input when the EnableCycleDetection property is set to False, then a stack overflow exception is thrown as the loop goes on forever.


[] 

Advantages

Cyclic paths are very useful to demonstrate work flows which involve repeated processes.

[] 

See Also

 Refer Getting Started -\> Automatic Layout

 

[]{#related-topics}

