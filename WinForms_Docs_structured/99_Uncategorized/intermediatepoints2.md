---
title: intermediatepoints2.md
original_path: WinForms_Docs/99_Uncategorized/intermediatepoints2.md
created_at: 2025-08-05
---






##### Intermediate Points {#intermediate-points style="tab-stops: 0pt"}

Adding Intermediate Points

Intermediate points can be added in two ways:

[·    ]Using CTRL + SHIFT keys

[·    ]Through code behind

Intermediate points can be added at run time by holding CTRL + SHIFT and clicking on the line. Intermediate points can be added programmatically. The following code snippet illustrates the addition of intermediate lines.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                            |
|                                                                                                                                                                 |
|                                                                                                                                                                 |
|                                                                                                                                                                 |
| [            [LineConnector] lc = [new] [LineConnector]();] |
|                                                                                                                                                                 |
| [            lc.ConnectorType = [ConnectorType].Straight;]                                               |
|                                                                                                                                                                 |
| [            lc.StartPoint = [new] [DiagramPoint](100, 100);]                       |
|                                                                                                                                                                 |
| [            lc.EndPoint = [new] [DiagramPoint](300, 300);]                         |
|                                                                                                                                                                 |
| [            lc.IntermediatePoints.Add([new] [DiagramPoint](200, 100));]            |
|                                                                                                                                                                 |
| [            lc.IntermediatePoints.Add([new] [DiagramPoint](200, 300));]            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}[]

Figure 67: Adding Intermediate Points

[] 

Modifying Intermediate Points

Intermediate points can be modified in two ways:

[·      ][Dragging the vertex]

[·      ][Through code behind]

Intermediate points can be modified at run time by clicking and dragging the vertex of the line connector. Intermediate points can be modified programmatically also. The following code snippet illustrates the modification of intermediate lines.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                            |
|                                                                                                                                                                 |
|                                                                                                                                                                 |
|                                                                                                                                                                 |
| [            [LineConnector] lc = [new] [LineConnector]();] |
|                                                                                                                                                                 |
| [            lc.ConnectorType = [ConnectorType].Straight;]                                               |
|                                                                                                                                                                 |
| [            lc.StartPoint = [new] [DiagramPoint](100, 100);]                       |
|                                                                                                                                                                 |
| [            lc.EndPoint = [new] [DiagramPoint](300, 300);]                         |
|                                                                                                                                                                 |
| [            lc.IntermediatePoints.Add([new] [DiagramPoint](200, 100));]            |
|                                                                                                                                                                 |
| [            lc.IntermediatePoints.Add([new] [DiagramPoint](200, 300));]            |
|                                                                                                                                                                 |
| [            lc.IntermediatePoints\[1\] = [new] [DiagramPoint](200, 200);]          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

Figure 68: Modifying Intermediate Points

[] 

Delete Intermediate Points

Intermediate points can be deleted in two ways:

[·      ][Using CTRL + SHIFT keys]

[·      ][Through code behind]

Intermediate points can be deleted by holding CTRL + SHIFT and clicking on the vertex that represents the intermediate point to be deleted. Intermediate points can be deleted programmatically also. The following code snippet illustrates deletion of intermediate lines.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                            |
|                                                                                                                                                                 |
|                                                                                                                                                                 |
|                                                                                                                                                                 |
| [            [LineConnector] lc = [new] [LineConnector]();] |
|                                                                                                                                                                 |
| [            lc.ConnectorType = [ConnectorType].Straight;]                                               |
|                                                                                                                                                                 |
| [            lc.StartPoint = [new] [DiagramPoint](100, 100);]                       |
|                                                                                                                                                                 |
| [            lc.EndPoint = [new] [DiagramPoint](300, 300);]                         |
|                                                                                                                                                                 |
| [            lc.IntermediatePoints.Add([new] [DiagramPoint](200, 100));]            |
|                                                                                                                                                                 |
| [            lc.IntermediatePoints.Add([new] [DiagramPoint](200, 300));]            |
|                                                                                                                                                                 |
| [            lc.IntermediatePoints.RemoveAt(1);]                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 69: Deleting Intermediate Points

 

 

[]{#related-topics}

