---
title: propertiesdeprecated.md
original_path: WinForms_Docs/99_Uncategorized/propertiesdeprecated.md
created_at: 2025-08-05
---






##### Properties Deprecated {#properties-deprecated style="tab-stops: 0pt"}

+---------------------------------------------------------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Property                                                      | Alternatives                 | Comments                                                                                                                       |
+---------------------------------------------------------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| [[NullState]]{.MsoSubtleEmphasis}     | IsNull                       | Deprecated as it should have Getter alone.                                                                                     |
+---------------------------------------------------------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| [[UseNullString]]{.MsoSubtleEmphasis} | AllowNull                    | This behavior is incorporated with AllowNull; previously both AllowNull and UseNullString existed. Removed for better clarity. |
+---------------------------------------------------------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| [[IsNullValue]]{.MsoSubtleEmphasis}   | IsNull                       | IsNullValue means the same as NullState and IsNull, and it has been deprecated for better clarity.                             |
+---------------------------------------------------------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| [[MaxLength]]{.MsoSubtleEmphasis} | MaxValue,                    |                                                                                                                                |
|                                                               |                              |                                                                                                                                |
|                                                               | NumberDecimalDigits          |                                                                                                                                |
|                                                               |                              |                                                                                                                                |
|                                                               |                              | Max length is removed as there is a conflict. Hence use MaxValue and NumberDecimalDigits as alternatives.                      |
+---------------------------------------------------------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| EnforceMinMaxDuringValidating                                 | OnValidationFailed.KeepFocus | No need for a separate property                                                                                                |
|                                                               |                              |                                                                                                                                |
|                                                               |                              | as MinMaxValidation already exists                                                                                             |
|                                                               |                              |                                                                                                                                |
|                                                               |                              | The same behavior can be achieved with the alternative.                                                                        |
+---------------------------------------------------------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

