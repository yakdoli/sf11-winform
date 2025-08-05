---
title: lineconnectors1.md
original_path: WinForms_Docs/99_Uncategorized/lineconnectors1.md
created_at: 2025-08-05
---








  









## Line Connectors {#line-connectors style="tab-stops: 0pt"}

Connectors are objects that are used to create a link between two nodes. Each connector has two ends whose position can be specified as point or directly connected to Node. One end of the connector can be defined either by using the 'Start Point Position' or 'Head Node', similarly other end can be defined using 'End Point Position' or 'Tail Node'.

 

{border="0"}

Figure 50: Connector End Points Illustrated

 

[]{#p39}Table 28: Property Table[]

+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| Property                 | Description                                                                                                  | Type of the property                   | Value it accepts               | Any other dependencies/ sub properties associated |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| EnableConnection         | Gets or sets a value indicating whether  connection is enabled or not.                                       | Dependency property                    | Boolean (true/ false)          | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| IsLabelEditable          | Gets or sets a value indicating whether line's label can be edited or not. Default value: True               | Dependency property                    | Boolean (true/ false)          | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| IntermediatePoints       | Gets or sets the intermediate points.                                                                        | Dependency property                    | List\<Point\>                  | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| Label                    | Gets or sets the line\'s label. Default value: Empty String.                                                 | Dependency property                    | String                         | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelTemplate            | Gets or sets a template for the label. Default value: null.                                                  | Dependency property                    | DataTemplate                   | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelVisibility          | Gets or sets the label visibility. Default value: Visibility.Visible                                         | Dependency property                    | Visibility.Hidden              | No                                                |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | Visibility.Collapsed           |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | Visibility.Visible             |                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelHorizontalAlignment | Gets or sets the node's label horizontal Alignment. Default value: HorizontalAlignment.Center                | Dependency property                    | HorizontalAlignment.Center     | No                                                |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | HorizontalAlignment.Left       |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | HorizontalAlignment.Right      |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | HorizontalAlignment.Stretch    |                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| ConnectionEndSpace       | Gets or sets the distance between the connector end position and the node. Default Value: 6                  | CLR [property] | Double                         | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| ConnectorType            | Gets or sets the connector type to be used.                                                                  | Dependency property                    | ConnectorType.Orthogonal       | No                                                |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          | Three values namely Othogonal, Straight and Bezier can be specified. Default Value: ConnectorType.Orthogonal |                                        | ConnectorType.Bezier           |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | ConnectorType.Straight         |                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| HeadNode                 | Gets or sets the head node of the connection. Default value: null.                                           | Dependency property                    | IShape                         | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| TailNode                 | Gets or sets the tail node of the connection. Default value: null.                                           | Dependency property                    | IShape                         | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| HeadDecoratorShape       | Gets or sets the head decorator shape of the connection.                                                     | CLR [property] | DecoratorShape.None            | No                                                |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          | Four values namely None, Arrow , Diamond and Circle can be specified.                                        |                                        | DecoratorShape.Arrow           |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          | Default value: HeadDecoratorShape.None                                                                       |                                        | DecoratorShape.Diamond         |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | DecoratorShape.Circle          |                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| TailDecoratorShape       | Gets or sets the head decorator shape of the connection.                                                     | CLR [property] | DecoratorShape.None            | No                                                |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          | Four values namely None, Arrow , Diamond and Circle can be specified.                                        |                                        | DecoratorShape.Arrow           |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          | Default value: TailDecoratorShape.Arrow                                                                      |                                        | DecoratorShape.Diamond         |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | DecoratorShape.Circle          |                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| HeadDecoratorStyle       | Provides customization option for the head decorator shape.                                                  | CLR [property] | DecoratorStyle                 | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| TailDecoratorStyle       | Provides customization option for the tail decorator shape.                                                  | CLR [property] | DecoratorStyle                 | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LineStyle                | Provides customization option for the line connector.                                                        | CLR [property] | LineStyle                      | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelTextTrimming        | Gets or sets the text trimming style. Default value is CharacterEllipsis.                                    | Dependency property                    | TextTrimming.CharacterEllipsis | No                                                |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | TextTrimming.None              |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | TextTrimming.WordEllipsis      |                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelForeground          | Gets or sets the label foreground. Default value is Black.                                                   | Dependency property                    | Brush                          | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelBackground          | Gets or sets the label background. Default value is White.                                                   | Dependency property                    | Brush                          | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelFontStyle           | Gets or sets the label background. Default value is White.                                                   | Dependency property                    | FontStyle                      | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelFontFamily          | Gets or sets the label font family. Default value is Arial.                                                  | Dependency property                    | FontFamily                     | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelTextAlignment       | Gets or sets the label text alignment. Default value is Center.                                              | Dependency property                    | TextAlignment.Center           | No                                                |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | TextAlignment.Justify          |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | TextAlignment.Left             |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | TextAlignment.Right            |                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelFontSize            | Gets or sets the label font size. Default value is 11.                                                       | Dependency property                    | Double                         | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelFontWeight          | Gets or sets the label font weight. Default value is SemiBold.                                               | Dependency property                    | FontWeight                     | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelTextWrapping        | Gets or sets the label text wrapping. Default value is NoWrap.                                               | Dependency property                    | TextWrapping.NoWrap            | No                                                |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | TextWrapping.Wrap              |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | TextWrapping.WrapWithOverflow  |                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelWidth               | Gets or sets the label width. Default value is line's width.                                                 | Dependency property                    | Double                         | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LineBridgingEnabled      | Gets or sets a value indicating whether line bridging is enabled.                                            | Dependency property                    | Boolean (true/ false)          | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| FirstSegmentLength       | Gets or sets the FirstSegmentLength of the Orthogonal Lineconnector                                          | Dependency Property                    | double                         | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LastSegmentLength        | Gets or sets FirstSegmentLength of the Orthogonal Lineconnector                                              | Dependency Property                    | double                         | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| AutoAdjustPoints         | Gets or sets AutoAdjustPoints of Orthogonal LineConnector.                                                   | Dependency Property                    | Boolean(True/False)            | No                                                |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelPosition            | Gets or sets the Position of the LineConnector's Label from the DiagramPage.                                 | Dependency  property                   | Point                          | Point(0,0)                                        |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| CustomLabelPosition      | Gets or sets the Label of LineConnector is Dragging or Not.                                                  | Dependency  property                   | Enum.                          | CustomLabelPositions.Auto                         |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | CustomLabelPositions.Auto      |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | CustomLabelPositions.Custom    |                                                   |
|                          |                                                                                                              |                                        |                                |                                                   |
|                          |                                                                                                              |                                        | CustomLabelPositions.Drag      |                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+
| LabelAngle               | Gets or sets the angle of the Label of LineConnector.                                                        | Dependency  property                   | double                         | 0                                                 |
+--------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------------------+---------------------------------------------------+

**[]** 

 

FirstSegmentLength:

 

FirstSegmentLength defines the distance between StartPointPosition and the first IntermediatePoint. This property is applicable only for Orthogonal LineConnector whose end points are connected to ports.

 

 

LastSegmentLength:

 

LastSegmentLength defines the distance between the EndPointPosition and the last IntermediatePoint. This property is applicable only for Orthogonal LineConnector whose end points are connected to ports.

 

AutoAdjustPoints:

 

AutoAdjustPoints enables the Orthogonal LineConnector to adjust the intermediate points (add, remove, or modify intermediate points) depending upon the ports to which it is connected. This property is applicable only for Orthogonal LineConnector whose end points are connected to ports. 

 

 

{border="0"}

Figure 51: FirstSegmentLength and LastSegmentLength

 

                                             

The following is a code snippet that connects two Nodes with a LineConnector with FirstSegmentLength and LastSegmentLength.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [Node][ headnode = [new] [Node]();]                                                                                               |
|                                                                                                                                                                                                                                                                        |
| [headnode.Shape = [Shapes].RoundedRectangle;]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                        |
| [headnode.Label = [\"Head Node\"];]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [headnode.Height = 100;]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [headnode.Width = 100;]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                        |
| [headnode.OffsetX = 200;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                        |
| [headnode.OffsetY = 200;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                        |
| [diagramModel.Nodes.Add(headnode);]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [Node][ tailnode = [new] [Node]();]                                                                                               |
|                                                                                                                                                                                                                                                                        |
| [tailnode.Shape = [Shapes].RoundedRectangle;]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                        |
| [tailnode.Label = [\"Tail Node\"];]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [tailnode.Height = 100;]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [tailnode.Width = 100;]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                        |
| [tailnode.OffsetX = 400;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                        |
| [tailnode.OffsetY = 500;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                        |
| [diagramModel.Nodes.Add(tailnode);]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [ConnectionPort][ port1 = [new] [ConnectionPort](headnode, [new] [Point](50, 100));] |
|                                                                                                                                                                                                                                                                        |
| [port1.Width = 10;]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                        |
| [port1.Height = 10;]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                        |
| [port1.PortShape = [PortShapes].Circle;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [headnode.Ports.Add(port1);]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [ConnectionPort][ port2 = [new] [ConnectionPort](tailnode, [new] [Point](50, 0));]   |
|                                                                                                                                                                                                                                                                        |
| [port2.Width = 10;]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                        |
| [port2.Height = 10;]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                        |
| [port2.PortShape = [PortShapes].Diamond;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                        |
| [tailnode.Ports.Add(port2);]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [LineConnector][ line = [new] [LineConnector]();]                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [line.ConnectorType = [ConnectorType].Orthogonal;]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                        |
| [line.HeadNode = headnode;]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [line.TailNode = tailnode;]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [line.ConnectionHeadPort = port1;]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [line.ConnectionTailPort = port2;]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [line.FirstSegmentLength = 50;]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                        |
| [line.LastSegmentLength =100;]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| [line.AutoAdjustPoints = [true];]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                        |
| [diagramModel.Connections.Add(line);][ ]                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ headnode [As] [New] [Node]()]                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [headnode.Shape = [Shapes].RoundedRectangle]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [headnode.Label = [\"Head Node\"]]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [headnode.Height = 100]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [headnode.Width = 100]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [headnode.OffsetX = 200]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                 |
| [headnode.OffsetY = 200]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                 |
| [diagramModel.Nodes.Add(headnode)]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ tailnode [As] [New] [Node]()]                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [tailnode.Shape = [Shapes].RoundedRectangle]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [tailnode.Label = [\"Tail Node\"]]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [tailnode.Height = 100]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [tailnode.Width = 100]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [tailnode.OffsetX = 400]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                 |
| [tailnode.OffsetY = 50]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                 |
| [diagramModel.Nodes.Add(tailnode)]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ port1 [As] [New] [ConnectionPort](headnode, [New] [Point](50, 100))] |
|                                                                                                                                                                                                                                                                                 |
| [port1.Width = 10]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [port1.Height = 10]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [port1.PortShape = [PortShapes].Circle]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [headnode.Ports.Add(port1)]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ port2 [As] [New] [ConnectionPort](tailnode, [New] [Point](50, 0))]   |
|                                                                                                                                                                                                                                                                                 |
| [port2.Width = 10]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [port2.Height = 10]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [port2.PortShape = [PortShapes].Diamond]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [tailnode.Ports.Add(port2)]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ line [As] [New] [LineConnector]()]                                                                                |
|                                                                                                                                                                                                                                                                                 |
| [line.ConnectorType = [ConnectorType].Orthogonal]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                 |
| [line.HeadNode = headnode]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [line.TailNode = tailnode]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [line.ConnectionHeadPort = port1]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                 |
| [line.ConnectionTailPort = port2]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                 |
| [line.FirstSegmentLength = 50]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [line.LastSegmentLength = 100]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [line.AutoAdjustPoints = [True]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                 |
| [diagramModel.Connections.Add(line)][ ]                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

See Also

[] 

 Refer **Concepts and Features -\> Line Connector -\>** **ConnectorType**

 Refer **Concepts and Features -\> Line Connector -\>** **Decorator Shapes**[]

 Refer **Concepts and Features -\> Line Connector -\>** **Customize Line Connectors**[]

 Refer **Concepts and Features -\> Line Connector -\>** **Line Connector Label**[]

 Refer **Concepts and Features -\> General -\> Customize the label of Nodes and LineConnectors**[]

 Refer **Concepts and Features -\> General -\> Customize the contextMenu of Nodes and LineConnectors**[]

 Refer **Concepts and Features -\> Line Connector -\> Line Bridging**[]

 

More:























