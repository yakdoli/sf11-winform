---
title: predefinednodeshapes2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\predefinednodeshapes2.md
created_at: 2025-07-03
---






#### Predefined Node Shapes {#predefined-node-shapes style="tab-stops: 0pt"}

[] 

A node can be assigned with a shape using the **Shape** property. Several built-in shapes are provided. The user can select from any of the built-in shapes or specify their own custom shape using the **CustomPathStyle** property, which will be explained later in this user guide.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Node][ n = [new] [Node]();] |
|                                                                                                                                                                   |
| [n.Shape = [Shapes].FlowChart_Card;]                                                                  |
|                                                                                                                                                                   |
| [diagramModel.Nodes.Add(n);]                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Dim][ n [As] [New] [Node]()] |
|                                                                                                                                                                                      |
| [n.Shape = Shapes.FlowChart_Card]                                                                                                                |
|                                                                                                                                                                                      |
| [diagramModel.Nodes.Add(n)][]                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following is a list of built-in shapes.

[] 

 

{border="0"}

Figure 28: Built-in Shapes[]

[] 

{border="0"}

Figure 29: More Built-In Shapes[]

 

[]{#related-topics}

