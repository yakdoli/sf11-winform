---
title: treeorientation3.md
original_path: WinForms_Docs/99_Uncategorized/treeorientation3.md
created_at: 2025-08-05
---








  









### Tree Orientation  {#tree-orientation style="tab-stops: 0pt"}

The Layout Manager lets you orient the tree in many directions and can be used for the creation of many sophisticated arrangements. The **Orientation** property of **Diagram Model** can be used to specify the tree orientation. 

Properties

+-------------+-------------------------------+----------------------+---------------------------+--------------------------------------------------+
| Property    | Description                   | Type of the Property | Value it Accepts          | Any Other Dependencies/Sub-Properties Associated |
+-------------+-------------------------------+----------------------+---------------------------+--------------------------------------------------+
| Orientation | Gets or sets the orientation. | CLR Property         | TreeOrientation.LeftRight | No                                               |
|             |                               |                      |                           |                                                  |
|             |                               |                      | TreeOrientation.RightLeft |                                                  |
|             |                               |                      |                           |                                                  |
|             |                               |                      | TreeOrientation.TopBottom |                                                  |
|             |                               |                      |                           |                                                  |
|             |                               |                      | TreeOrientation.BottomTop |                                                  |
+-------------+-------------------------------+----------------------+---------------------------+--------------------------------------------------+

 

The following are the four orientations supported:

 

[·      ]**TopBottom**---Places the root node at the top and the child nodes are arranged below the root node.

[·      ]**BottomTop**---Places the root node at the bottom and the child nodes are arranged above the root node.

[·      ]**LeftRight**---Places the root node at the left and the child nodes are arranged on the right side of the root node.

[·      ]**RightLeft**---Places the root node at the right and the child nodes are arranged on the left side of the root node. 

 

The **RootOffsetX** and **RootOffsetY** properties can be used to specify the position of the root node based on which the entire tree gets generated. 

The tree orientation can be set using the following code: 

More:







