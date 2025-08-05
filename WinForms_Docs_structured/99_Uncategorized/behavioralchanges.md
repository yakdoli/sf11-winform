---
title: behavioralchanges.md
original_path: WinForms_Docs/99_Uncategorized/behavioralchanges.md
created_at: 2025-08-05
---






##### Behavioral Changes {#behavioral-changes style="tab-stops: 0pt"}

+---------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Property                                                                                                                              | Description                                                                                                                       | Behavior                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| \*MinMaxValidation[[.]]{.MsoSubtleEmphasis}On[[KeyPress]]{.MsoSubtleEmphasis} | [[Each and every key press is validated to make the value meet the constraints.]]{.MsoSubtleEmphasis} | [[This is most useful when the MinValue is less than 10.]]{.MsoSubtleEmphasis} |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   | Refer [Notes] column               |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| \*MinMaxValidation[[.]]{.MsoSubtleEmphasis}OnLostFocus                                                    | Validation happens only when the control loses its focus.                                                                         | This allows the user to enter any value and it is validated when the focus is lost.                        |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   | You can make use of OnValidationFailed property to gain control when validation fails.                     |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   | Refer Notes column                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| MinValue                                                                                                                              | Cannot be greater than MaxValue.                                                                                                  | [[Exception will be thrown.]]{.MsoSubtleEmphasis}                              |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   | [[MaxValue has to be reset the accordingly.]]{.MsoSubtleEmphasis}              |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| MaxValue                                                                                                                              | Cannot be lesser than MinValue                                                                                                    | [[Exception will be thrown.]]{.MsoSubtleEmphasis}                              |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   | [[MinValue  has to be reset the accordingly.]]{.MsoSubtleEmphasis}             |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| NullString                                                                                                                            | Cannot be a Numeric Value that could break the MinValue or MaxValue constraints.                                                  | Ex: MinValue 10, MaxValue 100                                                                              |
|                                                                                                                                       |                                                                                                                                   |                                                                                                            |
|                                                                                                                                       |                                                                                                                                   | and NullString as "111" will break the Min Max Values.                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

 


[]{#_NOTES:}{border="0"}Note:


[] 

[·      ]With **MinMaxValidation.OnKeyPress** and MinValue as 10 set,

 

[·      ]Each and every key press will be validated to meet the constraints, so this will not allow you to enter values less than 10, even if you try to enter 11 you cannot input value as every keypress is validated. This behavior is useful when MinValue is less than 10.

 

[·      ]With **MinMaxValidation.OnLostFocus**, user inputs will be validated only when the control loses its focus. Hence user can input any value.  **OnValidationFailed** will give you access to what action \[SetNullString, SetMinorMax, KeepFocus\] has to be done when Validation fails for the input.

 

[·      ]With **OnValidationFailed.SetNullString** set and AllowNull is **False**,the control will keep its focus.

[]{#related-topics}

