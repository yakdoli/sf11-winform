---
title: layoutspacing1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\layoutspacing1.md
created_at: 2025-07-03
---








  









### Layout Spacing {#layout-spacing style="tab-stops: 0pt"}

**[]** 

The following are general spacing properties used in many automatic layouts. Spacing refers to spaces between the nodes that lie at different levels of the tree layout, and the space between each node with their sibling.

**[]** 

Properties

**[]** 

  ---------------------- ---------------------------------------------------- ---------------------- ------------------ ---------------------------------------------------
  Property               Description                                          Type of the property   Value it accepts   Any other dependencies/ sub properties associated
  VerticalSpacing        Gets or sets the Vertical spacing between nodes.     CLR Property           Double             No
  HorizontalSpacing      Gets or sets the Horizontal spacing between nodes.   CLR Property           Double             No
  SpaceBetweenSubTrees   Gets or sets the space between sub trees.            CLR Property           Double             No
  ---------------------- ---------------------------------------------------- ---------------------- ------------------ ---------------------------------------------------

[] 

[] 

The user can set the horizontal and the vertical distance between the nodes in a tree layout using the **HorizontalSpacing** and **VerticalSpacing** properties. The spaces between sub-trees are specified using the **SpaceBetweenSubTrees** property.

[] 


{border="0"} Note: In case of Table layout, only the HorizontalSpacing and VerticalSpacing properties should be specified.


[] 

The following code illustrates these settings.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    ][\<][syncfusion][:][DiagramModel][ LayoutType][=\"DirectedTreeLayout\"][ HorizontalSpacing][=\"50\"][ [VerticalSpacing][=\"50\"][ SpaceBetweenSubTrees][=\"100\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    x][:][Name][=\"diagramModel\"\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    ][\</][syncfusion][:][DiagramModel][\>]                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][syncfusion][:][DiagramControl.Model][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [DiagramModel][ diagramModel = [new] [DiagramModel]();] |
|                                                                                                                                                                                              |
| [diagramModel.VerticalSpacing = 50;]                                                                                                                     |
|                                                                                                                                                                                              |
| [diagramModel.HorizontalSpacing = 50;]                                                                                                                   |
|                                                                                                                                                                                              |
| [diagramModel.SpaceBetweenSubTrees = 100;]                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [Dim][ diagramModel [As] [New] [DiagramModel]()] |
|                                                                                                                                                                                                         |
| [diagramModel.VerticalSpacing = 50]                                                                                                                                 |
|                                                                                                                                                                                                         |
| [diagramModel.HorizontalSpacing = 50]                                                                                                                               |
|                                                                                                                                                                                                         |
| [diagramModel.SpaceBetweenSubTrees = 100][]                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p67} 

[]{#related-topics}

