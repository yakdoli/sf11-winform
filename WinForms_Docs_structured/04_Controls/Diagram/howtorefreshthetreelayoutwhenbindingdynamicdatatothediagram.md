---
title: howtorefreshthetreelayoutwhenbindingdynamicdatatothediagram.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\howtorefreshthetreelayoutwhenbindingdynamicdatatothediagram.md
created_at: 2025-07-03
---








  









### How to refresh the tree layout when binding dynamic data to the diagram? {#how-to-refresh-the-tree-layout-when-binding-dynamic-data-to-the-diagram style="tab-stops: 0pt"}

 

 

Essential Diagram for Silverlight provides support to bind dynamic data to the diagram. But once the new data is assigned, the tree needs to be refreshed. This can be done using the RefreshLayout method.

 

The following code can be used to refresh the layout:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [diagramModel.ItemsSource = dataobj;]                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| [DirectedTreeLayout][ tree = [new] [DirectedTreeLayout](diagramModel, diagramView);] |
|                                                                                                                                                                                                                           |
| [tree.RefreshLayout();]                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [diagramModel.ItemsSource = dataobj]                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [Dim][ tree [As] [New] [DirectedTreeLayout](DiagramModel, DiagramView)] |
|                                                                                                                                                                                                                                |
| [tree.RefreshLayout()][]                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In case the hierarchical layout is being used, then the following code can be used:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [diagramModel.ItemsSource = dataobj;]                                                                                                                                                         |
|                                                                                                                                                                                                                                   |
| [HierarchicalTreeLayout][ tree = [new] [HierarchicalTreeLayout](diagramModel, diagramView);] |
|                                                                                                                                                                                                                                   |
| [tree.RefreshLayout();]                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [diagramModel.ItemsSource = dataobj]                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [Dim][ tree [As] [New] [HierarchicalTreeLayout](DiagramModel, DiagramView)] |
|                                                                                                                                                                                                                                    |
| [tree.RefreshLayout()][]                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\
Once the data is assigned, call the RefreshLayout() method of the corresponding tree-layout.

 

[]{#related-topics}

