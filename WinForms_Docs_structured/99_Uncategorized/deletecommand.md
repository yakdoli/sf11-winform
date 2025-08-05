---
title: deletecommand.md
original_path: WinForms_Docs/99_Uncategorized/deletecommand.md
created_at: 2025-08-05
---








  









### Delete Command {#delete-command style="tab-stops: 0pt"}

Diagram WPF provides support to delete nodes and connectors by using the **Delete** command.

 

The following steps illustrate how to delete a node or connector.

1.   Select the node or the connector to be deleted.

2.   Press the DELETE key. The selected node or connector will be deleted.

[] 


{border="0"}Note: When a node is deleted, all the connectors connected to that node are also deleted. Deleting a connector leads to the deletion of that particular connector only.


[] 

The following code example illustrates how to invoke the Delete command.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                  |
| [DiagramCommandManager][.Delete.Execute(diagramView.Page, diagramView);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [DiagramCommandManager][.Delete.Execute(diagramView.Page, diagramView)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

