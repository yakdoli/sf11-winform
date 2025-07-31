---
title: customizethelabelofnodesandlineconnectors.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizethelabelofnodesandlineconnectors.md
created_at: 2025-07-03
---








  









### Customize the Label of Nodes and Line Connectors {#customize-the-label-of-nodes-and-line-connectors style="tab-stops: 0pt"}

The labels of the nodes and connectors are equipped with Multiline support i.e. you can specify the labels to span multiple lines by setting the **LabelTextWrapping** property to wrap the text and by specifying the width of the label. Also, several other customization properties have been added for the labels. These are listed below:\
\

Table 87: Property Table


+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| Property           | Description                                                               | Type of the property | Value it accepts               | Any other dependencies/ sub properties associated |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| LabelTextTrimming  | Gets or sets the text trimming style. Default value is CharacterEllipsis. | Dependency property  | TextTrimming.CharacterEllipsis | No                                                |
|                    |                                                                           |                      |                                |                                                   |
|                    |                                                                           |                      | TextTrimming.None              |                                                   |
|                    |                                                                           |                      |                                |                                                   |
|                    |                                                                           |                      | TextTrimming.WordEllipsis      |                                                   |
|                    |                                                                           |                      |                                |                                                   |
|                    |                                                                           |                      |                                |                                                   |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| LabelForeground    | Gets or sets the foreground of the label. Default value is Black.         | Dependency property  | Brush                          | No                                                |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| LabelBakground     | Gets or sets the background of the label. Default value is White.         | Dependency property  | Brush                          | No                                                |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| LabelFontStyle     | Gets or sets the background of the label. Default value is White.         | Dependency property  | FontStyles.Oblique             | No                                                |
|                    |                                                                           |                      |                                |                                                   |
|                    |                                                                           |                      | FontStyles.Italic              |                                                   |
|                    |                                                                           |                      |                                |                                                   |
|                    |                                                                           |                      | FontStyles.Normal              |                                                   |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| LabelFontFamily    | Gets or sets the font family of the label. Default value is Arial.        | Dependency property  | FontFamily                     | No                                                |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| LabelTextAlignment | Gets or sets the text alignment of the label. Default value is Center.    | Dependency property  | TextAlignment.Right            | No                                                |
|                    |                                                                           |                      |                                |                                                   |
|                    |                                                                           |                      | TextAlignment.Left             |                                                   |
|                    |                                                                           |                      |                                |                                                   |
|                    |                                                                           |                      | TextAlignment.Center           |                                                   |
|                    |                                                                           |                      |                                |                                                   |
|                    |                                                                           |                      | TextAlignment.Justify          |                                                   |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| LabelFontSize      | Gets or sets the font size of the label. Default value is 11.             | Dependency property  | Double                         | No                                                |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| LabelFontWeight    | Gets or sets the font weight of the label. Default value is SemiBold.     | Dependency property  | FontWeights                    | No                                                |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| LabelTextWrapping  | Gets or sets the text wrapping of the label. Default value is NoWrap.     | Dependency property  | TextWrapping.NoWrap            | No                                                |
|                    |                                                                           |                      |                                |                                                   |
|                    |                                                                           |                      | TextWrapping.Wrap              |                                                   |
|                    |                                                                           |                      |                                |                                                   |
|                    |                                                                           |                      | TextWrapping.WrapWithOverflow  |                                                   |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+
| LabelWidth         | Gets or sets the width of the label. Default value is node's width.       | Dependency property  | Double                         | No                                                |
+--------------------+---------------------------------------------------------------------------+----------------------+--------------------------------+---------------------------------------------------+


[] 

The following code snippet illustrates the implementation of the properties mentioned in the table above.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [Node][ node1 = [new] [Node]([Guid].NewGuid(), [\"Register\"]);]          |
|                                                                                                                                                                                                                                                                |
| [            node1.Shape = [Shapes].RoundedSquare;]                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [            node1.Width = 150;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [            node1.Height = 50;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [            node1.OffsetX = 250;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            node1.OffsetY = 100;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            node1.Label = [\"This is a Multiline Label \"];]                                                                                                                                      |
|                                                                                                                                                                                                                                                                |
| [            node1.LabelWidth = 70;]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [            node1.LabelTextWrapping = [TextWrapping].Wrap;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [            node1.LabelForeground = [Brushes].IndianRed;]                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            node1.LabelFontSize = 14;]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                |
| [            node1.LabelFontStyle = [FontStyles].Italic;]                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [            node1.LabelBackground = [Brushes].Beige;]                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [           ]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
| [Node][ node2 = [new] [Node]([Guid].NewGuid(), [\"ClientAccountInfo\"]);] |
|                                                                                                                                                                                                                                                                |
| [            node2.Shape = [Shapes].FlowChart_Card;]                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [            node2.Width = 150;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [            node2.Height = 50;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [            node2.OffsetX = 450;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            node2.OffsetY = 100;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            node2.LabelWidth = 75;]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [            node2.LabelTextWrapping = [TextWrapping].Wrap;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [            node2.LabelForeground = [Brushes].White;]                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
| [            node2.LabelFontSize = 16;]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                |
| [            node2.LabelBackground = [Brushes].Gray;]                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
| [            node2.LabelTextAlignment = [TextAlignment].Left;]                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [            node2.Label = [\"Here text is aligned to Left\"];]                                                                                                                                    |
|                                                                                                                                                                                                                                                                |
| [             ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [LineConnector][ line = [new] [LineConnector]();]                                                                         |
|                                                                                                                                                                                                                                                                |
| [            line.ConnectorType = [ConnectorType].Straight;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [            line.TailNode = node1;]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [            line.HeadNode = node2;]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [            line.HeadDecoratorShape = [DecoratorShape].None;]                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [            line.Label = [\"This is a Multiline Label for Connectors\"];]                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [            line.LabelWidth = 84;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [            line.LabelTextWrapping = [TextWrapping].Wrap;]                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [            line.LabelForeground = [Brushes].Green;]                                                                                                                                              |
|                                                                                                                                                                                                                                                                |
| [            line.LabelFontSize = 12;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [            line.LabelFontStyle = [FontStyles].Normal;]                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [            line.LabelBackground = [Brushes].Yellow;]                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [Dim][ node1 [As] [New] [Node]([Guid].NewGuid(), [\"Register\"])]          |
|                                                                                                                                                                                                                                                                                   |
| [            node1.Shape = Shapes.RoundedSquare]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [            node1.Width = 150]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                   |
| [            node1.Height = 50]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                   |
| [            node1.OffsetX = 250]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [            node1.OffsetY = 100]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [            node1.Label = \"This [is] a Multiline Label \"]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [            node1.LabelWidth = 70]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [            node1.LabelTextWrapping = TextWrapping.Wrap]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                   |
| [            node1.LabelForeground = Brushes.IndianRed]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                   |
| [            node1.LabelFontSize = 14]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| [            node1.LabelFontStyle = FontStyles.Italic]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| [            node1.LabelBackground = Brushes.Beige]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [Dim][ node2 [As] [New] [Node]([Guid].NewGuid(), [\"ClientAccountInfo\"])] |
|                                                                                                                                                                                                                                                                                   |
| [            node2.Shape = Shapes.FlowChart_Card]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [            node2.Width = 150]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                   |
| [            node2.Height = 50]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                   |
| [            node2.OffsetX = 450]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [            node2.OffsetY = 100]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [            node2.LabelWidth = 75]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [            node2.LabelTextWrapping = TextWrapping.Wrap]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                   |
| [            node2.LabelForeground = Brushes.White]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [            node2.LabelFontSize = 16]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| [            node2.LabelBackground = Brushes.Gray]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [            node2.LabelTextAlignment = TextAlignment.Left]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [            node2.Label = \"Here [text] [is] aligned [to] Left\"]                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [Dim][ line [As] [New] [LineConnector]()]                                                                                  |
|                                                                                                                                                                                                                                                                                   |
| [            line.ConnectorType = ConnectorType.Straight]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                   |
| [            line.TailNode = node1]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [            line.HeadNode = node2]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [            line.HeadDecoratorShape = DecoratorShape.None]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [            line.Label = \"This [is] a Multiline Label [for] Connectors\"]                                                                                                                         |
|                                                                                                                                                                                                                                                                                   |
| [            line.LabelWidth = 84]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [            line.LabelTextWrapping = TextWrapping.Wrap]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                   |
| [            line.LabelForeground = Brushes.Green]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [            line.LabelFontSize = 12]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                   |
| [            line.LabelFontStyle = FontStyles.Normal]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                   |
| [            line.LabelBackground = Brushes.Yellow][]                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following output is generated using the code snippets above:

[] 

{border="0"}

Figure 209: Customized Multiline Label[]

[]{#related-topics}

