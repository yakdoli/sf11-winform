---
title: binomialcoefficient.md
original_path: WinForms_Docs/99_Uncategorized/binomialcoefficient.md
created_at: 2025-08-05
---






#### Binomial Coefficient {#binomial-coefficient style="tab-stops: 0pt"}

[] 

**Binomial Coefficient** is an utility function used in statistical calculations. This function is used to determine the possible number of combinations of \'k\' items that can  be selected from a set of \'n\' items. The binomial coefficient formula can be explicitly stated as given below.

[] 

[{border="0"}][]

[] 

where n! denotes the factorial of n.

 

An alternative name for the binomial coefficient is choose function; the binomial coefficient of n and k is often read as \"n choose k\". Alternative notations include C(n, k), [n]C[k] (C for combination). These numbers are called binomial coefficients because they are coefficients in binomial theorem.

[] 

Using the formula

[] 

The **Binomial** method of the **UtilityFunctions** class returns the binomial coefficient for given **n** and **k** values.

[] 


+-----------------------+-----------------------+-------------------------------------------------------------+
| Method Name           | Parameters            | Return Value                                                |
+-----------------------+-----------------------+-------------------------------------------------------------+
| Binomial              | 1.   The n value.     | An integer that represents the binomial coefficient  value. |
|                       |                       |                                                             |
|                       | 2.   The k value.     |                                                             |
+-----------------------+-----------------------+-------------------------------------------------------------+


[] 

Example

[] 

Here is a code snippet that shows a sample usage.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                       |
|                                                                                                                                                      |
| **[]**                                                                                             |
|                                                                                                                                                      |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                 |
|                                                                                                                                                      |
| [int][ result = UtilityFunctions.Binomial(n, k);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Dim][ ][int][ ][as][ result = UtilityFunctions.Binomial(n, k)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p234} 

[]{#related-topics}

