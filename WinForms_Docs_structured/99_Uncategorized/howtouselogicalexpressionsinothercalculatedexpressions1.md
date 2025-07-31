---
title: howtouselogicalexpressionsinothercalculatedexpressions1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtouselogicalexpressionsinothercalculatedexpressions1.md
created_at: 2025-07-03
---








  









### How To Use Logical Expressions In Other Calculated Expressions? {#how-to-use-logical-expressions-in-other-calculated-expressions style="tab-stops: 0pt"}

 

Logical expressions return a True or False value. If you use a logical expression as part of a calculation, then,

 

[·      ]A True is replaced with 1.

[·      ]A False is replaced with 0 as the whole expression is evaluated.

[] 

This allows you to easily write and compute formulas that involve logical conditions.

 

Consider the following expression:

 

(\[Cost\] \< 100) \* 1 + (\[Cost\] \>= 100) \* (\[Cost\] \< 200) \* 3 + (\[Cost\] \>= 200) \* (\[Cost\] \< 300) \* 5 + (\[Cost \> 300) \* 7

 

Depending upon the value of cost, this expression returns 1, 3, 5 or 7. This is an example of using a linear combination of logical expressions that times other values.

 


{border="0"}Note: The logical conditions are mutually exclusive[,] but~~[,]~~ when taken as a whole, cover all possible values of cost. It has the effect of assigning a unique value depending upon the input value.

 


[]{#related-topics}

