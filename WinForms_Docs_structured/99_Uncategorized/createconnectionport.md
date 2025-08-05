---
title: createconnectionport.md
original_path: WinForms_Docs/99_Uncategorized/createconnectionport.md
created_at: 2025-08-05
---








  









### Create Connection Port {#create-connection-port style="tab-stops: 0pt"}

To add a port to the node, the port\'s position has to be specified using the Left and Top properties. The node which hosts the port should then be specified using the **Node** property. Finally the port should be added to the node\'s Ports collection.

 

The following code shows how to add a connection port to the node.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [Node][ node = [new] [Node]([Guid].NewGuid(), [\"Node1\"]);] |
|                                                                                                                                                                                                                                                   |
| [node.Shape = [Shapes].RoundedSquare;]                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [node.Width = 150;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [node.Height = 50;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [node.OffsetX = 250;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [node.OffsetY = 100;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [ConnectionPort][ port = [new] [ConnectionPort]();]                                                          |
|                                                                                                                                                                                                                                                   |
| [port.Left = 50;]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [port.Top = 0;]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                   |
| [port.Node = node;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [node.Ports.Add(port);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [diagramModel.Nodes.Add(node);]                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [Dim][ node [As] [New] [Node]([Guid].NewGuid(), [\"Node1\"])] |
|                                                                                                                                                                                                                                                                      |
| [node.Shape = Shapes.RoundedSquare]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [node.Width = 150]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [node.Height = 50]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [node.OffsetX = 250]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [node.OffsetY = 100]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [Dim][ port [As] [New] [ConnectionPort]()]                                                                    |
|                                                                                                                                                                                                                                                                      |
| [port.Left = 50]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [port.Top = 0]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [port.Node = node]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [node.Ports.Add(port)]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [diagramModel.Nodes.Add(node)][]                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

This adds a port to the node at the location (50,0) with respect to the node.

[] 

{border="0"}

Figure 94: Connection Port[]

[] 


{border="0"}Note: The ports location should always be specified to be within the node\'s boundary. Therefore the values of the Left and Top property should always be less than the width and height of the node respectively.


 

[]{#p52} 

[]{#related-topics}

