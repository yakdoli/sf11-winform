---
title: symmetriclayoutmanager.md
original_path: WinForms_Docs/99_Uncategorized/symmetriclayoutmanager.md
created_at: 2025-08-05
---






#### Symmetric Layout Manager {#symmetric-layout-manager style="tab-stops: 0pt"}

[] 

The Symmetric layout manager arranges all the nodes in a symmetric fashion using the vertical input distance, which specifies the distance between the nodes.

 

The Model and Vertical Distance values are passed as parameters to the **SymmetricLayoutManager** class. The parameters and properties of Symmetric Layout Manager is listed below.

 


  ------------------ ----------------------------------------------------------------------------------------
  Property           Description
  Model              Represents the model of the diagram, which has to be displayed out as a directed tree.
  VerticalDistance   Defines the Graph Rotation angle. It accepts only integer values between 0 - 360.
  SpringFactor       Gets or sets the spring factor.
  SpringLength       Defines the spring length.
  MaxIteration       Holds the maximum count of iteration.
  ------------------ ----------------------------------------------------------------------------------------


[] 

Programmatically, the symmetric layout manager instance is created with the respective arguments, assigned to the LayoutManager and updated as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [SymmetricLayoutManager symmetricLayout = [new] SymmetricLayoutManager(diagram1.Model,100);]           |
|                                                                                                                                                                 |
| [symmetricLayout.SpringFactor = 0.442;]                                                                                     |
|                                                                                                                                                                 |
| [symmetricLayout.SpringLength = 100;]                                                                                       |
|                                                                                                                                                                 |
| [symmetricLayout.MaxIteration = 500;]                                                                                       |
|                                                                                                                                                                 |
| [this][.diagram1.LayoutManager = symmetricLayout;]                         |
|                                                                                                                                                                 |
| [this][.diagram1.LayoutManager.UpdateLayout([null]);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| **[]**                                                                                                                                                      |
|                                                                                                                                                                                                               |
| [Dim][ symmetricLayout [As] [New] SymmetricLayoutManager(diagram1.Model, 100)] |
|                                                                                                                                                                                                               |
| [symmetricLayout.SpringFactor = 0.442]                                                                                                                                    |
|                                                                                                                                                                                                               |
| [symmetricLayout.SpringLength = 100]                                                                                                                                      |
|                                                                                                                                                                                                               |
| [symmetricLayout.MaxIteration = 500]                                                                                                                                      |
|                                                                                                                                                                                                               |
| [Me][.diagram1.LayoutManager = symmetricLayout]                                                                          |
|                                                                                                                                                                                                               |
| [Me][.diagram1.LayoutManager.UpdateLayout([Nothing])]                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample Diagrams are as follows.

**[]** 

{border="0"}

**[]** 

Figure 56: Diagram With Symmetric Layout

**[]** 

{border="0"}

**[]** 

Figure 57: Symmetric Layout with Spring Factor Settings

 

[]{#p36} 

 

[]{#related-topics}

