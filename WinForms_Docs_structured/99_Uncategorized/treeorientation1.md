---
title: treeorientation1.md
original_path: WinForms_Docs/99_Uncategorized/treeorientation1.md
created_at: 2025-08-05
---








  









### Tree Orientation {#tree-orientation style="tab-stops: 0pt"}

 

[The Layout Manager lets you orient the tree in many directions and can be used for the creation of many sophisticated arrangements. The Orientation property of Diagram Model can be used to specify the tree orientation.]

 

Properties\
\

+-------------+-------------------------------+----------------------+---------------------------+---------------------------------------------------+
| Property    | Description                   | Type of the property | Value it accepts          | Any other dependencies/ sub properties associated |
+-------------+-------------------------------+----------------------+---------------------------+---------------------------------------------------+
| Orientation | Gets or sets the orientation. | CLR Property         | TreeOrientation.LeftRight | No                                                |
|             |                               |                      |                           |                                                   |
|             |                               |                      | TreeOrientation.RightLeft |                                                   |
|             |                               |                      |                           |                                                   |
|             |                               |                      | TreeOrientation.TopBottom |                                                   |
|             |                               |                      |                           |                                                   |
|             |                               |                      | TreeOrientation.BottomTop |                                                   |
+-------------+-------------------------------+----------------------+---------------------------+---------------------------------------------------+

 

The following are the four orientations supported:

[] 

[·      ]**TopBottom** - Places the root node at the top and the child nodes are arranged below the root node.

[·      ]**BottomTop** - Places the root node at the Bottom and the child nodes are arranged above the root node.

[·      ]**LeftRight** - Places the root node at the Left and the child nodes are arranged on the right side of the root node.

[·      ]**RightLeft** - Places the root node at the Right and the child nodes are arranged on the left side of the root node.

 

The **Bounds** property of the **DiagramView** class can be used to specify the position of the root node based on which the entire tree gets generated.

 

 

The tree orientation can be set using the following code:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    ][\<][syncfusion][:][DiagramModel][ LayoutType][=\"DirectedTreeLayout\"][ [Orientation][=\"BottomTop\"] [x][:][Name][=\"diagramModel\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    ][\</][syncfusion][:][DiagramModel][\>]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\</][syncfusion][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [DiagramModel][ diagramModel = [new] [DiagramModel]();] |
|                                                                                                                                                                                              |
| [diagramModel.Orientation = [TreeOrientation].BottomTop;]                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [Dim][ diagramModel [As] [New] [DiagramModel]()] |
|                                                                                                                                                                                                         |
| [diagramModel.Orientation = TreeOrientation.BottomTop][]                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The tree orientation can be changed dynamically at run time using the following code for the corresponding orientation types.

 

The following code may be specified in a Combobox SelectionChanged event.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [DirectedTreeLayout][ tree = [new] [DirectedTreeLayout](diagramModel, diagramView);] |
|                                                                                                                                                                                                                           |
| [diagramModel.Orientation = [TreeOrientation].RightLeft;]                                                                                                     |
|                                                                                                                                                                                                                           |
| [tree.PrepareActivity(tree);]                                                                                                                                                         |
|                                                                                                                                                                                                                           |
| [tree.StartNodeArrangement();]                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| [(diagramView.Page [as] [DiagramPage]).InvalidateMeasure();]                                                                             |
|                                                                                                                                                                                                                           |
| [(diagramView.Page [as] [DiagramPage]).InvalidateArrange();]                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [Dim][ tree [As] [New] [DirectedTreeLayout](diagramModel, DiagramView)] |
|                                                                                                                                                                                                                                |
| [diagramModel.Orientation = TreeOrientation.RightLeft]                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [tree.PrepareActivity(tree)]                                                                                                                                                               |
|                                                                                                                                                                                                                                |
| [tree.StartNodeArrangement()]                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| [TryCast][(diagramView.Page, DiagramPage).InvalidateMeasure()]                                                                            |
|                                                                                                                                                                                                                                |
| [TryCast][(diagramView.Page, DiagramPage).InvalidateArrange()][]                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The orientations are illustrated in the following figure:

[] 

{border="0"}

Figure 93: BottomTop Orientation[]

{border="0"}

Figure 94: TopBottom Orientation[]

[] 

{border="0"}

Figure 95: LeftRight Orientation**[]**

[] 

{border="0"}

Figure 96: RightLeft Orientation

[]{#p68} 

[]{#related-topics}

