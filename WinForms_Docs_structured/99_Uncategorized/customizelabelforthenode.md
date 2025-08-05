---
title: customizelabelforthenode.md
original_path: WinForms_Docs/99_Uncategorized/customizelabelforthenode.md
created_at: 2025-08-05
---








  









### Customize Label for the Node {#customize-label-for-the-node style="tab-stops: 0pt"}

Node labels are equipped with multiline support, i.e. you can specify the labels to span multiple lines by specifying the width of the label.

Vertical and horizontal alignments of a label are specified using the **LabelVerticalAlignment** and **LabelHorizontalAlignment** properties. By default, **LabelVerticalAlignment** is set to **Middle** and **LabelHorizontalAlignment** is set to **Center**.

The labels of the nodes are customized by the following properties. The user can specify the color and other font properties of the labels. Also, several other customization properties have been added for the labels. These are tabulated below.

Properties

+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| Property                 | Description                                                                          | Type of the Property | Value it Accepts           | Any Other Dependencies/ Sub-Properties Associated |
+==========================+======================================================================================+======================+============================+===================================================+
| LabelHorizontalAlignment | Specifies the horizontal alignment for the node label.                               | Server side          | HorizontalAlignment.Center | No                                                |
|                          |                                                                                      |                      |                            |                                                   |
|                          |                                                                                      |                      | HorizontalAlignment.Left   |                                                   |
|                          |                                                                                      |                      |                            |                                                   |
|                          |                                                                                      |                      | HorizontalAlignment.Right  |                                                   |
+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| LabelVerticalAlignment   | Specifies the vertical alignment for the node label.                                 | Server side          | VerticalAlignment.Bottom   | No                                                |
|                          |                                                                                      |                      |                            |                                                   |
|                          |                                                                                      |                      | VerticalAlignment.Center   |                                                   |
|                          |                                                                                      |                      |                            |                                                   |
|                          |                                                                                      |                      | VerticalAlignment.Top      |                                                   |
+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| LabelFontColor           | Gets or sets the color of the label. The default value is black.                     | Server side          | String                     | No                                                |
+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| LabelFontFamily          | Gets or sets the font family of the label. The default value is Arial.               | Server side          | FontFamily                 | No                                                |
+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| LabelFontSize            | Gets or sets the font size of the label. The default value is 11.                    | Server side          | Double                     | No                                                |
+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| LabelBackground          | Gets or sets the background of the label. The default value is Transparent.          | Server side          | string                     | No                                                |
+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| LabelBorderColor         | Gets or sets the border color of the label. The default value is Transparent.        | Server side          | String                     | No                                                |
+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| LabelBorderWidth         | Gets or sets the border width of the label. The default value is Transparent.        | Server side          | Int                        | No                                                |
+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| LabelWidth               | Gets or sets the width of the label. The default value is the node's width.          | Server side          | Double                     | No                                                |
+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+
| LabelHeight              | Gets or sets the height of the label. The default value is the  node's label height. | Server side          | Double                     | No                                                |
+--------------------------+--------------------------------------------------------------------------------------+----------------------+----------------------------+---------------------------------------------------+

[] 

The following code snippet illustrates the implementation of the properties mentioned in the table above.

More:







