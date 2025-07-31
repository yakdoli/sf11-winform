---
title: dragginganddroppinggridrowsintoanyotherelement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\dragginganddroppinggridrowsintoanyotherelement.md
created_at: 2025-07-03
---








  









### Dragging and Dropping Grid Rows into Any Other Element {#dragging-and-dropping-grid-rows-into-any-other-element style="tab-stops: 0pt"}

 

This feature allows you to select multiple rows (using **jQuery UI Selectable**) and drag and drop the selected rows to any other element which is specified using the **TargetHtmlElementId** property of the grid.

 

Properties

 


+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+--------------------------------------------------+
| Property               | Description                                                                                                                               | Type of property | Value it accepts          | Any other dependencies/sub-properties associated |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+--------------------------------------------------+
| TargetHtmlElementID    | Gets or sets the selector identification of the TargetElement to Drop.                                                                    | String           | Any string value          | AllowRowsDragging                                |
|                        |                                                                                                                                           |                  |                           |                                                  |
|                        | ie, To represent ID: "#TargetID",                                                                                                         |                  |                           |                                                  |
|                        |                                                                                                                                           |                  |                           |                                                  |
|                        |     To represent class: ".TargetClassname"                                                                                                |                  |                           |                                                  |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+--------------------------------------------------+
| RowsDraggingMode       | This property sets the type of dragand drop mode. Options are Normal and GhostRows.                                                       | Enum             | DragandDropMode.GhostRows | AllowRowsDragging                                |
|                        |                                                                                                                                           |                  |                           |                                                  |
|                        |                                                                                                                                           |                  | DragandDropMode.Normal    |                                                  |
|                        |                                                                                                                                           |                  |                           |                                                  |
|                        |                                                                                                                                           |                  |                           |                                                  |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+--------------------------------------------------+
| **AllowRowsDragging**  | This property enables this Rows Drag and Drop feature and JQuery UI Selection.                                                            | Boolean          | Any Boolean value         | NA                                               |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+--------------------------------------------------+
| **RowsDroppingMapper** | This property sets the mapping string. To update the source grid while dropping the rows, if you need one Action means you can give here. | string           | Any string value          | AllowRowsDragging                                |
|                        |                                                                                                                                           |                  |                           |                                                  |
|                        |                                                                                                                                           |                  |                           |                                                  |
|                        |                                                                                                                                           |                  |                           |                                                  |
|                        | For Example: if you move rows from one grid to another grid in Source grid the rows needs to be removed from database.                    |                  |                           |                                                  |
|                        |                                                                                                                                           |                  |                           |                                                  |
|                        |                                                                                                                                           |                  |                           |                                                  |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------+--------------------------------------------------+


[] 

Methods

 


+------------------------+---------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| Method                 | Parameters                | Return type     | Descriptions                                                                                                                       |
+------------------------+---------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| TargetHtmlElementID    | String                    | IGridBuilder    | Used to set the selector identification of the TargetElement to Drop.                                                              |
|                        |                           |                 |                                                                                                                                    |
|                        |                           |                 | ie, To represent ID: "#TargetID",                                                                                                  |
|                        |                           |                 |                                                                                                                                    |
|                        |                           |                 |     To represent class: ".TargetClassname"                                                                                         |
|                        |                           |                 |                                                                                                                                    |
|                        |                           |                 |                                                                                                                                    |
+------------------------+---------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| RowsDraggingMode       | DragandDropMode.GhostRows | IGridBuilder    | Used to set which type of dragand drop mode. Options are Normal and GhostRows.                                                     |
|                        |                           |                 |                                                                                                                                    |
|                        | DragandDropMode.Normal    |                 |                                                                                                                                    |
|                        |                           |                 |                                                                                                                                    |
|                        |                           |                 |                                                                                                                                    |
+------------------------+---------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| **AllowRowsDragging**  | Boolean                   | IGridBuilder    | Used to enable this Rows Drag and Drop feature and JQuery UI Selection.                                                            |
|                        |                           |                 |                                                                                                                                    |
|                        |                           |                 |                                                                                                                                    |
+------------------------+---------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| **RowsDroppingMapper** | String                    | IGridBuilder    | Used to set the mapping string, to update the source grid while dropping the rows, if you need one Action means you can give here. |
|                        |                           |                 |                                                                                                                                    |
|                        |                           |                 | For Example: if you move rows from one grid to another grid in Source grid the rows needs to be removed from database.             |
|                        |                           |                 |                                                                                                                                    |
|                        |                           |                 |                                                                                                                                    |
+------------------------+---------------------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------+


 

Events

 


+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| Name                  | Description                                                                                                                                                                                                                             | Arguments             |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| OnRowDropping         | The event which call its handler after draging operation and before dropping operation. Here you are providing option to cancel the drop. gridObject contains DroppingCancel variable if it is set as True. Dropping will be cancelled. | Event,                |
|                       |                                                                                                                                                                                                                                         |                       |
|                       |                                                                                                                                                                                                                                         | Data                  |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| OnRowDropped          | The event which calls the handler after dropped operation. By this event you can update your own target element by using ajax post.                                                                                                     | Event,                |
|                       |                                                                                                                                                                                                                                         |                       |
|                       |                                                                                                                                                                                                                                         | Data                  |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+


[] 

More:







