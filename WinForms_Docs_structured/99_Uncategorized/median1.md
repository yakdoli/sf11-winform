---
title: median1.md
original_path: WinForms_Docs/99_Uncategorized/median1.md
created_at: 2025-08-05
---






#### Median {#median style="tab-stops: 0pt"}

 

**Median** is a statistical formula that is used to find the median of y values of a series. Median can be calculated by arranging the values from the lowest to the highest and picking up the middle one. If the total number of values is even, then pick up the two middle values after sorting the values in ascending order. The mean of these two middle values will give you the median. Hence half of the series points have values less than the median and the values of the other half will be greater than the median.

 

Median can be found out for any series by using the Median method of **BasicStatisticalFormulas** class. The below table shows the details of this method.

 


  ------------- --------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------
  Method Name   Parameter                                                                               Return value
  Median        **InputSeries**: A ChartSeries type object for whose X values an average is required.   A **double** that represents the Median value of all the X values in the given series.
  ------------- --------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------


 

Example

 

Here is a code snippet that shows a sample usage.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                                       |
| []                                                                                                                                                              |
|                                                                                                                                                                                       |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                                  |
|                                                                                                                                                                                       |
| [\...\...\...\...]                                                                                                                  |
|                                                                                                                                                                                       |
| [double][ calculatedMedian = Statistics.BasicStatisticalFormulas.Median(series1);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                              |
|                                                                                                                                                                                 |
| []                                                                                                                                                        |
|                                                                                                                                                                                 |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                           |
|                                                                                                                                                                                 |
| [\...\...\...\....]                                                                                                           |
|                                                                                                                                                                                 |
| [Dim][ Median1 ][As Double] |
|                                                                                                                                                                                 |
| [calculatedMedian = BasicStatisticalFormulas.Median(series1)]                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}]Note: For further details, refer to this Browser Sample:


 

[\[Installed drive\]:\\Documents and Settings\\\[User name\]\\My Documents\\Syncfusion\\EssentialStudio\\\[Installed version\]\\Windows\\Chart.Windows\\Samples\\2.0\\Statistical Analysis\\Chart Statistical Formulas]{.UGHyperlink}

[]{#p223} 

 

[]{#related-topics}

