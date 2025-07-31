---
title: directedtreelayoutmanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\directedtreelayoutmanager.md
created_at: 2025-07-03
---






#### Directed Tree Layout Manager {#directed-tree-layout-manager style="tab-stops: 0pt"}

[] 

The Directed Tree Layout Manager implements a layout manager for arranging nodes in a tree-like structure. This Layout manager can be applied to any diagram that is composed of a directed tree graph with unique root and child nodes. The layout manager lets you orient the tree in any direction around the root and can be used for creating arrangements such as top-to-bottom vertical trees, bottom-to-top vertical trees, right-to-left horizontal trees, left-to-right horizontal trees, angular trees etc.

 

The **DirectedTreeLayoutManager** class is a subclass of the **GraphLayoutManager** and implements a layout manager for arranging nodes in a tree-like structure. The tree layout can be applied to any diagram that is composed as a directed tree graph with a unique root and child nodes. The layout manager lets you orient the tree in just about any direction around the root and can be used for creating arrangements such as top-to-bottom vertical trees, bottom-to-top vertical trees, right-to-left horizontal trees, left-to-right horizontal trees, angular trees and so on.

 

Graph orientation is determined by the rotation degree parameter while initializing the layout manager. A rotation degree of 0° specifies a top-to-bottom vertical tree while a rotation degree of 270° will result in a left-to-right horizontal tree layout.

 

The parameters to be defined for the DirectedTreeLayoutManager class are listed in the below table.

[] 


  ------------------- ----------------------------------------------------------------------------------------------
  Property            Description
  Model               Represents the model of the diagram, which has to be displayed out as a directed tree.
  RotationAngle       Gets or sets the rotation angle for the graph. It accepts only integer values between 0-360.
  HorizontalSpacing   Holds the value for the horizontal offset between adjacent nodes (float value).
  VerticalSpacing     Holds the value for the vertical offset between adjacent nodes (float value).
  ------------------- ----------------------------------------------------------------------------------------------


[] 

Programmatically, the directed tree layout manager instance is created with the respective arguments, assigned to the Layout Manager and updated as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [DirectedTreeLayoutManager directedLayout = [new]  DirectedTreeLayoutManager(diagram1.Model,0, 20, 20);] |
|                                                                                                                                                                   |
| [diagram1.LayoutManager = directedLayout;]                                                                                    |
|                                                                                                                                                                   |
| [diagram1.LayoutManager.UpdateLayout([null]);]                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                    |
|                                                                                                                                                                   |
| **[]**                                                                                                          |
|                                                                                                                                                                   |
| [DirectedTreeLayoutManager directedLayout = [new]  DirectedTreeLayoutManager(diagram1.Model,0, 20, 20);] |
|                                                                                                                                                                   |
| [diagram1.LayoutManager = directedLayout;]                                                                                    |
|                                                                                                                                                                   |
| [diagram1.LayoutManager.UpdateLayout(null);]                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Sample Diagrams are as follows.

**[]** 

{border="0"}

 

Figure 50: Top-to-Bottom Directed Tree Layout with 0 degree Rotation Angle

**[]** 

{border="0"}

**[]** 

Figure 51: Bottom-to-Top Directed Tree Layout with 180 degree Rotation Angle

**[]** 

{border="0"}

**[]** 

Figure 52: Left-to-Right with 270 degree Rotation Angle

**[]** 

{border="0"}

**[]** 

Figure 53: Right-to- Left with 90 degree Rotation Angle

 

[]{#p34} 

 

[]{#related-topics}

