---
title: gridresizingrowseventargs.md
original_path: WinForms_Docs/04_Controls/Grid/gridresizingrowseventargs.md
created_at: 2025-08-05
---






#### GridResizingRowsEventArgs {#gridresizingrowseventargs style="tab-stops: 0pt"}

[] 

The following table provides information on the properties of the event:

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| AllowResize                       | Boolean property;  When false, disallow the resizing action.                                                               |
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


[]{#p203} 

 

[]{#related-topics}

