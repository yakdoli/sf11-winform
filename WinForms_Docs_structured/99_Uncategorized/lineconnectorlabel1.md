---
title: lineconnectorlabel1.md
original_path: WinForms_Docs/99_Uncategorized/lineconnectorlabel1.md
created_at: 2025-08-05
---








  









### Line Connector Label {#line-connector-label style="tab-stops: 0pt"}

[] 

A Label is a single line or multiline text that is displayed over the Node. This Label is used to textually represent a LineConnector with a string that can be edited in run time. There are many properties used to change the alignment and appearance settings. Label can be represented as multiline text using the TextWrapping property.

 

Properties\
\

+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| Property                 | Description                                                                                        | Type of the property | Value it accepts              | Any other dependencies/ sub properties associated |
+==========================+====================================================================================================+======================+===============================+===================================================+
| IsLabelEditable          | Gets or sets a value indicating whether the line's label can be edited or not. Default value: True | Dependency property  | Boolean (true/ false)         | No                                                |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| Label                    | Gets or sets the line\'s label. Default value: Empty String                                        | Dependency property  | String                        | No                                                |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelTemplate            | Gets or sets a template for the label. Default value: null                                         | Dependency property  | DataTemplate                  | No                                                |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelVisibility          | Gets or sets the label visibility. Default value: Visibility.Visible                               | Dependency property  | Visibility.Hidden             | No                                                |
|                          |                                                                                                    |                      |                               |                                                   |
|                          |                                                                                                    |                      | Visibility.Collapsed          |                                                   |
|                          |                                                                                                    |                      |                               |                                                   |
|                          |                                                                                                    |                      | Visibility.Visible            |                                                   |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelHorizontalAlignment | Gets or sets the node's label horizontal Alignment. Default value: HorizontalAlignment.Center      | Dependency property  | HorizontalAlignment.Center    | No                                                |
|                          |                                                                                                    |                      |                               |                                                   |
|                          |                                                                                                    |                      | HorizontalAlignment.Left      |                                                   |
|                          |                                                                                                    |                      |                               |                                                   |
|                          |                                                                                                    |                      | HorizontalAlignment.Right     |                                                   |
|                          |                                                                                                    |                      |                               |                                                   |
|                          |                                                                                                    |                      | HorizontalAlignment.Stretch   |                                                   |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelForeground          | Gets or sets the label foreground. Default value is Black.                                         | Dependency property  | Brush                         | No                                                |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelBackground          | Gets or sets the label background. The default value is White.                                     | Dependency property  | Brush                         | No                                                |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontStyle           | Gets or sets the label background. The default value is White.                                     | Dependency property  | FontStyle                     | No                                                |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontFamily          | Gets or sets the label font family. The default value is Arial.                                    | Dependency property  | FontFamily                    | No                                                |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontSize            | Gets or sets the label font size. The default value is 11.                                         | Dependency property  | Double                        | No                                                |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelFontWeight          | Gets or sets the label font weight. The default value is SemiBold.                                 | Dependency property  | FontWeight                    | No                                                |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelTextWrapping        | Gets or sets the label text wrapping. The default value is NoWrap.                                 | Dependency property  | TextWrapping.NoWrap           | No                                                |
|                          |                                                                                                    |                      |                               |                                                   |
|                          |                                                                                                    |                      | TextWrapping.Wrap             |                                                   |
|                          |                                                                                                    |                      |                               |                                                   |
|                          |                                                                                                    |                      | TextWrapping.WrapWithOverflow |                                                   |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+
| LabelWidth               | Gets or sets the label width. The default value is the line's width.                               | Dependency property  | Double                        | No                                                |
+--------------------------+----------------------------------------------------------------------------------------------------+----------------------+-------------------------------+---------------------------------------------------+

 

[] 

