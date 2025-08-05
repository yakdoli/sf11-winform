---
title: directedtreelayout.md
original_path: WinForms_Docs/99_Uncategorized/directedtreelayout.md
created_at: 2025-08-05
---






#### Directed Tree Layout {#directed-tree-layout style="tab-stops: 0pt"}

[] 

The **DirectedTreeLayoutManager** implements a layout manager for arranging nodes in a tree-like structure. It includes the following parameters.

[] 

[·      ]**Model**: specifies the Current Model

[·      ]**RotationDegree**: specifies the angular orientation of the tree

[·      ]**VerticalOffset**: specifies the vertical distance between adjacent nodes

[·      ]**HorizontalOffset**: specifies the horizontal distance between adjacent nodes

[] 

The following code example illustrates how to create the DirectedTreeLayoutManager programmatically.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                         |
| [this][.DiagramWebControl1.LayoutManager = [new] DirectedTreeLayoutManager([this].DiagramWebControl1.Model, 0, 20, 20);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 19: Top-to-Bottom Directed Tree Layout with Rotation Degree set to 0

**[]** 

{border="0"}

[] 

Figure 20: Bottom-to-Top Directed Tree Layout with Rotation Degree set to 180

[] 

**[See Also]**

[] 

[Table Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Hierarchical Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Graph Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Subgraph Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Radial Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Symmetric Layout]{.UGHyperlink}[, ]{.UGHyperlink}[OrgChart Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Updating the Layout]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

