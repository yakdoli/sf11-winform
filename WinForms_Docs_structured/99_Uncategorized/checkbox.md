---
title: checkbox.md
original_path: WinForms_Docs/99_Uncategorized/checkbox.md
created_at: 2025-08-05
---






##### Check Box {#check-box style="tab-stops: 0pt"}

[] 

The **Check Box** cell type displays a check box in a grid cell. The check box has three states: **Checked, Unchecked and Indeterminate**. You can decide whether the check box should behave as a two-state check box or a three-state check box.

[] 

The following **GridStyleInfo** properties can be used to control the functioning of the check box.

[] 


  ------------------------ ---------------------------------------------------------------------------------------------------------------------------
  GridStyleInfo Property   Description
  CellType                 Set to \"check box\" for a check box control.
  CheckBoxOptions          Defines the display value of True, False, or indeterminate (i.e., the value returned by the GridStyleInfo.Text property).
  Description              Text that appears next to the check box.
  TriState                 Whether or not indeterminate value is supported.
  CellValue                Boolean true or false values, or empty (null or nothing).
  ------------------------ ---------------------------------------------------------------------------------------------------------------------------


[] 

The following code example illustrates how to set the cell type to CheckBox.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                   |
| [// Specify display values for True/False/Indeterminate.]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                   |
| [gridControl1.TableStyle.CheckBoxOptions = [new] [GridCheckBoxCellInfo]([\"True\"], [\"False\"], [\"\"], [false]);] |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [// Set up a check box with no tristate.]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                   |
| [gridControl1\[rowIndex,colIndex\].CellValue = [false];]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                   |
| [gridControl1\[rowIndex,colIndex\].Description = [\"Click Me\"];]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                   |
| [gridControl1\[rowIndex,colIndex\].CellType = [\"CheckBox\"];]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| [gridControl1\[rowIndex,colIndex\].TriState = [false];]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [// Set up a check box with tristate.]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [gridControl1\[rowIndex,colIndex + 1\].CellValue = [true];]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                   |
| [gridControl1\[rowIndex,colIndex + 1\].CellType = [\"CheckBox\"];]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| [gridControl1\[rowIndex,colIndex + 1\].TriState = [true];]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                   |
| [gridControl1\[rowIndex,colIndex + 1\].Description = [\"TriState\"];]                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [\' Specify display values for True/False/Indeterminate.]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                        |
| [gridControl1.TableStyle.CheckBoxOptions = [New] GridCheckBoxCellInfo([\"True\"], [\"False\"], [\"\"], [False])] |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [\' Set up a check box with no tristate.]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                        |
| [gridControl1(rowIndex, colIndex).CellValue = [False]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [gridControl1(rowIndex, colIndex).Description = [\"Click Me\"]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                        |
| [gridControl1(rowIndex, colIndex).CellType = [\"CheckBox\"]]                                                                                                                                               |
|                                                                                                                                                                                                                                                                        |
| [gridControl1(rowIndex, colIndex).TriState = [False]]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                        |
| [\' Set up a check box with tristate.]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                        |
| [gridControl1(rowIndex, colIndex + 1).CellValue = [True]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| [gridControl1(rowIndex, colIndex + 1).CellType = [\"CheckBox\"]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [gridControl1(rowIndex, colIndex + 1).TriState = [True]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                        |
| [gridControl1(rowIndex, colIndex + 1).Description = [\"TriState\"]]                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 74: Check Box Cells

 

[]{#p51} 

 

[]{#related-topics}

