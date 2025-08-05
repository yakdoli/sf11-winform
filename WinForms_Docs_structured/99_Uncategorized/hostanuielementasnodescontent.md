---
title: hostanuielementasnodescontent.md
original_path: WinForms_Docs/99_Uncategorized/hostanuielementasnodescontent.md
created_at: 2025-08-05
---








  









### Host an UIElement as Node's Content {#host-an-uielement-as-nodes-content style="tab-stops: 0pt"}

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

Figure 211: NodeContent[]

[] 

Here, Button is a UIElement. Similarly any UIElement can be hosted as Node's Content.

 

[]{#related-topics}

