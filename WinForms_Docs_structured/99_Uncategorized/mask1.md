---
title: mask1.md
original_path: WinForms_Docs/99_Uncategorized/mask1.md
created_at: 2025-08-05
---






#### Mask {#mask style="tab-stops: 0pt"}

MaskedTextBox has a Mask property by using which you can specify the following input without writing any custom validation logic in your application:

[·      ]Required input characters.

[·      ]Optional input characters.

[·      ]The type of input expected at a given position in the mask; for example, a digit or an alphabetic or alphanumeric character.

[·      ]Mask literals or characters that should appear directly in the MaskedTextBox; for example, the hyphens (-) in a phone number or the currency symbol in a price.

[·      ]Special processing for input characters; for example, to convert alphabetic characters to uppercase.

 

When a MaskedTextBox control is displayed at run time, it represents the mask as a series of prompt characters and optional literal characters. Each editable mask position, representing a required or optional input, is shown with a single prompt character. For example, the number sign (#) is often used as a placeholder for a numeric character input. You can use the PromptChar property to specify a custom prompt character.

Mask must be a string composed of one or more of the masking elements, as shown in the following table:

 

  ---------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Masking Element        Description
  0                      Digit, required. This element will accept any single digit between 0 and 9.
  9                      Digit or space, optional.
  \#                     Digit or space, optional. If this position is blank in the mask, it will be rendered as a space. Plus (+) and minus (-) signs are allowed.
  L                      Letter, required. Restricts input to the ASCII letters a-z and A-Z. This mask element is equivalent to \[a-z A-Z\] in regular expressions.
  ?                      Letter, optional. Restricts input to the ASCII letters a-z and A-Z. This mask element is equivalent to \[a-z A-Z\]? in regular expressions.
  C                      Character, optional. Any non-control character.
  A                      Alphanumeric, required.
  a                      Alphanumeric, optional.
  .                      Decimal placeholder. Determined by the Culture and DecimalSeparator property.
  ,                      Thousands placeholder. Determined by the Culture and NumberGroupSeparator.
  :                      Time separator. Determined by the Culture and TimeSeparator property.
  /                      Date separator. Determined by the Culture and DateSeparator property.
  \$                     Currency symbol. Determined by the Culture property.
  \<                     Shift down. Converts all the characters that follow to lowercase.
  \>                     Shift up. Converts all the characters that follow to uppercase.
  \|                     Disable a previous shift up or shift down.
  All other characters   Literals. All non-mask elements will appear as themselves within the MaskedTextBox. Literals always occupy a static position in the mask at run time and cannot be moved or deleted by the user.
  ---------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| XAML                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][syncfusion][:][MaskedTextBox][ x][:][Name][=\"maskedTextBox\"][ Height][=\"25\"][ Width][=\"150\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                          Mask][=\"00/00/0000\"][ Value][=\"07/02/2010\"/\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------+
| C#                                                                                                                 |
|                                                                                                                    |
|                                                                                                                    |
|                                                                                                                    |
| [maskedTextBox.Value = [\"07/02/2010\"];] |
+--------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

 

Figure 682: MaskedTextBox

 

See Also

[]{.UGHyperlink}

[]{.UGHyperlink}

[]{.UGHyperlink}

 

[]{#related-topics}

