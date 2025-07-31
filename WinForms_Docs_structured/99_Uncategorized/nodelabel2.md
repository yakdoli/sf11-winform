---
title: nodelabel2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nodelabel2.md
created_at: 2025-07-03
---








  









### Node Label {#node-label style="tab-stops: 0pt"}

Label is a single line or multiline text that is displayed over the Node. This Label is used to textually represent a Node with a string that can be edited in run time, there are many properties used to change the alignment and appearance settings. Label can be represented as multiline text using the **TextWrapping** property.

Table 23: Property Table**[]**

+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| Property                 | Description                                                                                                   | Type of the property | Value it Accept                                         | Any other dependencies/ sub properties associated   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| IsLabelEditable          | Gets or sets a value indicating whether node\'s label can be edited or not. The default value is set to True. | Dependency property  | Boolean (true/ false)                                   | No[] |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| Label                    | Gets or sets the node label.                                                                                  | Dependency property  | string                                                  | No                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelVisibility          | Gets or sets the label visibility.                                                                            | Dependency property  | Visibility.Hidden                                       | No                                                  |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | Visibility.Collapsed                                    |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | Visibility.Visible                                      |                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelHorizontalAlignment | Specifies the horizontal alignment for the node label.                                                        | Dependency property  | HorizontalAlignment.Center                              | No                                                  |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | HorizontalAlignment.Left                                |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | HorizontalAlignment.Right                               |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | HorizontalAlignment.Stretch                             |                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelVerticalAlignment   | Specifies the vertical alignment for the node label.                                                          | Dependency property  | VerticalAlignment.Bottom                                | No                                                  |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | VerticalAlignment.Center                                |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | VerticalAlignment.Stretch                               |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | VerticalAlignment.Top                                   |                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelAngle               | Gets or sets the angle of the node label.                                                                     | Dependency property  | double                                                  | No                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelTextTrimming        | Gets or sets the text trimming style. Default value is CharacterEllipsis.                                     | Dependency property  | TextTrimming.CharacterEllipsis                          | No                                                  |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | TextTrimming.None                                       |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | TextTrimming.WordEllipsis                               |                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelForeground          | Gets or sets the foreground of the label. Default value is Black.                                             | Dependency property  | Brush                                                   | No                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelBackground          | Gets or sets the background of the label. Default value is White.                                             | Dependency property  | Brush                                                   | No                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelFontStyle           | Gets or sets the background of the label. Default value is White.                                             | Dependency property  | FontStyle                                               | No                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelFontFamily          | Gets or sets the font family of the label. Default value is Arial.                                            | Dependency property  | FontFamily                                              | No                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelTextAlignment       | Gets or sets the text alignment of the label. Default value is Center.                                        | Dependency property  | TextAlignment.Center                                    | No                                                  |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | TextAlignment.Justify                                   |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | TextAlignment.Left                                      |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | TextAlignment.Right                                     |                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelFontSize            | Gets or sets the font size of the label. Default value is 11.                                                 | Dependency property  | Double                                                  | No                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelFontWeight          | Gets or sets the font weight of the label. Default value is SemiBold.                                         | Dependency property  | FontWeight                                              | No                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelTextWrapping        | Gets or sets the text wrapping of the label. Default value is NoWrap.                                         | Dependency property  | TextWrapping.NoWrap                                     | No                                                  |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | TextWrapping.Wrap                                       |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | TextWrapping.WrapWithOverflow                           |                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelWidth               | Gets or sets the width of the label. Default value is node's width.                                           | Dependency property  | Double                                                  | No                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| EnableMultilineLabel     | Gets or sets a value indicating whether the Node's label can be multiline or not. Default value is False.     | Dependency Property  | Boolean (True / False)                                  | No                                                  |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+
| LabelTextDecorations     | Gets or sets the text alignment of the label. Default value is Center.                                        | Dependency property  | [TextDecorations].Underline     | No                                                  |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | [TextDecorations].Baseline      |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | [TextDecorations].OverLine      |                                                     |
|                          |                                                                                                               |                      |                                                         |                                                     |
|                          |                                                                                                               |                      | [TextDecorations].Strikethrough |                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------------------+----------------------+---------------------------------------------------------+-----------------------------------------------------+

