---
title: removingtablelayoutfromthespecificnodes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\removingtablelayoutfromthespecificnodes.md
created_at: 2025-07-03
---






##### Removing Table Layout from the Specific Nodes {#removing-table-layout-from-the-specific-nodes style="tab-stops: 0pt"}

You can remove the table layout applied to specific nodes. To achieve this set the *[OrderedNodes]*[ property of the *DiagramMode* to ]*null*, and call the *RefreshLayout* method of the *TableLayout*. The layout will be applied to the entire diagram. By default the *OrderedNodes* property is set to *null*.

[] 

The following code illustrates how to remove the layout from the specific nodes:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
| [       // Set null value to the OrderedNodes property.][]                              |
|                                                                                                                                                                                                         |
| [          diagramModel.OrderedNodes = [null];]                                                                                   |
|                                                                                                                                                                                                         |
| [          [TableLayout] table = [new] [TableLayout](diagramModel, diagramView);] |
|                                                                                                                                                                                                         |
| [          table.RefreshLayout(300,400);]                                                                                                              |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                   |
|                                                                                                                                                                                  |
|  [\' Set null value to the OrderedNodes property.][]                                       |
|                                                                                                                                                                                  |
| [              diagramModel.OrderedNodes = [Nothing]]                                                                   |
|                                                                                                                                                                                  |
| [              [Dim] table [As] [New] TableLayout(diagramModel, diagramView)] |
|                                                                                                                                                                                  |
| [              table.RefreshLayout(300,400)]                                                                                                 |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

