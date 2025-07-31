---
title: howtoiteratethenodesfromthediagramcollections.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\howtoiteratethenodesfromthediagramcollections.md
created_at: 2025-07-03
---








  









## How to iterate the nodes from the Diagram collections?[] {#how-to-iterate-the-nodes-from-the-diagram-collections style="tab-stops: 0pt"}

[] 

It can be done using the below code.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                          |
|                                                                                                                                                                                              |
| [foreach][ ([Node] node [in] DiagramWebControl1.Model.Nodes)] |
|                                                                                                                                                                                              |
| [{]                                                                                                                                                      |
|                                                                                                                                                                                              |
| [// Your code here]                                                                                                                        |
|                                                                                                                                                                                              |
| [}]                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [\' Your code here]                                                                                                                                                  |
|                                                                                                                                                                                                                        |
| [For][ [Each] node [As] Node [In] DiagramWebControl1.Model.Nodes ] |
|                                                                                                                                                                                                                        |
| [Next][ ]                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

