---
title: tablelayout.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tablelayout.md
created_at: 2025-07-03
---






#### [       ]Table Layout {#table-layout style="tab-stops: 0pt"}

[] 

The **TableLayoutManager** arranges nodes in a Table layout, positioning the nodes in a rectangular grid of cells, with each node spanning over a single table cell. It includes the following parameters.

[] 

[·      ]**Model**: specifies the Current Model

[·      ]**MaxColumnCount**: specifies the maximum Columns Count

[·      ]**MaxRowsCount**: specifies the maximum Rows Count

[] 

The following code example illustrates how to create the TableLayoutManager programmatically.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [this][.DiagramWebControl1.LayoutManager = [new] TableLayoutManager([this].DiagramWebControl1.Model, 5, 5);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 17: Table Layout with Horizontal Orientation

[] 

[{border="0"}][]

[] 

Figure 18: Table Layout with Vertical Orientation

[] 

See Also

[] 

[Directed Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Hierarchical Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Graph Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Subgraph Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Radial Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Symmetric Layout]{.UGHyperlink}[, ]{.UGHyperlink}[OrgChart Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Updating the Layout]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

