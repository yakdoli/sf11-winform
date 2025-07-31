---
title: diagrammodel2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\diagrammodel2.md
created_at: 2025-07-03
---








  









## Diagram Model {#diagram-model style="tab-stops: 0pt"}

[]{#p66}A model represents data for an application and contains the logic for adding, accessing, and manipulating the data. Nodes and connectors are added to the Diagram control using the **Model** property. A predefined layout can be applied using the **LayoutType** property of the DiagramModel. The position of the nodes can be manually specified.

[] 

See Also

 Refer Concepts and Features -\> Diagram Model -\> Bind data to Diagram Control

 Refer Concepts and Features -\> Diagram Model -\> Tree Spacing

 Refer Concepts and Features -\> Diagram Model -\> Tree Orientation[]

 Refer Concepts and Features -\> Diagram Model -\> Table Expand Mode

[] 

[] 

Table 51: Methods Table[]

+-------------------------+----------------------------------------+-------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------+
| Name                    | Parameters                             | Return Type | Description                             | Reference Links                                                                                          |
+-------------------------+----------------------------------------+-------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------+
| Nodes.Add(object)       | object,                                | Void        | To add a node into the Model.           |           |
|                         |                                        |             |                                         |                                                                                                          |
|                         | object should be of type Node          |             |                                         |                                                                                                          |
+-------------------------+----------------------------------------+-------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------+
| Connections.Add(object) | object,                                | Void        | To add a line connector into the Model. |  |
|                         |                                        |             |                                         |                                                                                                          |
|                         | object should be of type LineConnector |             |                                         |                                                                                                          |
+-------------------------+----------------------------------------+-------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------+
| Layers.Add(Layer)       | Layer                                  | Void        | To add a layer into the model.          |          |
+-------------------------+----------------------------------------+-------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------+

[] 

More:





















