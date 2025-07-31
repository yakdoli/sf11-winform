---
title: automaticlayout1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\automaticlayout1.md
created_at: 2025-07-03
---








  









## Automatic Layout {#automatic-layout style="tab-stops: 0pt"}

[] 

Essential Diagram Silverlight allows the user to specify automatic layouts for the nodes. The following layout types are available:

[·      ]Directed-Tree layout

[·      ]Hierarchical-Tree layout

[·      ]Radial-Tree layout and

[·      ]Table layout

[] 

Properties

**[]** 

+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+
| Property                    | Description                                                                                                                                                                                                                                    | Type of the property | Value it accepts          | Any other dependencies/ sub properties associated |
+=============================+================================================================================================================================================================================================================================================+======================+===========================+===================================================+
| VerticalSpacing             | Gets or sets the Vertical spacing between nodes.                                                                                                                                                                                               | CLR Property         | Double                    | No                                                |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+
| HorizontalSpacing           | Gets or sets the Horizontal spacing between nodes.                                                                                                                                                                                             | CLR Property         | Double                    | No                                                |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+
| SpaceBetweenSubTrees        | Gets or sets the space between sub trees.                                                                                                                                                                                                      | CLR Property         | Double                    | No                                                |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+
| Orientation                 | Gets or sets the orientation.                                                                                                                                                                                                                  | CLR Property         |                           | No                                                |
|                             |                                                                                                                                                                                                                                                |                      |                           |                                                   |
|                             |                                                                                                                                                                                                                                                |                      | TreeOrientation.LeftRight |                                                   |
|                             |                                                                                                                                                                                                                                                |                      |                           |                                                   |
|                             |                                                                                                                                                                                                                                                |                      | TreeOrientation.RightLeft |                                                   |
|                             |                                                                                                                                                                                                                                                |                      |                           |                                                   |
|                             |                                                                                                                                                                                                                                                |                      | TreeOrientation.TopBottom |                                                   |
|                             |                                                                                                                                                                                                                                                |                      |                           |                                                   |
|                             |                                                                                                                                                                                                                                                |                      | TreeOrientation.BottomTop |                                                   |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+
| EnableCycleDetection        | Gets or sets a value indicating whether Cycle detection is enabled or not.                                                                                                                                                                     | DependencyProperty   | Boolean                   | No                                                |
|                             |                                                                                                                                                                                                                                                |                      |                           |                                                   |
|                             |                                                                                                                                                                                                                                                |                      | true/ false               |                                                   |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+
| TableExpandMode             | Gets or sets the table expand mode.                                                                                                                                                                                                            | DependencyProperty   | ExpandMode.Horizontal     | No                                                |
|                             |                                                                                                                                                                                                                                                |                      |                           |                                                   |
|                             |                                                                                                                                                                                                                                                |                      | ExpandMode.Vertical       |                                                   |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+
| RowCount                    | Gets or sets the Row Count for the table layout.                                                                                                                                                                                               | DependencyProperty   | int                       | No                                                |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+
| ColumnCount                 | Gets or sets the Column Count for the table layout.                                                                                                                                                                                            | DependencyProperty   | int                       | No                                                |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+
| EnableLayoutWithVariedSizes | Gets or sets a value indicating whether to enable the varied size algorithm. In case the Model consists of nodes of different sizes, this property can be set to true. This will align the differently sized nodes with respect to the center. | DependencyProperty   | Boolean (true/ false)     | No                                                |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+
| Bounds                      | Gets or sets the bounds value which specifies the position of the root node in case of a tree layout.                                                                                                                                          | CLR Property         | Thickness                 | No                                                |
+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+---------------------------+---------------------------------------------------+

[] 

[] 

Directed-Tree Layout

The Directed-Tree Layout automatically arranges nodes in a tree-like structure. This enables the user to position nodes in a tree-like fashion without specifying the coordinate location for each node. However, it is necessary to specify a layout root for the tree layout. The Directed-Tree layout will position the nodes based on the layout root.

Hierarchical-Tree Layout

**[]** 

The Hierarchical Tree Layout arranges nodes in a tree-like structure, where the nodes in hierarchical layout may have multiple parents. As a result, there is no need to specify the layout root.

[] 

Radial-Tree Layout

The Radial-Tree Layout Manager arranges nodes in a circular layout and positions the root-node at the center of the graph and child-nodes in a circular fashion around the root. Sub-trees formed by the branching of the child-node are located radially around the child-node. **[]**

Table Layout

**[]** 

Table layout is a layout manager that arranges the nodes in rows and column basis. The number of nodes in each row and column can be specified and the layout will take place accordingly.

More:













