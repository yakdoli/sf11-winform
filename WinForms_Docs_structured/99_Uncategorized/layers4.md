---
title: layers4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\layers4.md
created_at: 2025-07-03
---








  









### Layers {#layers style="tab-stops: 0pt"}

[] 

Essential Diagram for WPF supports layer display. Numerous nodes and line connectors can be added to a layer and the visible property of its contents can be hidden by changing the visible property of the layer. A node or line connector can be added to any number of layers and the node is visible only if all layers to which this node or line connector belongs to are visible.

 

This feature will be useful when there are many nodes or connector in the page. If it is required to see only a particular part or particular set of nodes or connector create separate layers and categorize nodes and connectors in different layers. Then set the **IsVisible** of each layers accordingly.

 

The following topics are explained subsequently,

[·      ]Creating a Layer

[·      ]Adding the Layer to a Model

[·      ]Active Layer

[·      ]Hiding a Layer\
\
\

[] 

Table 50: Methods Table[]

  ----------------- --------------- ------------- ----------------------------------------- -----------------
  Name              Parameters      Return Type   Description                               Reference Links
  Nodes.Add(Node)   Node            void          To add a node into the layer.             N/A
  Lines.Add(Node)   LineConnector   Void          To add a line connector into the layer.   N/A
  ----------------- --------------- ------------- ----------------------------------------- -----------------

