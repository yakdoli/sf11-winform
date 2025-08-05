---
title: eventmechanism4.md
original_path: WinForms_Docs/99_Uncategorized/eventmechanism4.md
created_at: 2025-08-05
---








  









## Event Mechanism {#event-mechanism style="tab-stops: 0pt"}

[]{#p103}This section describes several events triggered and handled while using Essential Diagram WPF in the following topic:

[] 

Events for Nodes and Connections

[] 

Diagram control has several events which respond to several actions performed on nodes and connections.

 

The various events and their descriptions are explained in the following table.

[] 

Table 86: Events Table


+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Event                                                | Description                                                         | Arguments                                                                                  |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeClick                                            | Raised when the node is clicked.\                                   | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeDoubleClick                                      | Raised when the node is clicked twice in succession.\               | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeStartLabelEdit                                   | Raised when the label editing on the node is started.\              | NewLabelValue -- The new label value.                                                      |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | OldLabelValue -- the old label value.                                                      |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | Node - Node on which event is raised.                                                      |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeLabelChanged                                     | Raised when the node\'s label value is changed.\                    | NewLabelValue -- The new label value.                                                      |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | OldLabelValue -- the old label value.                                                      |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | Node - Node on which event is raised.                                                      |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeDragStart                                        | Raised when the node is dragged.\                                   | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeDragEnd                                          | Raised when the drag operation on node is complete.                 | Node -- Node on which event is raised.                                                     |
|                                                      |                                                                     |                                                                                            |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeResizing                                         | Raised when the resize operation is being performed.\               | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeResized                                          | Raised after the node is resized.\                                  | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeRotationChanging                                 | Raised when the node is being rotated.\                             | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeRotationChanged                                  | Raised after the node is rotated.\                                  | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ConnectorDoubleClick                                 | Raised when the Connector is clicked twice in succession.\          | Connector -- Connector on which the event is raised.                                       |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | Head Node -- Head Node of the connector.                                                   |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | Tail Node -- Tail Node of the connector.                                                   |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ConnectorStartLabelEdit                              | Raised when the label editing on the Connector is started.\         | Connector -- Connector on which the event is raised.                                       |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     | Head Node -- Head Node of the connector.                                                   |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | Tail Node -- Tail Node of the connector.                                                   |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | OldLabelValue -- the old label value.                                                      |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ConnectorLabelChanged                                | Raised when the connector\'s label value is changed.\               | Connector -- Connector on which the event is raised.                                       |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     | Head Node -- Head Node of the connector.                                                   |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | Tail Node -- Tail Node of the connector.                                                   |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | OldLabelValue -- the old label value.                                                      |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | NewLabelValue -- The new label value.                                                      |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ConnectorDragStart                                   | Raised when either ends of the connector is dragged.\               | Connector -- Connector on which the event is raised.                                       |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | FixedNodeEnd -- Node on which the connection is fixed.                                     |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | MovableNodeEnd -- The old Node on which the Connector was connected.                       |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ConnectorDragEnd                                     | Raised when the drag operation is complete.\                        | Connector -- Connector on which the event is raised.                                       |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | FixedNodeEnd -- Node on which the connection is fixed.                                     |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | HitNodeEnd -- The new node on which the Connector is getting connected.                    |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeDrop                                             | Raised when a shape from the SymbolPalette is dropped on the page.\ | DroppedNode -- The new node just dropped from SymbolPalette.                               |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | SymbolPaletteItemName -- The name of the SymbolPalette item, which is dropped on the page. |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| HeadNodeChanged                                      | Raised when the headnode of the connector is changed\               | Connector -- The connector whose HeadNode is changed.                                      |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | PreviousNode -- The old Node on which the HeadNode of the Connector was connector.         |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | CurrentNode - The new Node on which the HeadNode of the Connector is connector.            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| TailNodeChanged                                      | Raised when the tailnode of the connector is changed.\              | Connector -- The connector whose HeadNode is changed.                                      |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | PreviousNode -- The old Node on which the TailNode of the Connector was connector.         |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | CurrentNode - The new Node on which the TailNode of the Connector is connector.            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ConnectorDrop                                        | Raised when the connector is dropped on the page.\                  | DroppedConnector -- Connector on which the event is raised.                                |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| BeforeConnectionCreate                               | Raised when a new connection is being made.\                        | Connector -- The connector whose HeadNode is changed.                                      |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| AfterConnectionCreate                                | Raised after the connection has been made.\                         | Connector -- Connector on which the event is raised.                                       |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | FixedNodeEnd -- Node on which the connection is fixed.                                     |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | HitNodeEnd -- The new node on which the Connector is getting connected.                    |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeSelected                                         | Raised when a node is selected.\                                    | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeUnSelected                                       | Raised when a node is not selected.\                                | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeDeleting                                         | Raised before a node is deleted from the model.\                    | DeletedNode -- Node which is going to get deleted.                                         |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeDeleted                                          | Raised when a node is deleted from the model.\                      | DeletedNode -- Node which is deleted.                                                      |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ConnectorDeleting                                    | Raised before a line connector is deleted from the model.\          | DeletedLineConnector -- LineConnector which is getting deleted.                            |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ConnectorDeleted                                     | Raised when a line connector is deleted from the model.\            | DeletedLineConnector -- LineConnector which is deleted.                                    |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| PreviewNodeDrop                                      | Raised before a node is dropped on the page.\                       | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| PreviewConnectorDrop                                 | Raised before a line connector is dropped on the page.\             | Connector -- Connector on which the event is raised.                                       |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
|                                                      |                                                                     |                                                                                            |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| NodeMoved                                            | Raised when the nudge operation on node is completed.\              | Node -- Node on which event is raised.                                                     |
|                                                      | Event cannot be cancelled.                                          |                                                                                            |
| (event is fired before nudge operation is completed) |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | oldOffset -- The old offset value before nudge operation.                                  |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     |                                                                                            |
|                                                      |                                                                     | newOffset -- The new offset value after performing nudge operation.                        |
+------------------------------------------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


[] 

The events can be specified using DiagramView object as follows.

[] 

[·      ]For instance, NodeClick event can be specified in the following way.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][sfdiagram][:][DiagramView][ [Name][=\"diagramView\"][ NodeClick][=\"diagramView_NodeClick\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][sfdiagram][:][DiagramView][\>][ ]                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [diagramView.NodeClick += [new] [NodeEventHandler](diagramView_NodeClick);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [AddHandler][ diagramView.NodeClick, [AddressOf] diagramView_NodeClick][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]And then the event handler can be specified in the code behind as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [//Event Handler]                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [void][ diagramView_NodeClick([object] sender, [NodeRoutedEventArgs] evtArgs)] |
|                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [//user specified code]                                                                                                                                        |
|                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                              |
| [\'Event Handler][]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] diagramView_NodeClick([ByVal] sender [As] [Object], [ByVal] evtArgs [As] [NodeRoutedEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                              |
| [     [\'user specified code]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]][]                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]As another example, the **ConnectorDoubleClick** event can be specified in the following way.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][sfdiagram][:][DiagramView][ [Name][=\"diagramView\"][ ConnectorDoubleClick][=\"diagramView_ConnectorDoubleClick\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][sfdiagram][:][DiagramView][\>]                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [diagramView.[ConnectorDoubleClick] += [new] [ConnChangedEventHandler](diagramView\_[ConnectorDoubleClick]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [AddHandler][ diagramView.ConnectorDoubleClick, [AddressOf] diagramView_ConnectorDoubleClick][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

And then the event handler can be specified in the code behind as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [// Event Handler]                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [void][ diagramView_ConnectorDoubleClick([object] sender, [ConnRoutedEventArgs] evtArgs)] |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [// user specified code]                                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [\'Event Handler][]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] diagramView_ConnectorDoubleClick([ByVal] sender [As] [Object], [ByVal] evtArgs [As] [ConnRoutedEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [     [\'user specified code]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]][]                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]NodeMoved and NodeDrop events

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
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

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Private][ diagramView.NodeMoved += New NodeNudgeEventHandler(AddressOf diagramView_NodeMoved)]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] diagramView_NodeMoved([ByVal] sender [As] [Object], [ByVal] evtArgs [As] [NodeNudgeEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Private][ diagramView.NodeDrop += New NodeNudgeEventHandler(AddressOf diagramView_LineMoved)]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] diagramView_NodeDrop([ByVal] sender [As] [Object], [ByVal] evtArgs [As] [NodeNudgeEventArgs])]  |
|                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]][]                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

