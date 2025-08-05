---
title: gridresizingcolumnseventargs.md
original_path: WinForms_Docs/04_Controls/Grid/gridresizingcolumnseventargs.md
created_at: 2025-08-05
---






#### GridResizingColumnsEventArgs {#gridresizingcolumnseventargs style="tab-stops: 0pt"}

[] 

The following table provides information on the properties of the event:

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| AllowResize                       | Boolean property;  When false, disallow the resizing action.                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Columns                           | Used to get or set the index of range of columns being resized.                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Reason                            | Gives a hint about user action and reason for this event.                                                                    |
|                                   |                                                                                                                              |
|                                   |                                                                                                                              |
|                                   |                                                                                                                              |
|                                   | Accepts a value of type GridResizeCellsReason enumeration:                                                                   |
|                                   |                                                                                                                              |
|                                   | []                                         |
|                                   |                                                                                                                              |
|                                   | [·      ]**CancelMode**--Indicates current operation was cancelled.                             |
|                                   |                                                                                                                              |
|                                   | [·      ]**DoubleClick**--Indicates user double-clicked.                                        |
|                                   |                                                                                                                              |
|                                   | [·      ]**HitTest**--Indicates this is a Hit-Test query.                                       |
|                                   |                                                                                                                              |
|                                   | [·      ]**MouseDown**--Indicates user pressed mouse down.                                      |
|                                   |                                                                                                                              |
|                                   | [·      ]**MouseMove**--Indicates user is moving the mouse.                                     |
|                                   |                                                                                                                              |
|                                   | [·      ]**MouseUp**--Indicates user released the mouse.                                        |
|                                   |                                                                                                                              |
|                                   | [·      ]**ResetDefault**--Indicates changed column widths will be reset back to default value. |
|                                   |                                                                                                                              |
|                                   | [·      ]**ResetHide**--Indicates hidden columns will be made visible.                          |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Width                             | Specifies the column width.                                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Point                             | Indicates the point at which the mouse hits the column before resizing.                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+


[] 

Example

**[]** 

This event can be triggered using the following code:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [grid.ResizingRows += [new] [GridResizingRowsEventHandler](grid_ResizingRows);]           |
|                                                                                                                                                                            |
| [grid.ResizingColumns += [new] [GridResizingColumnsEventHandler ](grid_ResizingColumns);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handlers

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [//Disallow resizing of row 2.      ]                                                                                                     |
|                                                                                                                                                                                             |
| [void][ grid_ResizingRows([object] sender, GridResizingRowsEventArgs args)]       |
|                                                                                                                                                                                             |
| [{]                                                                                                                                                     |
|                                                                                                                                                                                             |
| [    [if] (args.Rows.Top == 2)]                                                                                                    |
|                                                                                                                                                                                             |
| [       args.AllowResize = [false];]                                                                                               |
|                                                                                                                                                                                             |
| [}]                                                                                                                                                     |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [//Disallow resizing of column 3.]                                                                                                        |
|                                                                                                                                                                                             |
| [void][ grid_ResizingColumns([object] sender, GridResizingColumnsEventArgs args)] |
|                                                                                                                                                                                             |
| [{]                                                                                                                                                     |
|                                                                                                                                                                                             |
| [ [if] (args.Columns.Left == 3)]                                                                                                   |
|                                                                                                                                                                                             |
| [    args.AllowResize = [false];]                                                                                                  |
|                                                                                                                                                                                             |
| [}]                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p204} 

 

[]{#related-topics}

