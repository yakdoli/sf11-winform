---
title: actionmodes.md
original_path: WinForms_Docs/99_Uncategorized/actionmodes.md
created_at: 2025-08-05
---








  









## Action Modes {#action-modes style="tab-stops: 0pt"}

 

The Grid control handles data presentation operations like paging and sorting, or you can perform those operations. But this mode of action for the Grid control is decided using the **ActionMode** property whose options are described in the following table.

Essential Grid supports two kinds of ActionModes.

Properties

 

 


+-----------------+-----------------------------------------------------------------------------------------------------------------------------+------------------+------------------+
| Property        | Description                                                                                                                 | Type of property | Value it accepts |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------+------------------+------------------+
| ActionMode      | Used to set the action mode of the control.                                                                                 | String           | "Json"/"Server"  |
|                 |                                                                                                                             |                  |                  |
|                 | Server---All the operations like sorting and grouping are handled by Essential Grid itself (by default).                    |                  |                  |
|                 |                                                                                                                             |                  |                  |
|                 | JSON (JavaScript Object Notation)---You have to handle the operations. The only possible operations are paging and sorting. |                  |                  |
+=================+=============================================================================================================================+==================+==================+


**[]** 

Methods

 

 


  Method               Parameters   Return type         Descriptions
  -------------------- ------------ ------------------- -----------------------------------------
  ActionMode(string)   actionMode   IGridBuilder\<T\>   Used to set the action mode to control.


 

 

More:







