---
title: noderotate.md
original_path: WinForms_Docs/99_Uncategorized/noderotate.md
created_at: 2025-08-05
---








  









### Node Rotate {#node-rotate style="tab-stops: 0pt"}

[] 

A node can be rotated to any angle by dragging the rotate thumb. A node always rotates on its center.

[] 

Properties[]

[] 

  ------------- --------------------------------------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------
  Property      Description                                                                                               Type of the property   Value it Accept         Any other dependencies/ sub properties associated
  AllowRotate   Gets or sets a value indicating whether a node can be rotated or not. The default value is set to true.   Dependency property    Boolean (true/ false)   No[]
  ------------- --------------------------------------------------------------------------------------------------------- ---------------------- ----------------------- ---------------------------------------------------

[] 

Rotate Node

[] 

The steps to rotate a node are:

[] 

1.   Select the node to be rotated. The rotate thumb will be displayed in the top left corner.

2.   Click the rotate thumb and drag it clockwise or counterclockwise. The node will rotate correspondingly.

[] 

{border="0"}

Figure 32: Node Rotation**[]**

[] 

[] 

[]{#p27} 

[AllowRotate]{#AllowRotate}\
\

The **AllowRotate** property can be used to enable/disable rotation of the node.\
\
When this property is set to **true**, node rotation is enabled. Otherwise the rotation is disabled. The default value is **true**.

 

The AllowRotate property can be set in the following way:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]\                                                                                                                                                                                                                    |
| ]**[\                                                                                                                                                                       |
| ][Node][ nodeobject = [new] [Node]();] |
|                                                                                                                                                                                                                               |
| [nodeobject.AllowRotate = [false];]                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]\                                                                                                                                                                                                                                       |
| ]**[\                                                                                                                                                                                          |
| ][Dim][ nodeobject [As] [New] [Node]()] |
|                                                                                                                                                                                                                                                  |
| [nodeobject.AllowRotate = [False]][]                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p33}Rotation through Codebehind

Rotate angle property enables the rotation of the selected object with a specified angle. It enables the support to rotate all the selected Nodes.

+-------------+------------------------------------------+----------------------+------------------+---------------------------------------------------+
| Property    | Description                              | Type of the property | Value it accepts | Any other dependencies/ sub properties associated |
+-------------+------------------------------------------+----------------------+------------------+---------------------------------------------------+
| RotateAngle | Gets or sets the angle for the Rotation. | Dependency property  | Double           | No                                                |
|             |                                          |                      |                  |                                                   |
|             |                                          |                      |                  |                                                   |
+-------------+------------------------------------------+----------------------+------------------+---------------------------------------------------+

 

After Rotating the Node:

{border="0"}

Figure 33: RotateAngle with 60 degree

 

After Rotating the Group

 

{border="0"}

Figure 34: RotateAngle with 180 degree

 

[]{#related-topics}

