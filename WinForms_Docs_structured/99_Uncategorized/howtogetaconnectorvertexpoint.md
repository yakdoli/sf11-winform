---
title: howtogetaconnectorvertexpoint.md
original_path: WinForms_Docs/99_Uncategorized/howtogetaconnectorvertexpoint.md
created_at: 2025-08-05
---








  









## How to Get a Connector Vertex Point? {#how-to-get-a-connector-vertex-point style="tab-stops: 0pt"}

Connector has a method called GetPoint to get its vertex point.

This method has two parameters: *int* and *bool*[]

[·      ]int specifies the vertex point in the local coordinates

[·      ]bool specifies the path of the connector

Set the bool parameter to True to get the connector vertex point based on its graphical path and False to get the connector point based on its relative path.

The following code snippet illustrates this:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [//LineConnector]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                   |
| [ConnectorBase][ Connector = [new] [LineConnector]([new] Drawing.PointF(0F, 0F), [new] Drawing.PointF(10F, 10F));] |
|                                                                                                                                                                                                                                                                                                   |
| [//set points]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
| [Connector.SetPoints([new] [PointF]\[2\] { Connector.GetPoint(0), Connector.GetPoint(Connector.GetPoints().GetLength(0) - 1, [false]) });]                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\'LineConnector][]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ Connector [As] [ConnectorBase] = [New] [LineConnector]([New] Drawing.[PointF](0.0F, 0.0F), [New] Drawing.[PointF](10.0F, 10.0F))] |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\'set points][]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Connector.SetPoints([New] [PointF](1) {Connector.GetPoint(0), Connector.GetPoint(Connector.GetPoints().GetLength(0) - 1, [False])})]                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

