---
title: noderotate1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\noderotate1.md
created_at: 2025-07-03
---








  









### Node Rotate {#node-rotate style="tab-stops: 0pt"}

A node can be rotated to any angle by dragging the rotate thumb. A node always rotates on its center.

[] 

Table 20: Property Table []

  ------------- ------------------------------------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------
  Property      Description                                                                                             Type of the property   Value it Accept         Any other dependencies/ sub properties associated
  AllowRotate   Gets or sets a value indicating whether node can be rotated or not. The default value is set to True.   Dependency property    Boolean (true/ false)   No[]
  ------------- ------------------------------------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------

[] 

Rotate Node

[] 

The steps to rotate a node are as follows.

[] 

[·      ]Select the node to be rotated. The rotate thumb will be displayed in the top left corner.

[·      ]Click the rotate thumb and drag it clockwise or counterclockwise; the node will rotate correspondingly.

[] 

{border="0"}

Figure 33: Node Rotation[]

[]{#p27} 

**AllowRotate\
\**

The AllowRotate property can be used to enable/disable rotation of the node.\
\

Node rotation is enabled when this property is set to True. Otherwise the rotation is disabled. The default value is True.

 

The AllowRotate property can be set in the following way.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]\                                                                                                                                                                                                                    |
| ]**[\                                                                                                                                                                       |
| ][Node][ nodeobject = [new] [Node]();] |
|                                                                                                                                                                                                                               |
| [nodeobject.AllowRotate = [false];]                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []{#p33}**[\[VB\]\                                                                                                                                                                                                                               |
| ]**[\                                                                                                                                                                                          |
| ][Dim][ nodeobject [As] [New] [Node]()] |
|                                                                                                                                                                                                                                                  |
| [nodeobject.AllowRotate = [False]][]                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Rotation through Codebehind

Rotate angle property enables the rotation of the selected object with a specified angle. It enables the support to rotate all the selected Nodes.

 

Table 21: Property Table []

+-------------+------------------------------------------+----------------------+------------------+---------------------------------------------------+
| Property    | Description                              | Type of the property | Value it accepts | Any other dependencies/ sub properties associated |
+-------------+------------------------------------------+----------------------+------------------+---------------------------------------------------+
| RotateAngle | Gets or sets the angle for the Rotation. | Dependency property  | Double           | No                                                |
|             |                                          |                      |                  |                                                   |
|             |                                          |                      |                  |                                                   |
+-------------+------------------------------------------+----------------------+------------------+---------------------------------------------------+
|             |                                          |                      |                  |                                                   |
+-------------+------------------------------------------+----------------------+------------------+---------------------------------------------------+
|             |                                          |                      |                  |                                                   |
+-------------+------------------------------------------+----------------------+------------------+---------------------------------------------------+
|             |                                          |                      |                  |                                                   |
+-------------+------------------------------------------+----------------------+------------------+---------------------------------------------------+

 

After Rotating the Node:

{border="0"}

Figure 34: RotateAngle with 60 degree

 

After rotating the Group

 

{border="0"}

Figure 35: RotateAngle with 180 degree

 

 

[]{#related-topics}

