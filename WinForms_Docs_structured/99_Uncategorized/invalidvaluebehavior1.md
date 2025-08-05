---
title: invalidvaluebehavior1.md
original_path: WinForms_Docs/99_Uncategorized/invalidvaluebehavior1.md
created_at: 2025-08-05
---






##### InvalidValueBehavior {#invalidvaluebehavior style="tab-stops: 0pt"}

When the value does not match with the ValidationString the behavior is as follows:

[·      ]If the InvalidValueBehaviour is set to none, then it will check the ValidationString.

[·      ]If the InvalidValueBehaviour is set to DisplayErrorMessage, then the Error message will be displayed to you.

[·      ]If the InvalidValueBehaviour is set to ResetValue, then the key press is not allowed.


Note: When the Value matches with the ValidationString then the MaskCompleted property is set to true.


Here is a sample to validate the email address by using the ValidationString property:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **XAML**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][syncfusion][:][MaskedTextBox][ x][:][Name][=\"maskedTextBox\"][ Width][=\"200\"][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                           [ ValidationString][=\"\^(\[\\w-\\.\]+)@((\\\[\[0-9\]{1,3}\\.\[0-9\]{1,3}\\.\[0-]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                                 9\]{1,3}\\.)\|((\[\\w-\]+\\.)+))(\[a-zA-Z\]{2,4}\|\[0-9\]{1,3})\"][ ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                           [ InvalidValueBehavior][=\"DisplayErrorMessage\"][ ]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                            StringValidation][=\"OnLostFocus\"/\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

In the LostFocus if the given Value does not match with the ValidationString it will display an error message.

{border="0"}

 

Figure 683: MaskedTextBox with validation message

See Also

[]{.UGHyperlink}

[]{.UGHyperlink}

[]{.UGHyperlink}

 

[]{#related-topics}

