---
title: linerouting1.md
original_path: WinForms_Docs/99_Uncategorized/linerouting1.md
created_at: 2025-08-05
---








  









### Line Routing {#line-routing style="tab-stops: 0pt"}

[] 

When a link is drawn between two nodes, by enabling the **LineRoutingEnabled** property of that link and the diagram view, and if any other node is found in between them, the line will be automatically re-routed around those nodes.

[] 


  -------------------- ---------------------------------------------------------------------------------------------------------
  Property             Description
  LineRoutingEnabled   Specifies whether the links must be re-routed when nodes are found in the path. Default value is false.
  -------------------- ---------------------------------------------------------------------------------------------------------


[] 

Programmatically it can be set as follows:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [//enabling for model]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [this][.diagram1.Model.LineRoutingEnabled = ][true][;] |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [//enabling for link object]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [link.LineRoutingEnabled = ][true][;]                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                              |
|                                                                                                                                                             |
| []                                                                                                         |
|                                                                                                                                                             |
| [\'enabling for model]                                                                                    |
|                                                                                                                                                             |
| [Me][.diagram1.Model.LineRoutingEnabled = [True]] |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [\'enabling for link object]                                                                              |
|                                                                                                                                                             |
| [link.LineRoutingEnabled = [True].Model.LineBridgeSize = 5]                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note:

In the above code snippet, link refers to the instance of the Link node.

Only when LineRoutingEnabled property is set to true, LineRouter properties will be enabled.


[10.           ][]

Distance and Routing mode settings

[] 

To customize the distance between the connectors and the obstacles, and the type of routing to use, the **LineRouter** collection property should be handled. The below properties are available for the LineRouter Collection property.

**[]** 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Line Router Property              | Description                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| DistanceToObstacle                | Specifies the distance from routing connector to the obstacle.                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| RoutingMode                       | Specifies the type of LineRouting engine routing mode to be used. The default value is \'Inactive\'. The options includes, |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   | Inactive,                                                                                                                  |
|                                   |                                                                                                                            |
|                                   | Automatic and                                                                                                              |
|                                   |                                                                                                                            |
|                                   | SemiAutomatic.                                                                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+


**[]** 

Programmatically it can be set as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                        |
|                                                                                                                                                                            |
| [this][.diagram1.Model.LineRouter.DistanceToObstacles = 20;]            |
|                                                                                                                                                                            |
| [this][.diagram1.Model.LineRouter.RoutingMode = RoutingMode.Automatic;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                          |
|                                                                                                                                                                         |
| []                                                                                                                     |
|                                                                                                                                                                         |
| [Me][.diagram1.Model.LineRouter.DistanceToObstacles = 20]            |
|                                                                                                                                                                         |
| [Me][.diagram1.Model.LineRouter.RoutingMode = RoutingMode.Automatic] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The **LineBridgingEnabled**, **LineRoutingEnabled** properties can be set for the diagram, in which case it will be automatically applied to all the links added to the model. Else it can be enabled only for the required links individually.

[] 

Node settings

[] 

When line routing is enabled make sure to set the **TreatAsObstacle** property of the objects to true, to avoid the links running over them. If not set for an object, then that node will not be considered as an obstacle and the link will pass over it.

[] 

Programmatically it can be set as follows:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                           |
| [circle.TreatAsObstacle = ][true][;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                       |
|                                                                                                                                      |
| []                                                                                  |
|                                                                                                                                      |
| [circle.TreatAsObstacle = ][True] |
+--------------------------------------------------------------------------------------------------------------------------------------+

[] 

In the above code snippets, the TreatAsObstacle property is set to the circle object.

[]{#p29} 

[]{#related-topics}

