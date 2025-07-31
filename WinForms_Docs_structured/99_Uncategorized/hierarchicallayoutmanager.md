---
title: hierarchicallayoutmanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\hierarchicallayoutmanager.md
created_at: 2025-07-03
---






#### Hierarchical Layout Manager {#hierarchical-layout-manager style="tab-stops: 0pt"}

[] 

Hierarchical layout manager arranges the nodes in a hierarchical fashion depending on the parent-child relationship. Unlike the directed layout, more than one parent item can be defined for a child.

[] 

The parameters to be passed for the **HierarchicalLayoutManager** class are as follows:

[] 


  ------------------- ----------------------------------------------------------------------------------------
  Property            Description
  Model               Represents the model of the diagram, which has to be displayed out as a directed tree.
  RotationAngle       Defines the Graph Rotation angle. It accepts only integer values between 0-360.
  HorizontalSpacing   Holds the value for the horizontal offset between adjacent nodes (float value).
  VerticalSpacing     Holds the value for the vertical offset between adjacent nodes (float value).
  ------------------- ----------------------------------------------------------------------------------------


[] 

Programmatically, the hierarchical layout manager instance should be created with the respective arguments, assigned to the Layout Manager and updated as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                                 |
| **[]**                                                                                                        |
|                                                                                                                                                                 |
| [HierarchicLayoutManager hierarchyLayout = [new] HierarchicLayoutManager (diagram1.Model, 0, 10, 20);] |
|                                                                                                                                                                 |
| [this][.diagram1.LayoutManager = hierarchyLayout;]                         |
|                                                                                                                                                                 |
| [this][.diagram1.LayoutManager.UpdateLayout([null]);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                             |
|                                                                                                                                                                                                                      |
| [Dim][ hierarchyLayout [As] [New] HierarchicLayoutManager(diagram1.Model, 0, 10, 20)] |
|                                                                                                                                                                                                                      |
| [Me][.diagram1.LayoutManager = hierarchyLayout]                                                                                 |
|                                                                                                                                                                                                                      |
| [Me][.diagram1.LayoutManager.UpdateLayout([Nothing])]                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample diagrams are as follows:

[] 

{border="0"}

**[]** 

Figure 58: Top-to-Bottom Hierarchical Tree Layout

**[]** 

{border="0"}

**[]** 

Figure 59: Bottom-to-Top Hierarchical Tree Layout

 

[]{#p37} 

 

[]{#related-topics}

