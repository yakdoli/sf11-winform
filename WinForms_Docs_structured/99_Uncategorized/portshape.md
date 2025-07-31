---
title: portshape.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\portshape.md
created_at: 2025-07-03
---








  









### PortShape {#portshape style="tab-stops: 0pt"}

[] 

Several predefined shapes have been provided for the ports. They are:

[] 

[·      ]Arrow

[·      ]Circle

[·      ]Diamond

[] 

Property:

[] 

+-------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------+---------------------------------------------------+
| Property    | Description                                                                                                                         | Type of the property                   | Value it accepts   | Any other dependencies/ sub properties associated |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------+---------------------------------------------------+
| PortShape   | The PortShape property specifies the shape to be used for the port. Three types of shapes are provided: Arrow, Circle, and Diamond. | [CLR Property] | PortShapes.None    | No                                                |
|             |                                                                                                                                     |                                        |                    |                                                   |
|             |                                                                                                                                     |                                        | PortShapes.Arrow   |                                                   |
|             |                                                                                                                                     |                                        |                    |                                                   |
|             | Default Value: PortShapes.Diamond                                                                                                   |                                        | PortShapes.Diamond |                                                   |
|             |                                                                                                                                     |                                        |                    |                                                   |
|             |                                                                                                                                     |                                        | PortShapes.Circle  |                                                   |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+--------------------+---------------------------------------------------+

 

The following code shows how a port shape can be selected for the port.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| [ConnectionPort][ port = [new] [ConnectionPort](NewClient);] |
|                                                                                                                                                                                                   |
| [            port.Left = 70;]                                                                                                                                 |
|                                                                                                                                                                                                   |
| [            port.Top = 90;]                                                                                                                                  |
|                                                                                                                                                                                                   |
| [            port.PortShape = [PortShapes].Arrow;]                                                                                    |
|                                                                                                                                                                                                   |
| [            NewClient.Ports.Add(port);]                                                                                                                      |
|                                                                                                                                                                                                   |
| [            [ConnectionPort] port1 = [new] [ConnectionPort](NewClient);]                |
|                                                                                                                                                                                                   |
| [            port1.Left = 10;]                                                                                                                                |
|                                                                                                                                                                                                   |
| [            port1.Top = 50;]                                                                                                                                 |
|                                                                                                                                                                                                   |
| [            port1.PortShape = [PortShapes].Circle;]                                                                                  |
|                                                                                                                                                                                                   |
| [            NewClient.Ports.Add(port1);]                                                                                                                     |
|                                                                                                                                                                                                   |
| [            [ConnectionPort] port2 = [new] [ConnectionPort](NewClient);]                |
|                                                                                                                                                                                                   |
| [            port2.Left = 120;]                                                                                                                               |
|                                                                                                                                                                                                   |
| [            port2.Top = 50;]                                                                                                                                 |
|                                                                                                                                                                                                   |
| [            port2.PortShape = [PortShapes].Diamond;]                                                                                 |
|                                                                                                                                                                                                   |
| [            NewClient.Ports.Add(port2);]                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [Dim][ port [As] [New] [ConnectionPort](NewClient)] |
|                                                                                                                                                                                                            |
| [            port.Left = 70]                                                                                                                                           |
|                                                                                                                                                                                                            |
| [            port.Top = 90]                                                                                                                                            |
|                                                                                                                                                                                                            |
| [            port.PortShape = PortShapes.Arrow]                                                                                                                        |
|                                                                                                                                                                                                            |
| [            NewClient.Ports.Add(port)]                                                                                                                                |
|                                                                                                                                                                                                            |
| [    [Dim] port1 [As] [New] [ConnectionPort](NewClient)]                        |
|                                                                                                                                                                                                            |
| [            port1.Left = 10]                                                                                                                                          |
|                                                                                                                                                                                                            |
| [            port1.Top = 50]                                                                                                                                           |
|                                                                                                                                                                                                            |
| [            port1.PortShape = PortShapes.Circle]                                                                                                                      |
|                                                                                                                                                                                                            |
| [            NewClient.Ports.Add(port1)]                                                                                                                               |
|                                                                                                                                                                                                            |
| [    [Dim] port2 [As] [New] [ConnectionPort](NewClient)]                        |
|                                                                                                                                                                                                            |
| [            port2.Left = 120]                                                                                                                                         |
|                                                                                                                                                                                                            |
| [            port2.Top = 50]                                                                                                                                           |
|                                                                                                                                                                                                            |
| [            port2.PortShape = PortShapes.Diamond]                                                                                                                     |
|                                                                                                                                                                                                            |
| [            NewClient.Ports.Add(port2)][]                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

NewClient is the Node of Diagram Page.

[] 

{border="0"}

Figure 74: Port Shapes[]{#p53}

[]{#related-topics}

