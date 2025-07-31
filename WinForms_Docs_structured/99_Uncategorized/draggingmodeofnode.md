---
title: draggingmodeofnode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\draggingmodeofnode.md
created_at: 2025-07-03
---








  









### Dragging Mode of Node {#dragging-mode-of-node style="tab-stops: 0pt"}

Essential Diagram for MVC provides preview support while dragging a node in the diagram page[[. When you drag any node within the diagram page, a preview of the dragged node will be displayed. ]]{.apple-style-span}

Use Case Scenario

[[This feature displays a preview of the node you drag from diagram page, thus enables you to identify the node you are dragging from the diagram page.]]{.apple-style-span}

Property

+------------------------------------------+---------------------------------------------------------------------------------------+----------------------+----------------------------------------------------------------------------+----------------------------------------------------+
| Property                                 | Description                                                                           | Type of the Property | Value it Accepts                                                           | Any Other Dependencies/Sub-Properties Associated   |
+==========================================+=======================================================================================+======================+============================================================================+====================================================+
| [NodeDraggingMode] | Gets or sets a value indicating whether node is dragged with preview or default mode. | Dependency property  | [DraggingType].[DefaultMode] | No (This property is not supported in Canvas mode) |
|                                          |                                                                                       |                      |                                                                            |                                                    |
|                                          | ```                                                        |                      |                                                                            |                                                    |
|                                          | The default value is DefaultMode.                                                     |                      |                                                                            |                                                    |
|                                          | ```                                                                                   |                      | [DraggingType.][PreviewMode] |                                                    |
+------------------------------------------+---------------------------------------------------------------------------------------+----------------------+----------------------------------------------------------------------------+----------------------------------------------------+

More:







