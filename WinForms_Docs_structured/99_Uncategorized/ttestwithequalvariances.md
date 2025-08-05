---
title: ttestwithequalvariances.md
original_path: WinForms_Docs/99_Uncategorized/ttestwithequalvariances.md
created_at: 2025-08-05
---






##### TTest with Equal Variances {#ttest-with-equal-variances style="tab-stops: 0pt"}

[] 

This type of TTest can be performed on two random series that have no relationship with each other. But they should be of equal sizes, i.e., the number of data points of the two series should be same.

[] 

Steps to perform the test

**[]** 

1.   Specify the null hypothesis and alternate hypothesis.

[] 

[·      ]Null Hypothesis - Difference between the two means is **zero**.

[·      ]Alternate Hypothesis - Difference between the two means is not **zero**.

[] 

2.   Calculate the [means]{.UGHyperlink} of the two input series (µ1 and µ2)and calculate their difference (Md).

[] 

Md = µ1 - µ2

[] 

1\. Calculate the variances of the two input series (s1 and s2).

2\. Let n1 and n2 be the number of data points in first and second series respectively.

3\. Calculate the degrees of freedom.

[] 

D = n1 + n2 - 2

[] 

3.   As a next step, Calculate the Pooled Estimator as below.

[] 

Sp = (n1 - 1) \* s1 + (n2 - 1) \* s2

[] 

4.   Calculate the T-statistic as given below.

[] 

t = (µ1  - µ2 - Md) / Sqrt(Sp/n1 + Sp/n2)

[] 

5.   Construct a t-table at (n1+n2-2) degrees of freedom.

6.   Choose a level of significance(probability), say p = 0.05 and read the tabulated value.

7.   If the calculated tvalue exceeds the tabulated value we can say that the means are significantly different at that level of probability.

[] 

Using the Formula

**[]** 

The TTest formula for equal variances can be calculated by using the **TTestEqualVariances** method of the **BasicStatisticalFormulas** class. The following table presents the details of this method. This method returns an instance of **TTestResult** class that stores the resultant values of this test such as means of the two series, T value, degrees of freedom, number of points in every series, T critical value and confidence level(probability).

[] 


+-----------------------+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Method Name           | Parameters                                                                                                      | Return Value                                                          |
+-----------------------+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| TTestEqualVariances   | 1.   **HypothesizedMeanDifference**: A **double** value specifying the difference between two population means. | A TTestResult object that has the following members:                  |
|                       |                                                                                                                 |                                                                       |
|                       | 2.   **Probability**: A **double** value that gives the confidence level.                                       | []  |
|                       |                                                                                                                 |                                                                       |
|                       | 3.   **FirstInputSeries**: A ChartSeries object that stores the first group of data.                            | [·      ]FirstSeriesMean                 |
|                       |                                                                                                                 |                                                                       |
|                       | 4.   **SecondInputSeries**: A ChartSeries object that stores the second group of data.                          | [·      ]SecondSeriesMean                |
|                       |                                                                                                                 |                                                                       |
|                       |                                                                                                                 | [·      ]FirstSeriesVariance             |
|                       |                                                                                                                 |                                                                       |
|                       |                                                                                                                 | [·      ]SecondSeriesVariance            |
|                       |                                                                                                                 |                                                                       |
|                       |                                                                                                                 | [·      ]Tvalue                          |
|                       |                                                                                                                 |                                                                       |
|                       |                                                                                                                 | [·      ]DegreeOfFreedom                 |
|                       |                                                                                                                 |                                                                       |
|                       |                                                                                                                 | [·      ]ProbabilityTOneTail             |
|                       |                                                                                                                 |                                                                       |
|                       |                                                                                                                 | [·      ]TCriticalValueOneTail           |
|                       |                                                                                                                 |                                                                       |
|                       |                                                                                                                 | [·      ]ProbabilityTTwoTail             |
|                       |                                                                                                                 |                                                                       |
|                       |                                                                                                                 | [·      ]TCriticalValueTwoTail           |
+-----------------------+-----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+


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
| [TTestResult ttr = BasicStatisticalFormulas.TTestEqualVariances (0.2, 0.05, series1, series2);]       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [Imports][ Syncfusion.Windows.Forms.Chart.Statistics]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [Dim][ ttr ][As][ TTestResult = BasicStatisticalFormulas.TTestEqualVariances (0.2, 0.05, series1, series2)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p226} 

[]{#related-topics}

