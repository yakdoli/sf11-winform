---
title: resizingrowsandresizingcolumns.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\resizingrowsandresizingcolumns.md
created_at: 2025-07-03
---






#### ResizingRows and ResizingColumns {#resizingrows-and-resizingcolumns style="tab-stops: 0pt"}

[] 

These events are used to control over resizing of specific rows or columns. They are triggered when a row or column is being resized. The event handler receives an argument of type **GridResizingRowsEventArgs** or **GridResizingColumnsEventArgs** containing data related to the event. The following properties of the event arguments provide information specific to these events.

 

Properties of GridResizingRowsEventArgs

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| AllowResize                       | Boolean property; When false, disallow the resizing action.                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Rows                              | Used to get or set the index of range of rows being resized.                                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Reason                            | Gives a hint about user action and reason for this event.                                                                  |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   | Accepts a value of type GridResizeCellsReason enumeration:                                                                 |
|                                   |                                                                                                                            |
|                                   | []                                       |
|                                   |                                                                                                                            |
|                                   | [·      ]**CancelMode**--Indicates current operation was cancelled.                           |
|                                   |                                                                                                                            |
|                                   | [·      ]**DoubleClick**--Indicates user double-clicked.                                      |
|                                   |                                                                                                                            |
|                                   | [·      ]**HitTest**--Indicates this is a Hit-Test query.                                     |
|                                   |                                                                                                                            |
|                                   | [·      ]**MouseDown**--Indicates user pressed mouse down.                                    |
|                                   |                                                                                                                            |
|                                   | [·      ]**MouseMove**--Indicates user is moving the mouse.                                   |
|                                   |                                                                                                                            |
|                                   | [·      ]**MouseUp**--Indicates user released the mouse.                                      |
|                                   |                                                                                                                            |
|                                   | [·      ]**ResetDefault**--Indicates changed row heights will be reset back to default value. |
|                                   |                                                                                                                            |
|                                   | [·      ]**ResetHide**--Indicates hidden rows will be made visible.                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Height                            | Specifies the row height.                                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Point                             | Indicates the point at which the mouse hits the row before resizing.                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+


[] 

Properties of GridResizingColumnsEventArgs

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| AllowResize                       | Boolean property; When false, disallow the resizing action.                                                                  |
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


[         ]

Example

[] 

These events can be invoked as follows:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| **[]**                                                                                                               |
|                                                                                                                                                                        |
| [grid.ResizingRows += [new] [GridResizingRowsEventHandler](grid_ResizingRows);]          |
|                                                                                                                                                                        |
| [grid.ResizingColumns += [new] [GridResizingColumnsEventHandler](grid_ResizingColumns);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handlers:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [// Disallow resizing of row 2.      ]                                                                                                                           |
|                                                                                                                                                                                                                    |
| [void][ grid_ResizingRows([object] sender, [GridResizingRowsEventArgs] args)]       |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [if][ (args.Rows.Top == 2)]                                                                                                   |
|                                                                                                                                                                                                                    |
| [args.AllowResize = [false];]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [// Disallow resizing of column 3.]                                                                                                                              |
|                                                                                                                                                                                                                    |
| [void][ grid_ResizingColumns([object] sender, [GridResizingColumnsEventArgs] args)] |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [if][ (args.Columns.Left == 3)]                                                                                               |
|                                                                                                                                                                                                                    |
| [args.AllowResize = [false];]                                                                                                                             |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p202} 

 

[]{#related-topics}

