---
title: portvisibility.md
original_path: WinForms_Docs/99_Uncategorized/portvisibility.md
created_at: 2025-08-05
---








  









### PortVisibility {#portvisibility style="tab-stops: 0pt"}

[] 

[] 

By default the port visibility is set to collapse. So the ports get displayed only on moving the mouse over the respective node or on selecting the node.

 

However to display the ports on the nodes, the **PortVisibility** property can be set to **Visible**.

 

The following code shows how it can be done:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                         |
| [Node][ nodeObject = [new] [Node]([Guid].NewGuid(), [\"Node1\"]);] |
|                                                                                                                                                                                                                                                         |
| [diagramModel.Nodes.Add(nodeObject);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                         |
| [nodeObject.PortVisibility = [Visibility].Visible;]                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [Dim][ nodeObject [As] [New] [Node]([Guid].NewGuid(), [\"Node1\"])] |
|                                                                                                                                                                                                                                                                            |
| [diagramModel.Nodes.Add(nodeObject)]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [nodeObject.PortVisibility = Visibility.Visible][]                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

This displays the ports on the node by default.

 

[]{#p55} 

[]{#related-topics}

