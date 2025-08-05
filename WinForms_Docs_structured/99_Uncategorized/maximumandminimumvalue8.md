---
title: maximumandminimumvalue8.md
original_path: WinForms_Docs/99_Uncategorized/maximumandminimumvalue8.md
created_at: 2025-08-05
---






#### Maximum and Minimum Value {#maximum-and-minimum-value style="tab-stops: 0pt"}

[]{#_MinValue_3} 

MinValue

Minimum allowed PercentValue for the PercentTextBox. If the new MinValue property value is greater than the MaxValue property value, then the MaxValue is set equal to the MinValue. If the Value is less than the new MinValue, then the Value property is also set equal to the MinValue.

 

[]{#_MaxValue_3}MaxValue

Maximum allowed PercentValue for the PercentTextBox. If the MinValue property is greater than the new MaxValue property, then the MinValue property value is set equal to the MaxValue. If the current Value is greater than the new MaxValue, then the Value property is set equal to the Maxvalue.

 

[]{#_MinValidation_3}MinValidation

You can validate the MinValue in two ways:

[·      ]OnKeyPress -- MinValue of the PercentTextBox is validated on the key press.

[·      ]OnLostFocus -- MinValue of the PercentTextBox is validated on the lost focus only.

[] 

[]{#_MaxValidation_3}MaxValidation

You can validate the MaxValue in two ways:

[·      ]OnKeyPress -- MaxValue of the PercentTextBox is validated on the key press.

[·      ]OnLostFocus -- MaxValue of the PercentTextBox is validated on the lost focus only.

 

[]{#_MinValueOnExceedMinDigit_3}MinValueOnExceedMinDigit

If this property is set to true, then when you enter a value less than the MinValue then it will automatically assign the MinValue to the PercentValue property. Otherwise it will not allow the key press.


Note: This will be enabled only when the MinValidation is set to OnKeyPress.

 


[]{#_MaxValueOnExceedMaxDigit_3}MaxValueOnExceedMaxDigit

If this property is set to true, then when you enter a value greater than the MaxValue then it will automatically assign the MaxValue to the PercentValue property. Otherwise it will not allow the key press.

 


Note: This will be enabled only when the MaxValidation is set to OnKeyPress.

 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[XAML]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][syncfusion][:][PercentTextBox][ x][:][Name][=\"percentTextBox\"][ Height][=\"25\"][ Width][=\"150\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                           [ MinValue][=\"-999\"][ MaxValue][=\"999\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                           [ MinValidation][=\"OnKeyPress\"][ MaxValidation][=\"OnLostFocus\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                           [ MinValueOnExceedMinDigit][=\"True\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                           [ MaxValueOnExceedMaxDigit][=\"True\"/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[C# ]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [PercentTextBox][ percentTextBox = [new] [PercentTextBox]();] |
|                                                                                                                                                                                                                              |
| [percentTextBox.Width = 150;]                                                                                                                                               |
|                                                                                                                                                                                                                              |
| [percentTextBox.Height = 25;]                                                                                                                                               |
|                                                                                                                                                                                                                              |
| [percentTextBox.MinValue = -999.99;]                                                                                                                                        |
|                                                                                                                                                                                                                              |
| [percentTextBox.MaxValue = 999.99;]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [percentTextBox.MinValidation = [MinValidation].OnKeyPress;]                                                                                        |
|                                                                                                                                                                                                                              |
| [percentTextBox.MaxValidation = [MaxValidation].OnLostFocus;]                                                                                       |
|                                                                                                                                                                                                                              |
| [percentTextBox.MinValueOnExceedMinDigit = [true];]                                                                                                    |
|                                                                                                                                                                                                                              |
| [percentTextBox.MaxValueOnExceedMaxDigit = [true];]                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Initially there is no value assigned to the PercentTextBox. So it displays the default value as zero.

{border="0"}

 

Figure 785: PercentTextBox

 

MaxValidation is set to OnLostFocus, so the MaxValidation will be performed only in the lost focus.

{border="0"}

 

Figure 786: PercentTextBox

 

MinValidation is set to OnKeyPress, so you cannot enter a value less than the MinValue. If you try to enter a value less than the MinValue, then the MinValue will be set to the PercentValue property if the MinValueOnExceedMinDigit is set to true, otherwise it will not allow the key press.

 

{border="0"}

Figure 787: PercentTextBox

[]{#related-topics}

