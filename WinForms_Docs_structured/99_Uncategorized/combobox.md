---
title: combobox.md
original_path: WinForms_Docs/99_Uncategorized/combobox.md
created_at: 2025-08-05
---






##### Combo Box {#combo-box style="tab-stops: 0pt"}

[] 

When you add a combo box to a grid cell, it will enable you to choose from a drop-down list of choices. You can populate this list in several ways by setting the appropriate **GridStyleInfo** properties. Other properties restrict the choices to those items listed in the drop down, and enable auto completion of possible matches as the user types new items.

[] 


  ------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  GridStyleInfo Property   Description
  CellType                 Set to \"combo box\" for a combo box control.
  ChoiceList               StringCollection holding the strings for the drop down.
  ExclusiveChoiceList      *True* if you want to list the items in the drop-down, *false* otherwise.
  DataSource               This property lets you to populate the drop-down list from by using an object that implements IListSource or IList. Examples include DataTable, DataSet, DataView and ArrayList.
  DisplayMember            String that names the public property from the data source object to be displayed in the cell.
  ValueMember              String that names the public property from the data source object to be used as the value for this cell.
  ------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

The following code example illustrates how to set the cell type to ComboBox.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [// Generate the choices.]                                                                                                                  |
|                                                                                                                                                                                               |
| [StringCollection][ items = [new] [StringCollection]();] |
|                                                                                                                                                                                               |
| [items.Add([\"One\"]);]                                                                                                           |
|                                                                                                                                                                                               |
| [items.Add([\"Two\"]);]                                                                                                           |
|                                                                                                                                                                                               |
| [items.Add([\"Three\"]);]                                                                                                         |
|                                                                                                                                                                                               |
| [items.Add([\"Four\"]);]                                                                                                          |
|                                                                                                                                                                                               |
| [items.Add([\"Five\"]);]                                                                                                          |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [// Set up the control.]                                                                                                                    |
|                                                                                                                                                                                               |
| [gridControl1\[rowIndex, colIndex\].CellType = [\"ComboBox\"];]                                                                   |
|                                                                                                                                                                                               |
| [gridControl1\[rowIndex, colIndex\].ChoiceList = items;]                                                                                                  |
|                                                                                                                                                                                               |
| [gridControl1\[rowIndex, colIndex\].Text = [\"Five\"];]                                                                           |
|                                                                                                                                                                                               |
| [gridControl1\[rowIndex, colIndex\].CellType = [\"ComboBox\"];]                                                                   |
|                                                                                                                                                                                               |
| [gridControl1\[rowIndex, colIndex\].ExclusiveChoiceList = [true];]                                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [// Or use a data source such as a table in a data set.]                                                                                    |
|                                                                                                                                                                                               |
| [gridControl1\[2, 2\].CellType = [\"ComboBox\"];]                                                                                 |
|                                                                                                                                                                                               |
| [gridControl1\[2, 2\].DataSource = [this].dataSet11.Tables\[[\"Customers\"]\];]                              |
|                                                                                                                                                                                               |
| [gridControl1\[2, 2\].DisplayMember = [\"CustomerID\"];]                                                                          |
|                                                                                                                                                                                               |
| [gridControl1\[2, 2\].ValueMember = [\"CustomerID\"];]                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [\' Generate the choices.]                                                                                                                  |
|                                                                                                                                                                                               |
| [Dim][ items [As] StringCollection = [New] StringCollection()] |
|                                                                                                                                                                                               |
| [items.Add([\"One\"])]                                                                                                            |
|                                                                                                                                                                                               |
| [items.Add([\"Two\"])]                                                                                                            |
|                                                                                                                                                                                               |
| [items.Add([\"Three\"])]                                                                                                          |
|                                                                                                                                                                                               |
| [items.Add([\"Four\"])]                                                                                                           |
|                                                                                                                                                                                               |
| [items.Add([\"Five\"])]                                                                                                           |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [\' Set up the control. ]                                                                                                                   |
|                                                                                                                                                                                               |
| [gridControl1(rowIndex, colIndex).CellType = [\"ComboBox\"]]                                                                      |
|                                                                                                                                                                                               |
| [gridControl1(rowIndex, colIndex).ChoiceList = items]                                                                                                     |
|                                                                                                                                                                                               |
| [gridControl1(rowIndex, colIndex).Text = [\"Five\"]]                                                                              |
|                                                                                                                                                                                               |
| [gridControl1(rowIndex, colIndex).CellType = [\"ComboBox\"]]                                                                      |
|                                                                                                                                                                                               |
| [gridControl1(rowIndex, colIndex).ExclusiveChoiceList = [True]]                                                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                           |
|                                                                                                                                                                                               |
| [\' Or use a data source such as a table in a dataset.]                                                                                     |
|                                                                                                                                                                                               |
| [gridControl1(2, 2).CellType = [\"ComboBox\"]]                                                                                    |
|                                                                                                                                                                                               |
| [gridControl1(2, 2).DataSource = [Me].dataSet11.Tables([\"Customers\"])]                                     |
|                                                                                                                                                                                               |
| [gridControl1(2, 2).DisplayMember = [\"CustomerID\"]]                                                                             |
|                                                                                                                                                                                               |
| [gridControl1(2, 2).ValueMember = [\"CustomerID\"]]                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 76: Combo Box Cells

 

###### []{#p53}4.1.4.1.3.1 AutoComplete Support for Combo Box in Edit Mode {#autocomplete-support-for-combo-box-in-edit-mode style="tab-stops: 0pt"}

 

Essential Grid provides AutoComplete support for combo box cells. The AutoComplete feature is a filtered suggestion list presented in a drop-down that is pulled from a mapped data source as the user enters text into a text box.  AutoComplete for combo box cells provides the following properties:

 

[·      ]AutoComplete---Displays suggestion in the text box. The content other than what you have typed will be highlighted.

[·      ]AutoSuggest---Dynamically populates a list based on the entered text.

[·      ]Both---Enables normal editable behavior.

[·      ]None---No operations will be performed in the text box and list box areas.

 

Use Case Scenarios

You can choose the suggestion instead of typing the entire content.

 

Properties

 

Table 1: Properties Table


+--------------+---------------------------------------------------------------------+-------------+---------------+---------------------+
| **Property** | **Description**                                                     | **Type**    | **Data Type** | **Reference links** |
+--------------+---------------------------------------------------------------------+-------------+---------------+---------------------+
| AutoComplete | Gets the a suggestion from the list based on the entered text.      | Enumerator  | N/A           | N/A                 |
|              |                                                                     |             |               |                     |
|              | The suggestion will be highlighted.                                 |             |               |                     |
|              |                                                                     |             |               |                     |
|              |                                                                     |             |               |                     |
+--------------+---------------------------------------------------------------------+-------------+---------------+---------------------+
| AutoSuggest  | Dynamically populate a list based on the entered text.              | Enumerator  | N/A           | N/A                 |
+--------------+---------------------------------------------------------------------+-------------+---------------+---------------------+
| Both         | Enables normal editable behavior.                                   | Enumerator  | N/A           | N/A                 |
+--------------+---------------------------------------------------------------------+-------------+---------------+---------------------+
| None         | No operations will be performed in the text box and list box areas. | Enumerator  | N/A           | N/A                 |
+--------------+---------------------------------------------------------------------+-------------+---------------+---------------------+


[] 

Enabling AutoComplete in EditMode for a Combo Box Celltype

The following steps illustrates enabling AutoComplete in EditMode for a combo Box celltype:

1.   Declare the Celltype as Combo Box as given in the following code:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [this][.gridControl1\[RowIndex,ColIndex\].CellType = [GridCellTypeName].ComboBox;][  ] |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ \[VB\]]                                                                                                                                              |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [Me][.gridControl1(RowIndex,ColIndex).CellType = [GridCellTypeName].ComboBox] |
|                                                                                                                                                                                            |
| [  ]                                                                                                                                                   |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Set the Dropdown style as Editable as given in the following code:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [this][.gridControl1\[RowIndex,ColIndex\].DropDownStyle = [GridDropDownStyle].Editable;][] |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [\[VB\]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [Me][.gridControl1(RowIndex,ColIndex).DropDownStyle = [GridDropDownStyle].Editable  ]                                          |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Set the *GridComboSelectionOptions* using the *AutoCompleteInEditMode* property as given in the following code:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ][\[VB\]]                                                                                                        |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [Me][.gridControl1(RowIndex,ColIndex).AutoCompleteInEditMode = GridComboSelectionOptions.AutoSuggest] |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ \[VB\]]                                                                                                                                              |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [Me][.gridControl1(RowIndex,ColIndex).AutoCompleteInEditMode = GridComboSelectionOptions.AutoSuggest] |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

