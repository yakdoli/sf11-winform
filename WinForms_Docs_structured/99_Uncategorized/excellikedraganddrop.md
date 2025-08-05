---
title: excellikedraganddrop.md
original_path: WinForms_Docs/99_Uncategorized/excellikedraganddrop.md
created_at: 2025-08-05
---






#### Excel Like Drag and Drop {#excel-like-drag-and-drop style="tab-stops: 0pt"}

 

This Feature enables you to drag the content of cells including styles to different position of the grid and also to other grids. This enables you to copy data to one or more place.

**IDataObject** is used to copy data, store information and also to retrieve data.  DragDrop API available in WPF is used to initiate drag and drop operation in GridControl.

**[]** 

Table 12: Drag and drop operation


+-------------------------------+-------------------------------------------------------------------------------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name of the Property          | Description                                                                                                       | Type of Property | Value it Accepts | PropertySyntax                                                                                                                                                               |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AllowDragDrop                 | Enables ExcelLike MouseController which helps in Drag and Drop Operation.                                         | Normal           | Boolean          | [ [this].grid.AllowDragDrop = [true];]                                                              |
|                               |                                                                                                                   |                  |                  |                                                                                                                                                                              |
|                               |                                                                                                                   |                  |                  |                                                                                                                                                                              |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GridDataObjectConsumerOptions | Gets/Sets enum value for DragDrop Consumer Option.                                                                | Normal           | Enum             | [ [this].grid.Model.Options.DataObjectConsumerOptions = [GridDataObjectConsumerOptions].Styles;] |
|                               |                                                                                                                   |                  |                  |                                                                                                                                                                              |
|                               |                                                                                                                   |                  |                  |                                                                                                                                                                              |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DragDropDropTargetFlags       | Gets/Sets enum value for value that can be copied/Moved and also provides other options for DragDropTargetFlags.. | Normal           | Enum             | [  [this].grid.Model.Options.DragDropDropTargetFlags]                                                                    |
|                               |                                                                                                                   |                  |                  |                                                                                                                                                                              |
|                               |                                                                                                                   |                  |                  |                                                                                                                                                                              |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------+------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

Table 13


+-----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------+
| When is the event triggered?                                                                                                                  | How is it handled?                                                           | Method (event handler) that handles the event? | What are the event args associated? | Purpose of the event                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Occurs when the user releases the mouse over a cell at the end of an OLE drag-and-drop operation and before the data are applied to the grid. |                                                                              | GridOleDropAtRowColEventHandler                | GridOleDropAtRowColEventArgs        | This event lets you toprovide your own customized paste data behavior.                                         |
|                                                                                                                                               |                                                                              |                                                |                                     |                                                                                                                |
|                                                                                                                                               | Handled by setting Handled flag as True.                                     |                                                |                                     |                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------+
| The event is fired when the user hovers the mouse over the edge of a selected range.                                                          |     You can disallow the specified range to be used as OLE Data Source when\ | GridExcelLikeDragRangeEventHandler             | GridQueryCanDragRangeEventArgs      |    GridQueryCanOleDragRangeEventArgs is a custom event argument class used by the\                             |
|                                                                                                                                               | you assign true to "Cancel" flag.                                            |                                                |                                     |     GridControlBase.QueryCanOleDragRange event to determine whether\                                           |
|                                                                                                                                               |                                                                              |                                                |                                     | a specified range can serve as an OLE drag source.                                                             |
|                                                                                                                                               |                                                                              |                                                |                                     |                                                                                                                |
|                                                                                                                                               |                                                                              |                                                |                                     |                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------+
| This event is fired when a user starts dragging a range of selected cells\                                                                    | Handled by setting  Handled flag as True                                     | GridQueryOleDataSourceDataEventHandler         | GridQueryOleDataSourceDataEventArgs | This event lets you supply your own clipboard formats or add support for pasting additional clipboard content. |
|      using OLE drag-and-drop.                                                                                                                 |                                                                              |                                                |                                     |                                                                                                                |
|                                                                                                                                               |                                                                              |                                                |                                     |                                                                                                                |
|                                                                                                                                               |                                                                              |                                                |                                     |                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------+-------------------------------------+----------------------------------------------------------------------------------------------------------------+


[] 

[] 


{border="0"}Note:  Silverlight Grid do not support OLE Drag and Drop i.e from one grid to another but within itself.


[] 

Following are the properties for Enum properties:

Available Enum Values GridDataObjectConsumerOptions:


+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| Enum Value                        | Details                                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| None                              | No default data objects supported.                                                                       |
|                                   |                                                                                                          |
|                                   |                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| Styles                            | Enable styles (internal) data objects. This allows you to drag / copy / paste complete cell information. |
|                                   |                                                                                                          |
|                                   |                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| Text                              | Enable text data format. This allows you to drag cell values.                                            |
|                                   |                                                                                                          |
|                                   |                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| All                               | Enable support for all default data objects.                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+


[] 

[] 

Available Enum Values for DragDropTargetFlags:


+-----------------------------------+----------------------------------------------------------------+
| Enum Value                        | Details                                                        |
+-----------------------------------+----------------------------------------------------------------+
| Disabled                          | Disable drop target.                                           |
|                                   |                                                                |
|                                   |                                                                |
+-----------------------------------+----------------------------------------------------------------+
| Text                              | Force dragging of CF_TEXT clipboard format.                    |
|                                   |                                                                |
|                                   |                                                                |
+-----------------------------------+----------------------------------------------------------------+
| Styles                            | Force dragging of internal styles format.                      |
|                                   |                                                                |
|                                   |                                                                |
+-----------------------------------+----------------------------------------------------------------+
| EdgeScroll                        | Enable edgescroll when user drags to the corner of the window. |
|                                   |                                                                |
|                                   |                                                                |
+-----------------------------------+----------------------------------------------------------------+


[] 

[]{#related-topics}

