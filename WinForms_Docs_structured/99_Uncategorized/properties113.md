---
title: properties113.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\properties113.md
created_at: 2025-07-03
---








  









### Properties {#properties style="tab-stops: 0pt"}

 

+----------------+------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------------+--------------------------------------------------------------------------------------------+
| Property       | Description                                                                                                                  | Type of property | Value it accepts                                  | Dependencies                                                                               |
+----------------+------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------------+--------------------------------------------------------------------------------------------+
| AllowResizing  | This property allows you to choose if you would want to resize the content in a particular cell or not.\                     | bool             | [·      ]True        | NA                                                                                         |
|                | If not, this feature's properties and its other settings will be disabled.                                                   |                  |                                                   |                                                                                            |
|                |                                                                                                                              |                  | [·      ]False       |                                                                                            |
+----------------+------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------------+--------------------------------------------------------------------------------------------+
| AllowAutoWrap  | Specifies whether the autowrap is enabled                                                                                    | bool             | [·      ]True        | Depends on the AllowResizing property.\                                                    |
|                |                                                                                                                              |                  |                                                   | \                                                                                          |
|                |                                                                                                                              |                  | [·      ]False       | If AllowResizing is true, then you have the option of enabling the AllowAutoWrap property. |
|                |                                                                                                                              |                  |                                                   |                                                                                            |
|                | Content will wrap to the next line if the content exceeds the boundary of the Column Cells                                   |                  |                                                   |                                                                                            |
+----------------+------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------------+--------------------------------------------------------------------------------------------+
| ResizeSettings | Specifies if content is resizable or not.\                                                                                   | enum             | [·      ]ResizeToFit | Depends on the AllowResizing property.\                                                    |
|                | \                                                                                                                            |                  |                                                   | \                                                                                          |
|                |                                                                                                                              |                  | [·      ]ClipContent | If AllowResizing is true, then you have the option of enabling the AllowAutoWrap property. |
|                | If it is resizable, the ResizeToFit sub-property is enabled.\                                                                |                  |                                                   |                                                                                            |
|                | \                                                                                                                            |                  |                                                   |                                                                                            |
|                | If it is not resizable, the ClipContent sub-property is enabled.                                                             |                  |                                                   |                                                                                            |
+----------------+------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------------+--------------------------------------------------------------------------------------------+
| ResizeToFit    | Sets whether the resize to fit content  is enabled                                                                           | bool             | [·      ]True        | Depends on the ResizeSettings---\                                                          |
|                |                                                                                                                              |                  |                                                   | \                                                                                          |
|                |                                                                                                                              |                  | [·      ]False       | ResizeToFit is a sub-property of ResizeSettings                                            |
|                |                                                                                                                              |                  |                                                   |                                                                                            |
|                | Double-clicking the resize handle will have the column automatically resized to fit the widest cell content without wrapping |                  |                                                   |                                                                                            |
+----------------+------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------------+--------------------------------------------------------------------------------------------+
| ClipContent    | Specifies whether the cell content will be clipped on column resizing                                                        | bool             | [·      ]True        | Depends on the ResizeSettings---\                                                          |
|                |                                                                                                                              |                  |                                                   | \                                                                                          |
|                |                                                                                                                              |                  | [·      ]False       | ClipContent is a sub-property of ResizeSettings                                            |
+----------------+------------------------------------------------------------------------------------------------------------------------------+------------------+---------------------------------------------------+--------------------------------------------------------------------------------------------+

 

[]{#related-topics}

