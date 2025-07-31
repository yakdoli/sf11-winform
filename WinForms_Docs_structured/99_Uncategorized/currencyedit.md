---
title: currencyedit.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\currencyedit.md
created_at: 2025-07-03
---






##### Currency Edit {#currency-edit style="tab-stops: 0pt"}

[] 

The **Currency** **Edit** cell type lets you to edit monetary values and display them by using different currency type formats. To achieve this, you must set the **CellType** property to *Currency.* You can set additional properties such as the decimal and group separator for the cell value.

[] 

The following code example illustrates how to set the cell type to CurrencyEdit.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                              |
| []                                                                                         |
|                                                                                                                                              |
| [GridStyleInfo][ style = gridControl1\[row, 2\];]    |
|                                                                                                                                              |
| [style.CellType = [\"Currency\"];]                                               |
|                                                                                                                                              |
| [style.Text = [\"\$1.00\"];]                                                     |
|                                                                                                                                              |
| []                                                                                                       |
|                                                                                                                                              |
| [// Set the clip mode.]                                                                    |
|                                                                                                                                              |
| [style.CurrencyEdit.ClipMode = [CurrencyClipModes].IncludeFormatting;]           |
|                                                                                                                                              |
| []                                                                                                       |
|                                                                                                                                              |
| [// Set formatting properties.]                                                            |
|                                                                                                                                              |
| [style.CurrencyEdit.CurrencyDecimalDigits = 2;]                                                          |
|                                                                                                                                              |
| [style.CurrencyEdit.CurrencyDecimalSeparator = [\".\"];]                         |
|                                                                                                                                              |
| [style.CurrencyEdit.CurrencyGroupSeparator = [\",\"];]                           |
|                                                                                                                                              |
| [style.CurrencyEdit.CurrencyGroupSizes = [new] [int]\[\] {3};] |
|                                                                                                                                              |
| [style.CurrencyEdit.CurrencyNegativePattern = 1;]                                                        |
|                                                                                                                                              |
| [style.CurrencyEdit.CurrencyNumberDigits = 27;]                                                          |
|                                                                                                                                              |
| [style.CurrencyEdit.CurrencyPositivePattern = 0;]                                                        |
|                                                                                                                                              |
| [style.CurrencyEdit.CurrencySymbol = [\"\$\"];]                                  |
|                                                                                                                                              |
| [style.CurrencyEdit.NegativeColor = System.Drawing.[Color].Red;]                 |
|                                                                                                                                              |
| [style.CurrencyEdit.NegativeSign = [\"-\"];]                                     |
|                                                                                                                                              |
| [style.CurrencyEdit.PositiveColor = System.Drawing.[Color].Black;]               |
|                                                                                                                                              |
| [style.FloatCell = [true];]                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Dim][ style [As] GridStyleInfo = gridControl1(row, 2)] |
|                                                                                                                                                                   |
| [style.CellType = [\"Currency\"]]                                                                     |
|                                                                                                                                                                   |
| [style.Text = [\"\$1.00\"]]                                                                           |
|                                                                                                                                                                   |
| []                                                                                                            |
|                                                                                                                                                                   |
| [\' Set the clip mode.]                                                                                         |
|                                                                                                                                                                   |
| [style.CurrencyEdit.ClipMode = CurrencyClipModes.IncludeFormatting]                                                           |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [\' Set formatting properties.]                                                                                 |
|                                                                                                                                                                   |
| [style.CurrencyEdit.CurrencyDecimalDigits = 2]                                                                                |
|                                                                                                                                                                   |
| [style.CurrencyEdit.CurrencyDecimalSeparator = [\".\"]]                                               |
|                                                                                                                                                                   |
| [style.CurrencyEdit.CurrencyGroupSeparator = [\",\"]]                                                 |
|                                                                                                                                                                   |
| [style.CurrencyEdit.CurrencyGroupSizes = [New] [Integer]() {3}]                     |
|                                                                                                                                                                   |
| [style.CurrencyEdit.CurrencyNegativePattern = 1]                                                                              |
|                                                                                                                                                                   |
| [style.CurrencyEdit.CurrencyNumberDigits = 27]                                                                                |
|                                                                                                                                                                   |
| [style.CurrencyEdit.CurrencyPositivePattern = 0]                                                                              |
|                                                                                                                                                                   |
| [style.CurrencyEdit.CurrencySymbol = [\"\$\"]]                                                        |
|                                                                                                                                                                   |
| [style.CurrencyEdit.NegativeColor = System.Drawing.Color.Red]                                                                 |
|                                                                                                                                                                   |
| [style.CurrencyEdit.NegativeSign = [\"-\"]]                                                           |
|                                                                                                                                                                   |
| [style.CurrencyEdit.PositiveColor = System.Drawing.Color.Black]                                                               |
|                                                                                                                                                                   |
| [style.FloatCell = [True]]                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 78: Currency Cells

 

[]{#p55} 

 

[]{#related-topics}

