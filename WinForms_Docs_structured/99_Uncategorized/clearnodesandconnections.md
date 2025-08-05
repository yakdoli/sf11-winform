---
title: clearnodesandconnections.md
original_path: WinForms_Docs/99_Uncategorized/clearnodesandconnections.md
created_at: 2025-08-05
---








  









### Clear Nodes and Connections {#clear-nodes-and-connections style="tab-stops: 0pt"}

Essential Diagram WPF allows you to clear the nodes and connections added to the diagram. It can be done by clearing the collections of nodes and connections from DiagramModel.

[] 

Table 54: Property Table[]

  ------------- ----------------------- ---------------------- ------------------ ---------------------------------------------------
  Property      Description             Type of the property   Value it accepts   Any other dependencies/ sub properties associated
  Connections   Gets the connections.   CLR property           CollectionExt      No
  Nodes         Gets the shapes.        CLR property           CollectionExt      No
  ------------- ----------------------- ---------------------- ------------------ ---------------------------------------------------

[] 

The following lines of code can be used to clear nodes and connections.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [DiagramModel][ diagramModel = [new] [DiagramModel]();] |
|                                                                                                                                                                                              |
| [diagramModel.Nodes.Clear();]                                                                                                                            |
|                                                                                                                                                                                              |
| [diagramModel.Connections.Clear();]                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [Dim][ diagramModel [As] [New] [DiagramModel]()] |
|                                                                                                                                                                                                         |
| [diagramModel.Nodes.Clear()]                                                                                                                                        |
|                                                                                                                                                                                                         |
| [diagramModel.Connections.Clear()][]                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

