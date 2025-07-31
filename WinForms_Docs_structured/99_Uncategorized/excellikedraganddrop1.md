---
title: excellikedraganddrop1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\excellikedraganddrop1.md
created_at: 2025-07-03
---






#### Excel Like Drag and Drop {#excel-like-drag-and-drop style="tab-stops: 0pt"}

The Excel-like Drag and Drop feature enables dragging content with their styles from cells to different locations and grids.

You can use this feature to copy data to one or more locations.

 

You can use this feature by using the following code:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [this][.grid.AllowDragDrop = [true];]                                                              |
|                                                                                                                                                                                                    |
| [this][.grid.Model.Options.DataObjectConsumerOptions = [GridDataObjectConsumerOptions].Styles;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Excel Like Drag and Drop has the following features:

 

[·      ]Uses IDataObject to copy, store, and retrieve data.

[·    ]Uses DragDrop API, which is available in WPF, to initiate drag-and-drop.**[]**

**[]** 

Table 19: Property[]


+-------------------------------+-------------------------------------------------------------------------------------------------------------------------+------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Name of the Property          | Description                                                                                                             | Type of Property | Value it Accepts | PropertySyntax                                                                                                                              |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------+------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| AllowDragDrop                 | Allows dragging and dropping content and enables ExcelLike MouseController, which helps in the drag-and-drop operation. | Normal           | Boolean          |  [this].grid.AllowDragDrop = [true];                                                              |
|                               |                                                                                                                         |                  |                  |                                                                                                                                             |
|                               |                                                                                                                         |                  |                  | **[]**                                                                        |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------+------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| GridDataObjectConsumerOptions | Gets or sets the enum value for the DragDrop Consumer Option.                                                           | Normal           | Enum             |  [this].grid.Model.Options.DataObjectConsumerOptions = [GridDataObjectConsumerOptions].Styles; |
|                               |                                                                                                                         |                  |                  |                                                                                                                                             |
|                               |                                                                                                                         |                  |                  | **[]**                                                                        |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------+------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| DragDropDropTargetFlags       | Gets or sets the enum value for values that can be copied or moved and provides other options for DragDropTargetFlags.  | Normal           | Enum             |   [this].grid.Model.Options.DragDropDropTargetFlags                                                                    |
|                               |                                                                                                                         |                  |                  |                                                                                                                                             |
|                               |                                                                                                                         |                  |                  | **[]**                                                                        |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------+------------------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------+


 

Table 20:Event[]


+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| When is the event triggered?                                                                                                                 | How is it handled?                                                           | Method (event handler) that handles the event? | What are the event args associated? | Purpose of the Event                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Occurs when the user releases the mouse over a cell at the end of an OLE drag-and-drop operation and before the data is applied to the grid. | Handled by setting the Handled flag as True.                                 | GridOleDropAtRowColEventHandler                | GridOleDropAtRowColEventArgs        | This event allows you to customize the paste data behavior.                                                                                                                                  |
|                                                                                                                                              |                                                                              |                                                |                                     |                                                                                                                                                                                              |
|                                                                                                                                              |                                                                              |                                                |                                     |                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| The event is initiated when the user rolls the mouse over the edge of a selected range.                                                      | You can disallow the specified range to be used as the OLE Data Source when\ | GridExcelLikeDragRangeEventHandler             | GridQueryCanDragRangeEventArgs      | GridQueryCanOleDragRangeEventArgs is a custom event argument class used by the GridControlBase.QueryCanOleDragRange event to determine if a specified range can serve as an OLE drag source. |
|                                                                                                                                              | assigning true to "Cancel" flag.                                             |                                                |                                     |                                                                                                                                                                                              |
|                                                                                                                                              |                                                                              |                                                |                                     |                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This event is initiated when a user drags a range of selected cells by using the OLE drag-and-drop.                                          | Handled by setting the Handled flag as True.                                 | GridQueryOleDataSourceDataEventHandler         | GridQueryOleDataSourceDataEventArgs | This event allows you to provide customized clipboard formats or add support for pasting the additional clipboard content.                                                                   |
|                                                                                                                                              |                                                                              |                                                |                                     |                                                                                                                                                                                              |
|                                                                                                                                              |                                                                              |                                                |                                     |                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

 

[]{#related-topics}

