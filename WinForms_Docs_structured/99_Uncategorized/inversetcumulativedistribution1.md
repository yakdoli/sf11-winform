---
title: inversetcumulativedistribution1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\inversetcumulativedistribution1.md
created_at: 2025-07-03
---






#### Inverse T Cumulative Distribution {#inverse-t-cumulative-distribution style="tab-stops: 0pt"}

 

This formula computes the inverse of the cumulative distribution for T-statistic.

 

Using the Formula

 

InverseTCumulativeDistribution is calculated using the **Statistics.UtilityFunctions** class. The following table describes this function\'s parameters and its values.

 


+--------------------------------+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Method Name                    | Parameters                                                                                            | Return Value                                                                            |
+--------------------------------+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| InverseTCumulativeDistribution | 1\. **p**: the alpha value (probability).                                                             | A double that represents the Inverse of T cumulative distribution function probability. |
|                                |                                                                                                       |                                                                                         |
|                                | 2\. **degreeOfFreedom**: an integer value that represents the degree of freedom.                      |                                                                                         |
|                                |                                                                                                       |                                                                                         |
|                                | 3\. **oneTail**: If true, one-tailed distribution is used; otherwise two-tailed distribution is used. |                                                                                         |
+--------------------------------+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+


 

Example

 

Here is a code snippet that shows a sample usage.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                             |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                                                        |
|                                                                                                                                                                                                             |
| [double][ x= Statistics.UtilityFunctions. InverseTCumulativelDistribution(p, degreeOfFreedom,OneTail );] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                                                      |
|                                                                                                                                                                                                            |
| [double][ x= Statistics.UtilityFunctions. InverseTCumulativelDistribution(p, degreeOfFreedom,OneTail )] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p246} 

[]{#related-topics}

