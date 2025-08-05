---
title: addingtablelayoutforselectednodes.md
original_path: WinForms_Docs/99_Uncategorized/addingtablelayoutforselectednodes.md
created_at: 2025-08-05
---






##### Adding Table Layout for selected Nodes {#adding-table-layout-for-selected-nodes style="tab-stops: 0pt"}

[To apply a table layout to the selected nodes, assign the selected nodes to the *OrderNodes* property of the *DiagramModel*. You can also assign your own collection of IShape to the *OrderNodes* property. Then create an instance of the *TableLayout* and call the *RefreshLayout* method for this instance.]

[The following code illustrates this: ]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
| [       // Assigning selected node to the OrderedNodes property.][]                     |
|                                                                                                                                                                                                         |
| [          diagramModel.OrderedNodes= diagramView.SelectionList.OfType\<[IShape]\>().ToList(); ]                               |
|                                                                                                                                                                                                         |
| [       // Create an instance of TableLayout and refresh it.][]                         |
|                                                                                                                                                                                                         |
| [          [TableLayout] table = [new] [TableLayout](diagramModel, diagramView);] |
|                                                                                                                                                                                                         |
| [          table.RefreshLayout();]                                                                                                                     |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                   |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
| [         [\'Assigning selected node to the OrderedNodes property.]]                                                   |
|                                                                                                                                                                                  |
| [              diagramModel.OrderedNodes= diagramView.SelectionList.OfType([Of] IShape)().ToList()]                     |
|                                                                                                                                                                                  |
| [         [\'Create an instance of TableLayout and refresh it.]]                                                       |
|                                                                                                                                                                                  |
| [              [Dim] table [As] [New] TableLayout(diagramModel, diagramView)] |
|                                                                                                                                                                                  |
| [              table.RefreshLayout()]                                                                                                        |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[When the code runs, the table layout will be applied to the specified node collection.  ]


[{border="0"}][Note: If ][the OrderNodes property ][ is set to null, then the table layout will be applied to the entire diagram.]


 

{border="0"}

Figure 24: Table Layout Applied for Specified Nodes

[]{#related-topics}