[] 

Following is list of topics explained subsequently,

[] 

[·      ]Set Label for Node

[·      ]Label Editing

[·      ]Multiline label

[·      ]Label Visibility[]

[·      ]Label Angle

**[]** 

Set a label for the node using the **Label** property. The default value is an empty string. By default, the label is displayed at the top-center position.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Node][ n = [new] [Node]();] |
|                                                                                                                                                                   |
| [n.OffsetX = 50;]                                                                                                             |
|                                                                                                                                                                   |
| [n.OffsetY = 50;]                                                                                                             |
|                                                                                                                                                                   |
| [n.Shape = [Shapes].FlowChart_Card;]                                                                  |
|                                                                                                                                                                   |
| [n.Label = [\"WPF\"];]                                                                                |
|                                                                                                                                                                   |
| [diagramModel.Nodes.Add(n);]                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Dim][ n [As] [New] [Node]()] |
|                                                                                                                                                                                      |
| [n.OffsetX = 50]                                                                                                                                 |
|                                                                                                                                                                                      |
| [n.OffsetY = 50]                                                                                                                                 |
|                                                                                                                                                                                      |
| [n.Shape = Shapes.FlowChart_Card]                                                                                                                |
|                                                                                                                                                                                      |
| [n.Label = \"WPF\"]                                                                                                                              |
|                                                                                                                                                                                      |
| [diagramModel.Nodes.Add(n)][]                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 38:  Label[]

[] 

Label Editing[]

[] 

A node\'s label can be edited at run time by setting **IsLabelEditable** property to **True**.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Node][ n = [new] [Node]();] |
|                                                                                                                                                                   |
| [n.Shape = [Shapes].RoundedRectangle;]                                                                |
|                                                                                                                                                                   |
| [n.IsLabelEditable = [true];]                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Dim][ n [As] [New] [Node]()] |
|                                                                                                                                                                                      |
| [n.Shape = Shapes.RoundedRectangle]                                                                                                              |
|                                                                                                                                                                                      |
| [n.IsLabelEditable = [True]][]                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A user can specify a label at run time by following the below mentioned steps.

[] 

[·      ]Double click the left mouse button on the node. A text box will appear with the cursor at the beginning.

[·      ]Now type the label name and press ENTER. The label will be displayed on the node. Press ESC key if you do not want to apply the new label value.

[] 

{border="0"}

Figure 39: LabelEditor[]

[] 

 

[]{#p31}See Also:

 

]{.UGHyperlink}

 

Multiline label

**[]** 

Label text can be displayed in multiple lines using **LabelTextWrapping** property set to Wrap. If there is no enough space for the text to get displayed over the node in a single line then the text will get wrapped within the node boundaries and will start to display the label in multiple lines.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Node][ n = [new] [Node]();] |
|                                                                                                                                                                   |
| [n.Shape = [Shapes].RoundedRectangle;]                                                                |
|                                                                                                                                                                   |
| [n.Label = [\"This is Multiline Label\"];]                                                            |
|                                                                                                                                                                   |
| [n.Width = 75;]                                                                                                               |
|                                                                                                                                                                   |
| [n.Height = 100;]                                                                                                             |
|                                                                                                                                                                   |
| [n.LabelTextWrapping = [TextWrapping].Wrap;]                                                          |
|                                                                                                                                                                   |
| [n.IsLabelEditable = [true];]                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Dim][ n [As] [New] [Node]()] |
|                                                                                                                                                                                      |
| [n.Shape = Shapes.RoundedRectangle]                                                                                                              |
|                                                                                                                                                                                      |
| [n.Label = \"This [is] Multiline Label\"]                                                                                   |
|                                                                                                                                                                                      |
| [n.Width = 75]                                                                                                                                   |
|                                                                                                                                                                                      |
| [n.Height = 100]                                                                                                                                 |
|                                                                                                                                                                                      |
| [n.LabelTextWrapping = TextWrapping.Wrap]                                                                                                        |
|                                                                                                                                                                                      |
| [n.IsLabelEditable = [True]][]                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 40: Multi line label[]

[] 

[] 

Label Visibility

**[]** 

A label\'s visibility can be changed using the **LabelVisibility** property. The default value is visible.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Node][ n = [new] [Node]();] |
|                                                                                                                                                                   |
| [n.Shape = [Shapes].FlowChart_Card;]                                                                  |
|                                                                                                                                                                   |
| [n.Label = [\"Syncfusion\"];]                                                                         |
|                                                                                                                                                                   |
| [n.LabelVisibility = [Visibility].Hidden;]                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Dim][ n [As] [New] [Node]()] |
|                                                                                                                                                                                      |
| [n.Shape = Shapes.FlowChart_Card]                                                                                                                |
|                                                                                                                                                                                      |
| [n.Label = \"Syncfusion\"]                                                                                                                       |
|                                                                                                                                                                                      |
| [n.LabelVisibility = Visibility.Hidden][]                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Label Vertical Alignment & Label Horizontal Alignment

[] 

Vertical and horizontal alignments of a label is specified using **LabelVerticalAlignment** and **LabelHorizontalAlignment** properties. By default, **LabelVerticalAlignment** is set to Top and **LabelHorizontalAlignment** is set to Center.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Node][ n = [new] [Node]();] |
|                                                                                                                                                                   |
| [n.Shape = [Shapes].FlowChart_Card;]                                                                  |
|                                                                                                                                                                   |
| [n.Label = [\"Diagram\"];]                                                                            |
|                                                                                                                                                                   |
| [n.LabelHorizontalAlignment = [HorizontalAlignment].Center;]                                          |
|                                                                                                                                                                   |
| [n.LabelVerticalAlignment = [VerticalAlignment].Center;]                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Dim][ n [As] [New] [Node]()] |
|                                                                                                                                                                                      |
| [n.Shape = Shapes.FlowChart_Card]                                                                                                                |
|                                                                                                                                                                                      |
| [n.Label = \"Diagram\"]                                                                                                                          |
|                                                                                                                                                                                      |
| [n.LabelHorizontalAlignment = HorizontalAlignment.Center]                                                                                        |
|                                                                                                                                                                                      |
| [n.LabelVerticalAlignment = VerticalAlignment.Center][]                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

This will place the label at the center of the node.

[] 

{border="0"}

Figure 41: LabelAlignment[]

[] 

LabelAngle

**[]** 

The user can rotate the label by a specified angle and display it using the below code snippet.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Node][ n = [new] [Node]();] |
|                                                                                                                                                                   |
| [n.Shape = [Shapes].FlowChart_Card;]                                                                  |
|                                                                                                                                                                   |
| [n.Label = [\"Diagram\"];]                                                                            |
|                                                                                                                                                                   |
| [n.LabelHorizontalAlignment = [HorizontalAlignment].Right;]                                           |
|                                                                                                                                                                   |
| [n.LabelVerticalAlignment = [VerticalAlignment].Top;]                                                 |
|                                                                                                                                                                   |
| [n.Label = 45;]                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Dim][ n [As] [New] [Node]()] |
|                                                                                                                                                                                      |
| [n.Shape = Shapes.FlowChart_Card]                                                                                                                |
|                                                                                                                                                                                      |
| [n.Label = \"Diagram\"]                                                                                                                          |
|                                                                                                                                                                                      |
| [n.LabelHorizontalAlignment = HorizontalAlignment.Right]                                                                                         |
|                                                                                                                                                                                      |
| [n.LabelVerticalAlignment = VerticalAlignment.Top]                                                                                               |
|                                                                                                                                                                                      |
| [n.Label = 45][]                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 42: LabelAngle[]

Multiline Label Support for LabelEditor:

 

Node's Label can be set as Multiline Label by setting the **EnableMultiline** property as True. The default Value is False.

[           ]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][syncfusion][:][Node][ Shape][=\"FlowChart_Card\"][ Height][=\"100\"][ Width][=\"100\"][ OffsetX][=\"500\"][ OffsetY][=\"500\" ][Name][=\"Node1\"][ EnableMultilineLabel][=\"true"/\>][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [Node][ node1 = [new] [Node]();][] |
|                                                                                                                                                                                                             |
| [node1.Shape = [Shapes].RoundedSquare;]                                                                                                         |
|                                                                                                                                                                                                             |
| [node1.OffsetX = 500;]                                                                                                                                                  |
|                                                                                                                                                                                                             |
| [node1.OffsetY = 500;]                                                                                                                                                  |
|                                                                                                                                                                                                             |
| [node1.Width = 100;]                                                                                                                                                    |
|                                                                                                                                                                                                             |
| [node1.Height = 100;]                                                                                                                                                   |
|                                                                                                                                                                                                             |
| [node1.EnableMultilineLabel = [true];]                                                                                                             |
|                                                                                                                                                                                                             |
| [diagramModel.Nodes.Add(node1);][ ]                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [Dim][ node1 [As] [New] [Node]()] |
|                                                                                                                                                                                          |
| [node1.Shape = [Shapes].RoundedSquare]                                                                                       |
|                                                                                                                                                                                          |
| [node1.OffsetX = 500  ]                                                                                                                              |
|                                                                                                                                                                                          |
| [node1.OffsetY = 500]                                                                                                                                |
|                                                                                                                                                                                          |
| [node1.Width = 100]                                                                                                                                  |
|                                                                                                                                                                                          |
| [node1.Height = 100]                                                                                                                                 |
|                                                                                                                                                                                          |
| [node1.EnableMultilineLabel = [True]]                                                                                           |
|                                                                                                                                                                                          |
| [diagramModel.Nodes.Add(node1)][ ]                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 43: MultilineLabel for Node

 

 

 

Custom Label Support for Node

This feature enables you to customize the Label Position of the Nodes. The **IsLabelDragable** and **LabelDisplacement** property is used to customize the Label position of the node. **LabelDisplacement** property depends on LabelHorizontalAlignment and LabelVerticalAlignment.

 

Table 24: Properties Table

+-----------------------+--------------------------------------------------------------------------------------------------------+----------------------+------------------+----------------+
| Property              | Description                                                                                            | Type                 | Value It Accepts | Default Values |
+-----------------------+--------------------------------------------------------------------------------------------------------+----------------------+------------------+----------------+
| **IsLabelDragable**   | Gets or sets the Label of the Node to be  Dragged or Not.                                              | Dependency  property | bool(true/false) | False          |
|                       |                                                                                                        |                      |                  |                |
|                       |                                                                                                        |                      |                  |                |
+-----------------------+--------------------------------------------------------------------------------------------------------+----------------------+------------------+----------------+
| **LabelDisplacement** | Gets or sets the different between the Original position and the Current position of the Node's Label. | Dependency  property | Point            | Point(0,0)     |
|                       |                                                                                                        |                      |                  |                |
|                       |                                                                                                        |                      |                  |                |
+-----------------------+--------------------------------------------------------------------------------------------------------+----------------------+------------------+----------------+

[] 

Adding Custom Label Enhancements for Node to an Application

**[]** 

Set the LabelDisplacement for Node

Label is aligned within the bounds of Node using LabelHorizontalAlignment and LabelVerticalAlignment property, the LabelDisplacement can be used as to displace the Label from this original position. This value can be positive or negative.

**[]** 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [       ][(node [as] [Node]).LabelDisplacement = [new] [Point](100,100);] |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

Label Dragging support for Node

The Label can be dragged from the Node at runtime, if this property is set to true. When a label is dragged, it will automatically update the LabelDisplacement value.


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                         |
| [       ][(node [as] [Node]).IsLabelDragable = [true];][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

[]{#related-topics}

