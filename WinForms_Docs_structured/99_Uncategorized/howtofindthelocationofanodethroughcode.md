---
title: howtofindthelocationofanodethroughcode.md
original_path: WinForms_Docs/99_Uncategorized/howtofindthelocationofanodethroughcode.md
created_at: 2025-08-05
---








  









## How to find the location of a node through code?[] {#how-to-find-the-location-of-a-node-through-code style="tab-stops: 0pt"}

[] 

Each node is included in a rectangle called the **BoundingRectangle**.

[] 

{border="0"}

[] 

Figure 75: Bounding Rectangle

[] 

BoundingRectangle\'s Top and Left position is the node\'s Top and Left position too.

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
| [      [float] fLeft = node.BoundingRectangle.Left;]                                                                                |
|                                                                                                                                                                                              |
| [      [float] fTop = node.BoundingRectangle.Top;]                                                                                  |
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
| [Dim][ fLeft [As] [Single] = node.BoundingRectangle.Left]                               |
|                                                                                                                                                                                                                        |
| [Dim][ fTop [As] [Single] = node.BoundingRectangle.Top]                                 |
|                                                                                                                                                                                                                        |
| [Next]                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

