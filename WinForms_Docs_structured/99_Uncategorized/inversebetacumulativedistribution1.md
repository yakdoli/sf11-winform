---
title: inversebetacumulativedistribution1.md
original_path: WinForms_Docs/99_Uncategorized/inversebetacumulativedistribution1.md
created_at: 2025-08-05
---






#### Inverse Beta Cumulative Distribution {#inverse-beta-cumulative-distribution style="tab-stops: 0pt"}

 

This formula returns the inverse of Beta Cumulative Distribution.

[] 

Using the formula

 

The **InverseBetaCumulativeDistribution** method of the **UtilityFunctions** class returns the inverse of beta cumulative distribution ( for 1 \>= p \>= 0 , a \> 0, b \> 0 ).

 


+-----------------------------------+-------------------------------------------+----------------------------------------------------------------+
| Method Name                       | Parameters                                | Return Value                                                   |
+-----------------------------------+-------------------------------------------+----------------------------------------------------------------+
| InverseBetaCumulativeDistribution | 1\. a: First Parameter of Beta function.  | A double that inverses the beta cumulative distribution value. |
|                                   |                                           |                                                                |
|                                   | 2\. b: Second Parameter of Beta function. |                                                                |
|                                   |                                           |                                                                |
|                                   | 3\. p: The probability.                   |                                                                |
+-----------------------------------+-------------------------------------------+----------------------------------------------------------------+


 

 

Example

 

Here is a code snippet that shows a sample usage.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                                             |
|                                                                                                                                                                                      |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                                 |
|                                                                                                                                                                                      |
| [double][ result = UtilityFunctions.InverseBetaCumulativeDistribution (a, b, p);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Dim][ ][double][ ][as][ result = UtilityFunctions.InverseBetaCumulativeDistribution (a, b, p)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p235} 

[]{#related-topics}

