---
title: virtualizationfordiagramcontrol1.md
original_path: WinForms_Docs/04_Controls/Diagram/virtualizationfordiagramcontrol1.md
created_at: 2025-08-05
---








  









### Virtualization for DiagramControl {#virtualization-for-diagramcontrol style="tab-stops: 0pt"}

 

Virtualization

Virtualization is the process of loading the diagram page elements that are available in the visible area of the diagram control, i.e page elements that lie within the viewport of the ScrollViewer will be in loaded state and the rest will not be loaded until they come into view.

This feature gives optimizable performance while loading and dragging items to diagram control when many Nodes and LineConnectors are added in the diagram page.

 

Use Case Scenarios

The loading time and the UI response will be proportional to the number of elements used in a page. When you want to display a page with large number of Nodes and LineConnectors, such as floor plan application, the processing speed will be slow in user interaction. If virtualization is enabled, application will load only elements that lie in the visible area. This leads to fast loading and fast user interactivity.

 

Tables for Properties, Methods, and Events

Properties[]

*[Table ][66][: Property/ies Table]*


+----------------+--------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+-----------------+
| Property       | Description                                                                                                              | Type                | Data Type   | Reference links |
+----------------+--------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+-----------------+
| Enable         | Gets or sets a value indicating whether the diagram page can be virtualized. The default value is set to false.          | Dependency Property | Boolean     | No              |
|                |                                                                                                                          |                     |             |                 |
| Virtualization |                                                                                                                          |                     |             |                 |
+----------------+--------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+-----------------+
| Enable         | Gets or sets a value indicating whether the loaded object in diagram page can be virtualized. The default value is true. | Dependency Property | Boolean     |                 |
|                |                                                                                                                          |                     |             |                 |
| Caching        |                                                                                                                          |                     |             |                 |
+----------------+--------------------------------------------------------------------------------------------------------------------------+---------------------+-------------+-----------------+


 

Adding Virtualization feature to an Application

EnableVirtualization Property:

To enable virtualization set the *EnableVirtualization* property to true. Page elements within the viewport alone will be loaded. The default value is false.

The property is in DiagramView and can be set in the following methods.

[·      ]Through XAML.

[·      ]Through Code behind.

 

The following code illustrates how to set EnableVirtualization property through XAML.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<!\-\--DiagramControl\-\--\>         ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [             ][\<][syncfusion][:][DiagramControl][ [ Name][=\"diagramControl\" \>]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                ][\<][syncfusion][:][DiagramControl.Model][\>][]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                    ][\<][syncfusion][:][DiagramModel][  [ x][:][Name][=\"diagramModel\" \>]]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                    ][\</][syncfusion][:][DiagramModel][\>][]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                ][\</][syncfusion][:][DiagramControl.Model][\>][]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                ][\<][syncfusion][:][DiagramControl.View][\>][]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                   ][\<][syncfusion][:][DiagramView ][EnableVirtualization][=\"True\" ][Name][=\"diagramView\" ][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                    ][\</][syncfusion][:][DiagramView][\>][]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                ][\</][syncfusion][:][DiagramControl.View][\>][]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [            ][\</][syncfusion][:][DiagramControl][\>]**[]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code illustrates how to set EnableVirtualization property through Code behind.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                           |
| [DiagramView][ diagramView = [new] [DiagramView]();] |
|                                                                                                                                                                                           |
| [diagramView.EnableVirtualization = [true]; ][]                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                      |
|                                                                                                                                                                                                       |
| [Dim][ diagramView [As] [New] [DiagramView]()] |
|                                                                                                                                                                                                       |
| [diagramView.EnableVirtualization = [True]][ ][]                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

EnableCaching Property:

*EnableCaching* decides whether the element should be in loaded state or unloaded state, when the element is outside the viewport area. To set the element in unloaded state set the *EnableCaching* to false. To set it in loaded state set the *EnableCaching* to true.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                           |
| [DiagramView][ diagramView = [new] [DiagramView]();] |
|                                                                                                                                                                                           |
| [diagramView.EnableCaching = [true]; ][]                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                 |
| [Dim][ diagramView [As] [New] [DiagramView]()]           |
|                                                                                                                                                                                                                 |
| [diagramView.][EnableCaching][ = [True]][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Node/LineConnector AllowVirtualization Property:

AllowVirtualization property is used to enable/disable the Node/LineConnector virtualization. When AllowVirtualization is set to false for an element that lies outside the viewport, It will be in loaded state when Virtualization is enabled. The default value is true.

The AllowVirtualization property can be set as given in the following code.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                      |
|                                                                                                                                                                                                       |
| [//Node Virtualization]                                                                                                                             |
|                                                                                                                                                                                                       |
| [Node][ NodeObject = [new] [Node]();[]]    |
|                                                                                                                                                                                                       |
| [NodeObject.AllowVirtualization = [true];]                                                                                                   |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [//LineConnector Virtualization  ][]                                                                          |
|                                                                                                                                                                                                       |
| [LineConnector][ LineConnectorObject = [new] [LineConnector]();] |
|                                                                                                                                                                                                       |
| [LineConnectorObject.AllowVirtualization = [true];][]                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                 |
| [\'Node Virtualization]                                                                                                                                       |
|                                                                                                                                                                                                                 |
| [Dim][ NodeObject [As] [New] [Node]()]                   |
|                                                                                                                                                                                                                 |
| [NodeObject.AllowVirtualization = [True]]                                                                                                              |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                 |
| [\'LineConnector Virtualization]                                                                                                                              |
|                                                                                                                                                                                                                 |
| [Dim][ LineConnectorObject [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                                 |
| [LineConnectorObject.AllowVirtualization = [True]][]                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Limitations:

Due to virtualization behavior there are some limitations  in the diagram control. They are:

1.   As Gridlines and Rulers are not visualized, when node or line connector is placed at a distance for example 2,000,000 pixels away, rendering will take place from zero to end. This leads to performance issues in rendering Gridlines or Rulers.

2.   Save and load is not supported for Nodes and LineConnectors that are in unloaded state.

3.   When diagram is virtualized, many nodes will be in unloaded state and their Width and Height will not be set. As the automatic layout depends on the size of the node, predefined width and height for the node is required for updating the layout.

 

[]{#related-topics}

