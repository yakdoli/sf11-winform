---
title: resizingthroughtheresizehandle1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\resizingthroughtheresizehandle1.md
created_at: 2025-07-03
---






#### Resizing through the Resize handle {#resizing-through-the-resize-handle style="tab-stops: 0pt"}

Resizing a node affects the node\'s width and height. To resize a node, follow the steps below.

[] 

[·      ]Select the node that is to be resized.

[·      ]Move the pointer to the edge that you want to resize.

[·      ]The cursor will change to one with two arrows.

[·      ]Now drag the edge to the size you want. The node\'s height and width will correspondingly change.

 

{border="0"}

Figure 36: Node Resizing Illustrated[]

[] 

To resize both the width and height by the same factor, click and drag the corners of the resize adorner.

[]{#p26} 

[]{#_How_to_Rotate}AllowResize

The **AllowResize** property can be used to enable/disable the node resizing.\
\
When this property is set to **True**, it is possible to resize the node. Otherwise the node cannot be resized.\
The default value is **True**.

 

The **AllowResize** property can be set in the following way.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| [\                                                                                                                                                                                                                            |
| ][Node][ nodeobject = [new] [Node]();] |
|                                                                                                                                                                                                                               |
| [nodeobject.AllowResize = [false];]                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| [\                                                                                                                                                                                                                                               |
| ][Dim][ nodeobject [As] [New] [Node]()] |
|                                                                                                                                                                                                                                                  |
| [nodeobject.AllowResize = [False]][]                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

