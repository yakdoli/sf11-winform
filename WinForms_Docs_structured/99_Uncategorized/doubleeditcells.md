---
title: doubleeditcells.md
original_path: WinForms_Docs/99_Uncategorized/doubleeditcells.md
created_at: 2025-08-05
---






##### Double Edit Cells {#double-edit-cells style="tab-stops: 0pt"}

Using DoubleEdit cell type will restrict the user to enter only double(value type) values into the cell. Thus it can be used to display System.Double type values. Below are the style properties that affect this cell.

 

 Table 9: GridStyleInfo Property


  ------------------------ -------------------------------------------------------------------
  GridStyleInfo Property   Description
  Cell Type                Set to "DoubleEdit"
  NumberGroupSeparator     String that separates groups of digits to the left of the decimal
  NumberDecimalSeparator   String to use as decimal separator
  NumberDecimalDigits      Number of decimal places
  ------------------------ -------------------------------------------------------------------


**[]** 

Example

Setting up four Double Edit cells using different group separators and decimal digits.

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                            |
|                                                                                                                       |
| []                                                                   |
|                                                                                                                       |
| [int][\[\] sizes = { 2, 3, 4 };] |
|                                                                                                                       |
| [grid.Model\[6, 2\].CellType = [\"DoubleEdit\"];]         |
|                                                                                                                       |
| [grid.Model\[6, 2\].NumberFormat = [new] NumberFormatInfo ]  |
|                                                                                                                       |
| [{ ]                                                                              |
|                                                                                                                       |
| [    NumberGroupSeparator = [\";\"], ]                    |
|                                                                                                                       |
| [    NumberDecimalSeparator = [\".\"], ]                  |
|                                                                                                                       |
| [    NumberDecimalDigits = 4 ]                                                    |
|                                                                                                                       |
| [};]                                                                              |
|                                                                                                                       |
| [grid.Model\[6, 2\].NumberFormat.NumberGroupSizes = sizes;]                       |
|                                                                                                                       |
| [grid.Model\[6, 2\].CellValue = 2345.00; ]                                        |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [grid.Model\[8, 2\].CellType = [\"DoubleEdit\"];]         |
|                                                                                                                       |
| [grid.Model\[8, 2\].NumberFormat = [new] NumberFormatInfo ]  |
|                                                                                                                       |
| [{ ]                                                                              |
|                                                                                                                       |
| [    NumberGroupSeparator = [\",\"], ]                    |
|                                                                                                                       |
| [    NumberDecimalSeparator = [\".\"], ]                  |
|                                                                                                                       |
| [    NumberDecimalDigits = 4 ]                                                    |
|                                                                                                                       |
| [};]                                                                              |
|                                                                                                                       |
| [grid.Model\[8, 2\].NumberFormat.NumberGroupSizes = sizes;]                       |
|                                                                                                                       |
| [grid.Model\[8, 2\].CellValue = 12;]                                              |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [grid.Model\[10, 2\].CellType = [\"DoubleEdit\"];]        |
|                                                                                                                       |
| [grid.Model\[10, 2\].NumberFormat = [new] NumberFormatInfo ] |
|                                                                                                                       |
| [{ ]                                                                              |
|                                                                                                                       |
| [    NumberGroupSeparator = [\",\"], ]                    |
|                                                                                                                       |
| [    NumberDecimalSeparator = [\".\"], ]                  |
|                                                                                                                       |
| [    NumberDecimalDigits = 1 ]                                                    |
|                                                                                                                       |
| [};]                                                                              |
|                                                                                                                       |
| [grid.Model\[10, 2\].NumberFormat.NumberGroupSizes = sizes;]                      |
|                                                                                                                       |
| [grid.Model\[10, 2\].CellValue = 100;]                                            |
|                                                                                                                       |
| []                                                                                |
|                                                                                                                       |
| [grid.Model\[12, 2\].CellType = [\"DoubleEdit\"];]        |
|                                                                                                                       |
| [grid.Model\[12, 2\].NumberFormat = [new] NumberFormatInfo ] |
|                                                                                                                       |
| [{ ]                                                                              |
|                                                                                                                       |
| [    NumberGroupSeparator = [\"@\"], ]                    |
|                                                                                                                       |
| [    NumberDecimalSeparator = [\".\"], ]                  |
|                                                                                                                       |
| [    NumberDecimalDigits = 0 ]                                                    |
|                                                                                                                       |
| [};]                                                                              |
|                                                                                                                       |
| [grid.Model\[12, 2\].NumberFormat.NumberGroupSizes = sizes;]                      |
|                                                                                                                       |
| [grid.Model\[12, 2\].CellValue = 12345678.00;.00;]                                |
+-----------------------------------------------------------------------------------------------------------------------+

 

Output

The following output is generated using the code above.

 

{border="0"}

Figure 29: Double Edit Cell


{border="0"}Note: For complete code, please refer to the following browser sample.


 

\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\Cell Types\\Double Edit Cell Demo

 

[]{#related-topics}

