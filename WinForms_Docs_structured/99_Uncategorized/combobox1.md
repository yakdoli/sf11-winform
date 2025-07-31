---
title: combobox1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\combobox1.md
created_at: 2025-07-03
---






#### Combo Box {#combo-box style="tab-stops: 0pt"}

**[]** 

Essential XlsIO now provides support to read/write a Combo Box control. This is achieved by using the **IComboBoxShape** interface which is used to add a combo box inside a worksheet.

[] 

The following code example illustrates how to read/write a combo box control.

[] 

+----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                |
| **[]**                                                                     |
|                                                                                                                |
| [// Create a Combo Box.]                                     |
|                                                                                                                |
| [IComboBoxShape comboBox1 = sheet.ComboBoxes.AddComboBox(27, 5, 20, 100);] |
|                                                                                                                |
| []                                                                         |
|                                                                                                                |
| [// Assign a value to the Combo Box.]                        |
|                                                                                                                |
| [comboBox1.ListFillRange = sheet\[[\"A1:A12\"]\];] |
|                                                                                                                |
| [comboBox1.LinkedCell = sheet\[[\"C3\"]\];]        |
|                                                                                                                |
| []                                                                         |
|                                                                                                                |
| [// Select an item.]                                         |
|                                                                                                                |
| [comboBox1.SelectedIndex = 6;]                                             |
|                                                                                                                |
| []                                                                         |
|                                                                                                                |
| [// Read a Combo Box.]                                       |
|                                                                                                                |
| [IComboBoxShape comboBox2 = sheet.ComboBoxes\[0\];]                        |
|                                                                                                                |
| [comboBox2.SelectedIndex = 3;]                                             |
+----------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                           |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [\' Create a Combo Box.]                                                                                                                     |
|                                                                                                                                                                                                |
| [Dim][ comboBox1 [As] IComboBoxShape = sheet.ComboBoxes.AddComboBox(27, 5, 20, 100)] |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [\' Assign a value to the Combo Box.]                                                                                                        |
|                                                                                                                                                                                                |
| [comboBox1.ListFillRange = sheet([\"A1:A12\"])]                                                                                    |
|                                                                                                                                                                                                |
| [comboBox1.LinkedCell = sheet([\"C3\"])]                                                                                           |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [\' Select an item.]                                                                                                                         |
|                                                                                                                                                                                                |
| [comboBox1.SelectedIndex = 6]                                                                                                                              |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [\' Read a Combo Box.]                                                                                                                       |
|                                                                                                                                                                                                |
| [Dim][ comboBox2 [As] IComboBoxShape = sheet.ComboBoxes(0)]                          |
|                                                                                                                                                                                                |
| [comboBox2.SelectedIndex = 3]                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 98: Combo Box control added to the Spreadsheet by using Essential XlsIO[]

***[]*** 

[]{#related-topics}

