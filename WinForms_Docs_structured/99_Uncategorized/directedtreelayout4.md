---
title: directedtreelayout4.md
original_path: WinForms_Docs/99_Uncategorized/directedtreelayout4.md
created_at: 2025-08-05
---








  









### Directed Tree Layout {#directed-tree-layout style="MARGIN-BOTTOM: 12pt; tab-stops: 0pt"}

The directed tree layout automatically arranges nodes in a tree-like structure. This enables the user to position nodes in a tree-like fashion without specifying the coordinate location for each node.

This layout can be applied to any diagram that comprises a directed tree graph with unique root and child nodes. This makes creating diagrams easier because the node position is determined automatically, based on the connections. However, it is necessary to specify a layout root for the tree layout. The directed tree layout will position the nodes based on the layout root. 

Orientation

The layout manager lets you orient the tree in many directions and create sophisticated arrangements. The **Orientation** property of the **Diagram** model can be used to specify the tree orientation. 

[·      ]**TopBottom**---Places the root node at the top and the child nodes are arranged below the root node.

[·      ]**BottomTop**---Places the root node at the bottom and the child nodes are arranged above the root node.

[·      ]**LeftRight**---Places the root node at the left and the child nodes are arranged on the right side of the root node.

[·      ]**RightLeft**---Places the root node at the right and the child nodes are arranged on the left side of the root node.

The **RootOffsetX** and **RootOffsetY** properties can be used to specify the position of the root node based on which the entire tree gets generated. 

The following code shows how the automatic layout can be generated. 

 

1.   The **LayoutType** should be set to **DirectedTreeLayout**.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [\<%][{]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [      Html.Syncfusion().Diagram([\"DirectedTreeLayout\"])]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [          .LayoutType([LayoutType].DirectedTreeLayout)]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [          .Orientation([TreeOrientation].TopBottom)]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [          .HorizontalSpacing(100)]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [          .VerticalSpacing(50)]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [          .SpaceBetweenSubTrees(30)]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [          .RootOffsetX(400)]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [          .RootOffsetY(50)]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [           ][.DiagramMode(][DiagramMode][.SVG)][] |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [          .Render();]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [  }]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [%\>][]                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** If you want to create the diagram in the Canvas mode, change the **DiagramMode** to **Canvas**. By default the diagram is rendered in the SVG mode. 

 

2.   Then, the nodes are defined and the connections are made. 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[ ]                                                                                                                                           |
|                                                                                                                                                                                                                                                                         |
| [        DiagramPropertiesModel][ diagramModel = [new] [DiagramPropertiesModel]() { };]          |
|                                                                                                                                                                                                                                                                         |
| [        [public] [ActionResult] DirectedTreeLayout()]                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [            GetNodesConnectors(diagramModel);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [            diagramModel.Width = [Unit].Pixel(950);]                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            diagramModel.Height = [Unit].Pixel(600);]                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            ViewData\[[\"DirectedTreeLayout\"]\] = diagramModel;]                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [            [return] View();]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [        [public] [ActionResult] DirectedTreeLayout([string] s)]                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [            [return] null;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [        [private] [void] GetNodesConnectors([DiagramPropertiesModel] diagramModel)]                                                             |
|                                                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node1 = AddNode([\"Node1\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node2 = AddNode([\"Node2\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node3 = AddNode([\"Node3\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node4 = AddNode([\"Node4\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node5 = AddNode([\"Node5\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node6 = AddNode([\"Node6\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node7 = AddNode([\"Node7\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node8 = AddNode([\"Node8\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node9 = AddNode([\"Node9\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node10 = AddNode([\"Node10\"]);]                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node11 = AddNode([\"Node11\"]);]                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] line1 = AddConnector(node1, node2,[\"line1\"]);]                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] line2 = AddConnector(node1, node3,[\"line2\"]);]                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] line3 = AddConnector(node2, node4,[\"line3\"]);]                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] line4 = AddConnector(node2, node5,[\"line4\"]);]                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] line5 = AddConnector(node3, node6,[\"line5\"]);]                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] line6 = AddConnector(node3, node7,[\"line6\"]);]                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] line7 = AddConnector(node5, node8,[\"line7\"]);]                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] line8 = AddConnector(node5, node9,[\"line8\"]);]                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] line9 = AddConnector(node7, node10,[\"line9\"]);]                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] line10 = AddConnector(node7, node11,[\"line10\"]);]                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [            diagramModel.Nodes = [new NodesCollection()]]                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [                node1,node2,node3,node4,node5,node6,node7,node8,node9,node10,node11]                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [            };]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [            diagramModel.Connectors = [new LinesCollection()]]                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [                line1, line2, line3, line4, line5, line6,line7,line8,line9,line10]                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [            };]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [        [public] [Node] AddNode([string] name)]                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [            [Node] node = [new] [Node]()]                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [                Name = name,]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [                LabelHorizontalAlignment = [Horizontal].Center,]                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| [                LabelVerticalAlignment = [Vertical].Middle,]                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [                Shape = [Shapes].Ellipse,]                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [                Height = 50,]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                         |
| [                Width = 50,]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                         |
| [                BackgroundColor = [\"gray\"],]                                                                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [                BorderColor = [\"black\"],]                                                                                                                                               |
|                                                                                                                                                                                                                                                                         |
| [                BorderWidth = 1,]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [            };]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [            [return] node;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [        [public] [LineConnector] AddConnector([Node] headNode, [Node] TailNode,[ string] name)] |
|                                                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                         |
| [            [LineConnector] lineConnector = [new] [LineConnector]()]                                                                         |
|                                                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [                Name=name,]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                         |
| [                HeadNode = headNode,]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [                TailNode = tailNode,]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                         |
| [                ConnectorType = [ConnectorType].Straight,]                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [                LineColor = [\"black\"],]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [                LineWidth = 2]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [            };]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                         |
| [            [return] lineConnector;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                         |
| [        }]                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 118: Directed-Tree Layout

          * *

[]{#related-topics}

