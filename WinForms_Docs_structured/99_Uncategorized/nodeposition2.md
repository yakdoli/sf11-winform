---
title: nodeposition2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nodeposition2.md
created_at: 2025-07-03
---








  









### Node Position {#node-position style="tab-stops: 0pt"}

The node\'s location on the drawing area can be manually specified using the node\'s **OffsetX** and **OffsetY** properties.

 

Table 19: Property Table**[]**

  ----------- ----------------------------------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------
  Property    Description                                                                                           Type of the property   Value it Accept         Any other dependencies/ sub properties associated
  OffsetX     Gets or sets the offset x value of the node.                                                          CLR property           double                  No
  OffsetY     Gets or sets the offset y value of the node.                                                          CLR property           double                  No
  AllowMove   Gets or sets a value indicating whether node can be moved or not. The default value is set to true.   Dependency property    Boolean (true/ false)   No
  ----------- ----------------------------------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------

[] 


{border="0"} Note:[ ]There are two more properties called LogicalOffsetX and LogicalOffsetY which is used only for internal calculations and they do not support negative values,.So use only OffsetX and OffsetY property.


[] 

Specify node's location

Node's location can be changed in following two ways:

[] 

[·      ]At Runtime

[·      ]Through Code Behind

[] 

At Runtime

Node's location can be changed at run time by clicking and dragging the Node. To change the node's location, follow the steps below.

[] 

[·      ]Select the node that is to be dragged to change its location.

[·      ]Move the pointer and place it on the Node.

[·      ]The cursor will change to a four sided Arrow cursor.

[·      ]Now click and drag the node to the change the node's location. The node\'s OffsetX and OffsetY values will correspondingly change.

[] 

Through Code Behind

Node's location can be changed using the following code snippet.

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Node][ n = [new] [Node]();] |
|                                                                                                                                                                   |
| [n.OffsetX = 50;]                                                                                                             |
|                                                                                                                                                                   |
| [n.OffsetY = 50;]                                                                                                             |
|                                                                                                                                                                   |
| [n.Shape = [Shapes].FlowChart_Card;]                                                                  |
|                                                                                                                                                                   |
| [diagramModel.Nodes.Add(n);]                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Dim][ n [As] [New] [Node]()] |
|                                                                                                                                                                                      |
| [n.OffsetX = 50]                                                                                                                                 |
|                                                                                                                                                                                      |
| [n.OffsetY = 50]                                                                                                                                 |
|                                                                                                                                                                                      |
| [n.Shape = Shapes.FlowChart_Card]                                                                                                                |
|                                                                                                                                                                                      |
| [diagramModel.Nodes.Add(n)][]                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The node will be placed at the point: 50, 50.

[] 


{border="0"} Note:[ ]To dynamically change the position of the node, specify the offset values and call the InvalidateMeasure() of the DiagramPage as follows:


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                     |
|                                                                                                                                                                                    |
| []                                                                                                                               |
|                                                                                                                                                                                    |
| [nodeobj.OffsetX = 100;]                                                                                                                       |
|                                                                                                                                                                                    |
| [nodeobj.OffsetY = 100;]                                                                                                                       |
|                                                                                                                                                                                    |
| [DiagramPage][ page = [new] [DiagramPage]();] |
|                                                                                                                                                                                    |
| [page = diagramView.Page [as] [DiagramPage];]                                                     |
|                                                                                                                                                                                    |
| [page.InvalidateMeasure();]                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [nodeobj.OffsetX = 100]                                                                                                                                    |
|                                                                                                                                                                                                |
| [nodeobj.OffsetY = 100]                                                                                                                                    |
|                                                                                                                                                                                                |
| [Dim][ page [As] [New] [DiagramPage]()] |
|                                                                                                                                                                                                |
| [page = [TryCast](diagramView.Page, DiagramPage)]                                                                                     |
|                                                                                                                                                                                                |
| [page.InvalidateMeasure()][]                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In the above code, nodeobj refers to the instance of the node whose position is to be changed.

 

[]{#p24}[]{#_How_to_Resize}AllowMove

The **AllowMove** property can be used to enable/disable the node drag option.\
\
When this property is set to **True**, it is possible to move the node. Otherwise the node cannot be moved.\
The default value is **True**.

 

The **AllowMove** property can be set in the following way:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| [\                                                                                                                                                                                                                            |
| ][Node][ nodeobject = [new] [Node]();] |
|                                                                                                                                                                                                                               |
| [nodeobject.AllowMove = [false];]                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| [\                                                                                                                                                                                                                                               |
| ][Dim][ nodeobject [As] [New] [Node]()] |
|                                                                                                                                                                                                                                                  |
| [nodeobject.AllowMove = [False]][]                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

