---
title: supportedarithmeticoperatorsandcalculationprecedence.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\supportedarithmeticoperatorsandcalculationprecedence.md
created_at: 2025-07-03
---






##### Supported Arithmetic Operators and Calculation Precedence {#supported-arithmetic-operators-and-calculation-precedence style="tab-stops: 0pt"}

[] 

The current formula support will allow you to enter well-formed parenthetical algebraic expressions using operators and operands. The nine supported operators are shown in the precedence table given below, with operators on the same level being calculated as encountered when the expression is scanned from left to right.

[] 

Code Tables

**[]** 


  -------------------------------------------------------------------------------------- ------------------------- ------------------------
  Operations                                                                             Symbols                   Calculation Precedence
  Multiplication, Division                                                                /  \*                    1st
  Addition, Subtraction                                                                  +  -                      2nd
  Less Than, Greater Than, Equal, Less Than Or Equal, Greater Than Or Equal, Not Equal    \<  \> = \<= \>= \<\>    3rd
  -------------------------------------------------------------------------------------- ------------------------- ------------------------


[] 

The supported operands include those listed in the table given below. An operand by itself is also a well-formed algebraic expression that can serve as an entire formula in a cell.

[] 


  -------------------------------------- ---------------------------------------
  Operand                                Examples
  number                                 532.1, -10.2, or 18.
  cell reference                         A12, BB1010, or Q18.
  library formula with valid arguments   Abs(E14), Cos(-3.14), or Sum(A1:A14).
  any well formed algebraic expression   E1+E2, Cos(2)\<A4, or Abs(A1-A5).
  -------------------------------------- ---------------------------------------


[] 

Within a formula cell, a case is ignored. So, a1 is the same as A1, and Cos(3) is the same as COS(3).[]{#p22}

[]{#related-topics}

