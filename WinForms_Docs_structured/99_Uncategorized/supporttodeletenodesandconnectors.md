---
title: supporttodeletenodesandconnectors.md
original_path: WinForms_Docs/99_Uncategorized/supporttodeletenodesandconnectors.md
created_at: 2025-08-05
---








  









###        Support to Delete Nodes and Connectors {#support-to-delete-nodes-and-connectors style="tab-stops: 0pt"}

 

Essential Diagram for Silverlight provides support to delete selected nodes and connectors. 

[] 

Use Case Scenarios

When you restructure the workflow diagram, you may happen to delete some of the nodes and connectors.  Using this feature you can deleted the unwanted nodes and connectors.

 

Sample Link

A demo of this feature is available in the following location:

*{Installed Location}[ ]\\Syncfusion\\EssentialStudio\\[x.x.x.x]\\Silverlight\\Diagram.Silverlight\\ProductShowcase\\DiagramBuilder*

 

Deleting Nodes and Connectors

 

You can delete the nodes and connectors the following two methods:

[·      ]Using Delete Keyboard

[·      ]Using Delete Command

 

**Using Delete Keyboard**

This feature provides keyboard support to delete nodes and connectors:

[The following steps illustrate how to delete nodes or connectors using keyboard:]

[] 

[1.   Select the node or the connector to be deleted.]

[2.   Press the **Delete** key. The selected node or connector will be deleted. ]

***[\
]*Using the Delete Command**

[You can also delete nodes and connectors through commands. To delete nodes and connectors, invoke the *Delete* command as illustrated in the following code:]

[] 

+------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                 |
|                                                                                                |
|                                                                                                |
|                                                                                                |
| [diagramControl.Delete.Execute(diagramView);] |
+------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                 |
|                                                                                                |
|                                                                                                |
|                                                                                                |
| [diagramControl.Delete.Execute(diagramView);] |
+------------------------------------------------------------------------------------------------+

[] 

***[ ]**[{border="0"}]**[Note: When a node is deleted, all the connectors connected to that node will also be deleted. Deleting a connector leads to the deletion of that particular connector only.\
\
]***[]

[]{#related-topics}

