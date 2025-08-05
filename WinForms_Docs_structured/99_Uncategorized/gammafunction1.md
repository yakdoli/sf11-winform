---
title: gammafunction1.md
original_path: WinForms_Docs/99_Uncategorized/gammafunction1.md
created_at: 2025-08-05
---






#### Gamma Function {#gamma-function style="tab-stops: 0pt"}

 

The Gamma Function is an attempt to generalize the [factorial]{.UGHyperlink} function to real and complex numbers. It is related to the factorial function by

 

{border="0"}

 

The Gamma Function

 

For a complex number x with a positive real part, the function can be given by

[] 

{border="0"}

 

Special Values of gamma function

 

{border="0"}

 

Using the Formula

 

The Gamma function is calculated using the **Statistics.UtilityFunctions** class. The following table describes the parameters and the return value of the gamma function.

 


  ------------- ------------------------------------------------------- ----------------------------------------------------
  Method Name   Parameters                                              Return Value
  Gamma         **p**: a value for which the gamma value is required.   A double that represents the gamma function value.
  ------------- ------------------------------------------------------- ----------------------------------------------------


 

Example

 

Here is a code snippet that shows a sample usage.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                                           |
| **[]**                                                                                                  |
|                                                                                                                                                           |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                      |
|                                                                                                                                                           |
| [double][ x = Statistics.UtilityFunctions.Gamma( p );] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                       |
|                                                                                                                                                          |
| **[]**                                                                                                 |
|                                                                                                                                                          |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                    |
|                                                                                                                                                          |
| [double][ x = Statistics.UtilityFunctions.Gamma( p )] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p239} 

[]{#related-topics}

