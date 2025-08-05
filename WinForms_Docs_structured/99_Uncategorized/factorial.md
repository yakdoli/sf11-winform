---
title: factorial.md
original_path: WinForms_Docs/99_Uncategorized/factorial.md
created_at: 2025-08-05
---






#### Factorial {#factorial style="tab-stops: 0pt"}

[] 

The **Factorial** function returns the factorial value of a given number. In mathematics, the factorial of a natural number n is the product of all positive integers less than or equal to n. It is denoted as n! and pronounced \"n factorial\", or colloquially \"n shriek\", \"n bang\" or \"n crit\". Factorial finds its main application in combinatorics like Permutations and Combinations and is also used in Number Theory.

 

The factorial function is defined by the following expression.

[] 

[{border="0"}][]

[] 

which is equivalent to n! = n . (n-1) . \..... . 2 . 1.

 

The above definition incorporates the convention that the product of no numbers at all is 1, i.e., 0! = 1.

[] 

Using the formula

[] 

The **Factorial** method of the **UtilityFunctions** class returns the factorial value for any positive integer.

[] 


  Method Name   Parameters                                           Example
  ------------- ---------------------------------------------------- ---------------------------------------------
  Factorial     n: The number whose factorial should be found out.   An integer that returns the factorial of n.


**[]** 

Example

[] 

Here is a code snippet that shows a sample usage.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [int][ result = UtilityFunctions.Factorial(][int][ n);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ ][int as][ result = UtilityFunctions.Factorial(][int][ n)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p237} 

[]{#related-topics}

