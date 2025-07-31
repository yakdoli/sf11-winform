---
title: lineconnectors.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\lineconnectors.md
created_at: 2025-07-03
---








  









## Line Connectors {#line-connectors style="tab-stops: 0pt"}

[] 

Connectors are objects that are used to create a link between two nodes. Each connector has two ends whose position can be specified as point or directly connected to the Node. One end of the connector can be defined using the 'Start Point Position' or 'Head Node 'and  the other end can be defined using 'End Point Position' or 'Tail Node'.

 

{border="0"}

Figure 46: Connector End Points Illustrated**[]**

**[]** 

Properties

[] 

+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| Property                 | Description                                                                                                   | Type of the property | Value it accepts              | Any other dependencies/ sub properties associated |
+==========================+===============================================================================================================+======================+===============================+===================================================+
| EnableConnection         | Gets or sets a value indicating whether \[enable connection\].                                                | Dependency property  | Boolean (true/ false)         | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| IsLabelEditable          | Gets or sets a value indicating whether the line's label can be edited or not. Default value: True            | Dependency property  | Boolean (true/ false)         | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| Label                    | Gets or sets the line\'s label. Default value: Empty String                                                   | Dependency property  | String                        | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelTemplate            | Gets or sets a template for the label. Default value: null                                                    | Dependency property  | DataTemplate                  | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelVisibility          | Gets or sets the label visibility. Default value: Visibility.Visible                                          | Dependency property  | Visibility.Hidden             | No                                                |
|                          |                                                                                                               |                      |                               |                                                   |
|                          |                                                                                                               |                      | Visibility.Collapsed          |                                                   |
|                          |                                                                                                               |                      |                               |                                                   |
|                          |                                                                                                               |                      | Visibility.Visible            |                                                   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelHorizontalAlignment | Gets or sets the node's label horizontal Alignment. Default value: HorizontalAlignment.Center                 | Dependency property  | HorizontalAlignment.Center    | No                                                |
|                          |                                                                                                               |                      |                               |                                                   |
|                          |                                                                                                               |                      | HorizontalAlignment.Left      |                                                   |
|                          |                                                                                                               |                      |                               |                                                   |
|                          |                                                                                                               |                      | HorizontalAlignment.Right     |                                                   |
|                          |                                                                                                               |                      |                               |                                                   |
|                          |                                                                                                               |                      | HorizontalAlignment.Stretch   |                                                   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| ConnectionEndSpace       | Gets or sets the distance between the connector end position and the node. Default Value: 6                   | CLR Property         | Double                        | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| ConnectorType            | Gets or sets the connector type to be used.                                                                   | Dependency property  | ConnectorType.Orthogonal      | No                                                |
|                          |                                                                                                               |                      |                               |                                                   |
|                          | Three values namely Orthogonal, Straight and Bezier can be specified. Default Value: ConnectorType.Orthogonal |                      | ConnectorType.Bezier          |                                                   |
|                          |                                                                                                               |                      |                               |                                                   |
|                          |                                                                                                               |                      | ConnectorType.Straight        |                                                   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| HeadNode                 | Gets or sets the head node of the connection. Default value: null                                             | Dependency property  | IShape                        | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| TailNode                 | Gets or sets the tail node of the connection. Default value: null                                             | Dependency property  | IShape                        | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| HeadDecoratorShape       | Gets or sets the head decorator shape of the connection.                                                      | CLR Property         | DecoratorShape.None           | No                                                |
|                          |                                                                                                               |                      |                               |                                                   |
|                          | Four values namely None, Arrow, Diamond and Circle can be specified.                                          |                      | DecoratorShape.Arrow          |                                                   |
|                          |                                                                                                               |                      |                               |                                                   |
|                          | Default value: HeadDecoratorShape.None                                                                        |                      | DecoratorShape.Diamond        |                                                   |
|                          |                                                                                                               |                      |                               |                                                   |
|                          |                                                                                                               |                      | DecoratorShape.Circle         |                                                   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| TailDecoratorShape       | Gets or sets the head decorator shape of the connection.                                                      | CLR Property         | DecoratorShape.None           | No                                                |
|                          |                                                                                                               |                      |                               |                                                   |
|                          | Four values namely None, Arrow, Diamond and Circle can be specified.                                          |                      | DecoratorShape.Arrow          |                                                   |
|                          |                                                                                                               |                      |                               |                                                   |
|                          | Default value: TailDecoratorShape.Arrow                                                                       |                      | DecoratorShape.Diamond        |                                                   |
|                          |                                                                                                               |                      |                               |                                                   |
|                          |                                                                                                               |                      | DecoratorShape.Circle         |                                                   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| HeadDecoratorStyle       | Provides customization option for the head decorator shape.                                                   | CLR Property         | DecoratorStyle                | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| TailDecoratorStyle       | Provides customization option for the tail decorator shape.                                                   | CLR Property         | DecoratorStyle                | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LineStyle                | Provides customization option for the line connector.                                                         | CLR Property         | LineStyle                     | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelForeground          | Gets or sets the label foreground. The default value is Black.                                                | Dependency property  | Brush                         | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelBackground          | Gets or sets the label background. The default value is White.                                                | Dependency property  | Brush                         | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontStyle           | Gets or sets the label background. The default value is White.                                                | Dependency property  | FontStyle                     | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontFamily          | Gets or sets the label font family. The default value is Arial.                                               | Dependency property  | FontFamily                    | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontSize            | Gets or sets the label font size. The default value is 11.                                                    | Dependency property  | Double                        | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontWeight          | Gets or sets the label font weight. The default value is SemiBold.                                            | Dependency property  | FontWeight                    | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelTextWrapping        | Gets or sets the label text wrapping. The default value is NoWrap.                                            | Dependency property  | TextWrapping.NoWrap           | No                                                |
|                          |                                                                                                               |                      |                               |                                                   |
|                          |                                                                                                               |                      | TextWrapping.Wrap             |                                                   |
|                          |                                                                                                               |                      |                               |                                                   |
|                          |                                                                                                               |                      | TextWrapping.WrapWithOverflow |                                                   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelWidth               | Gets or sets the label width. The default value is the line's width.                                          | Dependency property  | Double                        | No                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+

**[]** 

See Also

[] 

[[• ]]{.UGHyperlink}[ConnectorType]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[Decorator Shapes]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[Customize Line Connectors]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[Line Connector Label]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[Label Template]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[Label Editing]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[Label Visibility]{.UGHyperlink}[]{.UGHyperlink}

[[• ]]{.UGHyperlink}[Customize the label of Nodes and LineConnectors]{.UGHyperlink}[]{.UGHyperlink}

 

More:





















