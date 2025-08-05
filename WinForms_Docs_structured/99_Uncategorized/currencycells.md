---
title: currencycells.md
original_path: WinForms_Docs/99_Uncategorized/currencycells.md
created_at: 2025-08-05
---








  









## Currency Cells {#currency-cells style="tab-stops: 0pt"}

 

Currency cell is useful to represent monetary values to achieve accuracy in the calculations.

This stripes the currency sign in the cell and attempts to parse only the number from the input.

 

The following table consists of GridStyleInfo properties are used to customize these cells:

[] 


+-------------------------+---------------------------------------------------------------------+------------------+------------------+-------------------------------------------------------------------------------------------------------+
| Name of Property        | Description                                                         | Type of Property | Value It Accepts | Property Syntax                                                                                       |
+-------------------------+---------------------------------------------------------------------+------------------+------------------+-------------------------------------------------------------------------------------------------------+
| CellType                | Set to "CurrencyEdit".                                              | Normal           |  string          | grid.Model\[6, 2\].CellType = \"CurrencyEdit\";                                                       |
+-------------------------+---------------------------------------------------------------------+------------------+------------------+-------------------------------------------------------------------------------------------------------+
| CurrencyDecimalDigits   | Sets the number of decimal places in currency value.                | Normal           | Int              |  grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                                              |
|                         |                                                                     |                  |                  |                                                                                                       |
|                         |                                                                     |                  |                  |                 CurrencyDecimalDigits = 2               };                                            |
+-------------------------+---------------------------------------------------------------------+------------------+------------------+-------------------------------------------------------------------------------------------------------+
| CurrencyNegativePattern | Sets the format pattern for negative currency values.               |  Normal          | Int              | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                                               |
|                         |                                                                     |                  |                  |                                                                                                       |
|                         |                                                                     |                  |                  |   CurrencyNegativePattern = 11 };                                                                     |
+-------------------------+---------------------------------------------------------------------+------------------+------------------+-------------------------------------------------------------------------------------------------------+
| CurrencyPositivePattern | Sets the format pattern for positive currency values.               | Normal           | Int              | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                                               |
|                         |                                                                     |                  |                  |                                                                                                       |
|                         |                                                                     |                  |                  |    CurrencyPositivePattern = 1 };                                                                     |
+-------------------------+---------------------------------------------------------------------+------------------+------------------+-------------------------------------------------------------------------------------------------------+
| CurrencySymbol          | Sets the string to use as currency symbol.                          | Normal           | String           | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{CurrencySymbol = \"\$\"};                      |
+-------------------------+---------------------------------------------------------------------+------------------+------------------+-------------------------------------------------------------------------------------------------------+
| CurrencyGroupSizes      | Sets the number of digits in each group to the left of the decimal. | Normal           | int\[\]          | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{CurrencyGroupSizes = new int\[\] { 2, 3, 4 }}; |
+-------------------------+---------------------------------------------------------------------+------------------+------------------+-------------------------------------------------------------------------------------------------------+


[] 

**[]** 

Creating a Currency Cell

 

1.   Create a Currency Cell with a Negative Currency Value and '\$' as the Currency Symbol. The following code illustrates this[.]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                          |
|                                                                                                                                               |
| [\[C#\]]                                                                                                  |
|                                                                                                                                               |
| [grid.Model\[6, 2\].CellType = [\"CurrencyEdit\"];]                               |
|                                                                                                                                               |
| [grid.Model\[6, 2\].CurrencyEdit.MinValue = 5;]                                                           |
|                                                                                                                                               |
| [grid.Model\[6, 2\].CurrencyEdit.MaxValue = 1000;]                                                        |
|                                                                                                                                               |
| [grid.Model\[6, 2\].NumberFormat = [new] [NumberFormatInfo]] |
|                                                                                                                                               |
| [            {]                                                                                           |
|                                                                                                                                               |
| [                CurrencyPositivePattern = 0,]                                                            |
|                                                                                                                                               |
| [                CurrencyDecimalDigits = 4,]                                                              |
|                                                                                                                                               |
| [                CurrencyNegativePattern = 0,]                                                            |
|                                                                                                                                               |
| [                CurrencySymbol = "\$",]                                                                  |
|                                                                                                                                               |
| [                CurrencyGroupSizes = new int\[\]{2, 3, 4}]                                               |
|                                                                                                                                               |
| [            };]                                                                                          |
|                                                                                                                                               |
| [grid.Model\[6, 2\].CellValue = -4.0;]                                                                    |
|                                                                                                                                               |
| []                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays.

[] 

{border="0"}

Figure 202: Currency Cell With Negative Value

***[]*** 

 

2.   Create a Currency Cell with a Positive Value and '\$' as the Currency Symbol and with a different positive pattern. The following code illustrates this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                |
| [grid.Model\[10, 2\].CellType = [\"CurrencyEdit\"];]                               |
|                                                                                                                                                |
| [grid.Model\[10, 2\].CurrencyEdit.MinValue = 5;]                                                           |
|                                                                                                                                                |
| [grid.Model\[10, 2\].CurrencyEdit.MaxValue = 1000;]                                                        |
|                                                                                                                                                |
| [grid.Model\[10, 2\].NumberFormat = [new] [NumberFormatInfo]] |
|                                                                                                                                                |
| [            {]                                                                                            |
|                                                                                                                                                |
| [                CurrencyPositivePattern = 1,]                                                             |
|                                                                                                                                                |
| [                CurrencyDecimalDigits = 2,]                                                               |
|                                                                                                                                                |
| [                CurrencyNegativePattern = 11,]                                                            |
|                                                                                                                                                |
| [                CurrencySymbol = [\"\$\"],]                                       |
|                                                                                                                                                |
| [                CurrencyGroupSizes = [new] [int]\[\]{2, 3, 4}]  |
|                                                                                                                                                |
| [            };]                                                                                           |
|                                                                                                                                                |
| [grid.Model\[10, 2\].CellValue = 36.0;]                                                                    |
|                                                                                                                                                |
| []                                                                                                         |
|                                                                                                                                                |
| []                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays.

[] 

[] 

{border="0"}

Figure 203: Currency Cell With Positive Value

**[]** 

DoubleEdit Cells

 

Using DoubleEdit cell restricts you to enter only double (value type) values into the cell. This is useful to display System.Double type values.

 

The following table consists of GridStyleInfo properties are used to customize these cells.

[] 


  ------------------------ ----------------------------------------------------------------------------- ------------------ ------------------ ----------------------------------------------------------------------------------------------------------------------
  Name of Property         Description                                                                   Type of Property   Value It Accepts   Property Syntax
  Cell Type                Set to "DoubleEdit"                                                           Normal              String            grid.Model\[6, 2\].CellType = \"DoubleEdit\";
  NumberGroupSeparator     Sets the string that separates groups of digits to the left of the decimal.   Normal              String            grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberGroupSeparator = \"@\" };
  NumberDecimalSeparator   Sets the string to use as decimal separator.                                  Normal              String            grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberDecimalSeparator = \".\" };
  NumberDecimalDigits      Sets the number of decimal places.                                            Normal             int                grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberDecimalDigits = 0};
  NumberGroupSizes         Sets the number of digits in each group to the left of the decimal.           Normal             Int\[\]             grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberGroupSizes = new int\[\] { 2, 3, 4 }};
  ------------------------ ----------------------------------------------------------------------------- ------------------ ------------------ ----------------------------------------------------------------------------------------------------------------------


**[]** 

Creating DoubleEdit Cells

 

The following code example illustrates creating three double edit cells using different group separator and different decimal digits.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [grid.Model\[6, 2\].CellType = [\"DoubleEdit\"];]                                                                                  |
|                                                                                                                                                                                                |
| [            [this].grid.Model.CoveredCells.Add([new] [CoveredCellInfo](6, 2, 6, 3));]   |
|                                                                                                                                                                                                |
| [            grid.Model\[6, 2\].NumberFormat = [new] [NumberFormatInfo]]                                      |
|                                                                                                                                                                                                |
| [            {]                                                                                                                                            |
|                                                                                                                                                                                                |
| [                NumberGroupSeparator = [\"@\"],]                                                                                  |
|                                                                                                                                                                                                |
| [                NumberDecimalSeparator = [\".\"],]                                                                                |
|                                                                                                                                                                                                |
| [                NumberDecimalDigits = 0,]                                                                                                                 |
|                                                                                                                                                                                                |
| [                NumberGroupSizes = [new] [int]\[\] { 2, 3, 4 }]                                                 |
|                                                                                                                                                                                                |
| [            };]                                                                                                                                           |
|                                                                                                                                                                                                |
| [            grid.Model\[6, 2\].CellValue = 12345678.00;]                                                                                                  |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [            grid.Model\[8, 2\].CellType = [\"DoubleEdit\"];]                                                                      |
|                                                                                                                                                                                                |
| [            [this].grid.Model.CoveredCells.Add([new] [CoveredCellInfo](8, 2, 8, 8));]   |
|                                                                                                                                                                                                |
| [            grid.Model\[8, 2\].NumberFormat = [new] [NumberFormatInfo]]                                      |
|                                                                                                                                                                                                |
| [            {]                                                                                                                                            |
|                                                                                                                                                                                                |
| [                NumberGroupSeparator = [\",\"],]                                                                                  |
|                                                                                                                                                                                                |
| [                NumberDecimalSeparator = [\".\"],]                                                                                |
|                                                                                                                                                                                                |
| [                NumberDecimalDigits = 4,]                                                                                                                 |
|                                                                                                                                                                                                |
| [                NumberGroupSizes = [new] [int]\[\] { 2, 3, 4 }]                                                 |
|                                                                                                                                                                                                |
| [            };]                                                                                                                                           |
|                                                                                                                                                                                                |
| [            grid.Model\[8, 2\].CellValue = 12;]                                                                                                           |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [            grid.Model\[10, 2\].CellValue = 2345.00;]                                                                                                     |
|                                                                                                                                                                                                |
| [            grid.Model\[10, 2\].CellType = [\"DoubleEdit\"];]                                                                     |
|                                                                                                                                                                                                |
| [            [this].grid.Model.CoveredCells.Add([new] [CoveredCellInfo](10, 2, 10, 3));] |
|                                                                                                                                                                                                |
| [            grid.Model\[10, 2\].NumberFormat = [new] [NumberFormatInfo]]                                     |
|                                                                                                                                                                                                |
| [            {]                                                                                                                                            |
|                                                                                                                                                                                                |
| [                NumberGroupSeparator = [\";\"],]                                                                                  |
|                                                                                                                                                                                                |
| [                NumberDecimalSeparator = [\".\"],]                                                                                |
|                                                                                                                                                                                                |
| [                NumberDecimalDigits = 4,]                                                                                                                 |
|                                                                                                                                                                                                |
| [                NumberGroupSizes = [new] [int]\[\]{2, 3, 4}]                                                    |
|                                                                                                                                                                                                |
| [            };]                                                                                                                                           |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

When the code runs, the following output displays.

[] 

{border="0"}

Figure 204: DoubleEdit Cells

**[]** 

IntegerEdit Cells

 

IntegerEdit is a specialized cell type that restricts the data entry to integers. The following table consists of GridStyleInfo properties are used to customize these cells.

[] 


  ---------------------- ------------------------------------------------- ------------------ ------------------ ----------------------------------------------------------------------------------------------------------------------
  Name of Property       Description                                       Type of Property   Value It Accepts   Property Syntax
  CellType               Set to "IntegerEdit"                              Normal             String              grid.Model\[6, 2\].CellType = \"IntegerEdit\";
  NumberGroupSeparator   Sets the string that separates groups of digits   Normal             String             grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberGroupSeparator = \";\" };
  NumberGroupSizes       Sets the number of digits in each group           Normal             int\[\]             grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                NumberGroupSizes = new int\[\] { 2, 3, 4 }};
  ---------------------- ------------------------------------------------- ------------------ ------------------ ----------------------------------------------------------------------------------------------------------------------


[] 

Creating Integer Edit Cells

 

The following code example illustrates creating three different Integer Edit Cells.

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                       |
| [            int][\[\] sizes = { 2, 3, 4 };]                                                                                     |
|                                                                                                                                                                                                                       |
| [            grid.Model\[4, 2\].CellType = [\"IntegerEdit\"];]                                                                                            |
|                                                                                                                                                                                                                       |
| [            grid.Model\[4, 2\].IsEditable = [true];]                                                                                                        |
|                                                                                                                                                                                                                       |
| [            grid.Model\[4, 2\].NumberFormat = [new] [NumberFormatInfo] { NumberGroupSeparator = [\"@\"] };] |
|                                                                                                                                                                                                                       |
| [            grid.Model\[4, 2\].NumberFormat.NumberGroupSizes = sizes;]                                                                                                           |
|                                                                                                                                                                                                                       |
| [            grid.Model\[4, 2\].CellValue = 1000; ]                                                                                                                               |
|                                                                                                                                                                                                                       |
| [            ]                                                                                                                                                                    |
|                                                                                                                                                                                                                       |
| [            grid.Model\[6, 2\].CellType = [\"IntegerEdit\"];]                                                                                            |
|                                                                                                                                                                                                                       |
| [            grid.Model\[6, 2\].IsEditable = [true];]                                                                                                        |
|                                                                                                                                                                                                                       |
| [            grid.Model\[6, 2\].NumberFormat = [new] [NumberFormatInfo] { NumberGroupSeparator = [\",\"] };] |
|                                                                                                                                                                                                                       |
| [            grid.Model\[6, 2\].NumberFormat.NumberGroupSizes = sizes;]                                                                                                           |
|                                                                                                                                                                                                                       |
| [            grid.Model\[6, 2\].CellValue = 1;]                                                                                                                                   |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [            grid.Model\[8, 2\].CellType = [\"IntegerEdit\"];]                                                                                            |
|                                                                                                                                                                                                                       |
| [            grid.Model\[8, 2\].IsEditable = [true];]                                                                                                        |
|                                                                                                                                                                                                                       |
| [            grid.Model\[8, 2\].NumberFormat = [new] [NumberFormatInfo] { NumberGroupSeparator = [\";\"] };] |
|                                                                                                                                                                                                                       |
| [            grid.Model\[8, 2\].NumberFormat.NumberGroupSizes = sizes;]                                                                                                           |
|                                                                                                                                                                                                                       |
| [            grid.Model\[8, 2\].CellValue = 222222;]                                                                                                                              |
|                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

When the code runs, the following output displays.

[] 

[] 

{border="0"}

Figure 205: Integer Edit Cells

***[]*** 

PercentEdit Cells

The PercentEdit cell type restricts you in data entry. This accepts only percentage values.

The following table consists of GridStyleInfo properties are used to customize these cells.

[] 


+-----------------------+----------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------------------------------------------------------------------+
| Name of Property      | Description                                                                | Type of Property | Value It Accepts | Property Syntax                                                                                              |
+-----------------------+----------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------------------------------------------------------------------+
| CellType              | Set to "PercentEdit".                                                      | Normal           | String           |  grid.Model\[6, 2\].CellType = \"PercentEdit\";                                                              |
+-----------------------+----------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------------------------------------------------------------------+
| PercentSymbol         | Sets the string to use as the percent symbol.                              | Normal           | String           | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                                                      |
|                       |                                                                            |                  |                  |                                                                                                              |
|                       |                                                                            |                  |                  | PercentSymbol = \"%\"};                                                                                      |
+-----------------------+----------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------------------------------------------------------------------+
| PercentGroupSizes     | Sets the number of digits in each group to the left of the decimal.        | Normal           |  int\[\]         | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                PercentGroupSizes = new int\[\] {3}}; |
+-----------------------+----------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------------------------------------------------------------------+
| PercentGroupSeparator | Sets the string that separates group of digits to the left of the decimal. | Normal           | String           | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                PercentGroupSeparator = \",\"};       |
+-----------------------+----------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------------------------------------------------------------------+
| PercentDecimalDigits  | Sets the number of digits that appear after the decimal.                   | Normal           | int              | grid.Model\[6, 2\].NumberFormat = new NumberFormatInfo{                PercentDecimalDigits = 4};            |
+-----------------------+----------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------------------------------------------------------------------+


[] 

**[]** 

Creating PercentEdit cell

The following code example illustrates creating two Percent Edit cells with different group sizes and decimal digits.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                 |
| [var][ percentStyleInfo = [this].grid.Model\[7, 2\];] |
|                                                                                                                                                                 |
| [            percentStyleInfo.CellType = [\"PercentEdit\"];]                                        |
|                                                                                                                                                                 |
| [            percentStyleInfo.NumberFormat = [new] [NumberFormatInfo]()]       |
|                                                                                                                                                                 |
| [            {]                                                                                                             |
|                                                                                                                                                                 |
| [                PercentSymbol = [\"%\"],]                                                          |
|                                                                                                                                                                 |
| [                PercentGroupSizes = [new] [int]\[\] { 1, 2, 3 },]                |
|                                                                                                                                                                 |
| [                PercentDecimalDigits = 2,]                                                                                 |
|                                                                                                                                                                 |
| [                PercentGroupSeparator = [\",\"],]                                                  |
|                                                                                                                                                                 |
| [            };]                                                                                                            |
|                                                                                                                                                                 |
| [            percentStyleInfo.CellValue = 19;]                                                                              |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [            [var] percentStyleInfo2 = [this].grid.Model\[9, 2\];]                |
|                                                                                                                                                                 |
| [            percentStyleInfo2.CellType = [\"PercentEdit\"];]                                       |
|                                                                                                                                                                 |
| [            percentStyleInfo2.NumberFormat = [new] [NumberFormatInfo]()]      |
|                                                                                                                                                                 |
| [            {]                                                                                                             |
|                                                                                                                                                                 |
| [                PercentSymbol = [\"%\"],]                                                          |
|                                                                                                                                                                 |
| [                PercentGroupSizes = [new] [int]\[\] { 3 },]                      |
|                                                                                                                                                                 |
| [                PercentDecimalDigits = 4,]                                                                                 |
|                                                                                                                                                                 |
| [                PercentGroupSeparator = [\",\"],]                                                  |
|                                                                                                                                                                 |
| [            };]                                                                                                            |
|                                                                                                                                                                 |
| [            percentStyleInfo2.CellValue = 91;]                                                                             |
|                                                                                                                                                                 |
| **[]**                                                                                                                      |
|                                                                                                                                                                 |
| []                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays.

[] 

{border="0"}

Figure 206: Percent Edit Cells

**[]** 

UpDownEdit Cells

 

UpDownEdit cell enables you to increase or decrease the cell value with a pair of arrow buttons in the cell.

The following table consists of GridStyleInfo properties are used to customize these cells.

 


  ------------------ ----------------------------------------------------------------------------------- ------------------ ------------------ -------------------------------------------------
  Name of Property   Description                                                                         Type of Property   Value It Accepts   Property Syntax
  CellType           Set to "UpDownEdit".                                                                Normal             String             grid.Model\[6, 2\].CellType = \"UpDownEdit\";
  MaxValue           Sets the upper limit in the range of applicable values.                             Normal             Double              grid.Model\[6, 2\].UpDownEdit.MaxValue = 1000;
  MinValue           Sets the lower limit in the range of applicable values.                             Normal             Double             grid.Model\[6, 2\].UpDownEdit.MinValue = 500;
  Step               Sets the unit value to be increased /decreased when the spin buttons are clicked.   Normal             Double             grid.Model\[6, 2\].UpDownEdit.Step = 50;
  ------------------ ----------------------------------------------------------------------------------- ------------------ ------------------ -------------------------------------------------


[] 

[] 

[] 

[] 

Creating UpDownEdit cell

The following code example illustrates sets up three different Up and Down controls in grid cells[.]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                 |
| [            grid.Model\[6, 2\].CellType = [\"UpDownEdit\"];]                       |
|                                                                                                                                                 |
| [            grid.Model\[6, 2\].UpDownEdit.MinValue = 500;]                                                 |
|                                                                                                                                                 |
| [            grid.Model\[6, 2\].UpDownEdit.MaxValue = 1000;]                                                |
|                                                                                                                                                 |
| [            grid.Model\[6, 2\].UpDownEdit.Step = 50;]                                                      |
|                                                                                                                                                 |
| [            grid.Model\[6, 2\].HorizontalAlignment = [HorizontalAlignment].Right;] |
|                                                                                                                                                 |
| []                                                                                                          |
|                                                                                                                                                 |
| [            grid.Model\[8, 2\].CellType = [\"UpDownEdit\"];]                       |
|                                                                                                                                                 |
| [            grid.Model\[8, 2\].UpDownEdit.MinValue = 5;]                                                   |
|                                                                                                                                                 |
| [            grid.Model\[8, 2\].UpDownEdit.MaxValue = 100;]                                                 |
|                                                                                                                                                 |
| [            grid.Model\[8, 2\].UpDownEdit.Step = 5;]                                                       |
|                                                                                                                                                 |
| [            grid.Model\[8, 2\].HorizontalAlignment = [HorizontalAlignment].Right;] |
|                                                                                                                                                 |
| []                                                                                                          |
|                                                                                                                                                 |
| [            grid.Model\[4, 2\].CellType = [\"UpDownEdit\"];]                       |
|                                                                                                                                                 |
| [            grid.Model\[4, 2\].UpDownEdit.MinValue = 10;]                                                  |
|                                                                                                                                                 |
| [            grid.Model\[4, 2\].UpDownEdit.MaxValue = 18;]                                                  |
|                                                                                                                                                 |
| [            grid.Model\[4, 2\].UpDownEdit.Step = 2;]                                                       |
|                                                                                                                                                 |
| [            grid.Model\[4, 2\].HorizontalAlignment = [HorizontalAlignment].Right;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays.

[] 

[] 

{border="0"}

Figure 207: UpDown Edit cells

[]{#related-topics}

