---
title: inversefcumulativedistribution1.md
original_path: WinForms_Docs/99_Uncategorized/inversefcumulativedistribution1.md
created_at: 2025-08-05
---






#### Inverse F Cumulative Distribution {#inverse-f-cumulative-distribution style="tab-stops: 0pt"}

 

This formula returns the inverse of the F cumulative distribution.

 

Using the Formula

 

InverseFCumulativeDistribution is calculated using the **Statistics.UtilityFunctions** class. The following table describes its parameters and its values.

 


+--------------------------------+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| Method Name                    | Parameters                                                                                    | Return Value                                                    |
+--------------------------------+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| InverseFCumulativeDistribution | 1\. **fValue**: The F value for which you need the distribution.                              | A double that represents the inverse F cumulative distribution. |
|                                |                                                                                               |                                                                 |
|                                | 2\. **firstDegreeOfFreedom**: an integer value that represents the first degree of freedom.   |                                                                 |
|                                |                                                                                               |                                                                 |
|                                | 3\. **secondDegreeOfFreedom**: an integer value that represents the second degree of freedom. |                                                                 |
+--------------------------------+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------+


 

Example

 

Here is a code snippet that shows a sample usage.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]\                                                                                                                                                                                                                             |
| \                                                                                                                                                                                                                                      |
| ]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                        |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [double][ x= Statistics.UtilityFunctions. InverseFCumulativelDistribution( fvalue, firstdegreeOf Freedom, secondDegreeOfFreedom );] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                                                                               |
|                                                                                                                                                                                                                                     |
| [double][ x= Statistics.UtilityFunctions. InverseFCumulativelDistribution(fvalue, firstdegreeOf Freedom, secondDegreeOfFreedom)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p242} 

[]{#related-topics}

