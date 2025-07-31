---
title: hierarchicallayout.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\hierarchicallayout.md
created_at: 2025-07-03
---






#### Hierarchical Layout {#hierarchical-layout style="tab-stops: 0pt"}

[] 

**HierarchicalLayoutManager** arranges the nodes in a hierarchical fashion depending on the parent-child relationship. Unlike the directed tree layout, more than one parent item can be defined for a child. It includes the following parameters.

[] 

[·      ]**Model**: specifies the Current Model

[·      ]**RotationDegree**: specifies the angular orientation of the tree

[·      ]**VerticalOffset**: specifies the vertical distance between adjacent nodes

[·      ]**HorizontalOffset**: specifies the horizontal distance between adjacent nodes

[] 

The following code example illustrates how to create the HierarchicalLayoutManager programmatically.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [this][.DiagramWebControl1.LayoutManager = [new] HierarchicLayoutManager([this].DiagramWebControl1.Model, 0, 25, 30);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 21: Top-to-Bottom Hierarchical Layout

[] 

{border="0"}

[] 

Figure 22: Bottom-to-Top Hierarchical Layout

[] 

**[See Also]**

[] 

[Table Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Directed Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Graph Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Subgraph Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Radial Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Symmetric Layout]{.UGHyperlink}[, ]{.UGHyperlink}[OrgChart Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Updating the Layout]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

