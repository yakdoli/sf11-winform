---
title: variance1.md
original_path: WinForms_Docs/99_Uncategorized/variance1.md
created_at: 2025-08-05
---






#### Variance {#variance style="tab-stops: 0pt"}

 

**Variance** is a statistical formula that calculates the variance of series y values. A Variance can be defined as the square of the standard deviation of a sample.

 

Using the Formula

 

The variance can be computed for any series by using the method **Variance** of **BasicStatisticalFormulas** class. Below table shows the details of this method.

 


+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Method Name           | Parameters                                                                                                                           | Return Value                                                        |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Variance              | 1\. **InputSeries**: A ChartSeries object that represents the input series.                                                          | A **double** that represents the variance within the group of data. |
|                       |                                                                                                                                      |                                                                     |
|                       | 2\. **SampleVariance**: A boolean value; **true** if the data is a sample of a population, **false** if it is the entire population. |                                                                     |
+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+


 

Example

 

Variance is the square of the standard deviation for the given data.  

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                                                   |
|                                                                                                                                                                            |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                       |
|                                                                                                                                                                            |
| [\...\...\...\...]                                                                                                       |
|                                                                                                                                                                            |
| [double][ Variance1= BasicStatisticalFormulas.Variance(series1,false);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                          |
|                                                                                                                                                                             |
| []                                                                                                                                                    |
|                                                                                                                                                                             |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                       |
|                                                                                                                                                                             |
| [\...\...\...\....]                                                                                                       |
|                                                                                                                                                                             |
| [Dim][ Variance1 ][As Double\                                            |
| ][Variance1=BasicStatisticalFormulas.Variance (series1,false)          ] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p229} 

[]{#related-topics}