A connector can be specified with a label, similar to the node, using the **Label** property. The default value is an empty string. By default, the label starts at the center point of the connector.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [LineConnector][ l1 = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [l1.HeadNode = n1;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.TailNode = n2;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.ConnecorType = [ConnectorType].Bezier;]                                                                              |
|                                                                                                                                                                                      |
| [l1.Label = [\"Connect\"];]                                                                                              |
|                                                                                                                                                                                      |
| [diagramModel.Connections.Add(l1);]                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ l1 [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [l1.HeadNode = n1]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.TailNode = n2]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.ConnecorType = ConnectorType.Bezier]                                                                                                                   |
|                                                                                                                                                                                                |
| [l1.Label = \"Connect\"]                                                                                                                                   |
|                                                                                                                                                                                                |
| [diagramModel.Connections.Add(l1)][]                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 68: Connector\'s Label**[]**

 

[]{#p45} 

[]{#_How_to_specify_16}Label Template

[] 

A user can set a custom template for the labels. The following code shows the setting of set a label template. First create a control template, then add the resource "text.png" to your application.    

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [\<][ControlTemplate][ [x][:][Key][=\"LabelCustomTemplate\"\>]]                                                   |
|                                                                                                                                                                                                                                                                                                                                                |
| [\<][StackPanel][ [Orientation][=\"Horizontal\"\>]]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [\<][Image][ [Source][=\"text.png\"] [Width][=\"20\"] [Height][=\"20\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                |
| [\<][Border][ [Background][=\"AliceBlue\"\>]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                |
| [\<][TextBlock][ [Text][=\"Hello\"/\>]]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                |
| [\</][Border][\>]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [\</][StackPanel][\>]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                |
| [\</][ControlTemplate][\>]                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The template can then be applied to the connector as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [LineConnector][ l1 = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [l1.HeadNode = n1;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.TailNode = n2;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.ConnectorType = [ConnectorType].Bezier;]                                                                             |
|                                                                                                                                                                                      |
| [l1.LabelTemplate = ([ControlTemplate])FindResource([\"LabelCustomTemplate\"]);]                 |
|                                                                                                                                                                                      |
| [diagramModel.Connections.Add(l1);]                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ l1 [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [l1.HeadNode = n1]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.TailNode = n2]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.ConnectorType = ConnectorType.Bezier]                                                                                                                  |
|                                                                                                                                                                                                |
| [l1.LabelTemplate = [CType](FindResource(\"LabelCustomTemplate\"), ControlTemplate)]                                                  |
|                                                                                                                                                                                                |
| [diagramModel.Connections.Add(l1)][]                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

This displays the text \"Hello\" on an Alice Blue background with an image on the left.

[] 

{border="0"}

Figure 69: Label Template**[]**

[]{#p46}Multi line label

**[]** 

The Label text can be displayed in multiple lines using LabelTextWrapping property set to Wrap,. If there is no enough space for the text to get displayed within the connector in a single line, the text will get wrapped within connector boundaries or LabelWidth and starts to display the label in multiple lines.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| []                                                                                                                                |
|                                                                                                                                                                                     |
| [LineConnector][ l = [new] [LineConnector]();] |
|                                                                                                                                                                                     |
| [l.Label = [\"This is a Multiline Label for Connectors\"];]                                                             |
|                                                                                                                                                                                     |
| [l.LabelHeight = 110;]                                                                                                                          |
|                                                                                                                                                                                     |
| [l.LabelTextWrapping = [TextWrapping].Wrap;]                                                                            |
|                                                                                                                                                                                     |
| [l.IsLabelEditable = [true];]                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [Dim][ l [As] [New] [LineConnector]()] |
|                                                                                                                                                                                               |
| [l.Label = \"This [is] a Multiline Label [for] Connectors\"]                                                    |
|                                                                                                                                                                                               |
| [l.LabelHeight = 110]                                                                                                                                     |
|                                                                                                                                                                                               |
| [l.LabelTextWrapping = TextWrapping.Wrap]                                                                                                                 |
|                                                                                                                                                                                               |
| [l.IsLabelEditable = [True]][]                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

{border="0"}

 

 

[]{#_How_to_edit_1}Label Editing

[] 

A connector\'s label can be edited at run time by setting **IsLabelEditable** to true. The following code shows how it can be done.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [LineConnector][ l1 = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [l1.Shape = [Shapes].RoundedRectangle;]                                                                                  |
|                                                                                                                                                                                      |
| [l1.IsLabelEditable = [true];]                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ l1 [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [l1.Shape = Shapes.RoundedRectangle]                                                                                                                       |
|                                                                                                                                                                                                |
| [l1.IsLabelEditable = [True]][]                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A user can specify a label at run time by:

[] 

1.   Double-click the left mouse button on any part of the connector. A text box will appear with the cursor at the beginning.

2.   Now type the label name and press ENTER. The label will be displayed on the connector. Press ESC key if you do not want to apply the new label value.

[] 

{border="0"}

Figure 70: Connector Label[]{#p47}

[]{#_How_to_specify_17}Label Visibility

[] 

A label\'s visibility can be changed using the **LabelVisibility** property. The default value is visible.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [LineConnector][ l1 = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [l1.LabelVisibility = [Visibility].Hidden;]                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ l1 [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [l1.LabelVisibility = Visibility.Hidden][]                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The label will not get displayed.

 

Custom Label Support for LineConnector

This feature enables you to customize the Label Position of the LineConnector. The **CustomLabelPosition** properties for LineConnector are Auto, Drag and Custom.

[·      ]**Drag**: The label can be dragged

[·      ]**Auto:** Label position and angle will be updated internally based on the position of the LineConnector. This is the default value.

[·      ]**Custom:** You can customize the Label position

We can also set the Label Position using LabelPosition property of the LineConnector.

 

+---------------------+------------------------------------------------------------------------------+----------------------+-----------------------------+---------------------------+---------------------------------------------------+
| Property            | Description                                                                  | Type                 | Value It Accepts            | Default Values            | Any other dependencies/ sub properties associated |
+---------------------+------------------------------------------------------------------------------+----------------------+-----------------------------+---------------------------+---------------------------------------------------+
| LabelPosition       | Gets or sets the Position of the LineConnector's Label from the DiagramPage. | Dependency  property | Point                       | Point(0,0)                | No                                                |
|                     |                                                                              |                      |                             |                           |                                                   |
|                     |                                                                              |                      |                             |                           |                                                   |
+---------------------+------------------------------------------------------------------------------+----------------------+-----------------------------+---------------------------+---------------------------------------------------+
| CustomLabelPosition | Gets or sets the Label of LineConnector is Dragging or Not.                  | Dependency  property | Enum.                       | CustomLabelPositions.Auto | No                                                |
|                     |                                                                              |                      |                             |                           |                                                   |
|                     |                                                                              |                      | CustomLabelPositions.Auto   |                           |                                                   |
|                     |                                                                              |                      |                             |                           |                                                   |
|                     |                                                                              |                      | CustomLabelPositions.Custom |                           |                                                   |
|                     |                                                                              |                      |                             |                           |                                                   |
|                     |                                                                              |                      | CustomLabelPositions.Drag   |                           |                                                   |
+---------------------+------------------------------------------------------------------------------+----------------------+-----------------------------+---------------------------+---------------------------------------------------+
| LabelAngle          | Gets or sets the angle of the Label of LineConnector.                        | Dependency  property | double                      | 0                         | No                                                |
+---------------------+------------------------------------------------------------------------------+----------------------+-----------------------------+---------------------------+---------------------------------------------------+

[] 

Adding Custom Label Enhancements for LineConnector to an Application

**[]** 

Label Dragging support for LineConnector

The Label can be dragged from the Line Connector.


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [       ][(line [as] [LineConnector]).CustomLabelPosition = [CustomLabelPositions].Drag;] |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

Set the LabelPosition for LineConnector

When the values are given the position of the label will be exactly at the point of the specified values.


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| [       ][(line [as] [LineConnector]).LabelPosition = [new] [Point](100,100);] |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

Set the LabelAngle for LineConnector

The labels rotate when values are given for the lable angle.


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                              |
| [       ][(line [as] [LineConnector]).LabelAngle = 45;] |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

[]{#related-topics}

