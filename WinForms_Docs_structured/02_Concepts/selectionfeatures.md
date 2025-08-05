---
title: selectionfeatures.md
original_path: WinForms_Docs/02_Concepts/selectionfeatures.md
created_at: 2025-08-05
---






##### Selection Features {#selection-features style="tab-stops: 0pt"}

GridTree control does not use the selection support inherited from the Grid control, because the selections in the Grid Tree need to be persisted, as the nodes are expanded/collapsed and sorted. The GridTreeNode.IsSelected property indicates whether the node is selected or not and the GridTreeNode.SelectedColumns property contains the names of the columns selected for the node. You can access selected nodes by using the GridTreeControl.SelectedNodes property.

The following code example illustrates cell range selections in the Grid Tree.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                      |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                         |
|                                                                                                                                                                                                 |
| [foreach][ ([GridTreeNode] node [in] treeGrid.SelectedNodes)] |
|                                                                                                                                                                                                 |
| [{]                                                                                                                                                         |
|                                                                                                                                                                                                 |
| [    [foreach] ([string] columnName [in] node.SelectedColumns)]                              |
|                                                                                                                                                                                                 |
| [    {]                                                                                                                                                     |
|                                                                                                                                                                                                 |
| [        [Console].Write([\"{0} \"], treeGrid.InternalGrid.GetValueFromNode(columnName, node));]            |
|                                                                                                                                                                                                 |
| [    }]                                                                                                                                                     |
|                                                                                                                                                                                                 |
| [    [Console].WriteLine();]                                                                                                        |
|                                                                                                                                                                                                 |
| [}]                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

