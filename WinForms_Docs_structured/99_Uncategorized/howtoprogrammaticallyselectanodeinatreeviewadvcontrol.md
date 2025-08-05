---
title: howtoprogrammaticallyselectanodeinatreeviewadvcontrol.md
original_path: WinForms_Docs/99_Uncategorized/howtoprogrammaticallyselectanodeinatreeviewadvcontrol.md
created_at: 2025-08-05
---






#### How to programmatically select a node in a TreeViewAdv control {#how-to-programmatically-select-a-node-in-a-treeviewadv-control style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

**[]** 

Set the HideSelection property of the TreeViewAdv control to false and use the code snippet shown below.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                  |
| [//Select][ the ][first][ node][ under node 1.]                        |
|                                                                                                                                                                                                                                                                                                                                  |
| [this][.treeViewAdv1.SelectedNode = ][this][.treeViewAdv1.Nodes\[1\];][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                       |
| [\'Select the first node under node 1.]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                       |
| [Me][.treeViewAdv1.SelectedNode = ][Me][.treeViewAdv1.Nodes(1)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Setting the **HideSelection** property to false, ensures that the node remains selected, even when the TreeViewAdv control loses focus or does not have focus.

 

 

 

 

[]{#related-topics}