[]{#_Create_and_Add} 

Creating a Layer

The following code snippet illustrates the creation of a layer with two Nodes and one LineConnector added.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Node][ n1 = [new] [Node]();]                   |
|                                                                                                                                                                                      |
| [n1.Shape = [Shapes].FlowChart_Card;]                                                                                    |
|                                                                                                                                                                                      |
| [diagramModel.Nodes.Add(n1);]                                                                                                                    |
|                                                                                                                                                                                      |
| [n1.OffsetX = 50;]                                                                                                                               |
|                                                                                                                                                                                      |
| [n1.OffsetY = 50;]                                                                                                                               |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Node][ n2 = [new] [Node]();]                   |
|                                                                                                                                                                                      |
| [n2.Shape = [Shapes].FlowChart_Delay;]                                                                                   |
|                                                                                                                                                                                      |
| [diagramModel.Nodes.Add(n2);]                                                                                                                    |
|                                                                                                                                                                                      |
| [n2.OffsetX = 150;]                                                                                                                              |
|                                                                                                                                                                                      |
| [n2.OffsetY = 250;]                                                                                                                              |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [LineConnector][ l1 = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [l1.HeadNode = n1;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.TailNode = n2;]                                                                                                                              |
|                                                                                                                                                                                      |
| [diagramModel.Connections.Add(l1);]                                                                                                              |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Layer][ Lan1;]                                                                              |
|                                                                                                                                                                                      |
| [Lan1 = [new] [Layer]();]                                                                           |
|                                                                                                                                                                                      |
| [Lan1.Name = [\"Lan1\"];]                                                                                                |
|                                                                                                                                                                                      |
| [Lan1.Nodes.Add(n1);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Nodes.Add(n2);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Lines.Add(l1);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Background = [Brushes].Transparent;]                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ n1 [As] [New] [Node]()]          |
|                                                                                                                                                                                                |
| [n1.Shape = Shapes.FlowChart_Card]                                                                                                                         |
|                                                                                                                                                                                                |
| [diagramModel.Nodes.Add(n1)]                                                                                                                               |
|                                                                                                                                                                                                |
| [n1.OffsetX = 50]                                                                                                                                          |
|                                                                                                                                                                                                |
| [n1.OffsetY = 50]                                                                                                                                          |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ n2 [As] [New] [Node]()]          |
|                                                                                                                                                                                                |
| [n2.Shape = Shapes.FlowChart_Delay]                                                                                                                        |
|                                                                                                                                                                                                |
| [diagramModel.Nodes.Add(n2)]                                                                                                                               |
|                                                                                                                                                                                                |
| [n2.OffsetX = 150]                                                                                                                                         |
|                                                                                                                                                                                                |
| [n2.OffsetY = 250]                                                                                                                                         |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ l1 [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [l1.HeadNode = n1]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.TailNode = n2]                                                                                                                                         |
|                                                                                                                                                                                                |
| [diagramModel.Connections.Add(l1)]                                                                                                                         |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ Lan1 [As] [Layer]]                                    |
|                                                                                                                                                                                                |
| [Lan1 = [New] Layer()]                                                                                                                |
|                                                                                                                                                                                                |
| [Lan1.Name = \"Lan1\"]                                                                                                                                     |
|                                                                                                                                                                                                |
| [Lan1.Nodes.Add(n1)]                                                                                                                                       |
|                                                                                                                                                                                                |
| [Lan1.Nodes.Add(n2)]                                                                                                                                       |
|                                                                                                                                                                                                |
| [Lan1.Lines.Add(l1)]                                                                                                                                       |
|                                                                                                                                                                                                |
| [Lan1.Background = Brushes.Transparent][]                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Adding the Layer to a Model

The following code snippet illustrates the addition of a layer to a model.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]\                                                                                                                                                                           |
| \                                                                                                                                                                                    |
| ]**                                                                                                                                |
|                                                                                                                                                                                      |
| [Node][ n1 = [new] [Node]();]                   |
|                                                                                                                                                                                      |
| [n1.Shape = [Shapes].FlowChart_Card;]                                                                                    |
|                                                                                                                                                                                      |
| [diagramModel.Nodes.Add(n1);]                                                                                                                    |
|                                                                                                                                                                                      |
| [n1.OffsetX = 50;]                                                                                                                               |
|                                                                                                                                                                                      |
| [n1.OffsetY = 50;]                                                                                                                               |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Node][ n2 = [new] [Node]();]                   |
|                                                                                                                                                                                      |
| [n2.Shape = [Shapes].FlowChart_Delay;]                                                                                   |
|                                                                                                                                                                                      |
| [diagramModel.Nodes.Add(n2);]                                                                                                                    |
|                                                                                                                                                                                      |
| [n2.OffsetX = 150;]                                                                                                                              |
|                                                                                                                                                                                      |
| [n2.OffsetY = 250;]                                                                                                                              |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [LineConnector][ l1 = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [l1.HeadNode = n1;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.TailNode = n2;]                                                                                                                              |
|                                                                                                                                                                                      |
| [diagramModel.Connections.Add(l1);]                                                                                                              |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Layer][ Lan1;]                                                                              |
|                                                                                                                                                                                      |
| [Lan1 = [new] [Layer]();]                                                                           |
|                                                                                                                                                                                      |
| [Lan1.Name = [\"Lan1\"];]                                                                                                |
|                                                                                                                                                                                      |
| [Lan1.Nodes.Add(n1);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Nodes.Add(n2);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Lines.Add(l1);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Background = [Brushes].Transparent;]                                                                               |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [diagramModel.Layers.Add(Lan1)]                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]\                                                                                                                                                                                     |
| \                                                                                                                                                                                              |
| ]**                                                                                                                                          |
|                                                                                                                                                                                                |
| [Dim][ n1 [As] [New] [Node]()]          |
|                                                                                                                                                                                                |
| [n1.Shape = Shapes.FlowChart_Card]                                                                                                                         |
|                                                                                                                                                                                                |
| [diagramModel.Nodes.Add(n1)]                                                                                                                               |
|                                                                                                                                                                                                |
| [n1.OffsetX = 50]                                                                                                                                          |
|                                                                                                                                                                                                |
| [n1.OffsetY = 50]                                                                                                                                          |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ n2 [As] [New] [Node]()]          |
|                                                                                                                                                                                                |
| [n2.Shape = Shapes.FlowChart_Delay]                                                                                                                        |
|                                                                                                                                                                                                |
| [diagramModel.Nodes.Add(n2)]                                                                                                                               |
|                                                                                                                                                                                                |
| [n2.OffsetX = 150]                                                                                                                                         |
|                                                                                                                                                                                                |
| [n2.OffsetY = 250]                                                                                                                                         |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ l1 [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [l1.HeadNode = n1]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.TailNode = n2]                                                                                                                                         |
|                                                                                                                                                                                                |
| [diagramModel.Connections.Add(l1)]                                                                                                                         |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ Lan1 [As] [Layer]]                                    |
|                                                                                                                                                                                                |
| [Lan1 = [New] Layer()]                                                                                                                |
|                                                                                                                                                                                                |
| [Lan1.Name = \"Lan1\"]                                                                                                                                     |
|                                                                                                                                                                                                |
| [Lan1.Nodes.Add(n1)]                                                                                                                                       |
|                                                                                                                                                                                                |
| [Lan1.Nodes.Add(n2)]                                                                                                                                       |
|                                                                                                                                                                                                |
| [Lan1.Lines.Add(l1)]                                                                                                                                       |
|                                                                                                                                                                                                |
| [Lan1.Background = Brushes.Transparent]                                                                                                                    |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [diagramModel.Layers.Add(Lan1)][]                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[]{#related-topics}

