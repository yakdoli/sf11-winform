---
title: howtopreselectacheckboxinsideagridcell.md
original_path: WinForms_Docs/04_Controls/Grid/howtopreselectacheckboxinsideagridcell.md
created_at: 2025-08-05
---








  









### How to pre-select a checkbox inside a grid cell {#how-to-pre-select-a-checkbox-inside-a-grid-cell style="tab-stops: 0pt"}

[] 

You need to set a style member called **CheckBoxOptions** for a particular grid cell, for this purpose. CheckBoxOptions.CheckedValue is used to specify what value should be given in the CellValue to make the checkbox checked.

[] 

Example

 

If you want \"true\" to be checked and \"false\" to be unchecked state then use the below code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [//Sets the cell type as Checkbox.]                                                                                                          |
|                                                                                                                                                                                                |
| [this][.gridControl1\[1,1\].CellType = [\"CheckBox\"]; ]                           |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [//Sets the Checked and Unchecked values for the checkbox.]                                                                                  |
|                                                                                                                                                                                                |
| [this][.gridControl1\[1,1\].CheckBoxOptions.CheckedValue = [\"true\"]; ]           |
|                                                                                                                                                                                                |
| [this][.gridControl1\[1,1\].CheckBoxOptions.UncheckedValue = [\"false\"]; ]        |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [//Sets the type of the cell value as bool.]                                                                                                 |
|                                                                                                                                                                                                |
| [this][.gridControl1\[1,1\].CellValueType = [typeof]([bool]); ] |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [//Sets the Cell value.]                                                                                                                     |
|                                                                                                                                                                                                |
| [this][.gridControl1\[1,1\].CellValue = [true];]                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [\'Sets the cell type as Checkbox.]                                                                                                          |
|                                                                                                                                                                                                |
| [Me][.gridControl1(1, 1).CellType = [\"CheckBox\"] ]                               |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [\'Sets the Checked and Unchecked values for the checkbox.]                                                                                  |
|                                                                                                                                                                                                |
| [Me][.gridControl1(1, 1).CheckBoxOptions.CheckedValue = [\"true\"] ]               |
|                                                                                                                                                                                                |
| [Me][.gridControl1(1, 1).CheckBoxOptions.UncheckedValue = [\"false\"] ]            |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [\'Sets the type of the cell value as bool.]                                                                                                 |
|                                                                                                                                                                                                |
| [Me][.gridControl1(1, 1).CellValueType = [GetType]([Boolean]) ] |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [\'Sets the Cell value.]                                                                                                                     |
|                                                                                                                                                                                                |
| [Me][.gridControl1(1, 1).CellValue = [True]]                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p561} 

 

[]{#related-topics}

