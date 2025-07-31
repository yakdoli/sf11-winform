---
title: customizeportstyle.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\customizeportstyle.md
created_at: 2025-07-03
---








  









### Customize PortStyle {#customize-portstyle style="tab-stops: 0pt"}

The port shapes can be customized by specifying the property values under the **PortStyle** property.

 

Table 47: Property Table[]

  ----------- ------------------------------------------------------------------------ ---------------------------------------- ------------------ ---------------------------------------------------
  Property    Description                                                              Type of the property                     Value it accepts   Any other dependencies/ sub properties associated
  PortStyle   The PortStyle property provides option for the customization of ports.   CLR [property]   PortStyle          No
  ----------- ------------------------------------------------------------------------ ---------------------------------------- ------------------ ---------------------------------------------------

[] 

The various properties under the PortStyle property are,[]

[·      ]Fill---Specifies the color to be used to fill the port.

[·      ]StrokeThickness---Specifies the thickness value of the port\'s border.

[·      ]Stroke---Specifies the color to be used for the border of the port.

[·      ]StrokeStartLineCap---Specifies the shape used at the start of a line or segment.

[·      ]StrokeEndLineCap---Specifies the shape at the end of a line or segment.

[·      ]StrokeLineJoin---Specifies the shape that joins two lines or segments.

[] 

The following code shows how to set some of these properties.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [Node][ node = [new] [Node]([Guid].NewGuid(), [\"Node1\"]);] |
|                                                                                                                                                                                                                                                   |
| [node.Shape = [Shapes].RoundedSquare;]                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| [node.Width = 150;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [node.Height = 50;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [node.OffsetX = 250;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| [node.OffsetY = 100;]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [ConnectionPort][ port = [new] [ConnectionPort]();]                                                          |
|                                                                                                                                                                                                                                                   |
| [port.Left = 50;]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [port.Top = 0;]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                   |
| [port.Node = node;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [port.PortShape = [PortShapes].Diamond;]                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [port.PortStyle.Fill = [Brushes].Orange;]                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [port.PortStyle.Stroke = [Brushes].Red;]                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [node.Ports.Add(port);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [diagramModel.Nodes.Add(node);]                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [Dim][ node [As] [New] [Node]([Guid].NewGuid(), [\"Node1\"])] |
|                                                                                                                                                                                                                                                                      |
| [node.Shape = Shapes.RoundedSquare]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [node.Width = 150]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [node.Height = 50]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [node.OffsetX = 250]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [node.OffsetY = 100]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [Dim][ port [As] [New] [ConnectionPort]()]                                                                    |
|                                                                                                                                                                                                                                                                      |
| [port.Left = 50]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [port.Top = 0]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [port.Node = node]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [port.PortShape = PortShapes.Diamond]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                      |
| [port.PortStyle.Fill = Brushes.Orange]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [port.PortStyle.Stroke = Brushes.Red]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                      |
| [node.Ports.Add(port)]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [diagramModel.Nodes.Add(node)][]                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 96: Port Style[]

CustomPathStyle

The CustomPathStyle property enables you to customize the appearance of ConnectionPort.

 

**Properties**

Table 48: Property/ies Table


  ----------------- ----------------------------------------------- --------------------- ----------- -----------------
  Property          Description                                     Type                  Data Type   Reference links
  CustomPathStyle   Get or Set CustomPathStyle for ConnectionPort   Dependency Property   Style       NA
  ----------------- ----------------------------------------------- --------------------- ----------- -----------------


[] 

Adding CustomPathStyle for ConnectionPort to an Application

Appearance of the ConnectionPort can be customized by applying style for the *CustomPathStyle* property. Style can be applied for *CustomPathStyle* as illustrated in the following code:

 

Through XAML

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [         \<][Style][ TargetType][=\"{][x][:][Type][ syncfusion][:][ConnectionPort][}\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [            ][\<][Setter][ Property][=\"PortShape\"][ Value][=\"Diamond\"/\>]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [            ][\<][Setter][ Property][=\"CustomPathStyle\" \>]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                ][\<][Setter.Value][\>]                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                    ][\<][Style][ TargetType][=\"{][x][:][Type][ Path][}\"\>]                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                        ][\<][Setter][ Property][=\"Stroke\"][ Value][=\"Red\" /\>]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                        ][\<][Setter][ Property][=\"StrokeThickness\"][ Value][=\"3\"/\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                    ][\</][Style][\>]                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                ][\</][Setter.Value][\>]                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [            ][\</][Setter][\>]                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [          ][\</][Style][\>]**[]**                                                                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 {border="0"}

Figure 97: Custom ConnectionPort using CustomPathStyle

 

 

 

[]{#related-topics}

