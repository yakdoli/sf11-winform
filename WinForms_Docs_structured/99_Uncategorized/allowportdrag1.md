---
title: allowportdrag1.md
original_path: WinForms_Docs/99_Uncategorized/allowportdrag1.md
created_at: 2025-08-05
---








  









### AllowPortDrag {#allowportdrag style="tab-stops: 0pt"}

It is possible to move the ports on the node to a different location on the node. All that is needed to do is to drag the respective port to the desired location. The connections (if any) which are already connected to the nodes will also get updated accordingly. The node drag can be enabled/disabled using the **AllowPortDrag** property. By default it is set to **False**.

 

The following code shows how to set the **AllowPortDrag** property.

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
| [nodeObject.AllowPortDrag = [true];]                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [Dim][ nodeObject [As] [New] [Node]([Guid].NewGuid(), [\"Node1\"])] |
|                                                                                                                                                                                                                                                                            |
| [diagramModel.Nodes.Add(nodeObject)]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [nodeObject.AllowPortDrag = [True]][]                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

