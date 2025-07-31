---
title: actionmodes1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\actionmodes1.md
created_at: 2025-07-03
---








  









## ActionModes {#actionmodes style="tab-stops: 0pt"}

The Grid control handles data presentation operations like paging and sorting, or you can perform those operations. But this mode of action for the Grid control is decided using the **ActionMode** property whose options are described in the following table.

Essential Grid supports two kinds of **ActionModes**.

Properties


+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------------------------------+-------------------------------+
| **Property** | **Description**                                                                                                                                                                     | **Type of Property** | **Value it Accepts**                           | **Dependency**                |
+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+------------------------------------------------+-------------------------------+
| ActionMode   | Used to set the action mode of the control.                                                                                                                                         | enum                 | [MobActionMode].Server |  NA[] |
|              |                                                                                                                                                                                     |                      |                                                |                               |
|              | Server---All the operations like sorting and grouping are handled by Essential Grid itself (by default).                                                                            |                      |                                                |                               |
|              |                                                                                                                                                                                     |                      |                                                |                               |
|              | JSON (JavaScript Object Notation)---you can perform all the grid operations. The performance of these operations in this mode will be much faster when compared to the server mode. |                      | [MobActionMode].JSON   |                               |
+==============+=====================================================================================================================================================================================+======================+================================================+===============================+


 

Methods


  **Method**         **Parameters**   **Return type**       **Descriptions**
  ------------------ ---------------- --------------------- -----------------------------------------
  ActionMode(enum)   actionMode       MobGridBuilder\<T\>   Used to set the action mode to control.


More:







