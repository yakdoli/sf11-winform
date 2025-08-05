---
title: customizingthelabelofnodesandlineconnectors1.md
original_path: WinForms_Docs/99_Uncategorized/customizingthelabelofnodesandlineconnectors1.md
created_at: 2025-08-05
---








  









### Customizing the Label of Nodes and Line Connectors {#customizing-the-label-of-nodes-and-line-connectors style="tab-stops: 0pt"}

 

[] 

The labels of the nodes and connectors are equipped with Multiline support i.e. the user can specify the labels to span multiple lines by setting the LabelTextWrapping property to wrap the text and by specifying the width of the label. Also, several other customization properties have been added for the labels. These are tabulated below:\
\

Properties[]

[] 


+-------------------+---------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| Property          | Description                                                               | Type of the property | Value it accepts              | Any other dependencies/ sub properties associated |
+===================+===========================================================================+======================+===============================+===================================================+
| LabelForeground   | Gets or sets the foreground of the label. The default value is Black.     | Dependency property  | Brush                         | No                                                |
+-------------------+---------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelBakground    | Gets or sets the background of the label. The default value is White.     | Dependency property  | Brush                         | No                                                |
+-------------------+---------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontStyle    | Gets or sets the background of the label. The default value is White.     | Dependency property  | FontStyles.Oblique            | No                                                |
|                   |                                                                           |                      |                               |                                                   |
|                   |                                                                           |                      | FontStyles.Italic             |                                                   |
|                   |                                                                           |                      |                               |                                                   |
|                   |                                                                           |                      | FontStyles.Normal             |                                                   |
+-------------------+---------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontFamily   | Gets or sets the font family of the label. The default value is Arial.    | Dependency property  | FontFamily                    | No                                                |
+-------------------+---------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontSize     | Gets or sets the font size of the label. The default value is 11.         | Dependency property  | Double                        | No                                                |
+-------------------+---------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontWeight   | Gets or sets the font weight of the label. The default value is SemiBold. | Dependency property  | FontWeights                   | No                                                |
+-------------------+---------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelTextWrapping | Gets or sets the text wrapping of the label. The default value is NoWrap. | Dependency property  | TextWrapping.NoWrap           | No                                                |
|                   |                                                                           |                      |                               |                                                   |
|                   |                                                                           |                      | TextWrapping.Wrap             |                                                   |
|                   |                                                                           |                      |                               |                                                   |
|                   |                                                                           |                      | TextWrapping.WrapWithOverflow |                                                   |
+-------------------+---------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelWidth        | Gets or sets the width of the label. The default value is node's width.   | Dependency property  | Double                        | No                                                |
+-------------------+---------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+


[] 

The following code snippet illustrates the implementation of the properties mentioned in the table above.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [Node][ node1 = [new] [Node]([Guid].NewGuid(), [\"Register\"]);] |
|                                                                                                                                                                                                                                                       |
| [            node1.Shape = [Shapes].RoundedSquare;]                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [            node1.Width = 150;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [            node1.Height = 50;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [            node1.OffsetX = 250;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [            node1.OffsetY = 100;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [            node1.Label = [\"This is a Multiline Label \"];]                                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [            node1.LabelWidth = 70;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [            node1.LabelHeight = 150;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [            node1.LabelTextWrapping = [TextWrapping].Wrap;]                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [            node1.LabelForeground = [new] [SolidColorBrush]([Colors].Red);]                                                                 |
|                                                                                                                                                                                                                                                       |
| [            node1.LabelFontSize = 14;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [            node1.LabelFontStyle = [FontStyles].Italic;]                                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [            ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [            [Node] node2 = [new] [Node]([Guid].NewGuid(), [\"ClientAccountInfo\"]);]        |
|                                                                                                                                                                                                                                                       |
| [            node2.Shape = [Shapes].FlowChart_Card;]                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [            node2.Width = 150;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [            node2.Height = 60;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [            node2.OffsetX = 450;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [            node2.OffsetY = 100;]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [            node2.LabelWidth = 75;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [            node2.LabelHeight = 150;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [            node2.LabelTextWrapping = [TextWrapping].Wrap;]                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [            node2.LabelForeground = [new] [SolidColorBrush]([Colors].Yellow);]                                                              |
|                                                                                                                                                                                                                                                       |
| [            node2.LabelFontSize = 16;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [            node2.LabelHorizontalAlignment = [HorizontalAlignment].Center;]                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [            node2.Label = [\"Here text is aligned to left\"];]                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [            [LineConnector] line = [new] [LineConnector]();]                                                                                |
|                                                                                                                                                                                                                                                       |
| [            line.ConnectorType = [ConnectorType].Straight;]                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [            line.TailNode = node1;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [            line.HeadNode = node2;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [            line.HeadDecoratorShape = [DecoratorShape].None;]                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [            line.Label = [\"Connected\"];]                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [            line.LabelWidth = 44;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [            line.LabelHeight = 100;]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [            line.LabelTextWrapping = [TextWrapping].Wrap;]                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [            line.LabelForeground = [new] [SolidColorBrush]([Colors].Green);]                                                                |
|                                                                                                                                                                                                                                                       |
| [            line.LabelFontSize = 12;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [            line.LabelFontStyle = [FontStyles].Normal;]                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [            line.LabelBackground = [new] [SolidColorBrush]([Colors].Yellow);]                                                               |
|                                                                                                                                                                                                                                                       |
| [            diagramControl.Model.Nodes.Add(node1);]                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [            diagramControl.Model.Nodes.Add(node2);]                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [            diagramControl.Model.Connections.Add(line);]                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [Dim][ node1 [As] [New] [Node]([Guid].NewGuid(), [\"Register\"])] |
|                                                                                                                                                                                                                                                                          |
| [                  node1.Shape = Shapes.RoundedSquare]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| [                  node1.Width = 150]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                          |
| [                  node1.Height = 50]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                          |
| [                  node1.OffsetX = 250]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                          |
| [                  node1.OffsetY = 100]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                          |
| [                  node1.Label = \"This [is] a Multiline Label \"]                                                                                                                                              |
|                                                                                                                                                                                                                                                                          |
| [                  node1.LabelWidth = 70]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                          |
| [                  node1.LabelHeight = 150]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [                  node1.LabelTextWrapping = TextWrapping.Wrap]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| [                  node1.LabelForeground = [New] SolidColorBrush(Colors.Red)]                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [                  node1.LabelFontSize = 14]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| [                  node1.LabelFontStyle = FontStyles.Italic]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [    [Dim] node2 [As] [New] [Node]([Guid].NewGuid(), [\"ClientAccountInfo\"])]                |
|                                                                                                                                                                                                                                                                          |
| [                  node2.Shape = Shapes.FlowChart_Card]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                          |
| [                  node2.Width = 150]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                          |
| [                  node2.Height = 60]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                          |
| [                  node2.OffsetX = 450]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                          |
| [                  node2.OffsetY = 100]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                          |
| [                  node2.LabelWidth = 75]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                          |
| [                  node2.LabelHeight = 150]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [                  node2.LabelTextWrapping = TextWrapping.Wrap]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| [                  node2.LabelForeground = [New] SolidColorBrush(Colors.Yellow)]                                                                                                                                |
|                                                                                                                                                                                                                                                                          |
| [                  node2.LabelFontSize = 16]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| [                  node2.LabelHorizontalAlignment = HorizontalAlignment.Center]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| [                  node2.Label = \"Here [text] [is] aligned [to] left\"]                                                                                              |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [    [Dim] line [As] [New] [LineConnector]()]                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| [                  line.ConnectorType = ConnectorType.Straight]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| [                  line.TailNode = node1]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                          |
| [                  line.HeadNode = node2]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                          |
| [                  line.HeadDecoratorShape = DecoratorShape.None]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                          |
| [                  line.Label = \"Connected\"]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| [                  line.LabelWidth = 44]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                          |
| [                  line.LabelHeight = 100]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| [                  line.LabelTextWrapping = TextWrapping.Wrap]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| [                  line.LabelForeground = [New] SolidColorBrush(Colors.Green)]                                                                                                                                  |
|                                                                                                                                                                                                                                                                          |
| [                  line.LabelFontSize = 12]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [                  line.LabelFontStyle = FontStyles.Normal]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [                  line.LabelBackground = [New] SolidColorBrush(Colors.Yellow)]                                                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| [                  diagramControl.Model.Nodes.Add(node1)]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                          |
| [                  diagramControl.Model.Nodes.Add(node2)]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                          |
| [                  diagramControl.Model.Connections.Add(line)][]                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following output is generated using the code snippets above:

[] 

{border="0"}

Figure 167:Customized Multiline Label[]{#p109}

[]{#related-topics}

