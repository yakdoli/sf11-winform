---
title: maxvalueonexceedmaxdigit5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\maxvalueonexceedmaxdigit5.md
created_at: 2025-07-03
---






##### MaxValueOnExceedMaxDigit {#maxvalueonexceedmaxdigit style="tab-stops: 0pt"}

 

If this property is set to true, then when you enter a value greater than the MaxValue then it will automatically assign the MaxValue to the Value property. Otherwise it will not allow the key press.


Note: This will be enabled only when the MaxValidation is set to OnKeyPress.


 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **XAML[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][DoubleTextBox][ x][:][Name][=\"doubleTextBox\"][ Height][=\"25\"][ Width][=\"150\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                           [ MinValue][=\"-999\"][ MaxValue][=\"999\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                           [ MinValidation][=\"OnKeyPress\"][ MaxValidation][=\"OnLostFocus\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                           [ MinValueOnExceedMinDigit][=\"True\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                           [ MaxValueOnExceedMaxDigit][=\"True\"/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **C#[]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                      |
| [Syncfusion.Windows.Shared.[DoubleTextBox] doubleTextBox = [new] Syncfusion.Windows.Shared.[DoubleTextBox]();] |
|                                                                                                                                                                                                                                      |
| [doubleTextBox.Width = 150;]                                                                                                                                                        |
|                                                                                                                                                                                                                                      |
| [doubleTextBox.Height = 25;]                                                                                                                                                        |
|                                                                                                                                                                                                                                      |
| [doubleTextBox.MinValue = -999;]                                                                                                                                                    |
|                                                                                                                                                                                                                                      |
| [doubleTextBox.MaxValue = 999;]                                                                                                                                                     |
|                                                                                                                                                                                                                                      |
| [doubleTextBox.MinValidation = Syncfusion.Windows.Shared.[MinValidation].OnKeyPress;]                                                                       |
|                                                                                                                                                                                                                                      |
| [doubleTextBox.MaxValidation = Syncfusion.Windows.Shared.[MaxValidation].OnLostFocus;]                                                                      |
|                                                                                                                                                                                                                                      |
| [doubleTextBox.MinValueOnExceedMinDigit = [true];]                                                                                                             |
|                                                                                                                                                                                                                                      |
| [doubleTextBox.MaxValueOnExceedMaxDigit = [true];]                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Initially there is no value assigned to the DoubleTextBox. So it displays the default value as zero.

 

{border="0"}

Figure 432:  DoubleTextBox

 

MaxValidation is set to OnLostFocus, so the MaxValidation will be performed only in the lost focus.

 

{border="0"}

Figure 433: DoubleTextBox

[] 

MinValidation is set to OnKeyPress, so you cannot enter a value less than the MinValue. If you try to enter a value less than the MinValue, then the MinValue will set to the Value property because MinValueOnExceedMinDigit is set to true.

 

{border="0"}

Figure 434: DoubleTextBox

See Also

[]{.UGHyperlink}

[]{.UGHyperlink}

 

[]{#related-topics}

