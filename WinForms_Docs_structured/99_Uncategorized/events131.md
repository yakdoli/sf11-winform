---
title: events131.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\events131.md
created_at: 2025-07-03
---








  









### Events[] {#events style="tab-stops: 0pt"}

The GridData control declares a number of events that it can handle, in response to the activities either by the end user or by the system. An event is a message that is handled, to notify an object or a class of the occurrence of an action. When an event is handled, all the event handlers will be notified.

 

The GridData control offers technical benefits by declaring all its events as Routed Events. Hence, being the high level visual element in the visual tree, it need not hook the same event on all of its descendants (e.g. rows, columns and cells), such as MouseMove. Instead, it hooks the event on itself and hence, when the mouse moves over one of its descendants, the grid will be notified appropriately, whenever the event is handled without expecting its descendants to notify it.

 

Subscribing to Events

 

In order to get event notifications, the grid needs to be wired up with the required events. This process is called as subscribing to the events. It can be done using either XAML or C# code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][GridDataControl][ x][:][Name][=\"dataGrid\"][ [AutoPopulateColumns][=\"True\" ][ItemsSource][=\"{][StaticResource][ ordersSource][}\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [MouseMove][=\"dataGrid_MouseMove\"\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                    |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [this][.dataGrid.MouseMove+=[new] [MouseEventHandler](dataGrid_MouseMove);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

For either of the above code languages, you should have the following C# code to handle the MouseMove event.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [private][ [void] dataGrid_MouseMove([object] sender, [MouseEventArgs] e)]     |
|                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [    [Console].WriteLine([\"Mouse cursor Postion:\"] + e.GetPosition(sender [as] [IInputElement]));] |
|                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: These Grid WPF mouse events are more advantageous than using any other default mouse events; Because the default mouse events are controlled by Mouse Controller, which makes it very hard to access the underlying data. Whereas in case of Grid mouse events, it is directly possible to access the underlying data easily.


**[]** 

Unsubscribing the events

 

If you do not want the grid to listen to the event, you can unwire the event from the grid as follows.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                    |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [this][.dataGrid.MouseMove-=[new] [MouseEventHandler](dataGrid_MouseMove);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

Table 46: GridData Control Events


  --------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Event                             Description
  CurrentCellActivating             This event is handled before the grid activates the specified cell as current cell.
  CurrentCellActivated              This event is handled after the grid activates the specified cell as current cell.
  CurrentCellActivateFailed         This event is handled after the grid fails to activate a specific cell as current cell.
  CurrentCellDeactivating           This event is handled before the grid deactivates the current cell.
  CurrentCellDeactivated            This event is handled after the grid deactivates current cell.
  CurrentCellDeactivateFailed       This event is handled after the grid fails to deactivate the current cell.
  CurrentCellConfirmChangesFailed   This event is handled when the grid fails to save the changes made to the active current cell.
  CurrentCellAcceptedChanges        This event is handled when the grid accepts the changes made to the active current cell.
  CurrentCellChanging               This event is handled when the user wants to modify contents of the current cell.
  CurrentCellStartEditing           This event is handled before the current cell switches to the editing mode.
  CurrentCellEditingComplete        This event is handled when the grid completes editing the active current cell.
  CurrentCellRejectedChanges        This event is handled when the grid rejects the changes made to the active current cell.
  CurrentCellChanged                This event is handled when the user changes the contents of the current cell.
  CurrentCellMoved                  This event is handled when the current cell is successfully moved to a new position.
  CurrentCellMoveFailed             This event is handled when the current cell fails to move to a new position.
  CurrentCellMoving                 This event is handled when the current cell is about to be moved to a new position.
  CurrentCellValidating             This event is handled when the grid is validating the contents of the active current cell.
  CurrentCellValidated              This event is handled when the grid has completed validating the contents of the active current cell.
  CellButtonClick                   This event is handled when the button in the grid cell is clicked.
  DropDownSelectionChanged          This event is handled when the selected item in the grid drop-down is changed.
  CellClick                         This event is handled when the grid cell is clicked.
  CellCursor                        This event is handled when the cell has a cursor.
  CellMouseHoverEnter               This event is handled when the mouse hits the cell and signals that the cell wants to handle the mouse events. This event is handled before the CellMouseHover event.
  CellMouseHover                    This event is handled when the mouse is moved over a grid cell.
  CellMouseHoverLeave               This event is handled when the mouse leaves a cell.
  CellMouseDown                     This event is handled when the mouse button is pressed.
  CellMouseMove                     This event is handled when the mouse is moved over the cell.
  CellMouseUp                       This event is handled when the mouse button is released.
  CellCancelMode                    This event is handled when any current user interaction is canceled, example-Cancel select cells when Escape key is pressed.
  CellRestoreMode                   This event is handled when a cell is trying to restore the canceled changes.
  ResizingColumns                   This event is handled when the user is about to resize a column or is in the process of re-sizing a column.
  QueryAllowDragColumn              This event is handled when the user hovers over a column header  or drags a column header using mouse.
  ResizingRows                      This event is handled when the user is about to resize a row or is in the process of re-sizing a row.
  --------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

 

[]{#related-topics}

