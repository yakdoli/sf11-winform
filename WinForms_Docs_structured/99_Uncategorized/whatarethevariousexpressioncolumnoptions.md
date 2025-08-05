---
title: whatarethevariousexpressioncolumnoptions.md
original_path: WinForms_Docs/99_Uncategorized/whatarethevariousexpressioncolumnoptions.md
created_at: 2025-08-05
---






#### What are the various ExpressionColumn options? {#what-are-the-various-expressioncolumn-options style="tab-stops: 0pt"}

[] 

The following code illustrates various expression column options.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [//1. Setting the operators in the expression.   ]                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [// The computations are performed with level one operations done first.                         ]                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [// Alpha constants used with match and like should be enclosed in apostrophes (\'). ]                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [// \*, / ,+, - ,\<, \>, =, \<=, \>=,match, like, in, between ,or, and ]                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [// \* operator used here.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [ExpressionFieldDescriptor exp= [new] ExpressionFieldDescriptor([\"Expr1\"],[\"\[ColumnName\] \*2\"], [\"System.Int32\"]);]  |
|                                                                                                                                                                                                                                                            |
| [      ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [//2. Setting the output/view type.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [// Output in double type.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                            |
| [ExpressionFieldDescriptor exp= [new] ExpressionFieldDescriptor([\"Expr1\"],[\"\[ColumnName\] \*2\"], [\"System.Double\"]);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' 1. Setting the operators in the expression. ]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' Setting operators in the expression.  ]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' The computations are performed with level one operations done first.                      ]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' Alpha constants used with match and like should be enclosed in apostrophes (\'). ]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' \*, / ,+, - ,\<, \>, =, \<=, \>=,match, like, in, between ,or, and ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' \* operator used here.]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                          |
| [Dim][ exp [As] ExpressionFieldDescriptor = [New] ExpressionFieldDescriptor([\"Expr1\"], [\"\[Id\] \*2\"], [\"System.Int32\"])]      |
|                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                          |
| [\' 2. Setting the output in double type.]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                          |
| [Dim][ exp2 [As] ExpressionFieldDescriptor = [New] ExpressionFieldDescriptor([\"Expr2\"], [\"\[Expr1\] \*2\"], [\"System.Double\"])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p688} 

 

[]{#related-topics}

