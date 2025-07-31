---
title: labelorientation.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\labelorientation.md
created_at: 2025-07-03
---






#### Label Orientation {#label-orientation style="tab-stops: 0pt"}

Essential Diagram for WPF provides support to orient the LineConnector label as needed.

 

Use Case Scenarios

When the label overlaps with the nodes or connectors, it will not be legible. In such case you can use this feature to align the label to make it legible.

Properties

Table 41: Property Table


+------------------+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------------------+------------------------------+
| **Property**     | **Description**                           | **Type**                                      | **Data Type**                                                             | **Reference links**          |
+------------------+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------------------+------------------------------+
| LabelOrientation | Gets or sets a value to  orient the label | Dependency property[] | [LabelOrientation].Auto[] | NA[] |
|                  |                                           |                                               |                                                                           |                              |
|                  | []                  |                                               | [LabelOrientation]                                |                              |
|                  |                                           |                                               |                                                                           |                              |
|                  | Default Value is Auto.                    |                                               | .Horizontal                                                               |                              |
|                  |                                           |                                               |                                                                           |                              |
|                  |                                           |                                               | [LabelOrientation]                                |                              |
|                  |                                           |                                               |                                                                           |                              |
|                  |                                           |                                               | .Vertical\                                                                |                              |
|                  |                                           |                                               | \                                                                         |                              |
+------------------+-------------------------------------------+-----------------------------------------------+---------------------------------------------------------------------------+------------------------------+


[] 

Orienting the Label

You can orient the label using the **LabelOrientation** property*.* You can set this to Horizontal, Vertical or Auto. By default this is set to Auto.

 

The following code illustrates how to set the LabelOrientation to Auto:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [  ][LineConnector][ line = [new] [LineConnector]();] |
|                                                                                                                                                                                                                                                |
| [  ][line.LabelOrientation = Syncfusion.Windows.Diagram.[LabelOrientation].Auto;][]        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                        |
| **[]**                                                                                                                             |
|                                                                                                                                                                        |
| [Dim][ line [As] [New] LineConnector()] |
|                                                                                                                                                                        |
| [        line.LabelOrientation = Syncfusion.Windows.Diagram.LabelOrientation.Auto]                                                 |
|                                                                                                                                                                        |
| []                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 


{border="0"}Note: when this property is set to Auto, the label will be positioned along the angle of the line drawn.


 

\
{border="0"}

Figure 89: LabelOrientation is Auto

 

The following code illustrates how to set the LabelOrientation to Horizontal:

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                        |
| **[]**                                                                                                                                             |
|                                                                                                                                                                                        |
| [LineConnector][ line = [new] [LineConnector]();] |
|                                                                                                                                                                                        |
| [line.LabelOrientation = Syncfusion.Windows.Diagram.[LabelOrientation].Horizontal;][]  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                       |
|                                                                                                                                                                                        |
| **[]**                                                                                                                                             |
|                                                                                                                                                                                        |
| [LineConnector][ line = [new] [LineConnector]();] |
|                                                                                                                                                                                        |
| [line.LabelOrientation = Syncfusion.Windows.Diagram.[LabelOrientation].Horizontal;][]  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

\
{border="0"}

Figure 90: LabelOrientation is Horizontal

**\
\**
The following code illustrates how to set the LabelOrientation to Vertical:

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                |
| [LineConnector][ line = [new] [LineConnector]();]                         |
|                                                                                                                                                                                                                |
| [line.LabelOrientation = Syncfusion.Windows.Diagram.[LabelOrientation].Vertical;[ ]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                        |
| [Dim][ line [As] [New] LineConnector()] |
|                                                                                                                                                                        |
| [      line.LabelOrientation = Syncfusion.Windows.Diagram.LabelOrientation.Vertical]                                               |
|                                                                                                                                                                        |
| []                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 91: LabelOrientation is Vertical

**[]** 

[]{#related-topics}

