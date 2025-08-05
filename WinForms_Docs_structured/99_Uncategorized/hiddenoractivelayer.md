---
title: hiddenoractivelayer.md
original_path: WinForms_Docs/99_Uncategorized/hiddenoractivelayer.md
created_at: 2025-08-05
---








  









### Hidden or Active Layer {#hidden-or-active-layer style="tab-stops: 0pt"}

Active Layer

When a new Node or LineConnector is dropped from SymbolPalette into the DiagramPage, it will be added into all the active layers automatically. A layer can be activated or deactivated as shown in following code snippet.

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
| [Lan1.Name = [\"Lan1\"]; ]                                                                                               |
|                                                                                                                                                                                      |
| [Lan1.Nodes.Add(n1);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Nodes.Add(n2);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Lines.Add(l1);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Background = [Brushes].Transparent;]                                                                               |
|                                                                                                                                                                                      |
| [diagramModel.Layers.Add(Lan1); ]                                                                                                                |
|                                                                                                                                                                                      |
| [Lan1.Active = [false];]                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

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
| [diagramModel.Layers.Add(Lan1)]                                                                                                                            |
|                                                                                                                                                                                                |
| [Lan1.Active = [False]][]                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Hiding a Layer

The following code snippet illustrates hiding a layer. When a layer is hidden all the nodes and connectors belonging to this layer will be hidden.

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
| [Lan1.Name = [\"Lan1\"]; ]                                                                                               |
|                                                                                                                                                                                      |
| [Lan1.Nodes.Add(n1);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Nodes.Add(n2);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Lines.Add(l1);]                                                                                                                            |
|                                                                                                                                                                                      |
| [Lan1.Background = [Brushes].Transparent;]                                                                               |
|                                                                                                                                                                                      |
| [diagramModel.Layers.Add(Lan1); ]                                                                                                                |
|                                                                                                                                                                                      |
| [Lan1.Visible = [false];]                                                                                                   |
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
| [Lan1.Background = Brushes.Transparent]                                                                                                                    |
|                                                                                                                                                                                                |
| [diagramModel.Layers.Add(Lan1)]                                                                                                                            |
|                                                                                                                                                                                                |
| [Lan1.Visible = [False]][]                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 117: Before hiding the layer[]

***[]*** 

{border="0"}

Figure 118: After hiding the layer

**[]** 

[]{#related-topics}

