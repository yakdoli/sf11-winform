---
title: connectionport.md
original_path: WinForms_Docs/99_Uncategorized/connectionport.md
created_at: 2025-08-05
---








  









## Connection Port {#connection-port style="tab-stops: 0pt"}

 

[]{#p51}[\
]Essential Diagram Silverlight provides the ability to define custom ports for making connections. The **ConnectionPort** class can be used for defining custom ports on the nodes. Any number of ports can be defined on a node. By default, every node has a center port.

[] 

**[]** 

**[]** 

ConnectionPort has the following properties

[] 

+-------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------+--------------------+---------------------------------------------------+
| Property    | Description                                                                                                                         | Type of the property | Value it accepts   | Any other dependencies/ sub properties associated |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------+--------------------+---------------------------------------------------+
| Left        | Gets or sets the position of the port in the x coordinate.                                                                          | Dependency property  | Double             | No                                                |
|             |                                                                                                                                     |                      |                    |                                                   |
|             |                                                                                                                                     |                      |                    |                                                   |
|             |                                                                                                                                     |                      |                    |                                                   |
|             | Default value: 0                                                                                                                    |                      |                    |                                                   |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------+--------------------+---------------------------------------------------+
| Top         | Gets or sets the position of the port in the y coordinate.                                                                          | Dependency property  | Double             | No                                                |
|             |                                                                                                                                     |                      |                    |                                                   |
|             |                                                                                                                                     |                      |                    |                                                   |
|             |                                                                                                                                     |                      |                    |                                                   |
|             | Default value: 0                                                                                                                    |                      |                    |                                                   |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------+--------------------+---------------------------------------------------+
| Node        | The Node property specifies the container of the port                                                                               | CLR Property         | Node               | No                                                |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------+--------------------+---------------------------------------------------+
| PortShape   | The PortShape property specifies the shape to be used for the port. Three types of shapes are provided: Arrow, Circle, and Diamond. | CLR Property         | PortShapes.None    | No                                                |
|             |                                                                                                                                     |                      |                    |                                                   |
|             |                                                                                                                                     |                      | PortShapes.Arrow   |                                                   |
|             |                                                                                                                                     |                      |                    |                                                   |
|             | Default Value: PortShapes.Diamond                                                                                                   |                      | PortShapes.Diamond |                                                   |
|             |                                                                                                                                     |                      |                    |                                                   |
|             |                                                                                                                                     |                      | PortShapes.Circle  |                                                   |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------+--------------------+---------------------------------------------------+
| PortStyle   | The PortStyle property provides option for the customization of the ports.                                                          | CLR Property         | PortStyle          | No                                                |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------+--------------------+---------------------------------------------------+

[] 

Node properties related to Connection Ports are:

[] 

+----------------+---------------------------------------------------------------------------------------+----------------------+-----------------------+---------------------------------------------------+
| Property       | Description                                                                           | Type of the property | Value it accepts      | Any other dependencies/ sub properties associated |
+----------------+---------------------------------------------------------------------------------------+----------------------+-----------------------+---------------------------------------------------+
| PortVisibility | Gets or sets a value indicating whether all the ports of the node are visible or not. | Dependency property  | Visibility.Hidden     | No                                                |
|                |                                                                                       |                      |                       |                                                   |
|                |                                                                                       |                      | Visibility.Collapsed  |                                                   |
|                |                                                                                       |                      |                       |                                                   |
|                | Default value: Visibility.Visible                                                     |                      | Visibility.Visible    |                                                   |
+----------------+---------------------------------------------------------------------------------------+----------------------+-----------------------+---------------------------------------------------+
| AllowPortDrag  | Gets or sets a value indicating whether the ports can be dragged or not.              | Dependency property  | Boolean (true/ false) | No                                                |
|                |                                                                                       |                      |                       |                                                   |
|                |                                                                                       |                      |                       |                                                   |
|                |                                                                                       |                      |                       |                                                   |
|                | Default value: True                                                                   |                      |                       |                                                   |
+----------------+---------------------------------------------------------------------------------------+----------------------+-----------------------+---------------------------------------------------+

[] 

[] 

LineConnector properties related to Connection Port are:

[] 

+--------------------+------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| Property           | Description                                                                                                                  | Type of the property | Value it accepts | Any other dependencies/ sub properties associated |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ConnectionHeadPort | Gets or sets the head port of the connection.                                                                                | Dependency property  | ConnectionPort   | No                                                |
|                    |                                                                                                                              |                      |                  |                                                   |
|                    | While specifying the CoonectionHeadPort, the node containing the port should be specified as the HeadNode of the connection. |                      |                  |                                                   |
|                    |                                                                                                                              |                      |                  |                                                   |
|                    | Default value: Null                                                                                                          |                      |                  |                                                   |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ConnectionTailPort | Gets or sets the head port of the connection.                                                                                | Dependency property  | ConnectionPort   | No                                                |
|                    |                                                                                                                              |                      |                  |                                                   |
|                    | While specifying the CoonectionTailPort, the node containing the port should be specified as the TailNode of the connection. |                      |                  |                                                   |
|                    |                                                                                                                              |                      |                  |                                                   |
|                    | Default value: Null                                                                                                          |                      |                  |                                                   |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+

[] 

See Also

[] 

[[·      ]]{.UGHyperlink}[Create Connection Port]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[PortShape]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[PortStyle]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[PortVisibility]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[AllowPortDrag]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[Connections to Port]{.UGHyperlink}[]{.UGHyperlink}

 

More:















