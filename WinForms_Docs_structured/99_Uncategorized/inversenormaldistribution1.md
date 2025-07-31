---
title: inversenormaldistribution1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\inversenormaldistribution1.md
created_at: 2025-07-03
---






#### Inverse Normal Distribution {#inverse-normal-distribution style="tab-stops: 0pt"}

 

This formula returns an approximation of the inverse of the standard normal cumulative distribution. That is, for a given P, it returns an approximation to the x satisfying P=Pr{z is smaller than x} where z is a random variable from the standard normal distribution.

 

Using the Formula

 

InverseNormalDistribution is calculated using the **Statistics.UtilityFunctions** class. The following table describes its parameters and its values.

 


  --------------------------- -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------
  Method Name                 Parameters                                                                                   Example
  InverseNormalDistribution   **p**: the probability at which the function value is evaluated. p must be in (0,1) range.   A double that represents the inverse of the normal distribution function.
  --------------------------- -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------


 

The algorithm uses a minimax approximation by rational functions and the result has a relative error whose absolute value is less than 1.15e-9.

 

**Example**

 

Here is a code snippet that shows a sample usage.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
| **[]**                                                                                                                      |
|                                                                                                                                                                               |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                          |
|                                                                                                                                                                               |
| [double][ x = Statistics.UtilityFunctions.InverseNormalDistribution( p );] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                           |
|                                                                                                                                                                              |
| **[]**                                                                                                                     |
|                                                                                                                                                                              |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                        |
|                                                                                                                                                                              |
| [double][ x = Statistics.UtilityFunctions.InverseNormalDistribution( p )] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p243} 

[]{#related-topics}

