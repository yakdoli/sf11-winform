---
title: fcumulativedistribution.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\fcumulativedistribution.md
created_at: 2025-07-03
---






#### F Cumulative Distribution {#f-cumulative-distribution style="tab-stops: 0pt"}

[] 

This formula returns cumulative F Distribution which can be defined as the ratio of two chi-square distributions. The formula can be expressed as given below.

[] 

[{border="0"}][]

where,

 

**U1** is the first chi square distribution with d1 degrees of freedom and

**[U2]** is the second chi square distribution with d2 degrees of freedom.

[] 

Using the Formula

[] 

FCumulativeDistribution is calculated using the **Statistics.UtilityFunctions** class. The following table describes the F Cumulative distribution method.

[] 


+-------------------------+------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| Method Name             | Parameters                                                                                     | Return Value                                        |
+-------------------------+------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| FCumulativeDistribution | 1.   **fValue**: The F value for which you want the distribution.                              | A double that represents T cumulative distribution. |
|                         |                                                                                                |                                                     |
|                         | 2.   **firstDegreeOfFreedom**: an integer value that represents the first degree of freedom.   |                                                     |
|                         |                                                                                                |                                                     |
|                         | 3.   **secondDegreeOfFreedom**: an integer value that represents the second degree of freedom. |                                                     |
+-------------------------+------------------------------------------------------------------------------------------------+-----------------------------------------------------+


[] 

Example

[] 

Here is a code snippet that shows a sample usage.

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [using][ Syncfusion.Windows.Forms.Chart.Statistics;]                                                                          |
|                                                                                                                                                                                                                                  |
| [double][ x = Statistics.UtilityFunctions. FCumulativelDistribution( fvalue, firstdegreeOf Freedom, secondDegreeOfFreedom );] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                               |
| [Imports][ Syncfusion.Windows.Forms.Chart.Statistics]                                                                      |
|                                                                                                                                                                                                                               |
| [double][ x = Statistics.UtilityFunctions. FCumulativelDistribution(fvalue, firstdegreeOf Freedom, secondDegreeOfFreedom)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p238} 

[]{#related-topics}

