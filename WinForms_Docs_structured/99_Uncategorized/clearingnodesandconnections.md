---
title: clearingnodesandconnections.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clearingnodesandconnections.md
created_at: 2025-07-03
---








  









### Clearing Nodes and Connections {#clearing-nodes-and-connections style="tab-stops: 0pt"}

[] 

Essential Diagram Silverlight allows the user to clear the nodes and connections added to the diagram. It can be done by clearing the collections of nodes and connections from DiagramModel.

[] 

Properties[]

[] 

  ------------- ----------------------- ---------------------- ------------------ ---------------------------------------------------
  Property      Description             Type of the property   Value it accepts   Any other dependencies/ sub properties associated
  Connections   Gets the connections.   CLR Property           CollectionExt      No
  Nodes         Gets the shapes.        CLR Property           CollectionExt      No
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

 

[]{#p69} 

[]{#related-topics}

