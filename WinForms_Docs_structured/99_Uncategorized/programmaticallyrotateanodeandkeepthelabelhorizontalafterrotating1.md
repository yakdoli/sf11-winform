---
title: programmaticallyrotateanodeandkeepthelabelhorizontalafterrotating1.md
original_path: WinForms_Docs/99_Uncategorized/programmaticallyrotateanodeandkeepthelabelhorizontalafterrotating1.md
created_at: 2025-08-05
---








  









### Programmatically Rotate a Node and Keep the Label Horizontal after Rotating {#programmatically-rotate-a-node-and-keep-the-label-horizontal-after-rotating style="tab-stops: 0pt"}

Node can be programmatically rotated and the Label can be kept horizontal after rotation using the following code snippet.\
\

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                       |
|                                                                                                                                                                            |
| [Node ][NewClient = new [Node]();[]] |
|                                                                                                                                                                            |
| [NewClient.][Shape = [Shapes].FlowChart_Card;]               |
|                                                                                                                                                                            |
| [diagramModel.Nodes.Add(NewClient);]                                                                                                   |
|                                                                                                                                                                            |
| []                                                                                                                       |
|                                                                                                                                                                            |
| [double][ angle = 90;]                                                                |
|                                                                                                                                                                            |
| [NewClient.RenderTransform = [new] [RotateTransform](angle);]                             |
|                                                                                                                                                                            |
| [NewClient.Label = [\"90 deg rotation\"];]                                                                     |
|                                                                                                                                                                            |
| [NewClient.RenderTransformOrigin = [new] System.Windows.[Point](0.5, 0.5);]               |
|                                                                                                                                                                            |
| [NewClient.LabelAngle = 360 - angle;]                                                                                                  |
|                                                                                                                                                                            |
| []                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [Dim][ NewClient [As] [New] [Node]()] |
|                                                                                                                                                                                              |
| [NewClient.Shape = Shapes.FlowChart_Card]                                                                                                                |
|                                                                                                                                                                                              |
| [diagramModel.Nodes.Add(NewClient)]                                                                                                                      |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [Dim][ angle [As] [Double] = 90]                              |
|                                                                                                                                                                                              |
| [NewClient.RenderTransform = [New] RotateTransform(angle)]                                                                          |
|                                                                                                                                                                                              |
| [NewClient.Label = \"90 deg rotation\"]                                                                                                                  |
|                                                                                                                                                                                              |
| [NewClient.RenderTransformOrigin = [New] System.Windows.Point(0.5, 0.5)]                                                            |
|                                                                                                                                                                                              |
| [NewClient.LabelAngle = 360 - angle][]                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Here diagramModel is an instance of DiagramModel.

 

[]{#related-topics}

