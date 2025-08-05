---
title: linebridging1.md
original_path: WinForms_Docs/99_Uncategorized/linebridging1.md
created_at: 2025-08-05
---








  









### Line Bridging {#line-bridging style="tab-stops: 0pt"}

**[\
]**Table 42: Property Table**[]**

  --------------------- ------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------
  Property              Description                                                         Type of the property   Value it accepts        Any other dependencies/ sub properties associated
  LineBridgingEnabled   Gets or sets a value indicating whether line bridging is enabled.   Dependency property    Boolean (true/ false)   No
  --------------------- ------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------

 

Line Bridging creates a bridge for lines to smartly cross over other line at points of intersection.

When two line connectors meets each other, line with higher z-order will draw an arc over the line with lower z-order.

Only Straight and Orthogonal Connector type supports line bridging.

[] 

{border="0"}

Figure 92: Line Bridge

 

Enabling Line Bridging for LineConnector

LineBridging for a line connector can be enabled using the **LineBridgingEnabled** property.

By default this property will be set to False.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [LineConnector][ lc = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [lc.ConnectorType = [ConnectorType].Straight;]                                                                           |
|                                                                                                                                                                                      |
| [lc.LineBridgingEnabled = [true];]                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ lc [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [lc.ConnectorType = ConnectorType.Straight]                                                                                                                |
|                                                                                                                                                                                                |
| [lc.LineBridgingEnabled = [True]]                                                                                                     |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The line bridge is enabled.

[] 

Disable LineBridging from DiagramModel

When LineBridging for DiagramModel is disabled, LineBridging for all the lines will be disabled. You can change this binding by specifying a value for an individual LineConnector.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [DiagramModel][ model = [new] [DiagramModel]();] |
|                                                                                                                                                                                       |
| [model.LineBridgingEnabled = [false];]                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [Dim][ model [As] [New] [DiagramModel]()] |
|                                                                                                                                                                                                  |
| [model.LineBridgingEnabled = [False]]                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The line bridge is disabled completely.

[]{#related-topics}

