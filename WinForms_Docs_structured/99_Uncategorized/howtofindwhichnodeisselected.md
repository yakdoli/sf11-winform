---
title: howtofindwhichnodeisselected.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtofindwhichnodeisselected.md
created_at: 2025-07-03
---








  









## How to find which node is selected[]{#p74}?[] {#how-to-find-which-node-is-selected style="tab-stops: 0pt"}

[] 

All selected nodes are in the **View.SelectionList** collection. Simply check the SelectionList in the presence of your node.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [foreach][ ([Node] node [in] DiagramWebControl1.Model.Nodes)] |
|                                                                                                                                                                                              |
| [{]                                                                                                                                                      |
|                                                                                                                                                                                              |
| [      [if]((DiagramWebControl1.View.SelectionList.Contains(node)))]                                                                |
|                                                                                                                                                                                              |
| [      {]                                                                                                                                                |
|                                                                                                                                                                                              |
| [            [// node is selected]]                                                                                                |
|                                                                                                                                                                                              |
| [      }]                                                                                                                                                |
|                                                                                                                                                                                              |
| [}]                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [For][ [Each] node [As] Node [In] DiagramWebControl1.Model.Nodes ] |
|                                                                                                                                                                                                                        |
| [\' node is selected ]                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [    [If] (DiagramWebControl1.View.SelectionList.Contains(node)) [Then] ]                                                                |
|                                                                                                                                                                                                                        |
| [    [End] [If] ]                                                                                                                        |
|                                                                                                                                                                                                                        |
| [Next][ ]                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

