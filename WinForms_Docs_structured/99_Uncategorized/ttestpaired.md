---
title: ttestpaired.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\ttestpaired.md
created_at: 2025-07-03
---






##### TTest Paired {#ttest-paired style="tab-stops: 0pt"}

[] 

This formula is used when there is a dependency between the samples. The two possible scenarios could be when there is a single sample that is tested twice (before and after an experiment), or when there are two samples whose values can be matched. This test assumes that there is some difference between the means of two input series populations. Input series are regarded as samples from normally distributed populations. The population variances are assumed to be unequal. This test is otherwise called as **Robust TTest**.

[] 

Steps to Perform the Test

**[]** 

1.   Specify the null hypothesis and alternate hypothesis.

[] 

[·      ]Null Hypothesis: Difference between the two means is zero.

[·      ]Alternate Hypothesis: Difference between the two means is not zero.

[] 

2.   Calculate the difference between two series on each pair of values.

*[]* 

3.   Calculate the mean difference ( *[Mdiff]* ), ie., mean of the new series values.

 

4.   Calculate the Standard Deviation of the differences ( *[Sd]* ).

 

5.   Get the degrees of freedom.

[] 

[{border="0"}][]

[] 

6.   Compute the t-statistic as given below.

[] 

t = ( Mdiff - Md ) / \[Sd \* Sqrt( 1/n1 )\]

[] 

7.   Construct a t-table at (n1 - 1) degrees of freedom and get the tabulated value for a given level of significance (probability).

[] 

8.   If the calculated tvalue exceeds the tabulated value we can say that the means are significantly different at that level of probability.

[] 

Using the Formula

[] 

The TTest formula for dependent samples can be calculated by using the **TTestPaired** method of the **BasicStatisticalFormulas** class. The following table presents the details of this method. This method returns an instance of **TTestResult** class that stores the resultant values of this test such as means of the two series, T value, degrees of freedom, number of points in every series, T critical value and confidence level (probability).

[] 


+-----------------------+-----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|                       |                                                                                                                 |                                                             |
|                       |                                                                                                                 |                                                             |
| Method Name           | Parameters                                                                                                      | Return Value                                                |
+-----------------------+-----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| TTestPaired           | 1.   **HypothesizedMeanDifference**: A **double** value specifying the difference between two population means. | A TTestResult object that has the following members:        |
|                       |                                                                                                                 |                                                             |
|                       | 2.   **Probability**: A **double** value that denotes the probability that gives the confidence level.          | [·      ]FirstSeriesMean       |
|                       |                                                                                                                 |                                                             |
|                       | 3.   **FirstSeries**: A ChartSeries object that stores the first group of data.                                 | [·      ]SecondSeriesMean      |
|                       |                                                                                                                 |                                                             |
|                       | 4.   **SecondSeries**: A ChartSeries object that stores the second group of data.                               | [·      ]FirstSeriesVariance   |
|                       |                                                                                                                 |                                                             |
|                       |                                                                                                                 | [·      ]SecondSeriesVariance  |
|                       |                                                                                                                 |                                                             |
|                       |                                                                                                                 | [·      ]Tvalue                |
|                       |                                                                                                                 |                                                             |
|                       |                                                                                                                 | [·      ]DegreeOfFreedom       |
|                       |                                                                                                                 |                                                             |
|                       |                                                                                                                 | [·      ]ProbabilityTOneTail   |
|                       |                                                                                                                 |                                                             |
|                       |                                                                                                                 | [·      ]TCriticalValueOneTail |
|                       |                                                                                                                 |                                                             |
|                       |                                                                                                                 | [·      ]ProbabilityTTwoTail   |
|                       |                                                                                                                 |                                                             |
|                       |                                                                                                                 | [·      ]TCriticalValueTwoTail |
+-----------------------+-----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+


[] 

Example

[] 

Here is a code snippet that shows a sample usage.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                                         |
| **[]**                                                                                                |
|                                                                                                                                                         |
| [using][ Syncfusion.Windows.Forms.Chart.Statistics;] |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [TTestResult ttr = BasicStatisticalFormulas.TTestPaired(0.2, 0.05, series1, series2);]                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [Imports][ Syncfusion.Windows.Forms.Chart.Statistics]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [Dim][ ttr ][As][ TTestResult = BasicStatisticalFormulas.TTestPaired(0.2, 0.05, series1, series2)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p228} 

[]{#related-topics}

