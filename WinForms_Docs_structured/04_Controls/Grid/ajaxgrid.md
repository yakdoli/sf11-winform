---
title: ajaxgrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\ajaxgrid.md
created_at: 2025-07-03
---








  









### AJAX Grid {#ajax-grid style="tab-stops: 0pt"}

The AJAX Grid control handles data presentation operations like paging, sorting, grouping, and filtering, or you can perform those operations. But this mode of action for the AJAX Grid control is decided using the **AjaxActionMode** property whose options are described in the following table. AJAX Grid supports two kinds of ActionModes.

 

+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------+-----------------------------+
| **Property**   | **Description**                                                                                                                             | **Type of Property** | **Value It Accepts**    | **Dependencies**            |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------+-----------------------------+
| EnableAjaxMode | Specifies the mode of GridGroupingControl                                                                                                   | Boolean              | True                    | NA                          |
|                |                                                                                                                                             |                      |                         |                             |
|                |                                                                                                                                             |                      | False                   |                             |
|                |                                                                                                                                             |                      |                         |                             |
|                |                                                                                                                                             |                      | Default value is False  |                             |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------+----------------------+-------------------------+-----------------------------+
| AjaxActionMode | Used to set the action mode of the control.                                                                                                 | Enum                 | Json                    | Dependent on EnableAjaxMode |
|                |                                                                                                                                             |                      |                         |                             |
|                | Server---All the operations like sorting and grouping are handled by Essential Grid itself (by default).                                    |                      | Server                  |                             |
|                |                                                                                                                                             |                      |                         |                             |
|                | JSON (JavaScript Object Notation)---You have to handle the operations. The possible operations are paging, sorting, grouping and filtering. |                      | Default value is Server |                             |
|                |                                                                                                                                             |                      |                         |                             |
|                |                                                                                                                                             |                      |                         |                             |
|                |                                                                                                                                             |                      |                         |                             |
|                |                                                                                                                                             |                      |                         |                             |
+================+=============================================================================================================================================+======================+=========================+=============================+

[] 

More:















