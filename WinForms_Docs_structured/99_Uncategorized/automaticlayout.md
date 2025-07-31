---
title: automaticlayout.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\automaticlayout.md
created_at: 2025-07-03
---








  









## Automatic Layout  {#automatic-layout style="MARGIN-BOTTOM: 12pt; tab-stops: 0pt"}

Essential Diagram for MVC allows the user to specify automatic layouts for the nodes. The directed tree layout type is available:

 

Properties 

+----------------------+----------------------------------------------------------------------------------------------------------------+----------------------+----------------------------+--------------------------------------------------+
| Property             | Description                                                                                                    | Type of the Property | Value it Accepts           | Any Other Dependencies/Sub-Properties Associated |
+======================+================================================================================================================+======================+============================+==================================================+
| VerticalSpacing      | Gets or sets the vertical spacing between nodes.                                                               | CLR Property         | Double                     | No                                               |
+----------------------+----------------------------------------------------------------------------------------------------------------+----------------------+----------------------------+--------------------------------------------------+
| HorizontalSpacing    | Gets or sets the horizontal spacing between nodes.                                                             | CLR Property         | Double                     | No                                               |
+----------------------+----------------------------------------------------------------------------------------------------------------+----------------------+----------------------------+--------------------------------------------------+
| SpaceBetweenSubTrees | Gets or sets the space between sub-trees.                                                                      | CLR Property         | Double                     | No                                               |
+----------------------+----------------------------------------------------------------------------------------------------------------+----------------------+----------------------------+--------------------------------------------------+
| Orientation          | Gets or sets the orientation.                                                                                  | CLR Property         |  TreeOrientation.LeftRight | No                                               |
|                      |                                                                                                                |                      |                            |                                                  |
|                      |                                                                                                                |                      | TreeOrientation.RightLeft  |                                                  |
|                      |                                                                                                                |                      |                            |                                                  |
|                      |                                                                                                                |                      | TreeOrientation.TopBottom  |                                                  |
|                      |                                                                                                                |                      |                            |                                                  |
|                      |                                                                                                                |                      | TreeOrientation.BottomTop  |                                                  |
+----------------------+----------------------------------------------------------------------------------------------------------------+----------------------+----------------------------+--------------------------------------------------+
| RootOffsetX          | Gets or sets the RootOffsetX value which specifies the position of the root node in the case of a tree layout. | CLR Property         | Double                     | No                                               |
+----------------------+----------------------------------------------------------------------------------------------------------------+----------------------+----------------------------+--------------------------------------------------+
| RootOffsetY          | Gets or sets the RootOffsetY value which specifies the position of the root node in the case of a tree layout. | CLR Property         | Double                     | No                                               |
+----------------------+----------------------------------------------------------------------------------------------------------------+----------------------+----------------------------+--------------------------------------------------+

 

More:









