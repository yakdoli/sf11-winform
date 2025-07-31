---
title: equalsigntheformulacharacter.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\equalsigntheformulacharacter.md
created_at: 2025-07-03
---








  









### Equal Sign, the Formula Character {#equal-sign-the-formula-character style="tab-stops: 0pt"}

 

To indicate that a particular string should be treated as a formula, you must start the string with a special character, **CalcEngine.FormulaCharacter**. This property is static (Shared in VB), so you can change the formula character within your code. It\'s default value is the equal sign, (=).

 

In general, in order for Essential Calculate to recognize a string as containing a formula; the string is required to start with the CalcEngine.FormulaCharacter. There is one exception though, if you explicitly call a CalcEngine **Parse** method like **CalcEngine.ParseFormula** or **CalcEngine.ParseAndComputeFormula**, including the formula character as the first character in the passed string, it is optional.

 

[]{#related-topics}

