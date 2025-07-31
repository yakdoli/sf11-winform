---
title: connectortypes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\connectortypes.md
created_at: 2025-07-03
---








  









### Connector Types {#connector-types style="tab-stops: 0pt"}

The **ConnectorType** property specifies the type of connector that is to be used for the connection.

 

Property

+---------------+---------------------------------------------------------------------------------------------------------------+----------------------+--------------------------+--------------------------------------------------+
| Property      | Description                                                                                                   | Type of the Property | Value it Accepts         | Any Other Dependencies/Sub-Properties Associated |
+===============+===============================================================================================================+======================+==========================+==================================================+
| ConnectorType | Gets or sets the connector type to be used.                                                                   | Dependency property  | ConnectorType.Orthogonal | No                                               |
|               |                                                                                                               |                      |                          |                                                  |
|               | Three values namely Orthogonal, Straight and Bezier can be specified. Default Value: ConnectorType.Orthogonal |                      | ConnectorType.Bezier     |                                                  |
|               |                                                                                                               |                      |                          |                                                  |
|               |                                                                                                               |                      | ConnectorType.Straight   |                                                  |
+---------------+---------------------------------------------------------------------------------------------------------------+----------------------+--------------------------+--------------------------------------------------+

 

Three types are supported. 

[·      ]**Orthogonal** creates a line in which line segments (if any) are placed at right angles to each other.

[·      ]**Bezier** renders a Bezier curve with two points.

[·      ]**Straight** renders a line with two points. 

The default type is orthogonal. 

The following code can be used to change the connector type. 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                               |
|                                                                                                                                                                                                                                            |
| [          LineConnector][ lineConnector = [new] [LineConnector]()] |
|                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [                Name=name,]                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [                HeadNode = headNode,]                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [                TailNode = tailNode,]                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [                **ConnectorType = [ConnectorType].Beizer,**]                                                                                                 |
|                                                                                                                                                                                                                                            |
| [                LineColor = [\"red\"],]                                                                                                                      |
|                                                                                                                                                                                                                                            |
| [                LineWidth = 2]                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [            };]                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 {border="0"}

Figure 62: Beizer Line Connectors

 

                                  * *

{border="0"}

Figure 63: Straight Line Connectors

 

{border="0"}

Figure 64: Orthogonal Line Connectors[]

[]{#related-topics}

