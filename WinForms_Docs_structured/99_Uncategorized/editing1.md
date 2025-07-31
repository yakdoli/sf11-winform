---
title: editing1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\editing1.md
created_at: 2025-07-03
---








  









## Editing {#editing style="tab-stops: 0pt"}

 

Essential Grid has built-in support for editing grid content. This can be achieved by defining a **GridEditing** class for the grid. Using this class, you can specify the action mappers for insert, edit, update, delete, and cancel requests.

Key Features

The key features of editing are as follows:

[·      ]Allows three modes of editing such as inline row editing, inline form editing, and inline custom template form editing.

[·      ]Enables MVC 2.0 client validation.

[·      ]Provides toolbar support for editing records.

 

Properties

 


+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| Property               | Description                                                                 | Type of property       | Value it accepts      | Any other dependencies/sub-properties associated |
+========================+=============================================================================+========================+=======================+==================================================+
| Editing                | Gets or sets the editing properties for the Grid control.                   | Class                  | NA                    | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| AllowNew               | Used to enable or disable the insert action in the editing mode.            | bool                   | True/False            | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| AllowEdit              | Used to enable or disable the edit action in the editing mode.              | bool                   | True/False            | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| AllowDelete            | Used to enable or disable the delete action in the editing mode.            | bool                   | True/False            | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| DeleteMapper           | Gets or sets the action mapper for the delete action.                       | string                 | Delete action name    | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| InsertMapper           | Gets or sets the action mapper for the insert actions.                      | string                 | Insert action name    | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| GridSaveMapper         | Gets or sets the action mapper for the update action.                       | string                 | Save action name      | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| EditMode               | Gets or sets the edit mode for editing.                                     | Enum                   | Normal                | NA                                               |
|                        |                                                                             |                        |                       |                                                  |
|                        |                                                                             |                        | InlineForm            |                                                  |
|                        |                                                                             |                        |                       |                                                  |
|                        |                                                                             |                        | InlineTemplateForm    |                                                  |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| FormModeEditorTemplate | Gets or sets the partial view name for the InlineTemplateForm mode editing. | string                 | Any partial view name | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| Toolbar                | Gets or sets the toolbar for grid.                                          | Class                  | NA                    | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| Enable                 | Used to enable or disable the toolbar in grid.                              | Bool                   | True/False            | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| Items                  | Used to add the items to grid toolbars.                                     | List\<ToolbarOptions\> | Any toolbar items     | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+
| AllowEditing           | Gets or sets the particular column enabling and disabling editing.          | Bool                   | True/False            | NA                                               |
+------------------------+-----------------------------------------------------------------------------+------------------------+-----------------------+--------------------------------------------------+


[] 

The following table illustrates the default **CellEditTypes** and their corresponding controls for specific data types.

[] 

 


  ----------- --------------------------- --------------------------------------------------------
  Data Type   Default CellEditType        Control
  String      CellEditType.StringEdit     TextBox control
  Boolean     CellEditType.BooleanEdit    CheckBox control
  Integer     CellEditType.NumericEdit    NumericTextBox control
  Decimal     CellEditType.NumericEdit    NumericTextBox control with default two decimal digits
  Double      CellEditType.NumericEdit    NumericTextBox control with default two decimal digits
  Date-time   CellEditType.DateTimeEdit   DatePicker control
  ----------- --------------------------- --------------------------------------------------------


[] 

Methods

 


+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| Method                                                | Parameters                            | Return type                 | Description                                                                                                     |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| Editing (Action\<IEditingBuilder\<T\>\> editing)      | Action\<IEditingBuilder\<T\>\>        | IGridBuilder\<T\>           | Used to configure the editing mode.                                                                             |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| AllowNew(bool allowDelete, string mapperName)         | Bool ,string                          | IEditingBuilder\<T\>        | Used to configure the **Add New** action in the editing mode.                                                   |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             | Used to set the mapper name and enable or disable the **Add New** action.                                       |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| AllowEdit(bool allowEdit, string mapperName)          | Bool ,string                          | IEditingBuilder\<T\>        | Used to configure the **Edit** action in the editing mode.                                                      |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             | Used to set the mapper name and to enable or disable the **Edit** action.                                       |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| AllowDelete(bool allowDelete, string mapperName)      | Bool ,string                          | IEditingBuilder\<T\>        | Used to configure the **Delete** action in the editing mode.                                                    |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             | Used to set the **mapperName** and enable or disable the **Delete** action                                      |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| EditMode(GridEditMode editMode)                       | GridEditMode                          | IEditingBuilder\<T\>        | Used to configure the grid's editing mode. Set any editing mode from an enum collection. Default is **Normal**. |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| FormModeEditorTemplate(string editmodeTemplate)       | String partialview name               | IEditingBuilder\<T\>        | Used to set the partial view name in the inline template form editing mode.                                     |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| PrimaryKey(Action\<IGridPrimaryKeyBuilder\<T\>\> key) | Action\<IGridPrimaryKeyBuilder\<T\>\> | IEditingBuilder\<T\>        | Used to add primary keys to grid which are used in the editing mode to uniquely identify the record.            |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| CloseOnEscape(bool enable)                            | Bool                                  | IEditingBuilder\<T\>        | Used to enable or disable the ESC key event in cancel request through the keyboard.                             |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| SaveOnEnter(bool enable)                              | Bool                                  | IEditingBuilder\<T\>        | Used to enable or disable the ENTER key event for raise the save request through the keyboard.                  |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| Add(Expression\<Func\<T, object\>\> expression)       | Expression                            | IGridPrimaryKeyBuilder\<T\> | Used to add primary keys to the grid.                                                                           |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| ToolBar(Action\<IToolBarBuilder\> toobar)             | Action\<IToolbarbuilder\> toolbar     | IEditingBuilder\<T\>        | Used to configure the toolbar in the editing mode.                                                              |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| Add(GridToolBarItems item)                            | GridToolBarItems                      | IToolBarBuilder             | Used to add a toolbar item to grid.                                                                             |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| Add(GridToolBarItems item, string caption)            | GridToolBarItems, string              | IToolBarBuilder             | Used to add a toolbar item with a caption.                                                                      |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+
| EnableToolbar(bool enable)                            | Bool                                  | IToolBarBuilder             | Used to enable or disable the toolbar in the grid.                                                              |
|                                                       |                                       |                             |                                                                                                                 |
|                                                       |                                       |                             |                                                                                                                 |
+-------------------------------------------------------+---------------------------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------+


[] 

More:





















