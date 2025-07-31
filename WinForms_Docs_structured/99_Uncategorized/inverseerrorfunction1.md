---
title: inverseerrorfunction1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\inverseerrorfunction1.md
created_at: 2025-07-03
---






#### Inverse Error Function {#inverse-error-function style="tab-stops: 0pt"}

 

The Inverse Error function, which is a rational approximation of the error function, gives the element-by-element inverse of the error function. The absolute value of the relative error is less than 1.15 -10.9 in the entire region.

 

Using the formula

 

The below table describes this function in detail.

 


  ---------------------- ------------------------------- ----------------------------------------------------
  Method Name            Parameters                      Return Value
  InverseErrorFunction   x must be less than 1.15-10.9   A double that gives the inverse of error function.
  ---------------------- ------------------------------- ----------------------------------------------------


 

Example

 

Here is a code snippet that shows a sample usage.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                                     |
| **[]**                                                                                            |
|                                                                                                                                                     |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                |
|                                                                                                                                                     |
| [int][ double = UtilityFunctions.InverseErf(x);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| **[]**                                                                                                     |
|                                                                                                                                                              |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                        |
|                                                                                                                                                              |
| [Dim double as][ result = UtilityFunctions.InverseErf(x)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p241} 

 

[]{#related-topics}

