---
title: datetimepicker.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\datetimepicker.md
created_at: 2025-07-03
---






##### Date Time Picker {#date-time-picker style="tab-stops: 0pt"}

[] 

The Date Time Picker cell type can be embedded into a cell as a drop-down container, where the date and time picker will be added in the drop-down. The cell value of the corresponding cell has to be specified as date value. Various formats of the date and time can be provided in the **Format** style property.

 

The following code examples illustrate how to set the cell type to DateTimePicker.

[] 

1.   Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].DateTimePicker);]   |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[4, 2\].CellType = [CustomCellTypes].DateTimePicker.ToString();]    |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[4, 2\].CellValueType = [typeof]([DateTime]);] |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[4, 2\].CellValue = [DateTime].Now;]                                |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[4, 2\].Format = [\"MM/dd/yyyy hh:mm\"];]                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [RegisterCellModel.GridCellType([Me].gridControl1, CustomCellTypes.DateTimePicker)]                            |
|                                                                                                                                                                         |
| [Me][.gridControl1(4, 2).CellType = CustomCellTypes.DateTimePicker.ToString()]     |
|                                                                                                                                                                         |
| [Me][.gridControl1(4, 2).CellValueType = [GetType](DateTime)] |
|                                                                                                                                                                         |
| [Me][.gridControl1(4, 2).CellValue = DateTime.Now]                                 |
|                                                                                                                                                                         |
| [Me][.gridControl1(4, 2).Format = [\"MM/dd/yyyy hh:mm\"]]  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][108][: Date Time Picker Cell]*

 

[]{#p97}[                                                                     ]

[] 

[]{#related-topics}

