---
title: howtohostauielementasthenodescontent.md
original_path: WinForms_Docs/99_Uncategorized/howtohostauielementasthenodescontent.md
created_at: 2025-08-05
---








  









### How to host a UI Element as the node's Content? {#how-to-host-a-ui-element-as-the-nodes-content style="tab-stops: 0pt"}

[] 

You can host any content inside the node using the **Content** property.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [Node][ n = [new] [Node]();]     |
|                                                                                                                                                                       |
| [n.Shape = [Shapes].FlowChart_Card;]                                                                      |
|                                                                                                                                                                       |
| [Button][ b = [new] [Button]();] |
|                                                                                                                                                                       |
| [b.Content = [\"Click ME!\"];]                                                                            |
|                                                                                                                                                                       |
| [n.Content = b;]                                                                                                                  |
|                                                                                                                                                                       |
| [(n.Content [as] [Button]).IsHitTestVisible = [true];]          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                           |
|                                                                                                                                                                                                          |
| []                                                                                                                                                     |
|                                                                                                                                                                                                          |
| [Dim][ n [As] [New] [Node]()]                     |
|                                                                                                                                                                                                          |
| [n.Shape = Shapes.FlowChart_Card]                                                                                                                                    |
|                                                                                                                                                                                                          |
| [Dim][ b [As] [New] [Button]()]                   |
|                                                                                                                                                                                                          |
| [b.Content = \"Click [ME]!\"]                                                                                                                   |
|                                                                                                                                                                                                          |
| [n.Content = b]                                                                                                                                                      |
|                                                                                                                                                                                                          |
| [TryCast][(n.Content, Button).IsHitTestVisible = [True]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 170:NodeContent**[]**

Here, Button is a UIElement; similarly any UIElement can be hosted as a Node's Content.

 

[]{#related-topics}

