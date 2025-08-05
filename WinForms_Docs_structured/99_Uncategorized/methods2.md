---
title: methods2.md
original_path: WinForms_Docs/99_Uncategorized/methods2.md
created_at: 2025-08-05
---








  









### Methods {#methods style="tab-stops: 0pt"}

The following table provides the methods of the **ToolbarOptions** class.

[] 


+------------------------------------------------------------------------------------+-----------------------------------+-----------------------------+-----------------------------------------------------------------------------+
| Method                                                                             | Method                            | Return type                 | Description                                                                 |
+====================================================================================+===================================+=============================+=============================================================================+
| Add(Expression\<Func\<T, object\>\> expression)                                    | Expression                        | IGridPrimaryKeyBuilder\<T\> | Used to add the primary keys to grid                                        |
|                                                                                    |                                   |                             |                                                                             |
|                                                                                    |                                   |                             |                                                                             |
+------------------------------------------------------------------------------------+-----------------------------------+-----------------------------+-----------------------------------------------------------------------------+
| ToolBar(Action\<IToolBarBuilder\> toobar)                                          | Action\<IToolbarbuilder\> toolbar | IEditingBuilder\<T\>        | Used to configure the toolbar in the editing mode                           |
|                                                                                    |                                   |                             |                                                                             |
|                                                                                    |                                   |                             |                                                                             |
+------------------------------------------------------------------------------------+-----------------------------------+-----------------------------+-----------------------------------------------------------------------------+
| Add(GridToolBarItems item)                                                         | GridToolBarItems                  | IToolBarBuilder             | Used to add the toolbar item to grid                                        |
|                                                                                    |                                   |                             |                                                                             |
|                                                                                    |                                   |                             |                                                                             |
+------------------------------------------------------------------------------------+-----------------------------------+-----------------------------+-----------------------------------------------------------------------------+
| Add(GridToolBarItems item, string caption)                                         | GridToolBarItems, string          | IToolBarBuilder             | Used to add the toolbar item with a caption                                 |
|                                                                                    |                                   |                             |                                                                             |
|                                                                                    |                                   |                             |                                                                             |
+------------------------------------------------------------------------------------+-----------------------------------+-----------------------------+-----------------------------------------------------------------------------+
| Add(string customItemTitle, string customItemCssClass)                             | string, string                    | IToolBarBuilder             | Used to add the custom toolbar item with title and customCss class          |
|                                                                                    |                                   |                             |                                                                             |
|                                                                                    |                                   |                             |                                                                             |
+------------------------------------------------------------------------------------+-----------------------------------+-----------------------------+-----------------------------------------------------------------------------+
| Add(GridToolBarItems item, string caption, string mapper)                          | GridToolBarItems, string, string  | IToolBarBuilder             | Used to add the toolbar item with caption and mapper                        |
|                                                                                    |                                   |                             |                                                                             |
|                                                                                    |                                   |                             |                                                                             |
+------------------------------------------------------------------------------------+-----------------------------------+-----------------------------+-----------------------------------------------------------------------------+
|  Add(string customItemTitle, string customItemCaption,  string customItemCssClass) | string, string, string            |  IToolBarBuilder            | Used to add the custom toolbar item with title, caption and customCss class |
+------------------------------------------------------------------------------------+-----------------------------------+-----------------------------+-----------------------------------------------------------------------------+
| EnableToolbar(bool enable)                                                         | Bool                              | IToolBarBuilder             | Used to enable or disable the toolbar in grid.                              |
|                                                                                    |                                   |                             |                                                                             |
|                                                                                    |                                   |                             |                                                                             |
+------------------------------------------------------------------------------------+-----------------------------------+-----------------------------+-----------------------------------------------------------------------------+


**[]** 

[]{#related-topics}

