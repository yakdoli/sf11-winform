---
title: radialtreelayout.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\radialtreelayout.md
created_at: 2025-07-03
---






#### Radial Tree Layout {#radial-tree-layout style="tab-stops: 0pt"}

[] 

The **RadialTreeLayoutManager** arranges nodes in a circular layout, positioning the root node at the center of the graph and the child nodes in a circular fashion around the root. It includes the following parameters.

[] 

[·      ]**Model**: specifies the Current Model

[·      ]**RotationDegree**: specifies the angular orientation of the tree

[·      ]**VerticalOffset**: specifies the vertical distance between adjacent nodes

[·      ]**HorizontalOffset**: specifies the horizontal distance between adjacent nodes

[] 

The following code example illustrates how to create the RadialTreeLayoutManager programmatically.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [this][.DiagramWebControl1.LayoutManager = [new] RadialTreeLayoutManager([this].DiagramWebControl1.Model, 0, 20, 25);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 25: Radial Tree Layout with Rotation Degree set to 0

[] 

{border="0"}

[] 

Figure 26: Radial Tree Layout with Rotation Degree set to 180

[] 

See Also

[] 

[Table Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Directed Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Hierarchical Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Graph Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Subgraph Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Symmetric Layout]{.UGHyperlink}[, ]{.UGHyperlink}[OrgChart Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Updating the Layout]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

