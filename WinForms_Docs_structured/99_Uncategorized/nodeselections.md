---
title: nodeselections.md
original_path: WinForms_Docs/99_Uncategorized/nodeselections.md
created_at: 2025-08-05
---








  









### Node Selections {#node-selections style="tab-stops: 0pt"}

[] 

A node\'s behavior can be customized and modified using the EditStyle collection properties which can be used for the following:

[] 

[·      ]To prohibit selection, rotation and deletion of nodes, by using **AllowSelect**, **AllowRotate** and **AllowDelete** properties.

[·      ]To restrict a node\'s movement along the x or y axis, by using **AllowMoveX** and **AllowMoveY** properties.

[·      ]To prevent re-sizing the height and width of the node, by using **AllowChangeHeight** and **AllowChangeWidth** and **AllowResize** properties.

[] 


  -------------------- -------------------------------------------------------------------------------------------------------------------
  EditStyle Property   Description
  AllowChangeHeight    Specifies whether or not to allow the height to be changed. Default value is ***True***.
  AllowChangeWidth     Specifies whether or not to allow the width to be changed. Default value is ***True***.
  AllowDelete          Specifies whether or not to allow the node to be deleted on clicking the DELETE key. Default value is ***True***.
  AllowMoveX           Specifies whether or not to allow the node to be moved along the x-axis. Default value is ***True***.
  AllowMoveY           Specifies whether or not to allow the node to be moved along the y-axis. Default value is ***True***.
  AllowRotate          Specifies whether or not to rotate the node using the PinPoint. Default value is ***True***.
  AllowSelect          Specifies whether or not to select the node on mouse click. Default value is ***True***.
  -------------------- -------------------------------------------------------------------------------------------------------------------


[] 

Programmatically, the properties can be set as follows:

[] 

+-------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                        |
|                                                                                                       |
| []                                                                |
|                                                                                                       |
| [rect.EditStyle.AllowChangeHeight = [true];] |
|                                                                                                       |
| [rect.EditStyle.AllowChangeWidth = [true];]  |
|                                                                                                       |
| [rect.EditStyle.AllowDelete = [false];]      |
|                                                                                                       |
| [rect.EditStyle.AllowMoveX = [true];]        |
|                                                                                                       |
| [rect.EditStyle.AllowMoveY = [false];]       |
|                                                                                                       |
| [rect.EditStyle.AllowRotate = [true];]       |
|                                                                                                       |
| [rect.EditStyle.AllowSelect = [true];]       |
+-------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                       |
|                                                                                                      |
| []                                                               |
|                                                                                                      |
| [rect.EditStyle.AllowChangeHeight = [True]] |
|                                                                                                      |
| [rect.EditStyle.AllowChangeWidth = [True]]  |
|                                                                                                      |
| [rect.EditStyle.AllowDelete = [False]]      |
|                                                                                                      |
| [rect.EditStyle.AllowMoveX = [True]]        |
|                                                                                                      |
| [rect.EditStyle.AllowMoveY = [False]]       |
|                                                                                                      |
| [rect.EditStyle.AllowRotate = [True]]       |
|                                                                                                      |
| [rect.EditStyle.AllowSelect = [True]]       |
+------------------------------------------------------------------------------------------------------+

**[]** 

In the above code snippets, the properties are set to the Rectangular node (rect) created through the code.

[] 

Behavior Settings

**[]** 


+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  Property                                                                             | Description                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AspectRatio                                                                           | Specifies whether to maintain the height and width ratio when the node is resized.                                                                                                                                                          |
+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DefaultHandleEditMode                                                                 | Specifies the mode in which the node should be handled. The default value for links and lines is Vertex and for all other nodes and polyline the default value is Resize. To move the nodes, DefaultHandleEditMode should be set to Resize. |
|                                                                                       |                                                                                                                                                                                                                                             |
| []  |                                                                                                                                                                                                                                             |
|                                                                                       |                                                                                                                                                                                                                                             |
|                                                                                       | The options provided are as follows.                                                                                                                                                                                                        |
|                                                                                       |                                                                                                                                                                                                                                             |
|                                                                                       | []                                                                                                                                                        |
|                                                                                       |                                                                                                                                                                                                                                             |
|                                                                                       | [·      ]None                                                                                                                                                                                                  |
|                                                                                       |                                                                                                                                                                                                                                             |
|                                                                                       | [·      ]Resize                                                                                                                                                                                                |
|                                                                                       |                                                                                                                                                                                                                                             |
|                                                                                       | [·      ]Vertex                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Enabled                                                                               | Specifies whether the node is enabled. Default value is ***True***.                                                                                                                                                                         |
+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AllowVertexEdit                                                                       | Specifies whether or not to edit the vertex. Default value is ***True***.                                                                                                                                                                   |
+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HidePinPoint                                                                          | Specifies whether to show or hide the PinPoint. Default value is ***False***.                                                                                                                                                               |
+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HideRotationHandle                                                                    | Specifies whether to show or hide the RotationHandle in order to control the rotation of the node. Default value is ***False***.                                                                                                            |
+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Programmatically these properties can be set as follows:

[] 

+--------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                         |
|                                                                                                        |
| []                                                                 |
|                                                                                                        |
| [rect.EditStyle.AspectRatio = [true];]        |
|                                                                                                        |
| [rect.EditStyle.DefaultHandleEditMode =HandleEditMode.Resize;]     |
|                                                                                                        |
| [rect.EditStyle.Enabled = [true];]            |
|                                                                                                        |
| [rect.EditStyle.AllowVertexEdit = [true];]    |
|                                                                                                        |
| [rect.EditStyle.DefaultHandleEditMode =HandleEditMode.Vertex;]     |
|                                                                                                        |
| [rect.EditStyle.HidePinPoint = [true];]       |
|                                                                                                        |
| [rect.EditStyle.HideRotationHandle = [true];] |
+--------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                        |
|                                                                                                       |
| **[]**                                              |
|                                                                                                       |
| [rect.EditStyle.AspectRatio = [True]]        |
|                                                                                                       |
| [rect.EditStyle.DefaultHandleEditMode = HandleEditMode.Resize]    |
|                                                                                                       |
| [rect.EditStyle.Enabled = [True]]            |
|                                                                                                       |
| [rect.EditStyle.AllowVertexEdit = [True]]    |
|                                                                                                       |
| [rect.EditStyle.DefaultHandleEditMode = HandleEditMode.Vertex]    |
|                                                                                                       |
| [rect.EditStyle.HidePinPoint = [True]]       |
|                                                                                                       |
| [rect.EditStyle.HideRotationHandle = [True]] |
+-------------------------------------------------------------------------------------------------------+

**[]** 

In the above code snippets, the properties are set to the Rectangular node (rect) created through the code.

**[         ]**

{border="0"}

**[]** 

Figure 64: Default Handle Edit Mode

**[]** 

{border="0"}

**[]** 

Figure 65: Default Handle Edit mode with Resize

**[]** 

{border="0"}

**[]** 

Figure 66: Pinpoint and Rotation Handle

**[]** 

{border="0"}

**[]** 

Figure 67: Hide Point and Rotation Handle

[]{#p43}[] 

[]{#related-topics}

