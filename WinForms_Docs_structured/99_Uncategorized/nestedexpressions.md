---
title: nestedexpressions.md
original_path: WinForms_Docs/99_Uncategorized/nestedexpressions.md
created_at: 2025-08-05
---






#### Nested Expressions {#nested-expressions style="tab-stops: 0pt"}

[] 

Nested Expressions are nothing but, combing the expression fields from different ExpressionFieldDescriptors to create a new ExpressionFieldDescriptors. The following code example illustrates this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [ExpressionFieldDescriptor Expcolumn1 = [new] ExpressionFieldDescriptor([\"ExpressionColumn1\"], [\"\[Col1\] + \[Col2\] + \[Col3\]\"]);]    |
|                                                                                                                                                                                                                                                      |
| [this][.GridGroupingControl1.TableDescriptor.ExpressionFields.Add(Expcolumn1);]                                                                                 |
|                                                                                                                                                                                                                                                      |
| [ExpressionFieldDescriptor Expcolumn2 = [new] ExpressionFieldDescriptor([\"ExpressionColumn2\"], [\"\[ExpressionColumn1\] \* \[Col3\]\"]);] |
|                                                                                                                                                                                                                                                      |
| [this][.GridGroupingControl1.TableDescriptor.ExpressionFields.Add(Expcolumn2);]                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 50

[]{#p38} 

[]{#related-topics}

