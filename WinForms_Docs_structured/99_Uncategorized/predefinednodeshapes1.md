---
title: predefinednodeshapes1.md
original_path: WinForms_Docs/99_Uncategorized/predefinednodeshapes1.md
created_at: 2025-08-05
---






#### Predefined Node Shapes {#predefined-node-shapes style="tab-stops: 0pt"}

[] 

A node can be assigned with a shape using the **Shape** property. Several built-in shapes are provided. The user can select from any one of the built-in shapes or specify their own custom shapes using the **CustomPathStyle** property, which will be explained later in this user guide.

 

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

The following is a list of built-in shapes:

[] 

{border="0"}

Figure 27: Built-in Shapes[]

{border="0"}

Figure 28: More Built-in Shapes**[]**

 

[]{#p22} 

[]{#related-topics}

