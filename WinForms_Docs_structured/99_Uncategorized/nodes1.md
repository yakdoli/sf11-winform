---
title: nodes1.md
original_path: WinForms_Docs/99_Uncategorized/nodes1.md
created_at: 2025-08-05
---








  









## Nodes {#nodes style="tab-stops: 0pt"}

**[]** 

Nodes are graphical objects that can be placed on the page; it is usually used to represent visual data to be placed on the page.

[\
]Properties

[] 

+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| Property                   | Description                                                                                                       | Type of the property | Value it Accept               | Any other dependencies/ sub properties associated |
+============================+===================================================================================================================+======================+===============================+===================================================+
| IsLabelEditable            | Gets or sets a value indicating whether the node\'s label can be edited or not. The default value is set to true. | Dependency property  |  Boolean(true/ false)         | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| Label                      | Gets or sets the node label                                                                                       | Dependency property  | string                        | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelVisibility            | Gets or sets the label visibility                                                                                 | Dependency property  |                               | No                                                |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | Visibility.Hidden             |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | Visibility.Collapsed          |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | Visibility.Visible            |                                                   |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelHorizontalAlignment   | Specifies the horizontal alignment for the node label                                                             | Dependency property  | HorizontalAlignment.Center    | No                                                |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | HorizontalAlignment.Left      |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | HorizontalAlignment.Right     |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | HorizontalAlignment.Stretch   |                                                   |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelVerticalAlignment     | Specifies the vertical alignment for the node label                                                               | Dependency property  | VerticalAlignment.Bottom      | No                                                |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | VerticalAlignment.Center      |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | VerticalAlignment.Stretch     |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | VerticalAlignment.Top         |                                                   |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| HorizontalContentAlignment | Specifies the horizontal alignment for the node content                                                           | Dependency property  | HorizontalAlignment.Center    | No                                                |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | HorizontalAlignment.Left      |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | HorizontalAlignment.Right     |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | HorizontalAlignment.Stretch   |                                                   |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| VerticalContentAlignment   | Specifies the vertical alignment for the node content                                                             | Dependency property  | VerticalAlignment.Bottom      | No                                                |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | VerticalAlignment.Center      |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | VerticalAlignment.Stretch     |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | VerticalAlignment.Top         |                                                   |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelAngle                 | Gets or sets the angle of the node label                                                                          | Dependency property  | double                        | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| Shape                      | Specifies the shape of the node                                                                                   | Dependency property  | Shapes                        | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| CustomPathStyle            | Gets or sets the CustomPathStyle for the node                                                                     | Dependency property  | Style                         | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| Level                      | Gets or sets the node level                                                                                       | Dependency property  | int                           | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| OffsetX                    | Gets or sets the offset x value of the node                                                                       | CLR Property         | double                        | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| OffsetY                    | Gets or sets the offset y value of the node                                                                       | CLR Property         | double                        | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| Content                    | Gets or sets the node\'s content                                                                                  | Dependency property  | object                        | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| AllowMove                  | Gets or sets a value indicating whether the node can be moved or not. The default value is set to true.           | Dependency property  | Boolean (true/ false)         | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| AllowSelect                | Gets or sets a value indicating whether the node can be selected or not. The default value is set to true.        | Dependency property  | Boolean (true/ false)         | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| AllowRotate                | Gets or sets a value indicating whether the node can be rotated or not. The default value is set to true.         | Dependency property  | Boolean (true/ false)         | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| AllowResize                | Gets or sets a value indicating whether the node can be resized or not. The default value is set to true.         | Dependency property  | Boolean (true/ false)         | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelForeground            | Gets or sets the foreground of the label. Default value is Black.                                                 | Dependency property  | Brush                         | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelBackground            | Gets or sets the background of the label. The default value is White.                                             | Dependency property  | Brush                         | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontStyle             | Gets or sets the background of the label. The default value is White.                                             | Dependency property  | FontStyle                     | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontFamily            | Gets or sets the font family of the label. The default value is Arial.                                            | Dependency property  | FontFamily                    | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontSize              | Gets or sets the font size of the label. The default value is 11.                                                 | Dependency property  | Double                        | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontWeight            | Gets or sets the font weight of the label. The default value is SemiBold.                                         | Dependency property  | FontWeight                    | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelTextWrapping          | Gets or sets the text wrapping of the label. The default value is NoWrap.                                         | Dependency property  | TextWrapping.NoWrap           | No                                                |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | TextWrapping.Wrap             |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      | TextWrapping.WrapWithOverflow |                                                   |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelWidth                 | Gets or sets the width of the label. The default value is node's width.                                           | Dependency property  | Double                        | No                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| IsLabelDragable            | Gets or sets the Label of Node is Dragging or Not.                                                                | Dependency  property | bool(true/false)              | False                                             |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelDisplacement          | Gets or sets the different between the Original position and the Current position of the Node's Label.            | Dependency  property | Point                         | Point(0,0)                                        |
|                            |                                                                                                                   |                      |                               |                                                   |
|                            |                                                                                                                   |                      |                               |                                                   |
+----------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+

[] 

[] 

See Also

[] 

[[·      ]]{.UGHyperlink}[[Custom Shapes]]{.UGHyperlink}

[[[·      ]]]{.UGHyperlink}[AllowRotate property]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[AllowMove property]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[AllowSelect property]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[AllowResize property]{.UGHyperlink}[]{.UGHyperlink}

[[·      ]]{.UGHyperlink}[Customize the label of Nodes and LineConnectors]{.UGHyperlink}[]{.UGHyperlink}

More:

























