---
title: validationstring3.md
original_path: WinForms_Docs/99_Uncategorized/validationstring3.md
created_at: 2025-08-05
---






#### Validation String {#validation-string style="tab-stops: 0pt"}

When the Mask property is null or empty then the MaskedTextBox will validate the string based on the ValidationString property by using RegEx. Based on the StringValidation property the Value is validated in LostFocus or in KeyPress. For each Validation the StringValidationCompleted Event is triggered.

More:





