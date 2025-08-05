---
title: connectionport1.md
original_path: WinForms_Docs/99_Uncategorized/connectionport1.md
created_at: 2025-08-05
---








  









## Connection Port {#connection-port style="tab-stops: 0pt"}

[]{#p51}Essential Diagram WPF provides the ability to define custom ports for making connections. The **ConnectionPort** class can be used for defining custom ports on the nodes. Any number of ports can be defined on a node. By default every node has a center port.

[] 

ConnectionPort has the following properties:

 

Table 43: Property Table[]

+-------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------+---------------------------------------------------+
| Property    | Description                                                                                                                     | Type of the property                   | Value it accepts   | Any other dependencies/ sub properties associated |
+-------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------+---------------------------------------------------+
| Left        | Gets or sets the position of the port in the x coordinate.                                                                      | Dependency property                    | Double             | No                                                |
|             |                                                                                                                                 |                                        |                    |                                                   |
|             |                                                                                                                                 |                                        |                    |                                                   |
|             |                                                                                                                                 |                                        |                    |                                                   |
|             | Default value: 0                                                                                                                |                                        |                    |                                                   |
+-------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------+---------------------------------------------------+
| Top         | Gets or sets the position of the port in the y coordinate.                                                                      | Dependency property                    | Double             | No                                                |
|             |                                                                                                                                 |                                        |                    |                                                   |
|             |                                                                                                                                 |                                        |                    |                                                   |
|             |                                                                                                                                 |                                        |                    |                                                   |
|             | Default value: 0                                                                                                                |                                        |                    |                                                   |
+-------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------+---------------------------------------------------+
| Node        | The Node property specifies the container of the port.                                                                          | CLR [property] | Node               | No                                                |
+-------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------+---------------------------------------------------+
| PortShape   | The PortShape property specifies the shape to be used for the port. Three types of shapes are provided: Arrow, Circle, Diamond. | CLR [property] | PortShapes.None    | No                                                |
|             |                                                                                                                                 |                                        |                    |                                                   |
|             |                                                                                                                                 |                                        | PortShapes.Arrow   |                                                   |
|             |                                                                                                                                 |                                        |                    |                                                   |
|             | Default Value is PortShapes.Diamond                                                                                             |                                        | PortShapes.Diamond |                                                   |
|             |                                                                                                                                 |                                        |                    |                                                   |
|             |                                                                                                                                 |                                        | PortShapes.Circle  |                                                   |
+-------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------+---------------------------------------------------+
| PortStyle   | The PortStyle property provides option for the customization of the ports.                                                      | CLR [property] | PortStyle          | No                                                |
+-------------+---------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------+---------------------------------------------------+

 

Node properties related to Connection Ports are:

 

Table 44: Property Table[]

+----------------+----------------------------------------------------------------------------------------+----------------------+-----------------------+---------------------------------------------------+
| Property       | Description                                                                            | Type of the property | Value it accepts      | Any other dependencies/ sub properties associated |
+----------------+----------------------------------------------------------------------------------------+----------------------+-----------------------+---------------------------------------------------+
| PortVisibility | Gets or sets a value indicating whether all the ports of  the node are visible or not. | Dependency property  | Visibility.Hidden     | No                                                |
|                |                                                                                        |                      |                       |                                                   |
|                |                                                                                        |                      | Visibility.Collapsed  |                                                   |
|                |                                                                                        |                      |                       |                                                   |
|                | Default value isVisibility.Visible                                                     |                      | Visibility.Visible    |                                                   |
+----------------+----------------------------------------------------------------------------------------+----------------------+-----------------------+---------------------------------------------------+
| AllowPortDrag  | Gets or sets a value indicating whether the ports can be dragged or not.               | Dependency property  | Boolean (true/ false) | No                                                |
|                |                                                                                        |                      |                       |                                                   |
|                |                                                                                        |                      |                       |                                                   |
|                |                                                                                        |                      |                       |                                                   |
|                | Default value is True.                                                                 |                      |                       |                                                   |
+----------------+----------------------------------------------------------------------------------------+----------------------+-----------------------+---------------------------------------------------+

[] 

[] 

 

LineConnector properties related to Connection Port are:

 

Table 45: Property Table[]

+--------------------+------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| Property           | Description                                                                                                                  | Type of the property | Value it accepts | Any other dependencies/ sub properties associated |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ConnectionHeadPort | Gets or sets the head port of the connection.                                                                                | Dependency property  | ConnectionPort   | No                                                |
|                    |                                                                                                                              |                      |                  |                                                   |
|                    | While dpecifying the CoonectionHeadPort, the node containing the port should be specified as the HeadNode of the connection. |                      |                  |                                                   |
|                    |                                                                                                                              |                      |                  |                                                   |
|                    | Default value is Null.                                                                                                       |                      |                  |                                                   |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+
| ConnectionTailPort | Gets or sets the head port of the connection.                                                                                | Dependency property  | ConnectionPort   | No                                                |
|                    |                                                                                                                              |                      |                  |                                                   |
|                    | While dpecifying the CoonectionTailPort, the node containing the port should be specified as the TailNode of the connection. |                      |                  |                                                   |
|                    |                                                                                                                              |                      |                  |                                                   |
|                    | Default value is Null.                                                                                                       |                      |                  |                                                   |
+--------------------+------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+---------------------------------------------------+

[] 

See Also

[] 

 Refer Concepts and Features -\> Connection Port -\> Create Connection Port

 Refer Concepts and Features -\> Connection Port -\> PortShape[]

 Refer Concepts and Features -\> Connection Port -\> PortStyle[]

 Refer Concepts and Features -\> Connection Port -\> PortVisibility[]

 Refer Concepts and Features -\> Connection Port -\> AllowPortDrag[]

 Refer Concepts and Features -\> Connection Port -\> Connections to Port[]

 

More:















