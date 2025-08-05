---
title: howtodisplayminandmaxindicatorsproperlyonmousehoveringoverthetopnodewhentwonodesareconnected.md
original_path: WinForms_Docs/99_Uncategorized/howtodisplayminandmaxindicatorsproperlyonmousehoveringoverthetopnodewhentwonodesareconnected.md
created_at: 2025-08-05
---








  









## How to display min and max indicators properly on mouse hovering over the top node when two nodes are connected?[] {#how-to-display-min-and-max-indicators-properly-on-mouse-hovering-over-the-top-node-when-two-nodes-are-connected style="tab-stops: 0pt"}

[] 

When a node is connected to another node and when the mouse is hovered over the top node on the bottom-right side, the selection cursor will be displayed along with the minimum and maximum indicators. Set the **SendAllLinksToBack** property to \'True\' to display the indicators without any rendering issues.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                     |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [this][.DiagramWebControl1.SendAllLinksToBack = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                              |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [Me][.DiagramWebControl1.SendAllLinksToBack = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

