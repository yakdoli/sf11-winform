---
title: maxvalueonexceedmaxdigit6.md
original_path: WinForms_Docs/99_Uncategorized/maxvalueonexceedmaxdigit6.md
created_at: 2025-08-05
---






##### MaxValueOnExceedMaxDigit {#maxvalueonexceedmaxdigit style="tab-stops: 0pt"}

If this property is set to true, then when you enter a value greater than the MaxValue then it will automatically assign the MaxValue to the Value property. Otherwise it will not allow the key press.


Note: This will be enabled only when the MaxValidation is set to OnKeyPress.

 


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[XAML][]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[\<][syncfusion][:][IntegerTextBox][ x][:][Name][=\"integerTextBox\"][ Height][=\"25\"][ Width][=\"150\"][ ]** |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[                           [ MinValue][=\"-999\"][ MaxValue][=\"999\"] ]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[                           [ MinValidation][=\"OnKeyPress\"][ MaxValidation][=\"OnLostFocus\"]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[                           [ MinValueOnExceedMinDigit][=\"True\"][ ]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[                            MaxValueOnExceedMaxDigit][=\"True\"/\>]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C#]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| **[Syncfusion.Windows.Shared.[IntegerTextBox] integerTextBox = [new] Syncfusion.Windows.Shared.[IntegerTextBox]();]** |
|                                                                                                                                                                                                                                             |
| **[integerTextBox.Width = 150;]**                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| **[integerTextBox.Height = 25;]**                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| **[integerTextBox.MinValue = -999;]**                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| **[integerTextBox.MaxValue = 999;]**                                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| **[integerTextBox.MinValidation = Syncfusion.Windows.Shared.[MinValidation].OnKeyPress;]**                                                                         |
|                                                                                                                                                                                                                                             |
| **[integerTextBox.MaxValidation = Syncfusion.Windows.Shared.[MaxValidation].OnLostFocus;]**                                                                        |
|                                                                                                                                                                                                                                             |
| **[integerTextBox.MinValueOnExceedMinDigit = [true];]**                                                                                                               |
|                                                                                                                                                                                                                                             |
| **[integerTextBox.MaxValueOnExceedMaxDigit = [true];]**[]                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Initially there is no value assigned to the IntegerTextBox. So it displays the default value as zero.

 

{border="0"}

 

Figure 626: IntegerTextBox

 

MaxValidation is set to OnLostFocus, so the MaxValidation will be performed only in the lost focus.

 

{border="0"}

 

Figure 627: IntegerTextBox

 

MinValidation is set to OnKeyPress, so you cannot enter a value less than the MinValue. If you try to enter a value less than the MinValue, then the MinValue will set to the Value property because MinValueOnExceedMinDigit is set to true.

{border="0"}

 

Figure 628: IntegerTextBox

See Also

[]{.UGHyperlink}

[]{.UGHyperlink}

 

[]{#related-topics}

