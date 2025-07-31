---
title: errorfunction1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\errorfunction1.md
created_at: 2025-07-03
---






#### Error Function {#error-function style="tab-stops: 0pt"}

 

The Error function, denoted as Erf(x), gives the probability that a measurement under the influence of accidental errors has a distance less than x from the average value at the center. It is the integral of Gauss curve, that is usually normalized to one with a factor of 2/Öp. It is otherwise called as integrated Gauss function or Gauss Error function.\
\
[]

{border="0"}

 

 

Here is the plot of error function.

[] 

{border="0"}

Figure 344: Error Function

 

 

Using the formula

[] 

The **Erf** method of the **UtilityFunctions** class returns integral of the Gauss curve for x \> 0.

 


  ------------- ------------------------------- ----------------------------------------------
  Method Name   Parameters                      Return Value
  Erf           x: must be greater than zero.   A double that represents the Gauss integral.
  ------------- ------------------------------- ----------------------------------------------


 

Example

 

Here is a code snippet that shows a sample usage.

 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                              |
| **[]**                                                                                     |
|                                                                                                                                              |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                         |
|                                                                                                                                              |
| [int][ double = UtilityFunctions.Erf(x);] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [Dim][ ][double as][ result = UtilityFunctions.Erf(x)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p236} 

[]{#related-topics}

