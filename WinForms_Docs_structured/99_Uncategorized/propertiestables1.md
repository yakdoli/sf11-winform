---
title: propertiestables1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\propertiestables1.md
created_at: 2025-07-03
---






#### Properties Tables[] {#properties-tables style="tab-stops: 0pt"}

 


+------------------------------------+--------------------------+--------------+-----------------------------+-------------------------------------------------------------------+
| **Property**                       | **Description**          | **Type**     | **Value it Accepts**        | **Dependencies**                                                  |
+------------------------------------+--------------------------+--------------+-----------------------------+-------------------------------------------------------------------+
| EditMode[] | Specifies the edit mode. | GridEditMode | Normal                      | Depends on AllowEditing---                                        |
|                                    |                          |              |                             |                                                                   |
|                                    |                          | (Enum)       | []  | If AllowEditing is set to True, the EditMode property is enabled. |
+------------------------------------+--------------------------+--------------+-----------------------------+-------------------------------------------------------------------+


** Commands properties:**


+--------------+---------------------------------------------------+--------------------+----------------------+-------------------------------------------------------------------+
| **Property** | **Description**                                   | **Type**           | **Value it Accepts** | **Dependencies**                                                  |
+--------------+---------------------------------------------------+--------------------+----------------------+-------------------------------------------------------------------+
| Command      | Specifies the grid command types.                 | CommandTypes       | AddNew               | Depends on AllowEditing---                                        |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    | Edit                 | If AllowEditing is set to True, the EditMode property is enabled. |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    | Update               |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    | Delete               |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    | Cancel               |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    | Custom               |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      |                                                                   |
+--------------+---------------------------------------------------+--------------------+----------------------+-------------------------------------------------------------------+
| Text         | Specifies the text of the grid commands.          | NA                 | String               | Depends on AllowEditing---                                        |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      | If AllowEditing is set to True, the EditMode property is enabled. |
+--------------+---------------------------------------------------+--------------------+----------------------+-------------------------------------------------------------------+
| ImageUrl     | Specifies the image for grid commands.            | NA                 | Image String         | Depends on AllowEditing---                                        |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      | If AllowEditing is set to True, the EditMode property is enabled. |
+--------------+---------------------------------------------------+--------------------+----------------------+-------------------------------------------------------------------+
| ItemType     | Specifies the UnBoundItemTypes of grid commands.  | UnBoundItemTypes   | Hyperlink            | Depends on AllowEditing---                                        |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    | Button               | If AllowEditing is set to True, the EditMode property is enabled. |
+--------------+---------------------------------------------------+--------------------+----------------------+-------------------------------------------------------------------+
| ItemOption   | Specifies the UnBoundItemOptions of grid commands | UnboundItemOptions | TextOnly             | Depends on AllowEditing---                                        |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      | If AllowEditing is set to True, the EditMode property is enabled. |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    | ImageOnly            |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    | ImagePlusText        |                                                                   |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      |                                                                   |
+--------------+---------------------------------------------------+--------------------+----------------------+-------------------------------------------------------------------+
| UnBound      | Specifies the column of grid commands             | Boolean            | True or False        | NA                                                                |
|              |                                                   |                    |                      |                                                                   |
|              |                                                   |                    |                      |                                                                   |
+--------------+---------------------------------------------------+--------------------+----------------------+-------------------------------------------------------------------+


[] 

[]{#related-topics}

