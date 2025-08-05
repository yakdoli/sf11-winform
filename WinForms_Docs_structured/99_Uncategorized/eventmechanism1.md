---
title: eventmechanism1.md
original_path: WinForms_Docs/99_Uncategorized/eventmechanism1.md
created_at: 2025-08-05
---








  









## Event Mechanism {#event-mechanism style="tab-stops: 0pt"}

This section describes the events that are triggered and handled when using Essential Diagram Silverlight.[]

Events for Nodes and Connections

DiagramControl has events, which respond to actions performed on nodes and connections.[]

Event Table

The events that are triggered and handled when using Essential Diagram Silverlight are described in the following tabulation:

Table 17: Events Table


+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| Event                                                     | Description                                                   | Arguments                                                                               | Type            |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeClick[]                       | Raised when the Node is clicked.\                             | Node - The Node on which the event is raised.[]                 | RoutedEvent     |
|                                                           | This event cannot be cancelled.[]     |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeDoubleClick                                           | Raised when the Node is double-clicked.\                      | Node - The Node on which the event is raised.                                           | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeStartLabelEdit                                        | Raised when the label editing for the Node has started.\      | NewLabelValue - The new label value.                                                    | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | OldLabelValue - The old label value.                                                    |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | Node - The Node on which the event is raised.                                           |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeLabelChanged                                          | Raised when the Node\'s label value is changed.\              | NewLabelValue - The new label value.                                                    | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | OldLabelValue - The old label value.                                                    |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | Node - The Node on which the event is raised.                                           |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeDragStart                                             | Raised when the Node is dragged.\                             | Node - The Node on which the event is raised.                                           | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeDragEnd                                               | Raised when the drag operation on the Node is completed.      | Node - The Node on which the event is raised.                                           | RoutedEvent     |
|                                                           |                                                               |                                                                                         |                 |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeResizing                                              | Raised when the resize operation is being performed.\         | Node - The Node on which the event is raised.                                           | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeResized                                               | Raised after the Node is resized.\                            | Node - The Node on which the event is raised.                                           | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeRotationChanging                                      | Raised when the Node is being rotated.\                       | Node - The Node on which the event is raised.                                           | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeRotationChanged                                       | Raised after the Node is rotated.\                            | Node - The Node on which the event is raised.                                           | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| ConnectorDoubleClick                                      | Raised when the Connector is double-clicked.\                 | Connector - The Connector on which the event is raised.                                 | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | HeadNode - The HeadNode of the Connector.                                               |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | TailNode - The TailNode of the Connector.                                               |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| ConnectorStartLabelEdit                                   | Raised when the label editing for the Connector has started.\ | Connector - The Connector on which the event is raised.                                 | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               | HeadNode - The HeadNode of the Connector.                                               |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | TailNode - The TailNode of the Connector.                                               |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | OldLabelValue - The old label value.                                                    |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| ConnectorLabelChanged                                     | Raised when the Connector\'s label value is changed.\         | Connector - The Connector on which the event is raised.                                 | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               | HeadNode - The HeadNode of the Connector.                                               |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | TailNode - The TailNode of the Connector.                                               |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | OldLabelValue - The old label value.                                                    |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | NewLabelValue - The new label value.                                                    |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| ConnectorDragStart                                        | Raised when either end of the Connector is dragged.\          | Connector - The Connector on which the event is raised.                                 | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | FixedNodeEnd - The Node on which the Connector is fixed.                                |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | MovableNodeEnd - The old Node on which the Connector was connected.                     |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| ConnectorDragEnd                                          | Raised when the drag operation is completed.\                 | Connector - The Connector on which the event is raised.                                 | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | FixedNodeEnd - The Node on which the Connector is fixed.                                |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | HitNodeEnd - The new Node on which the Connector is getting connected.                  |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeDrop                                                  | Raised when a shape from SymbolPalette is dropped on a page.\ | DroppedNode - The new Node that is dropped from SymbolPalette.                          | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | SymbolPaletteItemName - The name of the SymbolPalette item, which is dropped on a page. |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| HeadNodeChanged                                           | Raised when the HeadNode of the Connector is changed.\        | Connector - The Connector for which the HeadNode is changed.                            | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | PreviousNode - The old Node on which the HeadNode of the Connector was connected.       |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | CurrentNode - The new Node on which the HeadNode of the Connector is connected.         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| TailNodeChanged                                           | Raised when the TailNode of the Connector is changed.\        | Connector - The Connector for which the HeadNode is changed.                            | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | PreviousNode - The old Node on which the TailNode of the Connector was connected.       |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | CurrentNode - The new Node on which the TailNode of the Connector is connected.         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| ConnectorDrop                                             | Raised when the Connector is dropped on a page.\              | DroppedConnector - The Connector on which the event is raised.                          | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| BeforeConnectionCreate                                    | Raised when a new connection is being made.\                  | Connector - The Connector for which the HeadNode is changed.                            | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| AfterConnectionCreate                                     | Raised after the connection is made.\                         | Connector - The Connector on which the event is raised.                                 | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | FixedNodeEnd - The Node on which the Connector is fixed.                                |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | HitNodeEnd - The new Node on which the Connector is getting connected.                  |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeSelected                                              | Raised when a Node is selected.\                              | Node - The Node on which the event is raised.                                           | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeUnSelected                                            | Raised when a Node is not selected.\                          | Node - The Node on which the event is raised.                                           | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeDeleting                                              | Raised before a Node is deleted from the model.\              | DeletedNode - The Node, which is going to be deleted.                                   | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeDeleted                                               | Raised when a Node is deleted from the model.\                | DeletedNode - The Node, which is deleted.                                               | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| ConnectorDeleting                                         | Raised before a LineConnector is deleted from the model.\     | DeletedLineConnector - The LineConnector, which is being deleted.                       | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| ConnectorDeleted                                          | Raised when a LineConnector is deleted from the model.\       | DeletedLineConnector - The LineConnector, which is deleted.                             | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| PreviewNodeDrop                                           | Raised before a Node is dropped on a page.\                   | Node -- The Node on which the event is raised.                                          | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| PreviewConnectorDrop                                      | Raised before a Connector is dropped on a page.\              | Connector -- The Connector on which the event is raised.                                | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
+-----------------------------------------------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------+
| NodeMoved                                                 | Raised when the nudge operation on the Node is completed.\    | Node -- The Node on which the event is raised.                                          | RoutedEvent     |
|                                                           | This event cannot be cancelled.                               |                                                                                         |                 |
| (Event is fired before the nudge operation is completed.) |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | oldOffset -- The old offset value before the nudge operation.                           |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               |                                                                                         |                 |
|                                                           |                                                               | newOffset -- The new offset value after performing the nudge operation.                 |                 |
+===========================================================+===============================================================+=========================================================================================+=================+


 

Examples: 

The events that are triggered and handled while using Essential Diagram for Silverlight can be specified by using the DiagramView object, as shown in the following examples:

 The NodeClick event can be specified, as shown in the following code snippets.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**[ ]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][sfdiagram][:][DiagramView][ [Name][=\"diagramView\"][ NodeClick][=\"diagramView_NodeClick\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][sfdiagram][:][DiagramView][\>][]                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                                                        |
|                                                                                                                                                              |
| [diagramView.NodeClick += [new] [NodeEventHandler](diagramView_NodeClick);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[ ]                                                                                                                   |
|                                                                                                                                                                                                                         |
| [AddHandler][ diagramView.NodeClick, [AddressOf] diagramView_NodeClick][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Then, the event handler can be specified in code behind, as shown in the following code snippet.[]

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                                                                                                            |
|                                                                                                                                                                                                                  |
| [// The event handler.][]                                                                                                  |
|                                                                                                                                                                                                                  |
| [void][ diagramView_NodeClick([object] sender, [NodeRoutedEventArgs] evtArgs)] |
|                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [// User specified code.][]                                                                                                |
|                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[ ]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                      |
| [\'The event handler.][]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| [    [Private] [Sub] diagramView_NodeClick([ByVal] sender [As] [Object], [ByVal] evtArgs [As] [NodeRoutedEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                      |
| [        [\'User specified code.]]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                      |
| [    [End] [Sub]][]                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

The ConnectorDoubleClick event can be specified, as shown in the following code snippets.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**[ ]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][sfdiagram][:][DiagramView][ [Name][=\"diagramView\"][ ConnectorDoubleClick][=\"diagramView_ConnectorDoubleClick\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][sfdiagram][:][DiagramView][\>][]                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                                                                                                                                      |
|                                                                                                                                                                                                                                            |
| [diagramView.[ConnectorDoubleClick] += [new] [ConnChangedEventHandler](diagramView\_[ConnectorDoubleClick]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[ ]                                                                                                                                         |
|                                                                                                                                                                                                                                               |
| [AddHandler][ diagramView.ConnectorDoubleClick, [AddressOf] diagramView_ConnectorDoubleClick][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Then, the event handler can be specified in code behind, as shown in the following code snippet.[]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                                                                                                                       |
|                                                                                                                                                                                                                             |
| [// The event handler.][]                                                                                                             |
|                                                                                                                                                                                                                             |
| [void][ diagramView_ConnectorDoubleClick([object] sender, [ConnRoutedEventArgs] evtArgs)] |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [// User specified code.][]                                                                                                           |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[ ]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                 |
| [\'The event handler.][]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    [Private] [Sub] diagramView_ConnectorDoubleClick([ByVal] sender [As] [Object], [ByVal] evtArgs [As] [ConnRoutedEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                 |
| [        [\'User specified code.]]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                 |
| [    [End] [Sub]][]                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The NodeMoved and NodeDrop events can be specified, as shown in the following code snippet.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                                                                                                           |
|                                                                                                                                                                                                                 |
| [diagramView.NodeMoved += [new] [NodeNudgeEventHandler](diagramView_NodeMoved);]                                               |
|                                                                                                                                                                                                                 |
| [void][ diagramView_NodeMoved([object] sender, [NodeNudgeEventArgs] evtArgs)] |
|                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                         |
|                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                         |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [diagramView.NodeDrop += [new] [NodeNudgeEventHandler](diagramView_LineMoved);]                                                |
|                                                                                                                                                                                                                 |
| [void][ diagramView_NodeDrop([object] sender, [NodeNudgeEventArgs] evtArgs)]  |
|                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                         |
|                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[ ]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                     |
| [Private][ diagramView.NodeMoved += New NodeNudgeEventHandler(AddressOf diagramView_NodeMoved)]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                     |
| [    [Private] [Sub] diagramView_NodeMoved([ByVal] sender [As] [Object], [ByVal] evtArgs [As] [NodeNudgeEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                     |
| [    [End] [Sub]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                     |
| [Private][ diagramView.NodeDrop += New NodeNudgeEventHandler(AddressOf diagramView_LineMoved)]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                     |
| [    [Private] [Sub] diagramView_NodeDrop([ByVal] sender [As] [Object], [ByVal] evtArgs [As] [NodeNudgeEventArgs])]  |
|                                                                                                                                                                                                                                                                                                                                     |
| [    [End] [Sub]][]                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample Link

To view a sample:

1.   Open the Diagram Sample Browser from the dashboard. (Refer to the [Samples and Location] chapter.)

2.   Navigate to **Product Showcase** -\> **Features Demo**.

[]{#related-topics}

