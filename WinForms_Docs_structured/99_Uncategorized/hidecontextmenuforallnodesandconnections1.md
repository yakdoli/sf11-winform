---
title: hidecontextmenuforallnodesandconnections1.md
original_path: WinForms_Docs/99_Uncategorized/hidecontextmenuforallnodesandconnections1.md
created_at: 2025-08-05
---








  









### Hide ContextMenu for all Nodes and Connections {#hide-contextmenu-for-all-nodes-and-connections style="tab-stops: 0pt"}

ContextMenu for all Nodes and LineConnectors can be hidden using the following code snippet.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| [\                                                                                                                                                                                                             |
| diagramView.NodeContextMenu = [new] [ContextMenu] { Visibility = [Visibility].Collapsed };]           |
|                                                                                                                                                                                                                |
| [diagramView.LineConnectorContextMenu = [new] [ContextMenu] { Visibility = [Visibility].Collapsed };] |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                            |
| [\                                                                                                                                                                                                                         |
| ][diagramView.NodeContextMenu = [New] ContextMenu [With] {.Visibility = Visibility.Collapsed}]           |
|                                                                                                                                                                                                                            |
| [diagramView.LineConnectorContextMenu = [New] ContextMenu [With] {.Visibility = Visibility.Collapsed}][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Where, diagramView is an instance of DiagramView

[] 

[]{#related-topics}

