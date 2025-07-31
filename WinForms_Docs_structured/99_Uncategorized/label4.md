---
title: label4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\label4.md
created_at: 2025-07-03
---








  









### Label {#label style="tab-stops: 0pt"}

A label is a text object that is attached to a node and is positioned relative to node coordinates. This enables you to format the label text.  You can also customize the appearance of the label. You can bind the node name to the label so that the name will be displayed as the label text. This can be achieved using the *PropertyBinding* property.

 

The following formatting options are supports for the label text:

 

[·      ]WrapText

[·      ]HorizontalAlignment

[·      ]VerticalAlignment

[·      ]DirectionRightToLeft

[·      ]DirectionVertical

[·      ]TextCase

[·      ]NoClip

[·      ]LineLimit

[·      ]FitBlackBox

[·      ]MeasureTrailingSpace

 

The following options are supports for customizing the appearance of the label.

 

[·      ]BackGroundStyle

[·      ]FontColorStyle

[·      ]FontStyle

 

Use Case Scenarios                            

When you are drawing a Business Process Flow Diagram, using this support, you can name the node representing the stage.

 

Tables for Properties and Methods

Properties

 

Table 1: Properies Table


+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| **Property**          | **Description**                                                                                                                                       | **Type**    | **Data Type**        | **Reference links** |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| Name                  | Used to specify the name of a label.                                                                                                                  | NA          | string               | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| FullName              | Used to specify the full name of a label.                                                                                                             | NA          | string               | NA                  |
|                       |                                                                                                                                                       |             |                      |                     |
|                       | Label container's name is prefixed with its name.                                                                                                     |             |                      |                     |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| ReadOnly              | Used to add a flag indicating whether the text object is Read-only or not.                                                                            | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| Visible               | Specifies the visibility of the label.                                                                                                                | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| FontColorStyle        | Specifies the font color style.                                                                                                                       | NA          | FillStyle            | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| BackgroundStyle       | Specifies the text background style.                                                                                                                  | NA          | FillStyle            | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| Text                  | Gets or sets the label text.                                                                                                                          | NA          | String               | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| FontStyle             | Specifies the font style.                                                                                                                             | NA          | FontStyle            | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| PropertyBinding       | Binds the text value of the label to the Text property.                                                                                               | NA          | LabelPropertyBinding | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| Size                  | Gets or sets the label text size.                                                                                                                     | NA          | SizeF                | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| SizeToNode            | Set the node size to label size. This can be enabled  if the node has only one label and label\'s position is center.                                 | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| UpdatePosition        | Gets or Sets whether default positioning has to be used.                                                                                              | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| AdjustRotationAngle   | Gets or Sets whether the label should remain horizontal on rotation of the node.                                                                      | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| TextCase              | Gets or sets the case of the text in the label.                                                                                                       | NA          | TextCases            | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| HorizontalAlignment   | Gets or sets the horizontal alignment of the text.                                                                                                    | NA          | StringAlignment      | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| VerticalAlignment     | Gets or sets the vertical alignment of the text.                                                                                                      | NA          | StringAlignment      | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| FormatFlags           | Gets the flags used to format the text.                                                                                                               | NA          | StringFormatFlags    | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| WrapText              | Gets or sets a value indicating whether text should be wrapped, when it exceeds the width of the bounding box.                                        | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| DirectionRightToLeft  | Gets or sets a value indicating whether the text is right to left.                                                                                    | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| DirectionVertical     | Gets or sets a value indicating whether the text is vertical.                                                                                         | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| FitBlackBox           | Gets or sets a value indicating whether no part of any glyph overhangs the label bounds.                                                              | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| LineLimit             | Gets or sets a value indicating whether only entire lines are laid out in the formatting rectangle.                                                   | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| MeasureTrailingSpaces | Gets or sets a value indicating whether space at the end of each line in calculations that measure the size of the text.                              | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| NoClip                | Gets or sets a value indicating whether overhanging parts of glyphs and unwrapped text reaching outside the formatting rectangle are allowed to show. | NA          | Boolean              | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| OffsetX               | Gets or sets the label offset x in percent relative to node\'s width from node\'s top left point.                                                     | NA          | float                | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| OffsetY               | Gets or sets the label offset y in percent relative to node\'s width from node\'s top left point.                                                     | NA          | float                | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+
| Position              | Gets or sets the position of the label.                                                                                                               | NA          | Position             | NA                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------------+---------------------+


[] 

Methods

 

Table 2: Methods Table


  **[Method ]**[]   **[Description ]**[]   **[Parameters ]**[]   **[Type ]**[]   **[Return Type ]**[]   **[Reference links ]**[]
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  GetPosition                                                                                                                                                                                                     Gets the label position in the node coordinates.                                                                                                                                                                     Empty                                                                                                                                                                                                               NA                                                                                                                                                                                                            PointF                                                                                                                                                                                                               NA
  GetStringFormat                                                                                                                                                                                                 Creates a StringFormat object that encapsulates the properties of the text object.                                                                                                                                   Empty                                                                                                                                                                                                               NA                                                                                                                                                                                                            StringFormat                                                                                                                                                                                                         NA


[] 

[] 

Adding a Label to an Application

You can create label as illustrated in the following code example:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                  |
| [RoundRect][ node = [new] [RoundRect](0, 0, 170, 100,[MeasureUnits].Pixel);]                                                        |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [            [//Create a label with predefined position]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                  |
| [            Syncfusion.Windows.Forms.Diagram.[Label] lbl_TopCenter = [new] Syncfusion.Windows.Forms.Diagram.[Label](node, [\"Label_TopCenter\"]);            ] |
|                                                                                                                                                                                                                                                                                                  |
| [            [//Postion the label]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_TopCenter.Position = [Position].TopCenter; ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                  |
| [            [/\* Position enum has the values Center, TopLeft, TopCenter, TopRight, MiddleLeft, MiddleRight, BottomLeft, BottomCenter, BottomRight and Custom \*/]]                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                  |
| [            [//Apply font style]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_TopCenter.FontStyle.Bold = [true];]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_TopCenter.FontStyle.Family = [\"Corbel\"];]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_TopCenter.FontStyle.Size = 9;]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                  |
| [            [//Add the label to node\'s label collection]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                  |
| [            node.Labels.Add(lbl_TopCenter);            ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [            [//Create a lable with custom position]]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                  |
| [            Syncfusion.Windows.Forms.Diagram.[Label] lbl_Custom = [new] Syncfusion.Windows.Forms.Diagram.[Label](node, [\"Label_Custom\"]);]                   |
|                                                                                                                                                                                                                                                                                                  |
| [            [//Postion the label]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_Custom.Position = [Position].Custom;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_Custom.OffsetX = 0;]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_Custom.OffsetY = 0;]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                  |
| [            [//Apply font style]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_Custom.FontStyle.Bold = [true];]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_Custom.FontStyle.Family = [\"Corbel\"];]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_Custom.FontStyle.Size = 9;]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                  |
| [            [//Format the label text]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_Custom.HorizontalAlignment = [StringAlignment].Center;]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                  |
| [            lbl_Custom.VerticalAlignment = [StringAlignment].Far;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                  |
| [            [//WrapText is set to true by default]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                  |
| [            [//Add the label to node\'s label collection]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                  |
| [            node.Labels.Add(lbl_Custom);]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| [            [//Add the node to diagram model]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                  |
| [            diagram1.Model.AppendChild(node);][  ]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [Dim][ node [As] [New] RoundRect(0, 0, 170, 100,MeasureUnits.Pixel)]                                                         |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [                  \'Create a label with predefined position][]                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [                  [Dim] lbl_TopCenter [As] [New] Syncfusion.Windows.Forms.Diagram.Label(node, [\"Label_TopCenter\"])]           |
|                                                                                                                                                                                                                                                             |
| [                  \'Postion the label][]                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [                  lbl_TopCenter.Position = Position.TopCenter]                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [                  \' Position enum has the values Center, TopLeft, TopCenter, TopRight, MiddleLeft, MiddleRight, BottomLeft, BottomCenter, BottomRight and Custom][] |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [                  \'Apply font style][]                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [                  lbl_TopCenter.FontStyle.Bold = [True]]                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| [                  lbl_TopCenter.FontStyle.Family = [\"Corbel\"]]                                                                                                                               |
|                                                                                                                                                                                                                                                             |
| [                  lbl_TopCenter.FontStyle.Size = 9]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [                  \'Add the label to node\'s label collection][]                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [                  node.Labels.Add(lbl_TopCenter)]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [                  \'Create a lable with custom position][]                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [                  [Dim] lbl_Custom [As] [New] Syncfusion.Windows.Forms.Diagram.Label(node, [\"Label_Custom\"])]                 |
|                                                                                                                                                                                                                                                             |
| [                  \'Postion the label][]                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [                  lbl_Custom.Position = Position.Custom]                                                                                                                                                               |
|                                                                                                                                                                                                                                                             |
| [                  lbl_Custom.OffsetX = 0]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [                  lbl_Custom.OffsetY = 0]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [                  \'Apply font style][]                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [                  lbl_Custom.FontStyle.Bold = [True]]                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [                  lbl_Custom.FontStyle.Family = [\"Corbel\"]]                                                                                                                                  |
|                                                                                                                                                                                                                                                             |
| [                  lbl_Custom.FontStyle.Size = 9]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [                  \'Format the label text][]                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [                  lbl_Custom.HorizontalAlignment = StringAlignment.Center]                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [                  lbl_Custom.VerticalAlignment = StringAlignment.Far]                                                                                                                                                  |
|                                                                                                                                                                                                                                                             |
| [                  \'WrapText is true by default][]                                                                                                                   |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [                  \'Add the label to node\'s label collection][]                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [                  node.Labels.Add(lbl_Custom)]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [                  \'Add the node to diagram model][]                                                                                                                 |
|                                                                                                                                                                                                                                                             |
| [                  diagram1.Model.AppendChild(node)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [  ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

*[Figure ][47][: Label ]*

 

 

[]{#related-topics}

