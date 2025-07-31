---
title: polyline2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\polyline2.md
created_at: 2025-07-03
---








  









### Polyline {#polyline style="tab-stops: 0pt"}

Line connectors can be used to draw polylines using the **IntermediatePoints** property. Polylines are drawn using intermediate points for straight lines and orthogonal line connectors. For orthogonal lines, intermediate points are updated so that the adjacent line segments are always perpendicular to each other. These intermediate points are visually represented as vertices.

 

**Polylines**

Straight line connectors can be used as polylines by using the **IntermediatePoints** property. This can be achieved at run time by holding CTRL + SHIFT and clicking on the line, or by simply changing the **IntermediatePoints** collection. This will be reflected in the line connector.

{border="0"}

Figure 65: Polyline

**Poly-Orthogonal Lines**

Orthogonal lines can have more than two intermediate points. All these intermediate points can be dragged. Unlike straight lines, orthogonal lines maintain their perpendicularity even after the intermediate points are dragged.

{border="0"}

Figure 66: Poly-Orthogonal Line

Use Case Scenarios

[[Polylines can be used in such cases as connecting elements in a flow chart.]]{.apple-style-span}

 

Properties

+----------------------------------------------+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| **Property**                                 | **Description**                                                       | **Type**                                                                            | **Data Type**                                                                               |
+----------------------------------------------+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| IntermediatePoints[] | Gets or sets the intermediate points.[]       | [[Server side.]]{.apple-style-span}[] | [[List\<DiagramPoint\>]]{.apple-style-span}[] |
+----------------------------------------------+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| LineDistributingEnabled                      | Gets or sets a value indicating whether line distributing is enabled. | [[Server side.]]{.apple-style-span}                           | [[Boolean]]{.apple-style-span}                                        |
|                                              |                                                                       |                                                                                     |                                                                                             |
|                                              | Default value is False.                                               |                                                                                     |                                                                                             |
+----------------------------------------------+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

 

Methods

+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **[Method ]**[] | **[Description ]**[] | **[Parameters ]**[] | **[Type ]**[] | **[Return Type ]**[] |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| setLineDistributingEnabled                                                                        | sets a value indicating whether line distributing is enabled/disabled.                                 | **LineId**---ID of the LineConnector,                                                                 | Client side                                                                                     | void.                                                                                                  |
|                                                                                                   |                                                                                                        |                                                                                                       |                                                                                                 |                                                                                                        |
|                                                                                                   |                                                                                                        | **Boolean value**---Enable(true)/Disable(false).                                                      |                                                                                                 |                                                                                                        |
+===================================================================================================+========================================================================================================+=======================================================================================================+=================================================================================================+========================================================================================================+

[] 

Sample Link

**Dashboard** \> **ASP.NET MVC** \> **Diagram** \> **Getting Started** \> **Line Connector Demo**

More:





