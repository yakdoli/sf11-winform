---
title: stepsforaddingaconnectortoadiagramatruntime3.md
original_path: WinForms_Docs/04_Controls/Diagram/stepsforaddingaconnectortoadiagramatruntime3.md
created_at: 2025-08-05
---






#### Steps for Adding a Connector to a Diagram at Run Time  {#steps-for-adding-a-connector-to-a-diagram-at-run-time style="tab-stops: 0pt"}

1.   First, set the **EnableConnection** property to **true**. This has to be set to **true** every time the user makes a connection.

2.   The connector type of the dynamic line connector can be specified using this                                 **setDynamicConnector** method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                      |
| [ function][ dynamicConnector(sender, args) {]                                                                                                |
|                                                                                                                                                                                                                                                                      |
| [        diagram = \$find([FlatDiagram]);[]]                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [        diagram.setDynamicConnector(][\"Orthogonal\"][);] |
|                                                                                                                                                                                                                                                                      |
| [});][]                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   While the pointer is over the node, click where the connection is to start. This acts as the head node for the connector.

4.   While holding the left button, drag the pointer to the node to which you want to create a link. 

{border="0"}

Figure 52: Connector Drag Start 

 

5.   When you run into any node during the dragging process, a red border is displayed for that node. 

{border="0"}

Figure 53: Hit Node 

6.   Release the left mouse button over the target node where you want to connect. This acts as the tail node for the connector and the link is created. 

{border="0"}

Figure 54: Connection Ended

 

[]{#related-topics}

