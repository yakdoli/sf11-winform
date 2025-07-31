---
title: howtofindthesourcenodeanddestinationnodeforeachofthedirectedlinks.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\howtofindthesourcenodeanddestinationnodeforeachofthedirectedlinks.md
created_at: 2025-07-03
---








  









## How to find the source node and destination node for each of the directed links?[] {#how-to-find-the-source-node-and-destination-node-for-each-of-the-directed-links style="tab-stops: 0pt"}

[] 

User must bring each node to IEndPointContainer and check the two ports, i.e., the **TailEndPoint.Port and HeadEndPoint.Port.**

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [Node][ ndSource = (([IEndPointContainer])node).TailEndPoint.Port.Container;]      |
|                                                                                                                                                                                              |
| [Node][ ndDestination = (([IEndPointContainer])node).HeadEndPoint.Port.Container;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                       |
| [Dim][ ndSource [As] Syncfusion.Windows.Forms.Diagram.Node = [DirectCast](node, Syncfusion.Windows.Forms.Diagram.IEndPointContainer).TailEndPoint.Port.Container]      |
|                                                                                                                                                                                                                                                                                                       |
| [Dim][ ndDestination [As] Syncfusion.Windows.Forms.Diagram.Node = [DirectCast](node, Syncfusion.Windows.Forms.Diagram.IEndPointContainer).HeadEndPoint.Port.Container] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}[Note:] If the TailEndPoint.Port = \'Null\' or HeadEndPoint.Port = \'Null\', then it means that the link is not connected to another node.


[]{#related-topics}

