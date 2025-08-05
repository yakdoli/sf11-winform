---
title: draganyotherelementa.md
original_path: WinForms_Docs/99_Uncategorized/draganyotherelementa.md
created_at: 2025-08-05
---








  









### Drag  Any Other Element and Drop into Grid: {#drag-any-other-element-and-drop-into-grid style="tab-stops: 0pt"}

This feature allows you to drag any element using **jQuery UI Draggable** and drop it into your grid. You can also drop any element into a specified row in the table.

 

Properties

 


+---------------------------+-------------+-------------------+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                  | Type        | Value it accepts  | Dependency                                                    | Description                                                                                                                                                  |
+---------------------------+-------------+-------------------+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Droppable                 | Boolean     | Any boolean value | Normal                                                        | This property sets your Grid as Droppable.                                                                                                                   |
|                           |             |                   |                                                               |                                                                                                                                                              |
|                           |             |                   |                                                               |                                                                                                                                                              |
+---------------------------+-------------+-------------------+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ElementtoDrag             | String      | Any string value  | Dependecy on Droppable                                        | This property sets the Target element to be dragged. String must be like a normal selector.                                                                  |
|                           |             |                   |                                                               |                                                                                                                                                              |
|                           |             |                   |                                                               | ie, To represent ID: "#TargetID",                                                                                                                            |
|                           |             |                   |                                                               |                                                                                                                                                              |
|                           |             |                   |                                                               |     To represent class: ".TargetClassname"                                                                                                                   |
+---------------------------+-------------+-------------------+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EnableSelectionOnDragging | Boolean     | Any boolean value | Dependecy on Droppable property                               | This property is set if a row needs to be selected while draggable element is dragging on your GridRow. This happens only if no row is already selected.     |
|                           |             |                   |                                                               |                                                                                                                                                              |
|                           |             |                   |                                                               |                                                                                                                                                              |
+---------------------------+-------------+-------------------+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EnableHighlighting        | Boolean     | Any boolean value | Dependecy on Droppable and EnableSelectionOnDragging property | This property is set if a row(the current row which is accepting the Droppable) needs to be Highlighted while draggable element is dragging on your GridRow. |
|                           |             |                   |                                                               |                                                                                                                                                              |
|                           |             |                   |                                                               |                                                                                                                                                              |
+---------------------------+-------------+-------------------+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Methods


+---------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                    | Parameter type  | Return type     | Description                                                                                                                                                  |
+---------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Droppable                 | Boolean         | IGridBuilder    | This property sets your Grid as Droppable.                                                                                                                   |
|                           |                 |                 |                                                                                                                                                              |
|                           |                 |                 |                                                                                                                                                              |
+---------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ElementtoDrag             | String          | IGridBuilder    | This property sets the Target element to be dragged. String must be like a normal selector.                                                                  |
|                           |                 |                 |                                                                                                                                                              |
|                           |                 |                 | ie, To represent ID: "#TargetID",                                                                                                                            |
|                           |                 |                 |                                                                                                                                                              |
|                           |                 |                 |     To represent class: ".TargetClassname"                                                                                                                   |
|                           |                 |                 |                                                                                                                                                              |
|                           |                 |                 |                                                                                                                                                              |
+---------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EnableSelectionOnDragging | Boolean         | IGridBuilder    | This property is set if a row needs to be selected while draggable element is dragging on your GridRow. This happens only if no row is already selected.     |
|                           |                 |                 |                                                                                                                                                              |
|                           |                 |                 |                                                                                                                                                              |
+---------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EnableHighlighting        | Boolean         | IGridBuilder    | This property is set if a row(the current row which is accepting the Droppable) needs to be Highlighted while draggable element is dragging on your GridRow. |
|                           |                 |                 |                                                                                                                                                              |
|                           |                 |                 |                                                                                                                                                              |
+---------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

Events

[] 


+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| Name                  | Description                                                                                                                                                                                                                                         | Arguments             |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| OnGridRowDragEvent    | The event which call its handler while dragging in any of the grid row. In this event you are passing the Grid object, Json Record of the selected row and the dragging element.                                                                    | Event,                |
|                       |                                                                                                                                                                                                                                                     |                       |
|                       |                                                                                                                                                                                                                                                     | Data,                 |
|                       |                                                                                                                                                                                                                                                     |                       |
|                       |                                                                                                                                                                                                                                                     | DragElement           |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| OnGridRowsDropEvent   | The event which calls the handler after dropped operation. By this event you can update your own target element by using ajax post. In this event you are passing the Grid object, Json Record of the selected row and the element that is dropped. | Event,                |
|                       |                                                                                                                                                                                                                                                     |                       |
|                       |                                                                                                                                                                                                                                                     | Data,                 |
|                       |                                                                                                                                                                                                                                                     |                       |
|                       |                                                                                                                                                                                                                                                     | DragElement           |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+


[] 

More:









