---
title: combobox2.md
original_path: WinForms_Docs/99_Uncategorized/combobox2.md
created_at: 2025-08-05
---








  









### Combo Box {#combo-box style="tab-stops: 0pt"}

 

Skin cannot be applied for the *ListBox* control inside the combo box. To overcome this limitation Essential Grid uses the *GridListControl* in combo box. ColorStyle settings uses Combo box with the *GridDropDownGridListControlCellModel* which is inherited from the *GridComboBoxCellModel* Class, instead of using the GridComboBoxCellModel directly.

 

To use GridListControl in combo box (which enables you to apply styles), set the *EnableGridListControlInCobmoBox* property to *true. * This is the default value.

The following code illustrated this:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                           |
| []                                                                                                                                          |
|                                                                                                                                                                                                           |
| [this][.gridControl1.Model.EnableGridListControlInComboBox = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                        |
| []                                                                                                                                       |
|                                                                                                                                                                                                        |
| [Me][.gridControl1.Model.EnableGridListControlInComboBox = [true]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

If you want to create an application for which combo box is created from the *GridComboBoxCellModel* and not to use the *GridDropDownGridListControlCellModel*, you need to set the *EnableGridListControlInCobmoBox* property to false. By default this is set to true.

 

The following code illustrates how to disable the *EnableGridListControlInCobmoBox* property:

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                                      |
| [this][.gridControl1.Model.EnableGridListControlInComboBox = [false];][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                                      |
| [this][.gridControl1.Model.EnableGridListControlInComboBox = [false];][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

