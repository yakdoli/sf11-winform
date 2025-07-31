---
title: integereditcells.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\integereditcells.md
created_at: 2025-07-03
---






##### Integer Edit Cells {#integer-edit-cells style="tab-stops: 0pt"}

IntegerEdit is a specialized cell type that restricts the data entry to integers. The table below lists the style properties specific to this cell type.

 

Table 10: GridStyleInfo Property


  ------------------------ ----------------------------------------
  GridStyleInfo Property   Description
  Cell Type                Set to "IntegerEdit"
  NumberGroupSeparator     String that separates groups of digits
  NumberGroupSizes         Number of digits in each group
  ------------------------ ----------------------------------------


**[]** 

Example

Setting up Three Different Integer Edit Cells.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                      |
|                                                                                                                                                                                 |
| []                                                                                                                             |
|                                                                                                                                                                                 |
| [int][\[\] sizes = { 2, 3, 4 };]                                                           |
|                                                                                                                                                                                 |
| [grid.Model\[12, 2\].CellType = [\"IntegerEdit\"];]                                                                 |
|                                                                                                                                                                                 |
| [grid.Model\[12, 2\].IsEditable = [true];]                                                                             |
|                                                                                                                                                                                 |
| [grid.Model\[12, 2\].NumberFormat = [new] NumberFormatInfo { NumberGroupSeparator = [\",\"]};] |
|                                                                                                                                                                                 |
| [grid.Model\[12, 2\].NumberFormat.NumberGroupSizes = sizes;]                                                                                |
|                                                                                                                                                                                 |
| [grid.Model\[12, 2\].CellValue = 1;]                                                                                                        |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [grid.Model\[8, 2\].CellType = [\"IntegerEdit\"];]                                                                  |
|                                                                                                                                                                                 |
| [grid.Model\[8, 2\].IsEditable = [true];]                                                                              |
|                                                                                                                                                                                 |
| [grid.Model\[8, 2\].NumberFormat = [new] NumberFormatInfo { NumberGroupSeparator = [\";\"]};]  |
|                                                                                                                                                                                 |
| [grid.Model\[8, 2\].NumberFormat.NumberGroupSizes = sizes;]                                                                                 |
|                                                                                                                                                                                 |
| [grid.Model\[8, 2\].CellValue = 222222;]                                                                                                    |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [grid.Model\[10, 2\].CellType = [\"IntegerEdit\"];]                                                                 |
|                                                                                                                                                                                 |
| [grid.Model\[10, 2\].IsEditable = [true];]                                                                             |
|                                                                                                                                                                                 |
| [grid.Model\[10, 2\].NumberFormat = [new] NumberFormatInfo { NumberGroupSeparator = [\"@\"]};] |
|                                                                                                                                                                                 |
| [grid.Model\[10, 2\].NumberFormat.NumberGroupSizes = sizes;]                                                                                |
|                                                                                                                                                                                 |
| [grid.Model\[10, 2\].CellValue = 1000;]                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The following output is generated using the code above.

 

{border="0"}

Figure 30: Integer Edit


{border="0"}Note: For complete code, please refer to the following browser sample.


 

***\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\Cell Types\\Interger Edit Cell Demo***

**** 

**** 

**** 

[]{#related-topics}

