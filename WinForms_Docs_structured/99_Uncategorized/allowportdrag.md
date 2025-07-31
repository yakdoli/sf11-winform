---
title: allowportdrag.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\allowportdrag.md
created_at: 2025-07-03
---








  









### AllowPortDrag {#allowportdrag style="tab-stops: 0pt"}

[] 

It is possible to move the ports on the node to a different location on the node. All that is needed to do is to drag the respective port to the desired location. The connections (if any) which are already connected to the nodes are also updated accordingly. The node drag can be enabled/disabled using the AllowPortDrag property. By default it is set to **false**.

 

The following code shows the setting of the **AllowPortDrag** property:

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

 

[]{#p56} 

[]{#related-topics}

