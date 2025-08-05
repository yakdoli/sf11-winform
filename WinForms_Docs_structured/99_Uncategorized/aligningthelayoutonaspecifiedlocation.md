---
title: aligningthelayoutonaspecifiedlocation.md
original_path: WinForms_Docs/99_Uncategorized/aligningthelayoutonaspecifiedlocation.md
created_at: 2025-08-05
---






##### [ ]Aligning the Layout on a Specified Location {#aligning-the-layout-on-a-specified-location style="tab-stops: 0pt"}

[To align the ordered nodes in a particular position, call the *TableLayout's* *RefreshLayout* (Point PivotPoint) method and specify the particular point as a parameter. The layout will be positioned in the specified pivot point. ]

[The following code illustrates this:]****

**** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
| [       // Assigning selected node to the OrderedNodes.][]                              |
|                                                                                                                                                                                                         |
| [          diagramModel.OrderedNodes= diagramView.SelectionList.OfType\<[IShape]\>().ToList(); ]                               |
|                                                                                                                                                                                                         |
| [          [TableLayout] table = [new] [TableLayout](diagramModel, diagramView);] |
|                                                                                                                                                                                                         |
| [          table.RefreshLayout(300,400);]                                                                                                              |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| [         [\' Assigning selected node to the OrderedNodes.]]                                                           |
|                                                                                                                                                                                  |
| [diagramModel.OrderedNodes= diagramView.SelectionList.OfType([Of] IShape)().ToList()]                                   |
|                                                                                                                                                                                  |
| [              [Dim] table [As] [New] TableLayout(diagramModel, diagramView)] |
|                                                                                                                                                                                  |
| [              table.RefreshLayout(300,400)]                                                                                                 |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

