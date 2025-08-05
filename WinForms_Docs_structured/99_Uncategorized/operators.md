---
title: operators.md
original_path: WinForms_Docs/99_Uncategorized/operators.md
created_at: 2025-08-05
---








  









### Operators {#operators style="tab-stops: 0pt"}

 

The following is a list of the operators which are supported by Essential Calculate.

 

Unary Arithmetic Operator

[] 

[-         Unary Minus Sign]

[] 

Binary Arithmetic Operators

[] 

[+        Addition]

[-         Subtraction]

[\*         Multiplication]

[/         Division]

[\^        Exponentiation]

 

Binary Literal Operator

[] 

[&        Concatenation]

[] 

Binary Logical Operators

[] 

[\<        Less Than ]

[\>        Greater Than]

[=         Equal To]

[\<=       Less Than Or Equal]

[\>=       Greater Than Or Equal]

[\<\>       Not Equal]

[] 

[All operations are subject to the following hierarchy of operations. The level 1 operations are done first, followed by level 2, and so on. Within the same level, the operations are performed from left to right in the order in which they are encountered during the parsing of the formula.]

[] 

1.   - (Unary Minus)

2.   \*    /

3.   +    -

4.   \<   \>    =    \<=    \>=    \<\>

5.   & (Concatenation)

[] 

If you want to change the default operators precedence, then use parentheses to explicitly indicate the operation order.

[] 

Examples

[] 

1.   Formulas                Computed Value

2.   = 6 / 2 + 1                     4

3.   = 6 / (2 + 1)                   2

4.   = 2 + 4 / 2                     4

5.   = (2 + 4) / 2                   3

[] 

Logical operations return specific values: True or False. If you need specific numerical values associated with any logical expression, then use the logical expression as the first argument in the Formula Library IF-function, with the second argument being the numerical value of True and the third argument being the numerical value of False. If you use a well-formed logical expression in a larger calculation, True evaluates to numerical 1 and False evaluates to numerical 0 for use in the calculations.

[]{#p49} 

[]{#related-topics}

