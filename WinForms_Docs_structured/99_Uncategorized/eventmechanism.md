---
title: eventmechanism.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\eventmechanism.md
created_at: 2025-07-03
---








  









## Event Mechanism {#event-mechanism style="tab-stops: 0pt"}

The **Diagram** supports client-side event handling.

Events 


+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| Event                                             | Description                                                            | Arguments                                                                  | Type        | Reference Links                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnLoad                                  | This event is raised immediately when the diagram is loaded.           |               -                                                            | Client side | NA                                        |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeClick                             | Raised when a node is clicked.\                                        | Node---The node on which the event is raised.                              | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeDoubleClick                       | Raised when a node is double-clicked.\                                 | Node---The node on which the event is raised.                              | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeSelected                          | Raised when a node is selected.\                                       | Node---The node on which the event is raised.                              | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeUnSelected                        | Raised when a node is deselected.\                                     | Node---The node on which the event is raised.                              | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeStartLabelEdit                    | Raised when the label editing for a node has started.\                 | NewLabelValue---The new label value.                                       | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
|                                                   |                                                                        | OldLabelValue---The old label value.                                       |             |                                           |
|                                                   |                                                                        |                                                                            |             |                                           |
|                                                   |                                                                        | Node---The node on which the event is raised.                              |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeLabelChanged                      | Raised when a node\'s label value is changed.\                         | NewLabelValue---The new label value.                                       | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
|                                                   |                                                                        | OldLabelValue---The old label value.                                       |             |                                           |
|                                                   |                                                                        |                                                                            |             |                                           |
|                                                   |                                                                        | Node---The node on which the event is raised.                              |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeDragStart                         | Raised when a node is dragged.\                                        | Node---The node on which the event is raised.                              | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeDragging                          | Raised when a node is being dragged.                                   | Node---The node on which the event is raised.                              | Client side | NA                                        |
|                                                   |                                                                        |                                                                            |             |                                           |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeDragEnd                           | Raised when the drag operation on a node is completed.                 | Node---The node on which the event is raised.                              | Client side | NA                                        |
|                                                   |                                                                        |                                                                            |             |                                           |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeResizing                          | Raised when the resize operation is being performed.\                  | Node---The node on which the event is raised.                              | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeResized                           | Raised after a node is resized.\                                       | Node---The node on which the event is raised.                              | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeDeleting                          | Raised before a node is deleted from the model.\                       | DeletedNode---The node that is going to be deleted.                        | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeDeleted                           | Raised when a node is deleted from the model.\                         | DeletedNode - The Node, which is deleted.                                  | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnNodeDrop                              | Raised when a shape from the symbol palette is dropped on a page.\     | DroppedNode---The new node that is dropped from SymbolPalette.             | Client side | NA (This event not supported in SVG Mode) |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorClick                        | Raised when a line connector is clicked from the model.\               | LineConnector---The line connector which is deleted.                       | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorDoubleClick                  | Raised when a connector is double-clicked.\                            | Connector---The connector on which the event is raised.                    | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
|                                                   |                                                                        | HeadNode---The nead node of the connector.                                 |             |                                           |
|                                                   |                                                                        |                                                                            |             |                                           |
|                                                   |                                                                        | TailNode---The tail node of the connector.                                 |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorSelected                     | Raised when a connector is not selected.\                              | Connector---The connector on which the event is raised.                    | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorUnSelected                   | Raised when a connector is deselected.\                                | Connector---The connector on which the event is raised.                    | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorStartLabelEdit               | Raised when the label editing for a connector has started.\            | Connector---The connector on which the event is raised.                    | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
|                                                   |                                                                        | OldLabelValue---The old label value.                                       |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorLabelChanged                 | Raised when a connector\'s label value is changed.\                    | Connector---The connector on which the event is raised.                    | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
|                                                   |                                                                        | OldLabelValue---The old label value.                                       |             |                                           |
|                                                   |                                                                        |                                                                            |             |                                           |
|                                                   |                                                                        | NewLabelValue---The new label value.                                       |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorDragStart                    | Raised when either end of the connector is dragged.\                   | Connector---The connector on which the event is raised.                    | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorDragging                     | Raised when a connector is being dragged.\                             | Connector---The connector on which the event is raised.                    | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorDragEnd                      | Raised when the drag operation is completed.\                          | Connector---The connector on which the event is raised.                    | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
|                                                   |                                                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnHeadNodeChanged                       | Raised when the head node of a connector is changed.\                  | Connector---The connector for which the head node is changed.              | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
|                                                   |                                                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnTailNodeChanged                       | Raised when the tail node of a connector is changed.\                  | Connector---The connector for which the head node is changed.              | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorDeleting                     | Raised before a line connector is deleted from the model.\             | DeletedLineConnector---The line connector that is being deleted.           | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| ClientSideOnConnectorDeleted                      | Raised when a line connector is deleted from the model.\               | DeletedLineConnector---The line connector that is deleted.                 | Client side | NA                                        |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+---------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------+-------------------------------------------+
| [ClientSideOnConnectorDrop] | Raised when a connector from the symbol palette is dropped on a page.\ | DroppedConnector---The new connector that is dropped from symbol palette.  | Client side | NA (This event not supported in SVG Mode) |
|                                                   | This event cannot be cancelled.                                        |                                                                            |             |                                           |
+===================================================+========================================================================+============================================================================+=============+===========================================+


 

More:







