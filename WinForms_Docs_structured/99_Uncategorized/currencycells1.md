---
title: currencycells1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\currencycells1.md
created_at: 2025-07-03
---






##### Currency Cells {#currency-cells style="tab-stops: 0pt"}

This cell type can be used to represent monetary values to achieve accuracy in the calculations. It will stripe the currency sign in the cell and attempt to parse only the number from the input. Use the GridStyleInfo properties below to customize these cells.

[] 


  -------------------------- -------------------------------------------------------------
  GridStyleInfo Property     Description
  Cell Type                  Set to "CurrencyEdit".
  CurrencyDecimalDigits      Number of decimal places in currency value.
  CurrencyDecimalSeparator   String to use as decimal separator.
  CurrencyNeagtivePattern    Format pattern for negative currency values.
  CurrencyPostivePattern     Format pattern for positive currency values.
  CurrencySymbol             String to use as currency symbol.
  CurrencyGroupSizes         Number of digits in each group to the left of the decimal .
  -------------------------- -------------------------------------------------------------


**[]** 

Creating a Currency Cell with a Negative Currency Value with '.' as the Decimal Separator.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                               |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| [int][\[\] sizes = { 2, 3, 4 };   ] |
|                                                                                                                          |
| [grid.Model\[6, 2\].CellType = [\"CurrencyEdit\"];]          |
|                                                                                                                          |
| [grid.Model\[6, 2\].IsEditable = [true];]                       |
|                                                                                                                          |
| [grid.Model\[6, 2\].NumberFormat = [new] NumberFormatInfo ]     |
|                                                                                                                          |
| [{ ]                                                                                 |
|                                                                                                                          |
| [CurrencyDecimalDigits = 4, ]                                                        |
|                                                                                                                          |
| [CurrencyDecimalSeparator = [\".\"], ]                       |
|                                                                                                                          |
| [CurrencyNegativePattern = 0, ]                                                      |
|                                                                                                                          |
| [CurrencyPositivePattern = 0, ]                                                      |
|                                                                                                                          |
| [CurrencySymbol = [\"\$\"] ]                                 |
|                                                                                                                          |
| [};]                                                                                 |
|                                                                                                                          |
| [grid.Model\[6, 2\].NumberFormat.CurrencyGroupSizes = sizes;]                        |
|                                                                                                                          |
| [grid.Model\[6, 2\].CellValue = -4.0;]                                               |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

Output

The following output is generated using the code above.

[] 

[{border="0"}][]

Figure 25: Currency Cell

 

Currency Cell with a Negative Currency Value and a Different Negative Pattern

+--------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                               |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| [int][\[\] sizes = { 2, 3, 4 };   ] |
|                                                                                                                          |
| [grid.Model\[10, 2\].CellType = [\"CurrencyEdit\"];]         |
|                                                                                                                          |
| [grid.Model\[10, 2\].IsEditable = [true];]                      |
|                                                                                                                          |
| [grid.Model\[10, 2\].NumberFormat = [new] NumberFormatInfo ]    |
|                                                                                                                          |
| [{ ]                                                                                 |
|                                                                                                                          |
| [    CurrencyDecimalDigits = 2, ]                                                    |
|                                                                                                                          |
| [    CurrencyDecimalSeparator = [\".\"], ]                   |
|                                                                                                                          |
| [    CurrencyNegativePattern = 5, ]                                                  |
|                                                                                                                          |
| [    CurrencyPositivePattern = 1, ]                                                  |
|                                                                                                                          |
| [    CurrencySymbol = [\"\$\"] ]                             |
|                                                                                                                          |
| [};]                                                                                 |
|                                                                                                                          |
| [grid.Model\[10, 2\].NumberFormat.CurrencyGroupSizes = sizes;]                       |
|                                                                                                                          |
| [grid.Model\[10, 2\].CellValue = -14.0;]                                             |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

Output

The following output is generated using the code above.

[] 

[{border="0"}][]

Figure 26: Currency Cell

 

Currency Cell with a Positive Currency Value with '.' as the Decimal Separator and '\$' as Currency Symbol

 

+--------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                               |
|                                                                                                                          |
| []                                                                                   |
|                                                                                                                          |
| [int][\[\] sizes = { 2, 3, 4 };   ] |
|                                                                                                                          |
| [grid.Model\[14, 2\].CellType = [\"CurrencyEdit\"];]         |
|                                                                                                                          |
| [grid.Model\[14, 2\].IsEditable = [true];]                      |
|                                                                                                                          |
| [grid.Model\[14, 2\].NumberFormat = [new] NumberFormatInfo ]    |
|                                                                                                                          |
| [{]                                                                                  |
|                                                                                                                          |
| [    CurrencyDecimalDigits = 4, ]                                                    |
|                                                                                                                          |
| [    CurrencyDecimalSeparator = [\".\"], ]                   |
|                                                                                                                          |
| [    CurrencyNegativePattern = 11, ]                                                 |
|                                                                                                                          |
| [    CurrencyPositivePattern = 2, ]                                                  |
|                                                                                                                          |
| [    CurrencySymbol = [\"\$\"]]                              |
|                                                                                                                          |
| [};]                                                                                 |
|                                                                                                                          |
| [grid.Model\[14, 2\].NumberFormat.CurrencyGroupSizes = sizes;]                       |
|                                                                                                                          |
| [grid.Model\[14, 2\].CellValue = 36.0][;]        |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

Output

The following output is generated using the code above.

[] 

{border="0"}

Figure 27: Currency Cell with a Positive Value


{border="0"}Note: For complete code, please refer to the following browser sample.


[] 

***\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\Cell Types\\Currency Cell Demo***

**** 

[]{#related-topics}

