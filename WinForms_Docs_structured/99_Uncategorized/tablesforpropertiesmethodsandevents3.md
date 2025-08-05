---
title: tablesforpropertiesmethodsandevents3.md
original_path: WinForms_Docs/99_Uncategorized/tablesforpropertiesmethodsandevents3.md
created_at: 2025-08-05
---






#### Tables for Properties, Methods, and Events {#tables-for-properties-methods-and-events style="tab-stops: 0pt"}

Properties

 

The following table illustrates the properties under **GridColumn**, which is relevant to **CellEditType** functionality.

[] 

 


+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------+------------------------------------------------------------------------------+--------------+
| Name                  | Description                                                                                                                                             | Type of property | Data type                                      | Value it accepts                                                             | Dependency   |
+=======================+=========================================================================================================================================================+==================+================================================+==============================================================================+==============+
| CellEditType          | Used to set the **CellEditType** of the specified column.                                                                                               | Server-side      | CellEditType                                   | [CellEditType].StringEdit,                           | AllowEditing |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
|                       |                                                                                                                                                         |                  |                                                | [CellEditType][.]BooleanEdit,   |              |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
|                       |                                                                                                                                                         |                  |                                                | [CellEditType][.] DropdownEdit, |              |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
|                       |                                                                                                                                                         |                  |                                                | [CellEditType][.] DateTimeEdit, |              |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
|                       |                                                                                                                                                         |                  |                                                | [CellEditType][.] MaskEdit,     |              |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
|                       |                                                                                                                                                         |                  |                                                | [CellEditType][.] PercentEdit,  |              |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
|                       |                                                                                                                                                         |                  |                                                | [CellEditType][.] NumericEdit   |              |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------+------------------------------------------------------------------------------+--------------+
| NumericEditParams     | Used to set **NumericEditParams** when the **CellEditType** is NumericEdit.                                                                             | Server-side      | [NumericTextBoxModel]  | [NumericTextBoxModel] Object                         | CellEditType |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------+------------------------------------------------------------------------------+--------------+
| PercentEditParams     | Used to set **PercentEditParams** when the **CellEditType** is **PercentEdit**.                                                                         | Server-side      | [PercentTextBoxModel]  | [PercentTextBoxModel] Object                         | CellEditType |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
|                       |                                                                                                                                                         |                  |                                                |                                                                              |              |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------+------------------------------------------------------------------------------+--------------+
| MaskEditParams        | Used to set **MaskEditParams** when the **CellEditType** is **MaskEdit**.                                                                               | Server-side      | [MaskEditTextBoxModel] | [MaskEditTextBoxModel] Object                        | CellEditType |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------+------------------------------------------------------------------------------+--------------+
| AllowFormatinEditMode | Used to set the **AllowFormatinEditMode**. If any format is applied to the column, then when editing, it decides whether the format is required or not. | Server-side      | [Boolean]              | True/false[]                                         | AllowEditing |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------+------------------------------------------------------------------------------+--------------+


***[]*** 


{border="0"}Note: Refer to Tools MVC\>NumericTextbox UG to set NumericEditParams

Refer to Tools MVC\>PercentTextbox UG to set PercentEditParams

Refer to Tools MVC\>MaskEditTextbox UG to set MaskEditParams


[] 

The following table illustrates the CellEditType option usages and controls.

 


  CellEditType                       Control           Usage
  ---------------------------------- ----------------- -----------------------------------------------------------------------------------------
  CellEditType.StringEdit(Default)   Textbox           Used to edit any string valued column.
  CellEditType.BooleanEdit           Checkbox          Used to specify true or  false by checking and unchecking respectively.
  CellEditType.DropdownEdit          DropdownList      Used to select from a list of values in the column.
  CellEditType.NumericEdit           NumericTextbox    Used to edit integers, double or decimals.
  CellEditType.PercentEdit           PercentTextbox    Used to edit integer, double or decimal with display string appended to percent symbol.
  CellEditType.MaskEdit              MaskEditTextbox   Used to mask any common string to the column.
  CellEditType.DateTimeEdit          Datepicker        Used to directly set the date.


[] 

Sample Link

To view the samples:

1.   Open the **ASP.NET MVC** Sample Browser from the dashboard. (Refer to the Samples and Location[ ]chapter)

2.   Navigate to **Grid**\>**Editing**\>**Cell Edit Type** demo.

**[]** 

[] 

**[]** 

[]{#related-topics}

