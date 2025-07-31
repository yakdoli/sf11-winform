---
title: supportedalgebra.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\supportedalgebra.md
created_at: 2025-07-03
---








  









## Supported Algebra {#supported-algebra style="tab-stops: 0pt"}

[]{#p48} 

The explicit look of a valid formula in Essential Calculate may vary depending upon the context of the formula. For example, if you are using a formula in a **CalcSheet** class based on an Excel spreadsheet, then something like = A1 + A3 will be valid since CalcSheet recognizes the \"A1\" and \"A3\" as valid cell references. But, if you are using a **CalcQuickBase** object to manage formulas for controls on a Windows Form, then the same = A1 + A3 will not be valid since CalcQuickBase only recognizes registered names inside square brackets as valid arguments. Hence, all Essential Calculation formulas support the same algebra with the exception of what comprises the definition of valid arguments.

 

This section comprises the following topics:

 

More:











