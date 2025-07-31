---
title: maxvalueonexceedmaxdigit4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\maxvalueonexceedmaxdigit4.md
created_at: 2025-07-03
---






##### MaxValueOnExceedMaxDigit {#maxvalueonexceedmaxdigit style="tab-stops: 0pt"}

 

If this property is set to true, then when you enter a value greater than the MaxValue then it will automatically assign the MaxValue to the Value property. Otherwise it will not allow the key press.


Note: This will be enabled only when the MaxValidation is set to OnKeyPress.

 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][syncfusion][:][CurrencyTextBox][ x][:][Name][=\"currencyTextBox\"][ Height][=\"25\"][ Width][=\"150\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                           [ MinValue][=\"-999\"][ MaxValue][=\"999\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                           [ MinValidation][=\"OnKeyPress\"][ MaxValidation][=\"OnLostFocus\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                           [ MinValueOnExceedMinDigit][=\"True\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                           [ MaxValueOnExceedMaxDigit][=\"True\"/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                         |
| []                                                                                                                  |
|                                                                                                                                                         |
| [Syncfusion.Windows.Shared.[CurrencyTextBox] currencyTextBox = [new] ] |
|                                                                                                                                                         |
| [                          Syncfusion.Windows.Shared.[CurrencyTextBox]();]                  |
|                                                                                                                                                         |
| [currencyTextBox.Width = 100;]                                                                                      |
|                                                                                                                                                         |
| [currencyTextBox.Height = 25;]                                                                                      |
|                                                                                                                                                         |
| [currencyTextBox.MinValue = -999;]                                                                                  |
|                                                                                                                                                         |
| [currencyTextBox.MaxValue = 999;]                                                                                   |
|                                                                                                                                                         |
| [currencyTextBox.MinValidation = Syncfusion.Windows.Shared.[MinValidation].OnKeyPress;]     |
|                                                                                                                                                         |
| [currencyTextBox.MaxValidation = Syncfusion.Windows.Shared.[MaxValidation].OnLostFocus;]    |
|                                                                                                                                                         |
| [currencyTextBox.MinValueOnExceedMinDigit = [true];]                                           |
|                                                                                                                                                         |
| [currencyTextBox.MaxValueOnExceedMaxDigit = [true];]                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Initially there is no value assigned to the CurrencyTextBox. So it displays the default value as zero.

 

{border="0"}

Figure 242: CurrencyTextBox

MaxValidation is set to OnLostFocus, so the MaxValidation will be performed only in the lost focus.

 

{border="0"}

Figure 243: CurrencyTextBox

 

MinValidation is set to OnKeyPress, so you cannot enter a value less than the MinValue. If you try to enter a value less than the MinValue, then the MinValue will be set to the Value property if the MinValueOnExceedMinDigit is set to true, otherwise it will not allow the key press.

 

{border="0"}

Figure 244: CurrencyTextBox

 

 

[]{#related-topics}

